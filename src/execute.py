import grammar as g
import SymbolTable as TS
from semanticObject import *
from expressions import *
from instructions import *

contador = 4  #for grapho   
currentAmbit = 'main'   #current ambit
currentParams = []  #list of parameters that the current function will have
semanticErrorList = []

def execute(input):
    #print(input)
    f = open("../reports/graph.dot","a")
    f.write("n000 ;\n")
    f.write("n000 [label=\"Inicio\"] ;\n")
    f.write("n000 -- n001;\n")
    f.write("n001 [label=\"Instrucciones\"] ;\n")

    tsGlobal = TS.SymbolTable()
    printList = []
    process(input,tsGlobal, printList,f)
    f.close()
    print("Tabla de simbolos: ")
    for i in tsGlobal.symbols:
        print(str(i) + ", "+ str(tsGlobal.get(i).valor) + ", "+ str(tsGlobal.get(i).tipo)+ ", "+ str(tsGlobal.get(i).declarada) + ", " + str(tsGlobal.get(i).parametros))

    return printList

def process(instructions, ts, printList,f):
    global currentAmbit, pasadas, currentParams
    i = 0
    while i < len(instructions):
        #isinstance verificar tipos 
        b = instructions[i]      
        if isinstance(b, Print_):
            f.write("n001 -- n002;\n")
            f.write("n002 [label=\"Print\"] ;\n")
            Print(b,ts, printList,f)
        elif isinstance(b, Declaration):
            f.write("n001 -- n003;\n")
            f.write("n003 [label=\"Declaracion\"] ;\n")
            Declaration_(b, ts,f)
        elif isinstance(b, If):
            result = valueExpression(b.expression, ts)
            if result >= 1:
                tmp = i
                i = goto(i+1, instructions, b.label)
                if i != 0:
                    pasadas = 0
                    #print("realizando salto a: "+ str(b.label))
                else:
                    i = tmp
                    #print("error semantico, etiqueta no existe")
            #else:
                #print("false")
        elif isinstance(b, Goto):
            #seteamos la instruccion anterior como la llamada al goto
            tmp = i
            i = goto(i, instructions, b.label)
            if i != 0:
                pasadas = 0
                #print("realizando salto a: "+ str(b.label))
            else:
                i = tmp
                #print("error semantico, etiqueta no existe")
        elif isinstance(b, Label):
            #insert to symbols table
            #type_ = 0
            if len(currentParams) > 0:
                #procedimiento tipo 7, cambiara a funcion si lee un $Vn
                if ts.exist(b.label) == 1:
                    #print("exists: "+ str(b.label))
                    type_ = ts.get(b.label).tipo
                else:
                    type_ = TS.TypeData.PROCEDIMIENTO
            else:
                type_= TS.TypeData.CONTROL

            #print("antes de insertar funcion: " + str(currentParams))
            symbol = TS.Symbol(b.label, type_, 0, currentAmbit, currentParams.copy())
            currentParams[:] = [] #clean to current Params    
            #print("despues de insertar funcion: " + str(symbol.parametros))
            if ts.exist(symbol.id) != 1:
                ts.add(symbol)
            else:
                ts.update(symbol)
            currentAmbit = b.label
        elif isinstance(b, Exit):
            break
        i += 1

#---instructions 
pasadas = 0
def goto(i, instructions, label):
    #print("instruccion No: "+str(i))
    #print("etiqueta buscada: "+str(label))
    global pasadas
    c = i
    while c < len(instructions):
        d = instructions[c]
        #print(str(d))
        if isinstance(d,Label):
            if d.label == label:
                #print("lo encontre retornando: "+ str(c-1))
                return c-1
        c += 1
    #semantic error, this label dont exist
    pasadas += 1
    #print("pasadas: "+str(pasadas))
    if pasadas == 2:
        #ya dio 2 pasadas completas
        return 0
    i = goto(0, instructions, label)
    return i

def Print(instruction, ts, printList,f):
    #add to .dot
    global contador
    f.write("n002 -- n00"+str(contador)+";\n")
    f.write("n00"+str(contador)+" [label=\""+ str(valueString(instruction.cadena, ts))+"\"] ;\n")
    contador += 1
    printList.append(valueString(instruction.cadena, ts))

def Declaration_(instruction, ts,f):    
    val = valueExpression(instruction.val, ts)
    if val != 'array':
        type_ = getType(val)
        sym = TS.Symbol(instruction.id, type_, val, currentAmbit)

        if ts.exist(instruction.id) != 1:
            ts.add(sym)
        else:
            ts.update(sym)

        if sym.id[1] == 'a': #params, update label to procediment
            currentParams.append(sym.id)
            ts.updateFunction(currentAmbit, TS.TypeData.PROCEDIMIENTO)
        elif sym.id[1] == 'v':
            #update label to function
            ts.updateFunction(currentAmbit, TS.TypeData.FUNCION)
    else:
        type_ = TS.TypeData.ARRAY
        sym = TS.Symbol(instruction.id, type_, {}, currentAmbit, 0, 0)
        valueArray(sym, instruction.val, ts)
       
        if ts.exist(instruction.id) != 1:
            ts.add(sym)
        else:
            ts.update(sym)       

    #print("var " + str(sym.id) + ": "+str(ts.get(instruction.id).valor))
    global contador
    f.write("n003 -- n00"+str(contador)+";\n")
    f.write("n00"+str(contador)+" [label=\""+instruction.id +"= "+ str(val)+"\"] ;\n")
    contador += 1

####--------resolutions
def getType(val):
    if isinstance(val, int): return TS.TypeData.INT
    elif isinstance(val, float): return  TS.TypeData.FLOAT
    elif isinstance(val, str): return  TS.TypeData.STRING
    elif isinstance(val, str):
        if len(val) == 1: return TS.TypeData.CHAR

def valueString(expression, ts):
    if isinstance(expression, String_): return expression.string
    elif isinstance(expression, Number): return str(valueExpression(expression, ts))
    elif isinstance(expression, Identifier): return str(valueExpression(expression, ts))

def valueArray(sym, instruction, ts):
    
    dictionary = '{\n'
    i = 0
    while i < len(instruction.expressionIzq)-1:
        val = valueExpression(instruction.expressionIzq[i],ts)
        if isinstance(val, str):
            dictionary += '\''+val+'\''
        else:
            dictionary += str(val)
        dictionary += ': {'
        i += 1        
    o = 0
    while o < len(instruction.expressionIzq)-2:
        dictionary += '}'
        o += 1
    dictionary += '}\n}'
    #print(dictionary)

    import ast
    d = ast.literal_eval(dictionary)
    sym.valor = d
    size = len(instruction.expressionIzq)
    val = d
    i = 0
    #print(str(val))
    while i < len(instruction.expressionIzq)-1:
        val = val.setdefault(valueExpression(instruction.expressionIzq[i], ts))
        i +=1
    #print(str(val))
    val1 = val.setdefault(valueExpression(instruction.expressionIzq[size-1],ts), valueExpression( instruction.expressionDer,ts))
    sym.valor = d

def getArray(sym, instruccion, ts):
    print("get array")




def valueExpression(instruction, ts):
    if isinstance(instruction, BinaryExpression):
        num1 = valueExpression(instruction.op1, ts)
        num2 = valueExpression(instruction.op2, ts)
        #if isinstance(num1, str):
            #if isinstance(num2, str):
                #print("Error: types.")
        try:
            if instruction.operator == Aritmetics.MAS: return num1 + num2
            if instruction.operator == Aritmetics.MENOS: return num1 - num2
            elif instruction.operator == Aritmetics.POR: return num1 * num2
            elif instruction.operator == Aritmetics.DIV: return num1 / num2
            elif instruction.operator == Aritmetics.MODULO: return num1 % num2
        except:
            seob = seOb('Error Semantico: Tipos de datos en operacion aritmetica.')
            print("Error: types.")
            semanticErrorList.append(seob)
    elif isinstance(instruction, LogicAndRelational):
        val1 = valueExpression(instruction.op1, ts)
        val2 = valueExpression(instruction.op2, ts)
        try:
            if instruction.operator == LogicsRelational.MAYORQUE: 
                if val1 > val2: return 1
            elif instruction.operator == LogicsRelational.MENORQUE: 
                if val1 < val2: return 1
            elif instruction.operator == LogicsRelational.MAYORIGUAL: 
                if val1 >= val2: return 1
            elif instruction.operator == LogicsRelational.MENORIGUAL: 
                if val1 <= val2: return 1
            elif instruction.operator == LogicsRelational.IGUALQUE: 
                if val1 == val2: return 1
            elif instruction.operator == LogicsRelational.AND: 
                if val1 >= 1 and val2 >= 1: return 1
            elif instruction.operator == LogicsRelational.OR: 
                if val1 >= 1 or val2 >= 1: return 1
            elif instruction.operator == LogicsRelational.XOR: 
                if val1 >= 1 ^ val2 >= 1: return 1
        
            return 0
        except:
            seob = seOb('Error Semantico: Tipos de datos en operacion relacional.')
            print("Error: types.")
            semanticErrorList.append(seob)
    elif isinstance(instruction, Not):
        num1 = valueExpression(instruction.expression, ts)
        if num1 >= 1: return 0
        else: return 1
    elif isinstance(instruction, Abs):
        return abs(valueExpression(instruction.expression,ts))
    elif isinstance(instruction, NegativeNumber):
        num1 = valueExpression(instruction.expression, ts)
        return -1 * num1
    elif isinstance(instruction, Identifier):
        if ts.exist(instruction.id) == 1:
            return ts.get(instruction.id).valor
        else:
            seob = seOb('Error Semantico: Variable no existe.')
            print("Error: not fount.")
            semanticErrorList.append(seob)
    elif isinstance(instruction, Number):
        return instruction.val
    elif isinstance(instruction, Cast_):
        num1 = valueExpression(instruction.expression,ts)
        if isinstance(num1, int):
            if instruction.type == 'float':  return float(num1)
            elif instruction.type == 'char': return chr(num1)

        elif isinstance(num1, float):
            if instruction.type == 'int':  return int(num1)
            elif instruction.type == 'char': return chr(int(num1))               

        elif isinstance(num1, str):
            if instruction.type == 'int':  return ord(num1[0])
            elif instruction.type == 'float': return float(ord(num1[0]))
            elif instruction.type == 'char': return num1[0]
    elif isinstance(instruction, String_):
        return instruction.string
    elif isinstance(instruction, ExpressionsDeclarationArray):
        return 'array'
        '''print("declaracion de array")
        data = {}
        #$t1[0]['telefono'][0] = 123456789
        data[0] = { 'nombre': {0: '1234567489', 1:'987654321'}}
        data[1] = 2
        data['name'] = 'juan'
        print(str(data[0]['nombre'][0])+", "+ str(data['name'])+", "+ str(data[1]))'''

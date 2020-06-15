import grammar as g
import SymbolTable as TS
from semanticObject import *
from expressions import *
from instructions import *
import ast
import copy
import collections
import generator as g

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

contador = 4  #for grapho 
currentAmbit = 'main'   #current ambit
currentParams = []  #list of parameters that the current function will have
semanticErrorList = []
tsGlobal = {}
lecturasRead = []       #sera modificada desde gui
la = 0
co = 0 
pasadas = 0

def execute(input):
    #print(input)
    global semanticErrorList, currentAmbit, currentParams, contador, tsGlobal

    contador = 4  #for grapho   
    currentAmbit = 'main'   #current ambit
    currentParams[:] = []  #list of parameters that the current function will have
    semanticErrorList[:] = []
    tsGlobal = {}
    tsGlobal = TS.SymbolTable()
    printList = []
    printList[:] = []
    semanticErrorList[:] = []

    node = g.node(contador, contador, 'S')
    ge = g.genera()
    ge.add(node)
    node = g.node(contador, contador+1, 'A')
    ge.add(node)
    contador+=1
    process(input,tsGlobal, printList, ge, contador)

    print("Tabla de simbolos: ")
    for i in tsGlobal.symbols:
        print(str(i) + ", "+ str(tsGlobal.get(i).valor) + ", "+ str(tsGlobal.get(i).tipo)+ ", "+ str(tsGlobal.get(i).declarada) + ", " + str(tsGlobal.get(i).parametros))

    return printList

printDebug = []
def executeDebug(input):
    # print(input)
    global semanticErrorList, currentAmbit, currentParams, contador, tsGlobal

    contador = 4  # for grapho
    currentAmbit = 'main'  # current ambit
    currentParams[:] = []  # list of parameters that the current function will have
    semanticErrorList[:] = []
    tsGlobal = {}
    tsGlobal = TS.SymbolTableDebug()
    printList = []
    printList[:] = []
    #semanticErrorList[:] = []
    node = g.node(contador, contador, 'S')
    ge = g.genera()
    ge.add(node)
    node = g.node(contador, contador+1, 'A')
    ge.add(node)
    contador+=1
    process(input, tsGlobal, printList,ge,contador)
    print("Tabla de simbolos: ")
    for i in tsGlobal.symbols:
        val = tsGlobal.get(i)
        print(str(i) + ", " + str(val.valor) + ", " + str(val.tipo) + ", " + str(
            val.declarada) + ", " + str(val.parametros))

    return printList

def process(instructions, ts, printList, ge, padre):
    global currentAmbit, pasadas, currentParams, contador    
       
    try:
        i = 0
        while i < len(instructions):
            #isinstance verificar tipos 
            b = instructions[i]      
            if isinstance(b, Print_):
                node = g.node(padre, contador+1, 'INSTRUCCION')
                ge.add(node)
                contador += 1
                padreLocalprint = contador
                node = g.node(padreLocalprint, contador+1, 'PRINT')
                ge.add(node)
                node = g.node(contador+1, contador+2, 'print')
                ge.add(node)
                contador += 2
                
                Print(b,ts, printList,ge,padreLocalprint+1)
            elif isinstance(b, Declaration):
                node = g.node(padre, contador+1, 'DECLARACION')
                ge.add(node)
                contador += 1
                padreLocaldecla = contador

                Declaration_(b, ts,ge, padreLocaldecla)
            elif isinstance(b, If):
                result = valueExpression(b.expression, ts)
                if result == 1:
                    tmp = i
                    i = goto(i+1, instructions, b.label)
                    if i != 0:
                        pasadas = 0
                        #print("realizando salto a: "+ str(b.label))
                    else:
                        i = tmp
                        #print("error semantico, etiqueta no existe")
                        se = seOb(f"Error: etiqueta {b.label} no existe", b.line, b.column)
                        semanticErrorList.append(se)
                elif result == '#':
                    se = seOb(f"Error: Condicion no valida", b.line, b.column)
                    semanticErrorList.append(se)
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
                    se = seOb(f"Error: etiqueta {b.label} no existe", b.line, b.column)
                    semanticErrorList.append(se)
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
            elif isinstance(b, Unset):
                if ts.delete(b.id) == 1:
                    print('variable eliminada.')
                else:
                    se = seOb(f'Error Semantico: No se pudo eliminar {b.id}, en funcion unset.', b.line, b.column)
                    semanticErrorList.append(se)

            i += 1
    except:
        if isinstance(instructions, Print_):
            Print(instructions,ts, printList,ge,padre)
        elif isinstance(instructions, Declaration):
            Declaration_(instructions, ts,ge,padre)
        elif isinstance(instructions, If):
            result = valueExpression(instructions.expression, ts)
            if result == 1:
                tmp = i
                i = goto(i+1, instructions, instructions.label)
                if i != 0:
                    pasadas = 0
                        #print("realizando salto a: "+ str(b.label))
                else:
                    i = tmp
                    #print("error semantico, etiqueta no existe")
                    se = seOb(f"Error: etiqueta {instructions.label} no existe", instructions.line, instructions.column)
                    semanticErrorList.append(se)
            elif result == '#':
                se = seOb(f"Error: Condicion no valida", instructions.line, instructions.column)
                semanticErrorList.append(se)
        elif isinstance(instructions, Goto):
            #seteamos la instruccion anterior como la llamada al goto
            tmp = i
            i = goto(i, instructions, instructions.label)
            if i != 0:
                pasadas = 0
                #print("realizando salto a: "+ str(b.label))
            else:
                i = tmp
                #print("error semantico, etiqueta no existe")
                se = seOb(f"Error: etiqueta {instructions.label} no existe", instructions.line, instructions.column)
                semanticErrorList.append(se)
        elif isinstance(instructions, Label):
            #insert to symbols table
            #type_ = 0
            if len(currentParams) > 0:
                #procedimiento tipo 7, cambiara a funcion si lee un $Vn
                if ts.exist(instructions.label) == 1:
                    #print("exists: "+ str(b.label))
                    type_ = ts.get(instructions.label).tipo
                else:
                    type_ = TS.TypeData.PROCEDIMIENTO
            else:
                type_= TS.TypeData.CONTROL

            #print("antes de insertar funcion: " + str(currentParams))
            symbol = TS.Symbol(instructions.label, type_, 0, currentAmbit, currentParams.copy())
            currentParams[:] = [] #clean to current Params    
            #print("despues de insertar funcion: " + str(symbol.parametros))
            if ts.exist(symbol.id) != 1:
                ts.add(symbol)
            else:
                ts.update(symbol)
            currentAmbit = instructions.label
        elif isinstance(instructions, Exit):
            return
        elif isinstance(instructions, Unset):
            if ts.delete(instructions.id) == 1:
                print('variable eliminada.')
            else:
                se = seOb(f'Error Semantico: No se pudo eliminar {b.id}, en funcion unset.', b.line, b.column)
                semanticErrorList.append(se)

#---instructions
def goto(i, instructions, label):
    global pasadas
    c = i
    while c < len(instructions):
        d = instructions[c]
        if isinstance(d,Label):
            if d.label == label:
                return c-1
        c += 1
    #semantic error, this label dont exist
    pasadas += 1
    if pasadas == 2:
        return 0
    i = goto(0, instructions, label)
    return i

def Print(instruction, ts, printList,ge, padre):
    #add to .dot
    global contador
    var = valueString(instruction.cadena, ts)
    if var != '#':
        if var != None:
            
            node = g.node(padre, contador+1, str(var))
            ge.add(node)
            contador+=1
            
            printList.append(var)
        else:
            seob = seOb(f'Error Semantico: No se pudo imprimir {var}.', instruction.line, instruction.column)
            semanticErrorList.append(seob)
    else:
        seob = seOb(f'Error Semantico: No se pudo imprimir {var}.', instruction.line, instruction.column)
        semanticErrorList.append(seob)

def Declaration_(instruction, ts,ge, padre): 
    #print(str(instruction))
    try:
        global la, co,contador
        la = instruction.line
        co = instruction.column

        val = valueExpression(instruction.val, ts)
        if val == '#':
            seob = seOb(f'Error Semantico: No se pudo declarar {instruction.id}.', instruction.line, instruction.column)
            semanticErrorList.append(seob)
            return
        if val != 'array':

            node = g.node(padre, contador+1, str(instruction.id))
            ge.add(node)
            node = g.node(padre, contador+2, '=')
            ge.add(node)
            node = g.node(padre, contador+3, str(val))
            ge.add(node)
            contador += 3

            type_ = getType(val)
            sym = TS.Symbol(instruction.id, type_, val, currentAmbit)
            if isinstance(instruction.val, ReferenceBit):
                if isinstance(instruction.val.expression, Identifier):
                    sym.referencia = instruction.val.expression.id
                #elif isinstance(instruction.val.expression, IdentifierArray):
                    #sym.referencia = instruction.val.expression.id
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
            #print(instruction.id)
            valor = {}
            if ts.exist(instruction.id) == 1:
                valor = ts.get(instruction.id).valor

            if isinstance(instruction.val, ExpressionsDeclarationArray):
                valor = valueArray(instruction.id, instruction.val, ts, valor)

            if isinstance(valor, str):

                type_ = TS.TypeData.STRING
                listaKeys = []
            else:
                type_ = TS.TypeData.ARRAY
                listaKeys = valor.values()

            sym = TS.Symbol(instruction.id, type_, valor, currentAmbit, 0, len(listaKeys))
            #valueArray(sym, instruction.val, ts)
            if ts.exist(instruction.id) != 1:
                ts.add(sym)
            else:
                ts.update(sym)
            #print("var " + str(sym.id) + ": "+str(ts.get(instruction.id).valor))
        #validar las referencias
        UpdateReferences(instruction.id, val, ts)
    except:
        print("error en la declaracion de variable")

def UpdateReferences(idReferencia, val,ts):
    #print("Actualizando las referencias.")
    for key in ts.symbols:
        if ts.get(key).referencia == idReferencia:
            ts.updateReference(key,val)
            #call recursive a child the current variable
            UpdateReferences(key, ts.get(key).valor,ts)
                  
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
    else: return str(valueExpression(expression, ts))

def valueArray(id, instruction, ts, valor):
    # VALIDAR QUE NO SOBREESCRIBA CADA DICCIONARIO
    # el valor corresponde a la variable que queremos modificar entonces si es str solo podra tener una dimension de ambos lados
    if isinstance(valor, str):
        print("asignacion de una posicion a un string")
        if len(instruction.expressionIzq) == 1:
            indice = valueExpression(instruction.expressionIzq[0], ts)
            tmp = list(valor)
            if indice > len(tmp):
                # rellenar con espacios
                for i in range(0, (indice - (len(tmp) - 1))):
                    tmp.append(" ")
                tmp[indice] = valueExpression(instruction.expressionDer, ts)
            else:
                tmp[indice] = valueExpression(instruction.expressionDer, ts)
            tmp = "".join(tmp)
            valor = tmp
            return tmp
        else:
            se = seOb(f'Error: indice fuera de rango.', instruction.line, instruction.column)
            semanticErrorList.append(se)
            return valor
    else:
        dictionary = '{\n'
        i = 0
        if len(instruction.expressionIzq) == 1:
            dictionary += '}'
        else:
            while i < len(instruction.expressionIzq) - 1:
                val = valueExpression(instruction.expressionIzq[i], ts)
                if isinstance(val, str):
                    dictionary += '\'' + val + '\''
                else:
                    dictionary += str(val)
                dictionary += ': {'
                i += 1
            o = 0
            while o < len(instruction.expressionIzq) - 2:
                dictionary += '}'
                o += 1
            dictionary += '}\n}'

        d = ast.literal_eval(dictionary)
        # print("valor actual: "+ str(valor))
        # print("valor a adjuntar: "+ str(d))
        size = len(instruction.expressionIzq)
        val = d
        i = 0
        # print(str(val))
        auxaux = {**valor}
        while i < len(instruction.expressionIzq) - 1:
            valaux = auxaux.setdefault(valueExpression(instruction.expressionIzq[i], ts))
            if valaux != None:
                # verifico que no sea un entero
                # -------
                # -------
                if isinstance(valaux, int) or isinstance(valaux, float):  # string caso especial de concatenacion
                    se = seOb(f'Error: Posisicon ya esta ocupada.', instruction.line, instruction.column)
                    semanticErrorList.append(se)
                    return valor
                elif isinstance(valaux, str):  # retorno el mismo valor
                    print("es string ");
                    print("asignacion de una posicion a un string")
                    #t[0]['nombre'][4]  -> i se encuantra en 'nombre'
                    if len(instruction.expressionIzq) == i+2:
                        #t[0]['nombre'][4] -> i+1 seria 4
                        indice = valueExpression(instruction.expressionIzq[i+1], ts)
                        tmp = list(valaux)
                        if indice > len(tmp)-1:
                            # rellenar con espacios
                            for j in range(0, (indice - (len(tmp) - 1))):
                                tmp.append(" ")
                            tmp[indice] = valueExpression(instruction.expressionDer, ts)
                        else:
                            tmp[indice] = valueExpression(instruction.expressionDer, ts)
                        tmp = "".join(tmp)
                        #actualizar valor del diccionario
                        a = {valueExpression(instruction.expressionIzq[i], ts): tmp}
                        d = update(copy.deepcopy(valor), a)
                        return d
                    else:
                        se = seOb(f'Error: indice fuera de rango.', instruction.line, instruction.column)
                        semanticErrorList.append(se)
                        return valor
                # --------
                # -------
            val = val.setdefault(valueExpression(instruction.expressionIzq[i], ts))
            i += 1
        val1 = val.setdefault(valueExpression(instruction.expressionIzq[size - 1], ts),
                              valueExpression(instruction.expressionDer, ts))

        d = update(copy.deepcopy(valor), d)
        return d

def update(d1, d2):
    try:
        for key, value in d2.items():
            if value and isinstance(value, collections.Mapping):
                d1[key] = update(d1.get(key, {}), value)
            else:
                d1[key] = d2[key]
        return d1
    except:
        #seob = seOb('Error Semantico: Tipos de datos en operacion aritmetica.', )
        #semanticErrorList.append(seob)
        return {}

def getArray(sym, instruccion, ts):
    print("get array")

def valueExpression(instruction, ts):
    if isinstance(instruction, BinaryExpression):
        
        global la, co
        num1 = valueExpression(instruction.op1, ts)
        num2 = valueExpression(instruction.op2, ts)
        try:
            if instruction.operator == Aritmetics.MAS: 
                if isinstance((num1 + num2), str):
                    return str(num1 + num2)
                else:
                    return (num1 + num2)
            if instruction.operator == Aritmetics.MENOS: return num1 - num2
            elif instruction.operator == Aritmetics.POR: return num1 * num2
            elif instruction.operator == Aritmetics.DIV: 
                if num2 != 0:
                    return num1 / num2
                else:
                    seob = seOb('Error Semantico: Division entre 0.', la, co)
                    semanticErrorList.append(seob)
                    return '#'
            elif instruction.operator == Aritmetics.MODULO: return num1 % num2
        except:
            seob = seOb('Error Semantico: Tipos de datos en operacion aritmetica.', la, co)
            semanticErrorList.append(seob)
            return '#'
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
                if val1 == 1 and val2 == 1: return 1
            elif instruction.operator == LogicsRelational.OR: 
                if val1 == 1 or val2 == 1: return 1
            elif instruction.operator == LogicsRelational.XOR: 
                if val1 == 1 ^ val2 == 1: return 1
            elif instruction.operator == LogicsRelational.DIFERENTE:
                if val1 != val2: return 1
        
            return 0
        except:
            se = seOb('Error : Tipos de datos en operacion relacional.', instruction.line, instruction.column)
            semanticErrorList.append(se)
            return '#'
    elif isinstance(instruction, Not):
        try:
            num1 = valueExpression(instruction.expression, ts)
            if num1 >= 1: return 0
            else: return 1
        except:
            se = seOb(f'Error: Tipos de datos en la operacion Not {valueExpression(instruction.expression,ts)}.', instruction.line, instruction.column)
            semanticErrorList.append(se)
            return '#'
    elif isinstance(instruction, Abs):
        try:
            return abs(valueExpression(instruction.expression,ts))
        except:
            se = seOb(f'Error: Tipos de datos en la operacion Abs {valueExpression(instruction.expression,ts)}.', instruction.line, instruction.column)
            semanticErrorList.append(se)
            return '#'
    elif isinstance(instruction, NegativeNumber):
        try:
            num1 = valueExpression(instruction.expression, ts)
            if isinstance(num1, int) or isinstance(num1, float):
                return -1 * num1
            else:
                se = seOb(f'Error: No se puede aplicar negativo a {num1}.', instruction.line, instruction.column)
                semanticErrorList.append(se)
                return '#'
        except:
            se = seOb(f'Error: No se puede aplicar negativo a {num1}.', instruction.line, instruction.column)
            semanticErrorList.append(se)
            return '#'
    elif isinstance(instruction, Identifier):
        if ts.exist(instruction.id) == 1:
            return ts.get(instruction.id).valor
        else:
            se = seOb(f'Error Semantico: Variable  {instruction.id} no existe.', instruction.line, instruction.column)
            semanticErrorList.append(se)
            return '#'
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
    elif isinstance(instruction, ExpressionsDeclarationArray): return 'array'
    elif instruction == 'array': return 'array'
    elif isinstance(instruction, IdentifierArray):
        try:
            sym = ts.get(instruction.id).valor
            if isinstance(sym, str):
                #print("es string")
                #es un string pero con posiciones
                if len(instruction.expressions) > 1:
                    #es decir que trar mas de un indice es decir  $t1[0][4]
                    #lo cual es error en un string 
                    #print(f"tamaño: {len(instruction.expressions)}")
                    se = seOb(f'Error: Indice {sym} del arreglo no existe.', instruction.line, instruction.column)
                    semanticErrorList.append(se)
                    return '#'
                else:
                    #print(f"valor del indice: {str(sym[valueExpression(instruction.expressions[0], ts)])}")
                    return sym[valueExpression(instruction.expressions[0], ts)]
            else:
                #print("no es  string")
                #manejo normal de array
                d = ast.literal_eval(str(sym))
                tmp = d
                i = 0
                while i < len(instruction.expressions)-1:
                    value = valueExpression(instruction.expressions[i], ts)
                    tmp = tmp.setdefault(value, ts)
                    if tmp == None:
                        se = seOb(f'Error: Indice {value} del arreglo no existe.', instruction.line, instruction.column)
                        semanticErrorList.append(se)
                        return '#'
                    i += 1

                result = tmp.get(valueExpression(instruction.expressions[len(instruction.expressions)-1],ts))
                #print("Resultado de la consulta: " + str(result))
                return result
        except:
            se = seOb(f'Error: Indice {value} del arreglo no existe.', instruction.line, instruction.column)
            semanticErrorList.append(se)
            return '#'
    elif isinstance(instruction, ReadConsole):
        #lectura de consola
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Ingrese un valor en la consola.")
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
        msgBox.exec()
        valor = input("Porfavor ingrese un valor:")
        try:
            val = valor.split('.')
            if len(val) > 1:
                valor = float(valor)
            else:
                valor = int(valor)
            return valor
        except:
            return valor
    elif isinstance(instruction, RelationalBit):
        val1 = valueExpression(instruction.op1, ts)
        val2 = valueExpression(instruction.op2, ts)
        
        try:
            if instruction.operator == BitToBit.ANDBIT: 
                return (val1 & val2)
            elif instruction.operator == BitToBit.ORBIT: 
                return (val1 | val2)
            elif instruction.operator == BitToBit.XORBIT: 
                return (val1 ^ val2)
            elif instruction.operator == BitToBit.SHIFTI: 
                return (val1 << val2)
            elif instruction.operator == BitToBit.SHIFTD: 
                return (val1 >> val2)
        
            return 0
        except:
            se = seOb('Error : Tipos de datos en operacion bit a bit.', instruction.line, instruction.column)
            semanticErrorList.append(se)
            return '#'
    elif isinstance(instruction, NotBit):
        num1 = valueExpression(instruction.expression, ts)
        if isinstance(num1, int) or isinstance(num1, float):
            return  ~num1
        else:
            se = seOb(f'Error: No se puede aplicar not bit  a {num1}.', instruction.line, instruction.column)
            semanticErrorList.append(se)
            return '#'
    elif isinstance(instruction, ReferenceBit):
        val = valueExpression(instruction.expression, ts)
        if val != '#':
            return val
        else:
            se = seOb(f'Error Referencia: variable {instruction.expression.id} no existe.', instruction.line, instruction.column)
            semanticErrorList.append(se)
            return '#'

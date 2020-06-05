import grammar as g
import SymbolTable as TS
from expressions import *
from instructions import *

contador = 4
def execute(input):
    #print(input)
    f = open("./graph.dot","a")
    f.write("n000 ;\n")
    f.write("n000 [label=\"Inicio\"] ;\n")
    f.write("n000 -- n001;\n")
    f.write("n001 [label=\"Instrucciones\"] ;\n")

    tsGlobal = TS.SymbolTable()
    printList = []
    process(input,tsGlobal, printList,f)
    f.close()
    return printList

def process(instructions, ts, printList,f):
    for i in instructions:
        #isinstance verificar tipos       
        if isinstance(i, Print_):
            f.write("n001 -- n002;\n")
            f.write("n002 [label=\"Print\"] ;\n")
            Print(i,ts, printList,f)
        elif isinstance(i, Declaration):
            f.write("n001 -- n003;\n")
            f.write("n003 [label=\"Declaracion\"] ;\n")
            Declaration_(i, ts,f)

#---instructions 
def Print(instruction, ts, printList,f):
    #add to .dot
    global contador
    f.write("n002 -- n00"+str(contador)+";\n")
    f.write("n00"+str(contador)+" [label=\""+valueString(instruction.cadena, ts)+"\"] ;\n")
    contador += 1
    printList.append(valueString(instruction.cadena, ts))

def Declaration_(instruction, ts,f):    
    val = valueExpression(instruction.val, ts)
    type_ = getType(val)
    #print("valor: "+str(val))
    #print("tipo: "+ str(type_))
    sym = TS.Symbol(instruction.id, type_, val)

    if ts.exist(instruction.id) != 1:
            ts.add(sym)
    else:
        ts.update(sym)

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


def valueExpression(instruction, ts):
    if isinstance(instruction, BinaryExpression):
        num1 = valueExpression(instruction.op1, ts)
        num2 = valueExpression(instruction.op2, ts)

        #if isinstance(num1, str):
            #if isinstance(num2, str):
                #print("Error: types.")

        if instruction.operator == Aritmetics.MAS: return num1 + num2
        elif instruction.operator == Aritmetics.MENOS: return num1 - num2
        elif instruction.operator == Aritmetics.POR: return num1 * num2
        elif instruction.operator == Aritmetics.DIV: return num1 / num2
        elif instruction.operator == Aritmetics.MODULO: return num1 % num2

    elif isinstance(instruction, Abs):
        return abs(valueExpression(instruction.expression,ts))

    elif isinstance(instruction, NegativeNumber):
        num1 = valueExpression(instruction.expression, ts)
        return -1 * num1

    elif isinstance(instruction, Identifier):
        return ts.get(instruction.id).valor

    elif isinstance(instruction, Number):
        return instruction.val

    elif isinstance(instruction, Cast_):
        num1 = valueExpression(instruction.expression,ts)
        #print("este es el valor: "+ str(num1))
        if isinstance(num1, int):
            if(instruction.type == 'float'):
                # convert float to int 
                return float(num1)
        elif isinstance(num1, float):
            print("tipo float")
            if(instruction.type == 'int'):
                # convert float to int 
                print(num1)
                return int(num1)

    elif isinstance(instruction, String_):
        return instruction.string

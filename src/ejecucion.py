import gramatica as g
import tablaSimbolos as TS
from expresiones import *
from instrucciones import *

def execute(input):
    #print(input)
    tsGlobal = TS.SymbolTable()
    process(input,tsGlobal)

def process(instructions, ts):
    for i in instructions:
        #isinstance verificar tipos
        if isinstance(i, Print_): Print(i,ts)
        elif isinstance(i, Declaration): Declaration_(i, ts)

#---instructions 
def Print(instruction, ts):
    print("> ", valueString(instruction.cadena, ts))

def Declaration_(instruction, ts):
    
    val = valueExpression(instruction.val, ts)
    type_ = getType(val)
    sym = TS.Symbol(instruction.id, type_, val)

    if ts.exist(instruction.id) != 1:
            ts.add(sym)
    else:
        ts.update(sym)

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
        if instruction.operator == Aritmetics.MAS: return num1 + num2
        elif instruction.operator == Aritmetics.MENOS: return num1 - num2
        elif instruction.operator == Aritmetics.POR: return num1 * num2
        elif instruction.operator == Aritmetics.DIV: return num1 / num2
        elif instruction.operator == Aritmetics.MODULO: return num1 % num2

    elif isinstance(instruction, NegativeNumber):
        num1 = valueExpression(instruction.expression, ts)
        return -1 * num1

    elif isinstance(instruction, Identifier):
        return ts.get(instruction.id).valor

    elif isinstance(instruction, Number):
        return instruction.val

    elif isinstance(instruction, String_):
        return instruction.string

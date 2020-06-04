import gramatica as g
import tablaSimbolos as ts
from expresiones import *
from instrucciones import *

def execute(input):
    tsGlobal = ts.SymbolTable()
    process(input,tsGlobal)


def process(instructions, ts):
    for i in instructions:
        #isinstance verificar tipos
        if isinstance(i, Print_): Print(i,ts)


def Print(instruction, ts):
    print("> ", valueString(instruction.cadena, ts))

def valueString(expression, ts):
    if isinstance(expression, String_): return expression.string
    elif isinstance(expression, StringAritmetic): return str(valueBinaryExpression(expression.expression, ts))
    

def valueBinaryExpression(expression, ts):
    
    if isinstance(expression, BinaryExpression):
        num1 = valueBinaryExpression(expression.op1,ts)
        num2 = valueBinaryExpression(expression.op2,ts)

        if expression.operator == Aritmetics.MAS: return num1 + num2
    
    elif isinstance(expression, Number):
        return expression.val
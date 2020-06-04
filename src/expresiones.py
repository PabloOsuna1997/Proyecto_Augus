from enum import Enum

class Aritmetics(Enum):
    MAS     = 1
    MENOS   = 2
    POR     = 3
    DIV     = 4
    MODULO  = 5

class LogicsRelational(Enum):
    AND         = 1
    OR          = 2
    XOR         = 3
    IGUALQUE    = 4
    DIFERENTE   = 5
    MAYORIGUAL  = 6
    MENORIGUAL  = 7
    MAYORQUE    = 8
    MENORQUE    = 9

class BitToBit(Enum):
    ANDBIT  = 1
    ORBIT   = 2
    XORBIT  = 3
    SHIFTI = 4
    SHIFTD = 5

########--------------- Numeric Section
class NumericExpression:
    ''' this class represent an numeric expresion'''

class BinaryExpression(NumericExpression):
        def __init__(self, op1, op2, operator):
            self.op1 = op1
            self.op2 = op2
            self.operator = operator

class Number(NumericExpression):
        def __init__(self, val=0):
            self.val = val
        
class Identifier(NumericExpression):
        def __init__(self, id = ""):
            self.id = id

class NegativeNumber(NumericExpression):
        def __init__(self, expression):
            self.expression = expression

class Abs(NumericExpression):
    def __init__(self, expression):
        self.expression = expression

class IdentifierArray(NumericExpression):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression

######----------------Strings section
class StringExpression:
    '''this class represent an string expression'''

class String_(StringExpression):
    def __init__(self, string):
        self.string = string

class StringAritmetic(StringExpression):
    def __init__(self, expression):
        self.expression = expression


######---------------- Logical Section
class LogicalExpression:
    '''this class represent an logical expresions'''

class RelationAndRelational(LogicalExpression):
    def __init__(self, op1, op2, operator):
        self.op1 = op1
        self.op2 = op2
        self.operator = operator

class Not(LogicalExpression):
    def __init__(self, expression):
        self.expression = expression



######----------------- bit-bit section
class BitBit:
    '''this class represent an bit to bit expressions'''

class NotBit(BitBit):
    def __init__(self, expression):
        self.expression = expression

class RelationalBit(BitBit):
    def __init__(self, op1, op2, operator):
        self.op1 = op1
        self.op2 = op2
        self.operator = operator


###----------------------cast section
class Cast:
    'this class represent the diferents types of the cast'

class toInt(Cast):
    def __init__(self, expression):
        self.expression = expression

class toFloat(Cast):
    def __init__(self, expression):
        self.expression = expression

class toChar(Cast):
    def __init__(self, expression):
        self.expression = expression


###------------------------read setcion
class Read:
    'this class represent the read to console'

class ReadConsole(Read):
    def __init__(self, read = 1):
        self.read = read
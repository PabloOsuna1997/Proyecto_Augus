class Instruction:
    '''this is an abstractab class'''

class Print_(Instruction) :
    '''print statment, recieve a string'''
    
    def __init__(self, cadena):
         self.cadena = cadena

class Declaration(Instruction):
    '''variables declarations'''

    def __init__(self, id, val):
        self.id = id
        self.val = val

class Unset(Instruction):
    '''variables destruction'''

    def __init__(self, id):
        self.id = id

class Exit(Instruction):
    def __init__(self, exit = 1):
        self.exit = exit

class If(Instruction):
    '''if statment, recieve a label for jump'''
    def __init__(self, label):
        self.label = label

class Goto(Instruction):
    '''label jump'''

    def __init__(self, label):
        self.label = label


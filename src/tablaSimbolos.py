from enum import Enum

class TypeData(Enum):
    INT = 1
    FLOAT = 2
    CHAR = 3
    STRING = 4

class Symbol():
    'this class represent a symbol in our symbol table'
    def __init__(self, id, tipo, valor):
        self.id = id
        self.tipo = tipo
        self.valor = valor

class SymbolTable():
    'this class represent our symbol table'
    def __init__(self, symbols = {}):
        self.symbols = symbols

    def add(self, symbol):
        self.symbols[symbol.id] = symbol
    
    def get(self, id):
        if not id in self.symbols:
            print("Error: variable "+ id + " not defiened." )
        return self.symbols[id]
    
    def update(self, symbol):
        if not symbol.id in self.symbols:
            print("Error: variable "+ symbol.id + " not defiened." )
        else:
            self.symbols[symbol.id] = symbol
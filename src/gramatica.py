# ---------------------
# @Autor
# Juan Pablo Osuna de Leon 
# 201503911
#----------------------

reservadas = {
    'if': 'IF',
    'goto': 'GOTO',
    'print': 'PRINT',
    'unset': 'UNSET',
    'exit': 'EXIT',    
    'read': 'READ',
    'array': 'ARRAY',
    'abs': 'ABS',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'xor': 'XOR',
    'main': 'MAIN'
}

tokens = [
    'PUNTOCOMA',
    'DOSPUNTOS',
    'LLAVEIZQ',
    'LLAVEDER',
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'DOLAR',
    'NOTBIT',
    'ANDBIT',
    'ORBIT',
    'XORBIT',
    'SHIFTIZQ',
    'SHIFTDER',
    'NOTLOGICA',
    'MENOS',
    'MAS',
    'POR',
    'DIV',
    'NUMERAL',
    'MODULO',
    'AND',
    'OR',
    'IGUAL',
    'IGUALQUE',
    'DIFERENTE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'MAYORQUE',
    'MENORQUE',
    'NUMERO',
    'ID',
    'CADENA',
    'CHAR_',
    'LABEL'
] + list(reservadas.values())

# er tokens

t_PUNTOCOMA  = r';'
t_DOSPUNTOS = r':'
t_LLAVEIZQ  = r'\{'
t_LLAVEDER  = r'\}'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CORIZQ    = r'\['
t_CORDER    = r'\]'
t_DOLAR     = r'\$'
t_NOTBIT    = r'~'
t_ANDBIT    = r'&'
t_ORBIT     = r'\|'
t_XORBIT    = r'\^'
t_SHIFTIZQ  = r'<<'
t_SHIFTDER  = r'>>'
t_NOTLOGICA = r'\!'
t_MENOS     = r'-'
t_MAS       = r'\+'
t_POR       = r'\*'
t_DIV       = r'/'
t_MODULO    = r'%'
t_AND       = r'&&'
t_OR        = r'\|\|'
t_IGUAL     = r'\='
t_IGUALQUE  = r'=='
t_DIFERENTE = r'!='
t_MAYORIGUAL= r'>='
t_MENORIGUAL= r'<='
t_MAYORQUE  = r'>'
t_MENORQUE  = r'<'


def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except:
        print("this number is not an integer.")
        t.value = 0
    return t

def t_ID(t):
    r'\$(t || a || v )[0-9]+'
    t.type = reservadas.get(t.value.lower(),'ID')
    return t

def t_LABEL(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'LABEL')
    #print(t)
    return t

def t_CHAR_(t):
    r'\'[a-zA-Z_]\''
    t.value = t.value[1:-1]
    return t

def t_CADENA(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t

def t_COMENTARIO(t):
    r'\#.*\n'
    t.lexer.lineno += 1

#ignored characters 
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


import ply.lex as lex
lexer = lex.lex()


#sintactic

#definition of grammar 

def p_init(t):
    'S : A'

def p_main(t):
    'A : MAIN DOSPUNTOS SENTENCIAS'

def p_sentencias_lista(t):
    '''SENTENCIAS   : SENTENCIAS SENTENCIA
                    | SENTENCIA '''

def p_sentencia(t):
    '''SENTENCIA    : ETIQUETA
                    | INSTRUCCIONES
                    | DECLARACIONES'''
                
def p_etiqueta(t):
    # i call label to recognize the label

    'ETIQUETA   : LABEL DOSPUNTOS'  

def p_instrucciones(t):
    '''INSTRUCCIONES    : PRINT PARIZQ CADENA PARDER PUNTOCOMA
                        | IF PARIZQ CADENA PARDER GOTO LABEL PUNTOCOMA
                        | UNSET PARIZQ ID PARDER PUNTOCOMA
                        | EXIT PUNTOCOMA
                        | GOTO LABEL PUNTOCOMA'''
      
def p_declaraciones(t):
    'DECLARACIONES  : ID ARRAY_'

def p_array(t):
    '''ARRAY_    : CORIZQ F CORDER IGUAL EXPRESION PUNTOCOMA
                | IGUAL EXPRESION PUNTOCOMA'''

def p_expresion(t):
    '''EXPRESION    : F OPERADOR F
                    | MENOS F
                    | NOTLOGICA F
                    | NOTBIT F
                    | F
                    | ABS PARIZQ EXPRESION PARDER
                    | PARIZQ TIPO PARDER ID
                    | READ PARIZQ PARDER
                    | ARRAY PARIZQ PARDER
                    | ID CORIZQ EXPRESION CORDER '''

def p_operador(t):
    '''OPERADOR     :   MAS
                        | MENOS
                        | DIV
                        | POR
                        | MODULO
                        | AND
                        | OR
                        | XOR
                        | IGUALQUE
                        | DIFERENTE
                        | MAYORIGUAL
                        | MENORIGUAL
                        | MAYORQUE
                        | MENORQUE
                        | ANDBIT
                        | ORBIT
                        | XORBIT
                        | SHIFTIZQ
                        | SHIFTDER'''

def p_tipo(t):
    ''' TIPO    : INT
                | FLOAT
                | CHAR'''

def p_f(t):
    '''F    : NUMERO
            | ID
            | CADENA'''

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    return parser.parse(input)
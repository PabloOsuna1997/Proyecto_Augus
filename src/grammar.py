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
t_IGUALQUE  = r'\=\='
t_DIFERENTE = r'\!\='
t_MAYORIGUAL= r'>='
t_MENORIGUAL= r'<='
t_MAYORQUE  = r'>'
t_MENORQUE  = r'<'

from lexicalObject import *
from sintacticObject import *
sintacticErroList = []
sintacticErroList[:] = []
LexicalErrosList = []
LexicalErrosList[:] =[ ]
input_ = ''

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    try:
        x = t.value.split(".")
        if len(x) > 1:
            t.value = float(t.value)
        else: 
            t.value = int(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r'\$(t|a|v|ra|sp?)[0-9]*'
    #print(str(t.value))
    t.type = reservadas.get(t.value.lower(),'ID')
    return t

def t_LABEL(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'LABEL')
    #print(t)
    return t

def t_CHAR_(t):
    r'\'[a-zA-Z_]\''
    print("char: " + str(t.value))
    t.value = t.value[1:-1]
    return t

def t_CADENA(t):
    r'(\'|\").*?(\'|\")'
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

# method for obtention the column
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1
    
def t_error(t):
    global input_,LexicalErrosList
    print("Illegal character '%s'" % t.value[0]+", linea: "+str(t.lexer.lineno))
    lo = lexOb(t.value[0],find_column(input_,t),t.lexer.lineno)
    LexicalErrosList.append(lo)
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()


#sintactic
#construction the ast
from expressions import *
from instructions import *

primeravez = 0
treeList = [] #list for save nodes
contador = 0
contadorSente = 1
conNode = 1
senteList = [] #para guardar las sentencias y despues apuntarlas
senteList_ = []
corcheList = []
bandera = 0
corcheListaux = []
corcheListaux = []
csList = []
sentenciaHija = 0
bandera = 0
res = []
fgraph = ''

#definition of grammar 
def p_init(t):
    'S : A'
    #code (sintetize result the A to S)
    t[0] = t[1]
    #region graph
    global fgraph,senteList, contador, conNode
    
    fgraph.write("n00"+str(conNode+1)+" [label=\"A\"] ;\n")
    for i in senteList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    contador += 1;
    fgraph.write("n00"+str(conNode+2)+" [label=\"S\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode+1)+";\n")
    conNode +=3
    #endregion
    
    fgraph.flush()
    fgraph.close()

def p_main(t):
    'A : MAIN DOSPUNTOS SENTENCIAS'
    #solo agrego las sentencias 
    t[0] = t[3]
    #region graph
    global contador, conNode, fgraph    
    fgraph.write("n00"+str(conNode+1)+" [label=\"MAIN\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" [label=\":\"] ;\n")
    fgraph.write("n00"+str(conNode+3)+" [label=\"SENTENCIAS\"] ;\n")

    for i in senteList_:
        fgraph.write("n00"+str(conNode+3)+" -- "+"n00"+str(i)+";\n")
    senteList_[:] = []
    senteList.append(conNode+1)
    senteList.append(conNode+2)
    senteList.append(conNode+3)
    conNode +=3
    #endregion

def p_sentencias_lista(t):
    'SENTENCIAS   : SENTENCIAS SENTENCIA'

    t[1].append(t[2])
    t[0] = t[1]
    #region graph
    global contador, conNode, fgraph, sentenciaHija, senteList_,contadorSente
    fgraph.write("n00"+str(conNode+1)+" [label=\"SENTENCIAS\"] ;\n")
    for i in senteList_:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList_[:] = []
    fgraph.write("n00"+str(conNode+2)+" [label=\"SENTENCIA\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode-1)+";\n")
    senteList_.append(conNode +1)
    senteList_.append(conNode +2)
    conNode +=3
    #endregion

def p_sentecias_sentencia(t):
    'SENTENCIAS     : SENTENCIA'
    t[0] = [t[1]]
    #region draw graph
    global contador, conNode, fgraph, sentenciaHija, primeravez,contadorSente
    fgraph.write("n00"+str(conNode+1)+" [label=\"SENTENCIA\"] ;\n")
    if primeravez == 0:
        primeravez = 1
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(conNode-1)+";\n")
    else:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(conNode)+";\n")

    senteList_.append(conNode+1)
    conNode += 2
    #endregion

def p_sentencia_eti(t):
    'SENTENCIA    : ETIQUETA'

    t[0] = t[1]
    #region draw graph
    global contador, conNode, senteList
    fgraph.write("n00"+str(conNode+1)+" [label=\"ETIQUETA\"] ;\n")
    #print(senteList)
    for i in senteList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    #print(senteList)
    conNode +=2
    #endregion

def p_sentencia_instr(t):
    'SENTENCIA    :  INSTRUCCIONES'

    t[0] = t[1]
    #region draw graph
    global contador, conNode, fgraph, senteList, treeList 
    fgraph.write("n00"+str(conNode+1)+" [label=\"INSTRUCCIONES\"] ;\n")
    for i in senteList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    conNode +=2
    #endregion

def p_sentencia_decla(t):
    'SENTENCIA    :  DECLARACIONES'

    t[0] = t[1]
    #region graph
    global contador, conNode, fgraph, senteList
    fgraph.write("n00"+str(conNode+1)+" [label=\"DECLARACIONES\"] ;\n")
    for i in senteList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    conNode +=2
    #endregion
                
def p_etiqueta(t):
    # i call label to recognize the label
    'ETIQUETA   : LABEL DOSPUNTOS' 
    t[0] = Label(t[1], t.lineno(1), t.lexpos(1))
    #region draw graph
    global contador,conNode, senteList
    fgraph.write("n00"+str(conNode+1)+" [label=\""+t[1]+"\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" [label=\":\"] ;\n")        
    senteList.append(conNode+1)
    senteList.append(conNode+2)
    conNode += 2
    #endregion

def p_instrucciones(t):
    '''INSTRUCCIONES    : PRINT PARIZQ EXPRESION PARDER PUNTOCOMA
                        | IF PARIZQ EXPRESION PARDER GOTO LABEL PUNTOCOMA
                        | UNSET PARIZQ ID PARDER PUNTOCOMA
                        | EXIT PUNTOCOMA
                        | GOTO LABEL PUNTOCOMA'''

    global contador, conNode, fgraph, senteList
    if(t[1] == 'print'): 
        t[0] = Print_(t[3])
        #region graph
        fgraph.write("n00"+str(conNode+1)+" [label=\"print\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" [label=\"(\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+" [label=\"EXPRESION\"] ;\n")
        fgraph.write("n00"+str(conNode+4)+" [label=\")\"] ;\n")
        fgraph.write("n00"+str(conNode+5)+" [label=\";\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+" -- "+"n00"+str(conNode)+";\n")
        
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        senteList.append(conNode+4)
        senteList.append(conNode+5)
        conNode += 5
        #endregion      

    elif(t[1] == 'if'): 
        t[0] = If(t[3], t[6])
        #region graph
        fgraph.write("n00"+str(conNode+1)+" [label=\"if\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" [label=\"(\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+" [label=\"EXPRESION\"] ;\n")
        fgraph.write("n00"+str(conNode+4)+" [label=\")\"] ;\n")
        fgraph.write("n00"+str(conNode+5)+" [label=\"goto\"] ;\n")
        fgraph.write("n00"+str(conNode+6)+" [label=\"label\"] ;\n")
        fgraph.write("n00"+str(conNode+7)+" [label=\";\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+" -- "+"n00"+str(conNode)+";\n")
        
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        senteList.append(conNode+4)
        senteList.append(conNode+5)
        senteList.append(conNode+6)
        senteList.append(conNode+7)
        conNode += 7
        #endregion

    elif(t[1] == 'unset'): 
        t[0] = Unset(t[3])
        #region graph
        fgraph.write("n00"+str(conNode+1)+" [label=\"unset\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" [label=\"(\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+" [label=\""+t[3]+"\"] ;\n")
        fgraph.write("n00"+str(conNode+4)+" [label=\")\"] ;\n")
        fgraph.write("n00"+str(conNode+5)+" [label=\";\"] ;\n")
        
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        senteList.append(conNode+4)
        senteList.append(conNode+5)
        conNode += 5
        #endregion

    elif(t[1] == 'goto'): 
        t[0] = Goto(t[2])
        #region graph
        fgraph.write("n00"+str(conNode+1)+" [label=\"goto\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" [label=\""+t[2]+"\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+" [label=\";\"] ;\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        conNode += 3
        #endregion

    elif(t[1] == 'exit'): 
        t[0] = Exit();
        #region graph
        fgraph.write("n00"+str(conNode+1)+" [label=\"exit\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" [label=\"(\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+" [label=\")\"] ;\n")
        fgraph.write("n00"+str(conNode+4)+" [label=\";\"] ;\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        senteList.append(conNode+4)
        conNode += 4
        #endregion

def p_declaraciones(t):
    'DECLARACIONES  : ID ARRAY_'   
    #insertion a new variable
    t[0] = Declaration(t[1], t.lineno(1), t.lexpos(1),t[2])
    #region
    global contador, conNode, fgraph, senteList, corcheList
    fgraph.write("n00"+str(conNode+1)+" [label=\""+t[1]+"\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" [label=\"ARRAY_\"] ;\n")    
    for i in senteList:
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []

    for i in corcheList:
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(i)+";\n")
    corcheList[:] = []
    senteList.append(conNode+1)
    senteList.append(conNode+2)
    conNode +=3
    #endregion

def p_array(t):
    '''ARRAY_    :  CORCHETES IGUAL EXPRESION PUNTOCOMA
                | IGUAL EXPRESION PUNTOCOMA'''

    #region graph
    global contador, conNode, fgraph, senteList, corcheList,res, bandera, corcheListaux
    if t[1] == '=':
        fgraph.write("n00"+str(conNode+1)+" [label=\"=\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" [label=\"EXPRESION\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
        fgraph.write("n00"+str(conNode+3)+" [label=\";\"] ;\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        conNode += 4    
    else:      
        fgraph.write("n00"+str(conNode+1)+" [label=\"CORCHETES\"] ;\n")
        #print("hijos de corchete: "+ str(res))
        if bandera == 1:
            for i in corcheListaux:
                fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
            corcheListaux[:] = []
        else:
            for i in corcheList:
                fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
            corcheList[:] = []

        fgraph.write("n00"+str(conNode+2)+" [label=\"=\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+" [label=\"EXPRESION\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+" -- "+"n00"+str(conNode)+";\n")
        fgraph.write("n00"+str(conNode+4)+" [label=\";\"] ;\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        senteList.append(conNode+4)
        conNode += 4
    #endregion
     
    if(t[1] == '='): t[0] = t[2]  #if expresion is array, expression contain 'array'
    else: t[0] = ExpressionsDeclarationArray(t[1], t[3], t.lineno(1), t.lexpos(1))

def p_corchete_lista(t):
    'CORCHETES : CORCHETES CORCHETE'
    t[1].append(t[2])
    t[0] = t[1]
    #region
    global contador, conNode, fgraph, corcheList, res
    fgraph.write("n00"+str(conNode+1)+" [label=\"CORCHETES\"] ;\n")
    contador = 0    
    for i in corcheList:
        if contador < 2:
            contador += 1
            fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    corcheList[:] = []

    fgraph.write("n00"+str(conNode+2)+" [label=\"CORCHETE\"] ;\n")
    for i in senteList:
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    corcheList.append(conNode+1)
    corcheList.append(conNode+2)
    res = corcheList[:]
    conNode += 3
    #endregion
    
def p_corchetes_corchete(t):
    'CORCHETES : CORCHETE'
    t[0] = [t[1]]
    #region
    global contador, conNode, fgraph,corcheList, bandera,corcheListaux    
    if len(corcheList) != 0:
        bandera = 1
        corcheListaux = corcheList[:]
    else:
        bandera = 0

    fgraph.write("n00"+str(conNode+1)+" [label=\"CORCHETE\"] ;\n")
    #print(senteList)
    for i in senteList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    corcheList[:] = []
    corcheList.append(conNode+1)
    conNode += 2
    #endregion

def p_corchete(t):
    'CORCHETE : CORIZQ F CORDER'
    t[0] = t[2]
    #region
    global contador, conNode, fgraph, senteList,csList
    fgraph.write("n00"+str(conNode+1)+";\n")   #f
    fgraph.write("n00"+str(conNode+1)+" [label=\"[\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" [label=\"F\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
    fgraph.write("n00"+str(conNode+3)+" [label=\"]\"] ;\n")
    senteList.append(conNode+1)
    senteList.append(conNode+2)
    senteList.append(conNode+3)
    csList[:] = []
    conNode += 3
    #endregion

def p_expresion_ato(t):
    'EXPRESION    :  ATOMICO'
    t[0] = t[1]
    #region
    global contador, conNode, fgraph
    fgraph.write("n00"+str(conNode+1)+";\n")   #f
    fgraph.write("n00"+str(conNode+1)+" [label=\"ATOMICO\"] ;\n")
    fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(conNode)+";\n")
    conNode += 1
    #endregion

def p_expresion_fun(t):
    'EXPRESION    :  FUNCION'
    t[0] = t[1]
    #region
    global contador, conNode, fgraph
    fgraph.write("n00"+str(conNode+1)+";\n")   #f
    fgraph.write("n00"+str(conNode+1)+" [label=\"FUNCION\"] ;\n")
    for i in senteList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    conNode += 1
    #endregion

def p_expresion_ope(t):
    'EXPRESION    :  OPERACION'
    t[0] = t[1]
    #region
    global contador, conNode, fgraph,senteList
    fgraph.write("n00"+str(conNode+1)+";\n")   #f
    fgraph.write("n00"+str(conNode+1)+" [label=\"OPERACION\"] ;\n")
    for i in senteList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    conNode += 1
    #endregion

def p_operacion(t):
    '''OPERACION    : F OPERADOR F
                    | MENOS F
                    | NOTLOGICA F
                    | NOTBIT F
                    | ANDBIT F'''

    #code
    #aritmetics
    #region
    global contador, conNode, fgraph,senteList,corcheList
    if len(t) == 4:

        fgraph.write("n00"+str(conNode+1)+" [label=\"F\"] ;\n")
        
        fgraph.write("n00"+str(conNode+2)+" [label=\""+t[2]+"\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+" [label=\"F\"] ;\n")
        for i in csList:
            fgraph.write("n00"+str(conNode+3)+" -- "+"n00"+str(i)+";\n")
        csList[:] = []
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        conNode += 3
    #endregion
    #print(str(t[1]) +", "+str(t[2]))
    if(t[2] == '+'):
        print(f'linea: {t.lineno(0)}')
        print(f'linea: {t.lineno(1)}')
        print(f'linea: {t.lineno(2)}')
        print(f'linea: {t.lineno(3)}')
        t[0] = BinaryExpression(t[1],t[3],Aritmetics.MAS, t.lineno(2), t.lexpos(2))        
    elif(t[2] == '-'): t[0] = BinaryExpression(t[1],t[3],Aritmetics.MENOS, t.lineno(2), t.lexpos(2))
    elif(t[2] == '*'): t[0] = BinaryExpression(t[1],t[3],Aritmetics.POR, t.lineno(2), t.lexpos(2))
    elif(t[2] == '/'): t[0] = BinaryExpression(t[1],t[3],Aritmetics.DIV, t.lineno(2), t.lexpos(2))
    elif(t[2] == '%'): t[0] = BinaryExpression(t[1],t[3], Aritmetics.MODULO, t.lineno(2), t.lexpos(2))
    #unitaries
    elif(t[1] == '-'): 
        t[0] = NegativeNumber(t[2], t.lineno(2), t.lexpos(2))
        #region
        fgraph.write("n00"+str(conNode+1)+";\n")   #-
        fgraph.write("n00"+str(conNode+1)+" [label=\""+t[1]+"\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #f
        fgraph.write("n00"+str(conNode+2)+" [label=\"F\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        conNode += 2
        #endregion

    elif(t[1] == '!'): 
        t[0] = Not(t[2], t.lineno(2), t.lexpos(2))
        #region
        fgraph.write("n00"+str(conNode+1)+";\n")   #!
        fgraph.write("n00"+str(conNode+1)+" [label=\""+t[1]+"\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #f
        fgraph.write("n00"+str(conNode+2)+" [label=\"F\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        conNode += 2
        #endregion

    elif(t[1] == '~'): 
        t[0] = NotBit(t[2], t.lineno(1), t.lexpos(1))
        #region
        fgraph.write("n00"+str(conNode+1)+";\n")   #~
        fgraph.write("n00"+str(conNode+1)+" [label=\""+t[1]+"\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #f
        fgraph.write("n00"+str(conNode+2)+" [label=\"F\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        conNode += 2
        #endregion

    #relational and logical
    elif(t[2] == '&&'): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.AND, t.lineno(2), t.lexpos(2))
    elif(t[2] == '||'): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.OR, t.lineno(2), t.lexpos(2))
    elif(t[2] == 'xor'): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.XOR, t.lineno(2), t.lexpos(2))
    elif(t[2] == '=='): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.IGUALQUE, t.lineno(2), t.lexpos(2))
    elif(t[2] == '!='): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.DIFERENTE, t.lineno(2), t.lexpos(2))
    elif(t[2] == '>='): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.MAYORIGUAL, t.lineno(2), t.lexpos(2))
    elif(t[2] == '<='): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.MENORIGUAL, t.lineno(2), t.lexpos(2))
    elif(t[2] == '>'): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.MAYORQUE, t.lineno(2), t.lexpos(2))
    elif(t[2] == '<'): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.MENORQUE, t.lineno(2), t.lexpos(2))
    #bit to bit
    elif(t[2] == '&'): 
        t[0] = RelationalBit(t[1],t[3], BitToBit.ANDBIT, t.lineno(1), t.lexpos(1))
        #region
        fgraph.write("n00"+str(conNode+1)+";\n")   #&
        fgraph.write("n00"+str(conNode+1)+" [label=\""+str(t[1])+"\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #f
        fgraph.write("n00"+str(conNode+2)+" [label=\"F\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        conNode += 2
        #endregion

    elif(t[2] == '|'): t[0] = RelationalBit(t[1],t[3], BitToBit.ORBIT, t.lineno(1), t.lexpos(1))
    elif(t[2] == '^'): t[0] = RelationalBit(t[1],t[3], BitToBit.XORBIT, t.lineno(1), t.lexpos(1))
    elif(t[2] == '<<'): t[0] = RelationalBit(t[1],t[3], BitToBit.SHIFTI, t.lineno(1), t.lexpos(1))
    elif(t[2] == '>>'): t[0] = RelationalBit(t[1],t[3], BitToBit.SHIFTD, t.lineno(1), t.lexpos(1))

def p_numero(t):
    'ATOMICO     : F'
    t[0] = t[1]
    #region
    global contador,fgraph, conNode,csList
    fgraph.write("n00"+str(conNode+1)+";\n")   #node
    fgraph.write("n00"+str(conNode+1)+" [label=\"F\"] ;\n")
    for i in csList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    csList[:] = []
    conNode += 1
    #endregion

def p_funcion(t):
    '''FUNCION      : ABS PARIZQ EXPRESION PARDER
                    | READ PARIZQ PARDER
                    | PARIZQ TIPO PARDER ID
                    | ARRAY PARIZQ PARDER'''
    
    global contador, conNode, fgraph
    if(t[1] == 'abs'):      
        t[0] = Abs(t[3], t.lineno(3), t.lexpos(3))
        #region
        fgraph.write("n00"+str(conNode+1)+";\n")   #abs
        fgraph.write("n00"+str(conNode+1)+" [label=\""+ str(t[1])+"\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #(
        fgraph.write("n00"+str(conNode+2)+" [label=\""+ str(t[2])+"\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+";\n")   #expresion
        fgraph.write("n00"+str(conNode+3)+" [label=\"EXPRESION\"] ;\n")        
        fgraph.write("n00"+str(conNode+3)+" -- "+"n00"+str(conNode)+";\n")
        fgraph.write("n00"+str(conNode+4)+";\n")   #)
        fgraph.write("n00"+str(conNode+4)+" [label=\""+ str(t[4])+"\"] ;\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        senteList.append(conNode+4)
        conNode +=4
        #endregion

    elif(t[1] == 'read'):   
        t[0] = ReadConsole(t.lineno(1), t.lexpos(1))
        #region
        fgraph.write("n00"+str(conNode+1)+" [label=\""+ str(t[1])+"\"] ;\n") #read
        fgraph.write("n00"+str(conNode+2)+" [label=\""+ str(t[2])+"\"] ;\n") #(
        fgraph.write("n00"+str(conNode+3)+" [label=\""+ str(t[3])+"\"] ;\n")  #)
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        conNode +=3
        #endregion

    elif(t[1] == '('):        
         
        t[0] = Cast_(Identifier(t[4], t.lineno(4), t.lexpos(4)),t[2], t.lineno(2), t.column(2))
        #region
        fgraph.write("n00"+str(conNode+1)+";\n")   #(
        fgraph.write("n00"+str(conNode+1)+" [label=\""+ str(t[1])+"\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #tipo
        fgraph.write("n00"+str(conNode+2)+" [label=\"TIPO\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
        fgraph.write("n00"+str(conNode+3)+";\n")   #)
        fgraph.write("n00"+str(conNode+3)+" [label=\""+ str(t[3])+"\"] ;\n")
        fgraph.write("n00"+str(conNode+4)+";\n")   #id
        fgraph.write("n00"+str(conNode+4)+" [label=\""+ str(t[4])+"\"] ;\n")

        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        senteList.append(conNode+4)
        conNode +=5
        #endregion

    elif(t[1] == 'array'):  
        t[0] = t[1]  #devolvemos la palabra array
        #region
        fgraph.write("n00"+str(conNode+1)+";\n")   #array
        fgraph.write("n00"+str(conNode+1)+" [label=\""+ str(t[1])+"\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #(
        fgraph.write("n00"+str(conNode+2)+" [label=\""+ str(t[2])+"\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+";\n")   #)
        fgraph.write("n00"+str(conNode+3)+" [label=\""+ str(t[3])+"\"] ;\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        conNode +=3
        #endregion

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

    t[0] = t[1]
    #region
    global contador, conNode, fgraph
    conNode += 1
    fgraph.write("n00"+str(conNode)+";\n")   #node
    fgraph.write("n00"+str(conNode)+" [label=\""+ str(t[1])+"\"] ;\n")
    conNode += 1
    #endregion

def p_tipo(t):
    ''' TIPO    : INT
                | FLOAT
                | CHAR'''
    
    t[0] = t[1]
    #region
    global contador, conNode, fgraph
    fgraph.write("n00"+str(conNode)+";\n")   #node
    fgraph.write("n00"+str(conNode)+" [label=\""+ str(t[1])+"\"] ;\n")
    #endregion

def p_f_numero(t):
    'F  : NUMERO'
    t[0] = Number(t.lineno(1), t.lexpos(1), t[1])
    #region
    global contador, conNode, fgraph,csList
    fgraph.write("n00"+str(conNode)+";\n")   #node
    fgraph.write("n00"+str(conNode)+" [label=\""+ str(t[1])+"\"] ;\n")
    csList.append(conNode)
    #endregion

def p_f_id(t):
    'F  : ID'
    t[0] = Identifier(t[1], t.lineno(1), t.lexpos(1))
    #region
    global contador, conNode, fgraph,corcheList
    fgraph.write("n00"+str(conNode)+";\n")   #node
    fgraph.write("n00"+str(conNode)+" [label=\""+ str(t[1])+"\"] ;\n")
    csList.append(conNode)
    #endregion

def p_f_idARRAY(t):
    'F  : ID CORCHETES'
    t[0] = IdentifierArray(t[1],t[2],t.lineno(1), t.lexpos(1))
    #region
    global contador, conNode, fgraph,corcheList
    fgraph.write("n00"+str(conNode+1)+" [label=\""+t[1]+"\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" [label=\"CORCHETES\"] ;\n")
    
    for i in corcheList:
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(i)+";\n")
    corcheList[:] = []
    csList.append(conNode+1)
    csList.append(conNode+2)
    conNode += 2
    #endregion

def p_f_cadena(t):
    'F  : CADENA'
    #region
    global contador, conNode, fgraph,corcheList
    fgraph.write("n00"+str(conNode)+";\n")   #node
    fgraph.write("n00"+str(conNode)+" [label=\""+ str(t[1])+"\"] ;\n")
    csList.append(conNode)
    #endregion
    t[0] = String_(t[1], t.lineno(1), t.lexpos(1))

def p_f_char(t):
    'F  : CHAR_'
    #region
    global contador, conNode, fgraph,corcheList
    fgraph.write("n00"+str(conNode)+";\n")   #node
    fgraph.write("n00"+str(conNode)+" [label=\""+ str(t[1])+"\"] ;\n")
    csList.append(conNode)
    #endregion
    t[0] = String_(t[1], t.lineno(1), t.lexpos(1))

def p_error(t):
    print("Error sintactico en '%s'" % t.value + "line: "+ str(t.lineno))
    global sintacticErroList
    so = sinOb(t.value, t.lineno, t.lexpos)
    sintacticErroList.append(so)
   

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    global input_, fgraph, primeravez, treeList, contador, contadorSente, conNode, senteList, senteList_, corcheList, bandera
    global corcheListaux, csList, sentenciaHija, res, fgraph, sintacticErroList, LexicalErrosList
    primeravez = 0
    treeList = [] #list for save nodes
    contador = 0
    contadorSente = 1
    conNode = 1
    senteList = [] #para guardar las sentencias y despues apuntarlas
    senteList_ = []
    corcheList = []
    bandera = 0
    corcheListaux = []
    corcheListaux = []
    csList = []
    sentenciaHija = 0
    bandera = 0
    res = []
    fgraph = ''
    sintacticErroList[:] = []
    LexicalErrosList[:] =[]

    input_ = input
    fgraph = open('../reports/ast.dot','a') #creamos el archivo
    fgraph.write("\n") 
    #print(input_)
    instructions = parser.parse(input)
    lexer.lineno = 1
    parser.restart()
    if len(LexicalErrosList) > 0 or len(sintacticErroList) > 0:
        if instructions == None:
            instructions = []
        else:
            instructions[:] = []
        return instructions
    return instructions
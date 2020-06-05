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
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


import ply.lex as lex
lexer = lex.lex()


#sintactic

#construction the ast
from expressions import *
from instructions import *
from nodeAST import *

primeravez = 0
treeList = [] #list for save nodes
contador = 0
contadorSente = 1
conNode = 1
senteList = [] #para guardar las sentencias y despues apuntarlas
senteList_ = []
sentenciaHija = 0

fgraph = open('./ast.dot','a') #creamos el archivo
fgraph.write("\n") 

#definition of grammar 

def p_init(t):
    'S : A'
    #code (sintetize result the A to S)
    t[0] = t[1]
    #print("result the t[0]: " + str(t[0]))
    #print(treeList)
    #print(len(treeList))
    global fgraph,senteList
    global contador, conNode
    node = node_("A",t[1],contador)
    
    treeList.append(node)
    node = node_("S",t[0],contador)
    contador += 1;
    treeList.append(node)
    
    fgraph.write("n00"+str(conNode+1)+" [label=\"A\"] ;\n")
    for i in senteList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    contador += 1;
    fgraph.write("n00"+str(conNode+2)+" [label=\"S\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode+1)+";\n")
    conNode +=3
    
    fgraph.close()

    ####ejecutar analisis
    """treeList.reverse()
    fgraph = open('./ast.dot','a') #creamos el archivo
    fgraph.write("\n")  
    level = treeList[0].level
    si = 0
    for i in treeList:
        if i.level == level:
            #if si == 1:
                #fgraph.write(str(i.label)+"_"+str(i.level)+" ")
                #print(str(i.label))
                
            #else:
                #fgraph.write("\""+str(i.label)+"_"+str(i.level))
                #si = 1
            print("etiqueta: "+ str(i.label) + " , level: "+ str(i.level) +" , sente: " + str(i.sente))

        else:
            #si = 0
            #fgraph.write("\"->")
            print("--->")
            level -= 1
            #fgraph.write("\""+str(i.label)+"_"+str(i.level))
            #si = 1
            #print(str(i.label))
            print("etiqueta: "+ str(i.label) + " , level: "+ str(i.level) +" , sente: " + str(i.sente))

    fgraph.write("\"")
    fgraph.close()"""

def RecursiveFunction(padre):
    print("sdd")


def p_main(t):
    'A : MAIN DOSPUNTOS SENTENCIAS'
    #solo agrego las sentencias 
    t[0] = t[3]

    global contador, conNode, fgraph, treeList
    node = node_("MAIN",t[1],contador)
    node1 = node_(":",t[2],contador)
    node2 = node_("SENTENCIAS",t[3],contador)
    contador += 1;

    treeList.append(node)
    treeList.append(node1)
    treeList.append(node2)

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

def p_sentencias_lista(t):
    'SENTENCIAS   : SENTENCIAS SENTENCIA'

    t[1].append(t[2])
    t[0] = t[1]

    global contador, conNode, fgraph, sentenciaHija, senteList_
    global contadorSente
    node = node_("SENTENCIAS",t[1],contador,contadorSente)
    node1 = node_("SENTENCIA",t[2],contador,contadorSente)
    contador += 1;
    contadorSente += 1
    treeList.append(node)
    treeList.append(node1)

    print(senteList_)
    fgraph.write("n00"+str(conNode+1)+" [label=\"SENTENCIAS\"] ;\n")
    for i in senteList_:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList_[:] = []
    fgraph.write("n00"+str(conNode+2)+" [label=\"SENTENCIA\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode-1)+";\n")
    senteList_.append(conNode +1)
    senteList_.append(conNode +2)
    conNode +=3

def p_sentecias_sentencia(t):
    'SENTENCIAS     : SENTENCIA'
    t[0] = [t[1]]

    global contador, conNode, fgraph, sentenciaHija, primeravez
    global contadorSente
    node = node_("SENTENCIA",t[1],contador,contadorSente)
    contador += 1;
    contadorSente += 1
    treeList.append(node)

    fgraph.write("n00"+str(conNode+1)+" [label=\"SENTENCIA\"] ;\n")
    if primeravez == 0:
        primeravez = 1
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(conNode-1)+";\n")
    else:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(conNode)+";\n")

    senteList_.append(conNode+1)
    conNode += 2

def p_sentencia_eti(t):
    'SENTENCIA    : ETIQUETA'

    t[0] = t[1]

    global contador
    node = node_("ETIQUETA",t[1],contador)
    contador += 1;
    treeList.append(node)

def p_sentencia_instr(t):
    'SENTENCIA    :  INSTRUCCIONES'

    t[0] = t[1]

    global contador, conNode, fgraph, senteList, treeList 
    node = node_("INSTRUCCIONES",t[1],contador)
    contador += 1
    treeList.append(node)

    fgraph.write("n00"+str(conNode+1)+" [label=\"INSTRUCCIONES\"] ;\n")
    #print(senteList)
    for i in senteList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    print(senteList)
    conNode +=2

def p_sentencia_decla(t):
    'SENTENCIA    :  DECLARACIONES'

    t[0] = t[1]

    global contador, conNode, fgraph, senteList
    node = node_("DECLARACIONES",t[1],contador)
    contador += 1;
    treeList.append(node)

    fgraph.write("n00"+str(conNode+1)+" [label=\"DECLARACIONES\"] ;\n")
    for i in senteList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    conNode +=2
                
def p_etiqueta(t):
    # i call label to recognize the label

    'ETIQUETA   : LABEL DOSPUNTOS' 
    t[0] = t[1]
    
    global contador
    node = node_("LABEL",t[1],contador)
    node1 = node_(":",t[2],contador)
    contador += 1;
    treeList.append(node)
    treeList.append(node1)

def p_instrucciones(t):
    '''INSTRUCCIONES    : PRINT PARIZQ EXPRESION PARDER PUNTOCOMA
                        | IF PARIZQ EXPRESION PARDER GOTO LABEL PUNTOCOMA
                        | UNSET PARIZQ ID PARDER PUNTOCOMA
                        | EXIT PUNTOCOMA
                        | GOTO LABEL PUNTOCOMA'''

    global contador, conNode, fgraph, senteList
    if(t[1] == 'print'): 
        t[0] = Print_(t[3])
        
        node = node_("print",t[1],contador)
        node1 = node_("(",t[2],contador)
        node2 = node_(" EXPRESION",t[3],contador)
        node3 = node_(")",t[4],contador)
        node4 = node_(";",t[5],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)
        treeList.append(node2)
        treeList.append(node3)
        treeList.append(node4)

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

        

    elif(t[1] == 'if'): 
        t[0] = If(t[3])

        node = node_("if",t[1],contador)
        node1 = node_("(",t[2],contador)
        node2 = node_(" EXPRESION",t[3],contador)
        node3 = node_(")",t[4],contador)
        node4 = node_("goto",t[5],contador)
        node5 = node_("LABEL",t[6],contador)
        node6 = node_(";",t[7],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)
        treeList.append(node2)
        treeList.append(node3)
        treeList.append(node4)
        treeList.append(node5)
        treeList.append(node6)

    elif(t[1] == 'unset'): 
        t[0] = Unset(t[3])

        node = node_("unset",t[1],contador)
        node1 = node_("(",t[2],contador)
        node2 = node_(" ID",t[3],contador)
        node3 = node_(")",t[4],contador)
        node4 = node_(";",t[5],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)
        treeList.append(node2)
        treeList.append(node3)
        treeList.append(node4)

    elif(t[1] == 'goto'): 
        t[0] = Unset(t[2])

        node = node_("goto",t[1],contador)
        node1 = node_("LABEL",t[2],contador)
        node2 = node_(" ;",t[3],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)
        treeList.append(node2)

    elif(t[1] == 'exit'): 
        t[0] = Exit();

        node = node_("exit",t[1],contador)
        node1 = node_(";",t[2],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)


def p_declaraciones(t):
    'DECLARACIONES  : ID ARRAY_'
    
    #insertion a new variable
    t[0] = Declaration(t[1], t[2])

    global contador, conNode, fgraph, senteList
    node = node_("ID",t[1],contador)
    node1 = node_("ARRAY_",t[2],contador)
    contador += 1;
    treeList.append(node)
    treeList.append(node1)

    fgraph.write("n00"+str(conNode+1)+" [label=\""+t[1]+"\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" [label=\"ARRAY_\"] ;\n")    
    for i in senteList:
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    senteList.append(conNode+1)
    senteList.append(conNode+2)
    conNode +=3

def p_array(t):
    '''ARRAY_    :  CORCHETES IGUAL EXPRESION PUNTOCOMA
                | IGUAL EXPRESION PUNTOCOMA'''

    global contador, conNode, fgraph, senteList
    if t[1] == '=':
        node = node_("IGUAL",t[1],contador)
        node1 = node_("EXPRESION",t[2],contador)
        node2 = node_("PUNTOCOMA",t[3],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)
        treeList.append(node2)

        fgraph.write("n00"+str(conNode+1)+" [label=\"=\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" [label=\"EXPRESION\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
        fgraph.write("n00"+str(conNode+3)+" [label=\";\"] ;\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        conNode += 4
    
    else:
        node = node_("CORCHETES",t[1],contador)
        node1 = node_("=",t[2],contador)
        node2 = node_("EXPRESION",t[3],contador)
        node3 = node_(";",t[4],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)
        treeList.append(node2)
        treeList.append(node3)

    if(t[1] == '='): t[0] = t[2]  #if expresion is array, expression contain 'array'

def p_corchete_lista(t):
    'CORCHETES : CORCHETES CORCHETE'
    t[1].append(t[2])
    t[0] = t[1]

    global contador, conNode, fgraph
    node = node_("CORCHETES",t[1],contador)
    node1 = node_("CORCHETE",t[2],contador)
    contador += 1;
    treeList.append(node)
    treeList.append(node1)

    fgraph.write("n00"+str(conNode+1)+" [label=\"CORCHETES\"] ;\n")
    fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(conNode)+";\n")
    fgraph.write("n00"+str(conNode+2)+" [label=\"CORCHETE\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode-1)+";\n")
    conNode += 3

    
def p_corchetes_corchete(t):
    'CORCHETES : CORCHETE'
    t[0] = [t[1]]

    global contador, conNode, fgraph
    node = node_("CORCHETE",t[1],contador)
    contador += 1;
    treeList.append(node)

    fgraph.write("n00"+str(conNode+1)+" [label=\"CORCHETE\"] ;\n")
    fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(conNode)+";\n")
    fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(conNode-1)+";\n")
    fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(conNode-2)+";\n")
    conNode += 2

def p_corchete(t):
    'CORCHETE : CORIZQ F CORDER'
    t[0] = t[2]

    global contador, conNode, fgraph
    node = node_("[",t[1],contador)
    node1 = node_("F",t[2],contador)
    node2 = node_("]",t[2],contador)
    contador += 1;
    treeList.append(node)
    treeList.append(node1)
    treeList.append(node2)

    fgraph.write("n00"+str(conNode+1)+";\n")   #f
    fgraph.write("n00"+str(conNode+1)+" [label=\"[\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" [label=\"F\"] ;\n")
    fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
    fgraph.write("n00"+str(conNode+3)+" [label=\"]\"] ;\n")
    conNode += 4


def p_expresion_ato(t):
    'EXPRESION    :  ATOMICO'
    t[0] = t[1]
    global contador, conNode, fgraph
    node = node_("ATOMICO",t[1],contador)
    contador += 1;
    treeList.append(node)

    fgraph.write("n00"+str(conNode+1)+";\n")   #f
    fgraph.write("n00"+str(conNode+1)+" [label=\"ATOMICO\"] ;\n")
    fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(conNode)+";\n")
    conNode += 1

def p_expresion_fun(t):
    'EXPRESION    :  FUNCION'
    t[0] = t[1]
    global contador, conNode, fgraph
    node = node_("FUNCION",t[1],contador)
    contador += 1;
    treeList.append(node)

    fgraph.write("n00"+str(conNode+1)+";\n")   #f
    fgraph.write("n00"+str(conNode+1)+" [label=\"FUNCION\"] ;\n")
    for i in senteList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    conNode += 1

def p_expresion_ope(t):
    'EXPRESION    :  OPERACION'
    t[0] = t[1]

    global contador, conNode, fgraph,senteList
    node = node_("OPERACION",t[1],contador)
    contador += 1;
    treeList.append(node)

    fgraph.write("n00"+str(conNode+1)+";\n")   #f
    fgraph.write("n00"+str(conNode+1)+" [label=\"OPERACION\"] ;\n")
    for i in senteList:
        fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(i)+";\n")
    senteList[:] = []
    conNode += 1

def p_operacion(t):
    '''OPERACION    : F OPERADOR F
                    | MENOS F
                    | NOTLOGICA F
                    | NOTBIT F
                    | ANDBIT F
                    | ID CORCHETES '''

    #PENDIENTEE    ID CORCHETES PARA GRAFICAR

    #code
    #aritmetics
    global contador, conNode, fgraph
    if len(t) == 4:
        node = node_("F",t[1],contador)
        node1 = node_("OPERADOR",t[2],contador)
        node2 = node_("F",t[3],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)
        treeList.append(node2)

        fgraph.write("n00"+str(conNode+1)+";\n")   #f
        fgraph.write("n00"+str(conNode+1)+" [label=\"F\"] ;\n")
        #fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(conNode-1)+";\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #operador
        fgraph.write("n00"+str(conNode+2)+" [label=\""+t[2]+"\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+";\n")   #f
        fgraph.write("n00"+str(conNode+3)+" [label=\"F\"] ;\n")
        fgraph.write("n00"+str(conNode+3)+" -- "+"n00"+str(conNode)+";\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        conNode += 3

    if(t[2] == '+'): t[0] = BinaryExpression(t[1],t[3],Aritmetics.MAS)        
    elif(t[2] == '-'): t[0] = BinaryExpression(t[1],t[3],Aritmetics.MENOS)
    elif(t[2] == '*'): t[0] = BinaryExpression(t[1],t[3],Aritmetics.POR)
    elif(t[2] == '/'): t[0] = BinaryExpression(t[1],t[3],Aritmetics.DIV)
    elif(t[2] == '%'): t[0] = BinaryExpression(t[1],t[3], Aritmetics.MODULO)
    #unitaries
    elif(t[1] == '-'): 
        t[0] = NegativeNumber(t[2])
        node = node_("-",t[1],contador)
        node1 = node_("F",t[2],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)

        fgraph.write("n00"+str(conNode+1)+";\n")   #-
        fgraph.write("n00"+str(conNode+1)+" [label=\""+t[1]+"\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #f
        fgraph.write("n00"+str(conNode+2)+" [label=\"F\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        conNode += 2

    elif(t[1] == '!'): 
        t[0] = Not(t[2])
        node = node_("-",t[1],contador)
        node1 = node_("F",t[2],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)

        fgraph.write("n00"+str(conNode+1)+";\n")   #!
        fgraph.write("n00"+str(conNode+1)+" [label=\""+t[1]+"\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #f
        fgraph.write("n00"+str(conNode+2)+" [label=\"F\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        conNode += 2

    elif(t[1] == '~'): 
        t[0] = NotBit(t[2])
        node = node_("-",t[1],contador)
        node1 = node_("F",t[2],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)

        fgraph.write("n00"+str(conNode+1)+";\n")   #~
        fgraph.write("n00"+str(conNode+1)+" [label=\""+t[1]+"\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #f
        fgraph.write("n00"+str(conNode+2)+" [label=\"F\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        conNode += 2

    #relational and logical
    elif(t[2] == '&&'): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.AND)
    elif(t[2] == '||'): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.OR)
    elif(t[2] == 'xor'): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.XOR)
    elif(t[2] == '=='): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.IGUALQUE)
    elif(t[2] == '!='): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.DIFERENTE)
    elif(t[2] == '>='): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.MAYORIGUAL)
    elif(t[2] == '<='): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.MENORIGUAL)
    elif(t[2] == '>'): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.MAYORQUE)
    elif(t[2] == '<'): t[0] = LogicAndRelational(t[1],t[3], LogicsRelational.MENORQUE)
    #bit to bit
    elif(t[2] == '&'): 
        t[0] = RelationalBit(t[1],t[3], BitToBit.ANDBIT)
        node = node_("-",t[1],contador)
        node1 = node_("F",t[2],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)

        fgraph.write("n00"+str(conNode+1)+";\n")   #&
        fgraph.write("n00"+str(conNode+1)+" [label=\""+t[1]+"\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #f
        fgraph.write("n00"+str(conNode+2)+" [label=\"F\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        conNode += 2

    elif(t[2] == '|'): t[0] = RelationalBit(t[1],t[3], BitToBit.ORBIT)
    elif(t[2] == '^'): t[0] = RelationalBit(t[1],t[3], BitToBit.XORBIT)
    elif(t[2] == '<<'): t[0] = RelationalBit(t[1],t[3], BitToBit.SHIFTI)
    elif(t[2] == '>>'): t[0] = RelationalBit(t[1],t[3], BitToBit.SHIFTD)
    
    else: 
        t[0] = IdentifierArray(t[1],t[2])
        
        fgraph.write("n00"+str(conNode+1)+";\n")   #id
        fgraph.write("n00"+str(conNode+1)+" [label=\""+t[1]+"\"] ;\n")
        fgraph.write("n00"+str(conNode+2)+";\n")   #corchetes
        fgraph.write("n00"+str(conNode+2)+" [label=\"CORCHETES\"] ;\n")  ##3debo hacer un for para sus hijos
        fgraph.write("n00"+str(conNode+2)+" -- "+"n00"+str(conNode)+";\n")
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        conNode += 2


def p_numero(t):
    'ATOMICO     : F'
    t[0] = t[1]

    global contador
    node = node_("F",t[1],contador)
    #contador += 1;
    treeList.append(node)

    
    global fgraph, conNode
    fgraph.write("n00"+str(conNode+1)+";\n")   #node
    fgraph.write("n00"+str(conNode+1)+" [label=\"F\"] ;\n")
    fgraph.write("n00"+str(conNode+1)+" -- "+"n00"+str(conNode)+";\n")
    conNode += 1

def p_funcion(t):
    '''FUNCION      : ABS PARIZQ EXPRESION PARDER
                    | READ PARIZQ PARDER
                    | PARIZQ TIPO PARDER ID
                    | ARRAY PARIZQ PARDER'''
    
    global contador, conNode, fgraph
    if(t[1] == 'abs'):      
        t[0] = Abs(t[3])
        node = node_("abs",t[1],contador)
        node1 = node_("(",t[2],contador)
        node2 = node_("EXPRESION",t[3],contador)
        node3 = node_(")",t[4],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)
        treeList.append(node2)
        treeList.append(node3)

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


    elif(t[1] == 'read'):   
        t[0] = ReadConsole()
        node = node_("read",t[1],contador)
        node1 = node_("(",t[2],contador)
        node2 = node_(")",t[3],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)
        treeList.append(node2)

        fgraph.write("n00"+str(conNode+1)+" [label=\""+ str(t[1])+"\"] ;\n") #read
        fgraph.write("n00"+str(conNode+2)+" [label=\""+ str(t[2])+"\"] ;\n") #(
        fgraph.write("n00"+str(conNode+3)+" [label=\""+ str(t[3])+"\"] ;\n")  #)
        senteList.append(conNode+1)
        senteList.append(conNode+2)
        senteList.append(conNode+3)
        conNode +=3

    elif(t[1] == '('):        
         
        t[0] = Cast_(Identifier(t[4]),t[2])
        node = node_("(",t[1],contador)
        node1 = node_("TIPO",t[2],contador)
        node2 = node_(")",t[3],contador)
        node3 = node_("ID",t[4],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)
        treeList.append(node2)
        treeList.append(node3)

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

    elif(t[1] == 'array'):  
        t[0] = t[1]  #devolvemos la palabra array
        node = node_("array",t[1],contador)
        node1 = node_("(",t[2],contador)
        node2 = node_(")",t[3],contador)
        contador += 1;
        treeList.append(node)
        treeList.append(node1)
        treeList.append(node2)

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
    
    global contador, conNode, fgraph
    fgraph.write("n00"+str(conNode)+";\n")   #node
    fgraph.write("n00"+str(conNode)+" [label=\""+ str(t[1])+"\"] ;\n")

    node = node_("OPERADOR",t[1],contador)
    contador += 1;
    treeList.append(node)

def p_tipo(t):
    ''' TIPO    : INT
                | FLOAT
                | CHAR'''
    
    t[0] = t[1]
    
    global contador, conNode, fgraph
    fgraph.write("n00"+str(conNode)+";\n")   #node
    fgraph.write("n00"+str(conNode)+" [label=\""+ str(t[1])+"\"] ;\n")
    
    node = node_("TIPO_",t[1],contador)
    contador += 1;
    treeList.append(node)

def p_f_numero(t):
    'F  : NUMERO'
    print(str(t[1]))
    t[0] = Number(t[1])
    
    global contador, conNode, fgraph
    fgraph.write("n00"+str(conNode)+";\n")   #node
    fgraph.write("n00"+str(conNode)+" [label=\""+ str(t[1])+"\"] ;\n")

    node = node_("NUMERO",t[1],contador)
    contador += 1;
    treeList.append(node)

def p_f_id(t):
    'F  : ID'
    t[0] = Identifier(t[1])

    global contador, conNode, fgraph
    fgraph.write("n00"+str(conNode)+";\n")   #node
    fgraph.write("n00"+str(conNode)+" [label=\""+ str(t[1])+"\"] ;\n")
    
    node = node_("IDENTIFICADOR",t[1],contador)
    contador += 1;
    treeList.append(node)

def p_f_cadena(t):
    'F  : CADENA'

    global contador, conNode, fgraph
    fgraph.write("n00"+str(conNode)+";\n")   #node
    fgraph.write("n00"+str(conNode)+" [label=\""+ str(t[1])+"\"] ;\n")

    node = node_("CADENA",t[1],contador)
    contador += 1;
    treeList.append(node)

    t[0] = String_(t[1])

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    return parser.parse(input)
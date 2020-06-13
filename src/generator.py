class node():
    def __init__(self, padre, hijo,  valor):
        self.padre = padre
        self.hijo = hijo
        self.valor = valor

class genera() :
    def add(self, nodo):
        fgraph = open('../reports/graph.dot','a') #creamos el archivo
        fgraph.write(f"n00{str(nodo.padre)} -- n00{str(nodo.hijo)};\n")
        fgraph.write(f"n00{str(nodo.hijo)} [label=\"{nodo.valor}\"] ;\n")        
        fgraph.close()
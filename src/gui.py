# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PIL import Image
import grammar
import reportGenerator as rg
import execute
from expressions import *
from instructions import *
import SymbolTable as TS
import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
#from PyQt5.QtGui import QColor

contadorVentanas = 0
data = []
dataS = []
dataSema = []
dataTs = []
pasadas = 0

tsDebug = TS.SymbolTable()
printListDebug = []
instructionsDebug = []
printPases = []
conttadorIns = 0
from semanticObject import *
class Ui_Augus(object):
    
    def setupUi(self, Augus):        
        Augus.setObjectName("Augus")
        Augus.resize(980, 616)
        self.centralwidget = QtWidgets.QWidget(Augus)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 471, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.textEditConsole = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditConsole.setGeometry(QtCore.QRect(510, 20, 461, 541))
        self.textEditConsole.setObjectName("textEditConsole")
        self.textEditConsole.setStyleSheet('''background-color: rgb(33, 33, 33);
                                            border-color: rgb(18, 18, 18);
                                            color: rgb(51, 252, 255);
                                            font: 12pt \"consolas\";''' )
        self.textEditConsole.setPlainText("CONSOLE:\n")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(985, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Next")
        self.textDebug = QtWidgets.QTextEdit(self.centralwidget)
        self.textDebug.setGeometry(QtCore.QRect(985, 50, 480, 510))
        self.textDebug.setObjectName("textDebug")
        self.textDebug.setStyleSheet('''background-color: rgb(33, 33, 33);
                                            border-color: rgb(18, 18, 18);
                                            color: rgb(0, 255, 60);
                                            font: 12pt \"consolas\";''' )
        self.textDebug.setPlainText("DEBUG:\n")
        Augus.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Augus)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuEjecutar = QtWidgets.QMenu(self.menubar)
        self.menuEjecutar.setObjectName("menuEjecutar")
        self.menuOpciones = QtWidgets.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        self.menuReportes = QtWidgets.QMenu(self.menubar)
        self.menuReportes.setObjectName("menuReportes")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        Augus.setMenuBar(self.menubar)
       
        self.statusbar = QtWidgets.QStatusBar(Augus)
        self.statusbar.setObjectName("statusbar")
        Augus.setStatusBar(self.statusbar)
        self.actionNuevo = QtWidgets.QAction(Augus)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionReporteLexico = QtWidgets.QAction(Augus)
        self.actionReporteLexico.setObjectName("actionReporteLexico")
        self.actionReporteSintactico = QtWidgets.QAction(Augus)
        self.actionReporteSintactico.setObjectName("actionReporteSintactico")
        self.actionReporteSemantico = QtWidgets.QAction(Augus)
        self.actionReporteSemantico.setObjectName("actionReporteSemantico")
        self.actionReporteAST = QtWidgets.QAction(Augus)
        self.actionReporteAST.setObjectName("actionReporteAST")
        self.actionReporteTS = QtWidgets.QAction(Augus)
        self.actionReporteTS.setObjectName("actionReporteTS")
        self.actionAbrir = QtWidgets.QAction(Augus)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(Augus)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_Como = QtWidgets.QAction(Augus)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionCerrar = QtWidgets.QAction(Augus)
        self.actionCerrar.setObjectName("actionCerrar")
        self.actionSalir = QtWidgets.QAction(Augus)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCopiar = QtWidgets.QAction(Augus)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionPegar = QtWidgets.QAction(Augus)
        self.actionPegar.setObjectName("actionPegar")
        self.actionCortar = QtWidgets.QAction(Augus)
        self.actionCortar.setObjectName("actionCortar")
        self.actionBuscar = QtWidgets.QAction(Augus)
        self.actionBuscar.setObjectName("actionBuscar")
        self.actionAscendente = QtWidgets.QAction(Augus)
        self.actionAscendente.setObjectName("actionAscendente")
        self.actionDescendente = QtWidgets.QAction(Augus)
        self.actionDescendente.setObjectName("actionDescendente")
        self.actionDebuguer = QtWidgets.QAction(Augus)
        self.actionDebuguer.setObjectName("actionDebuguer")
        self.actionCambiar_color_de_fondo = QtWidgets.QAction(Augus)
        self.actionCambiar_color_de_fondo.setObjectName("actionCambiar_color_de_fondo")
        self.actionAyuda = QtWidgets.QAction(Augus)
        self.actionAyuda.setObjectName("actionAyuda")
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuReportes.addAction(self.actionReporteLexico)
        self.menuReportes.addAction(self.actionReporteSintactico)
        self.menuReportes.addAction(self.actionReporteSemantico)
        self.menuReportes.addAction(self.actionReporteAST)
        self.menuReportes.addAction(self.actionReporteTS)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addAction(self.actionCerrar)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuEditar.addAction(self.actionCopiar)
        self.menuEditar.addAction(self.actionPegar)
        self.menuEditar.addAction(self.actionCortar)
        self.menuEditar.addAction(self.actionBuscar)
        self.menuEjecutar.addAction(self.actionAscendente)
        self.menuEjecutar.addAction(self.actionDescendente)
        self.menuEjecutar.addAction(self.actionDebuguer)
        self.menuOpciones.addAction(self.actionCambiar_color_de_fondo)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuEjecutar.menuAction())
        self.menubar.addAction(self.menuOpciones.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(Augus)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Augus)

        #actions
        self.actionNuevo.triggered.connect(lambda : self.fn_Nuevo())
        self.actionAbrir.triggered.connect(lambda : self.fn_Abrir())
        self.actionAscendente.triggered.connect(lambda : self.fn_Ejecutar_Ascendente())
        self.actionDescendente.triggered.connect(lambda : self.fn_Ejecutar_Descendente())
        self.actionDebuguer.triggered.connect(lambda : self.fn_Ejecutar_Debuguer())
        self.actionGuardar.triggered.connect(lambda : self.fn_Guardar())
        self.actionGuardar_Como.triggered.connect(lambda : self.fn_Guardar_Como())
        self.actionCerrar.triggered.connect(lambda : self.fn_Cerrar())
        self.actionSalir.triggered.connect(lambda : self.fn_Salir())
        self.actionReporteLexico.triggered.connect(lambda : self.fn_repLexico())
        self.actionReporteSintactico.triggered.connect(lambda : self.fn_repSintactico())
        self.actionReporteSemantico.triggered.connect(lambda : self.fn_repSemantico())
        self.actionReporteAST.triggered.connect(lambda : self.fn_repAST())
        self.actionReporteTS.triggered.connect(lambda : self.fn_repTS())
        self.pushButton.clicked.connect(lambda : self.fn_Next())

    def retranslateUi(self, Augus):
        _translate = QtCore.QCoreApplication.translate
        Augus.setWindowTitle(_translate("Augus", "Augus"))
        self.menuArchivo.setTitle(_translate("Augus", "Archivo"))
        self.menuEditar.setTitle(_translate("Augus", "Editar"))
        self.menuEjecutar.setTitle(_translate("Augus", "Ejecutar"))
        self.menuOpciones.setTitle(_translate("Augus", "Opciones"))
        self.menuReportes.setTitle(_translate("Augus", "Reportes"))
        self.menuAyuda.setTitle(_translate("Augus", "Ayuda"))
        self.actionNuevo.setText(_translate("Augus", "Nuevo"))
        self.actionReporteLexico.setText(_translate("Augus", "Reporte Lexico"))
        self.actionReporteSintactico.setText(_translate("Augus", "Reporte Sintactico"))
        self.actionReporteSemantico.setText(_translate("Augus", "Reporte Semantico"))
        self.actionReporteTS.setText(_translate("Augus", "Reporte Tabla de Simbolos"))
        self.actionReporteAST.setText(_translate("Augus", "Reporte AST"))
        self.actionAbrir.setText(_translate("Augus", "Abrir"))
        self.actionGuardar.setText(_translate("Augus", "Guardar"))
        self.actionGuardar_Como.setText(_translate("Augus", "Guardar Como"))
        self.actionCerrar.setText(_translate("Augus", "Cerrar"))
        self.actionSalir.setText(_translate("Augus", "Salir"))
        self.actionCopiar.setText(_translate("Augus", "Copiar"))
        self.actionPegar.setText(_translate("Augus", "Pegar"))
        self.actionCortar.setText(_translate("Augus", "Cortar"))
        self.actionBuscar.setText(_translate("Augus", "Buscar"))
        self.actionAscendente.setText(_translate("Augus", "Ascendente"))
        self.actionDescendente.setText(_translate("Augus","Descendente"))
        self.actionDebuguer.setText(_translate("Augus","Debuguer"))
        self.actionCambiar_color_de_fondo.setText(_translate("Augus", "Cambiar color de fondo"))
        self.actionAyuda.setText(_translate("Augus", "Ayuda"))

    def fn_Nuevo(self):
        global contadorVentanas
        contadorVentanas += 1
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(0,0,460,520))
        self.textEdit.setStyleSheet('''background-color: rgb(33, 33, 33);
                                            border-color: rgb(18, 18, 18);
                                            color: rgb(255, 255, 255);
                                            font: 12pt \"consolas\";''' )
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(
            self.tab,"Tab "+ str(contadorVentanas)
        )
        self.tabWidget.setCurrentIndex(self.tabWidget.count()-1)    #para poner el focus en la nueva pestaña
        self.msgBox = QtWidgets.QMessageBox()
        self.msgBox.setText("New area.")
        self.msgBox.exec()

    def fn_Abrir(self):
        try:
            filename = QFileDialog.getOpenFileName(None,' Open document',r"c:\\Users\\", "All Files (*)")
            path = filename[0]
            print(path)
            with open(path, 'r') as f:
                data = f.read()
                            
                #creating a new tab
                self.tab = QtWidgets.QWidget()
                self.tab.setObjectName("tab")
                self.textEdit = QtWidgets.QTextEdit(self.tab)
                self.textEdit.setGeometry(QtCore.QRect(0,0,460,520))
                self.textEdit.setStyleSheet('''background-color: rgb(33, 33, 33);
                                            border-color: rgb(18, 18, 18);
                                            color: rgb(255, 255, 255);
                                            font: 12pt \"consolas\";''' )
                self.textEdit.setObjectName("textEdit")
                self.textEdit.setPlainText(data)
                self.tabWidget.addTab(
                    self.tab,path
                )
                self.tabWidget.setCurrentIndex(self.tabWidget.count()-1)    #para poner el focus en la nueva pestaña

                #close the file
                f.close()
        except:
            print("closing file dialog.")

    def fn_repAST(self):
        try:
            os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
            os.system('dot -Tpng ../reports/ast.dot -o ../reports/ast.png')

            ruta = ("../reports/ast.png")
            im = Image.open(ruta)
            im.show()
        except:
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("Error al crear reporte.")
            self.msgBox.setIcon(QtWidgets.QMessageBox.Critical)
            self.msgBox.exec()

    def fn_repTS(self):
        print("reporte de tabla de simbolos")
        try:
            fgraph = open('../reports/tsReport.dot','w+') #creamos el archivo
            fgraph.write("digraph H { parent [ shape=plaintext label=< <table border=\'1\' cellborder=\'1\'>")                    
            fgraph.write("<tr><td colspan=\"3\">REPORTE DE TABLA DE SIMBOLOS</td></tr>")
            fgraph.write("<tr><td port=\'port_one\'>ID</td><td port=\'port_two\'>TIPO</td><td port=\'port_three\'>VALOR</td><td port=\'port_four\'>DECLARADA EN</td><td port=\'port_five\'>DIMENSION</td><td port=\'port_six\'>REFERENCIA</td><td port=\'port_seven\'>PARAMETROS</td></tr>")
            
            for key, val in execute.tsGlobal.symbols.items():
                fgraph.write(f"<tr><td port=\'port_one\'>{str(key)}</td><td port=\'port_two\'>{str(val.tipo)}</td><td port=\'port_three\'>{str(val.valor)}</td><td port=\'port_four\'>{str(val.declarada)}</td><td port=\'port_five\'>{str(val.dimension)}</td><td port=\'port_six\'>{str(val.referencia)}</td><td port=\'port_seven\'>{str(val.parametros)}</td></tr>")
                        
            fgraph.write("</table> >]; }")
            fgraph.close()

            os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
            os.system('dot -Tpng ../reports/tsReport.dot -o ../reports/tsReport.png')    

            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("Reporte creado.")
            self.msgBox.setIcon(QtWidgets.QMessageBox.Information)
            self.msgBox.exec()

            ruta = ("../reports/tsReport.png")
            im = Image.open(ruta)
            im.show()

            execute.tsGlobal = {}
        except:
            print("error")
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("Error al crear el reporte.")
            self.msgBox.setIcon(QtWidgets.QMessageBox.Critical)
            self.msgBox.exec()

    def fn_repSemantico(self):
        print("reportando semantico")
        global dataSema
        try:
            rg.export_to_pdf(dataSema,3)
            dataSema[:] = []
            execute.semanticErrorList[:] = []         

            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("Despelgando reporte.")
            self.msgBox.setIcon(QtWidgets.QMessageBox.Information)
            self.msgBox.exec()
            import os
            os.startfile('..\\reports\\semanticReport.pdf')
        except:
            print("error")
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("Porfavor cierre el reporte de errores semanticos.")
            self.msgBox.setIcon(QtWidgets.QMessageBox.Critical)
            self.msgBox.exec()

    def fn_repSintactico(self):
        print("reportando sintactico")
        global dataS
        try:
            rg.export_to_pdf(dataS,2)
            dataS[:] = []
            grammar.sintacticErroList[:] = []           

            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("Despelgando reporte.")
            self.msgBox.setIcon(QtWidgets.QMessageBox.Information)
            self.msgBox.exec()
            import os
            os.startfile('..\\reports\\sintacticReport.pdf')
        except:
            print("error")
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("Porfavor cierre el reporte sintactico.")
            self.msgBox.setIcon(QtWidgets.QMessageBox.Critical)
            self.msgBox.exec()
    
    def fn_repLexico(self):
        print("reportando lexico")
        global data
        try:
            rg.export_to_pdf(data,1)
            data[:] = []
            grammar.LexicalErrosList[:] = []           

            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("Despelgando reporte.")
            self.msgBox.setIcon(QtWidgets.QMessageBox.Information)
            self.msgBox.exec()
            import os
            os.startfile('..\\reports\\lexicalReport.pdf')
        except:
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("please close report lexical.")
            self.msgBox.setIcon(QtWidgets.QMessageBox.Critical)
            self.msgBox.exec()

    def fn_Next(self):
        print("siguiente.")
        global tsDebug, printListDebug, instructionsDebug, conttadorIns, printPases
        #not exist errors
        # para debuguear debo ir mandando instruccion por instruccion
        if conttadorIns < len(instructionsDebug):
            if isinstance(instructionsDebug[conttadorIns], If):
                result = execute.valueExpression(instructionsDebug[conttadorIns].expression, execute.tsGlobal)                
                self.textDebug.append(f'if: {result} ->')                
                if result == 1:
                    self.textDebug.append('true')
                    tmp = conttadorIns
                    conttadorIns = execute.goto(conttadorIns + 1, instructionsDebug, instructionsDebug[conttadorIns].label)
                    if conttadorIns != 0:
                        execute.pasadas = 0
                        # print("realizando salto a: "+ str(b.label))
                    else:
                        conttadorIns = tmp
                        # print("error semantico, etiqueta no existe")
                        se = seOb(f"Error: etiqueta {instructionsDebug[conttadorIns].label} no existe", instructionsDebug[conttadorIns].line, instructionsDebug[conttadorIns].column)
                        execute.semanticErrorList.append(se)
                elif result == '#':
                    se = seOb(f"Error: Condicion no valida", instructionsDebug[conttadorIns].line, instructionsDebug[conttadorIns].column)
                    execute.semanticErrorList.append(se)
                else:
                    self.textDebug.append('false\n')
            elif isinstance(instructionsDebug[conttadorIns], Goto):
                # seteamos la instruccion anterior como la llamada al goto
                tmp = conttadorIns
                conttadorIns = execute.goto(conttadorIns, instructionsDebug,instructionsDebug[conttadorIns].label)
                if conttadorIns != 0:
                    execute.pasadas = 0
                    # print("realizando salto a: "+ str(b.label))
                else:
                    conttadorIns = tmp
                    # print("error semantico, etiqueta no existe")
                    se = seOb(f"Error: etiqueta {instructionsDebug[conttadorIns].label} no existe", instructionsDebug[conttadorIns].line, instructionsDebug[conttadorIns].column)
                    execute.semanticErrorList.append(se)
            else:
                printListDebug.append(execute.executeDebug(instructionsDebug[conttadorIns]))
                #tsDebug.updateDict(execute.tsGlobal)
            conttadorIns += 1

        print("\nConsole:")
        self.textEditConsole.setText("")
        self.textEditConsole.setPlainText("CONSOLE:\n")
        textoLinea = '> '
        if len(printListDebug) > 0:
            for element in printListDebug:
                if len(element) > 0:
                    if element[0]== "\\n" or element[0] == '\\n':
                        self.textEditConsole.append(textoLinea +"\n")
                        textoLinea = '> '          
                    else:
                        textoLinea += str(element[0])
                        #self.textEditConsole.append("> " + str(element))
                        print( "> " + str(element))
            self.textEditConsole.append(textoLinea +"\n")
            textoLinea = '> '

        self.textDebug.setText("")
        self.textDebug.setPlainText("DEBUG:\n")
        for key, val in execute.tsGlobal.symbols.items():
            self.textDebug.append(f'id: {str(key)} valor: {str(val.valor)} \n')

        if conttadorIns == len(instructionsDebug)-1:
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("Analisis correcto.")
            self.msgBox.setIcon(QtWidgets.QMessageBox.Information)
            self.msgBox.exec()
            Augus.resize(980, 616)

        elif len(execute.semanticErrorList) != 0:                              
            dataSema = [("DESCRIPCION", "COLUMNA", "LINEA")]
            for i in execute.semanticErrorList:
                dataSema.append((str(i.description), str(i.column), str(i.line)))
                    
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("Existen errores semanticos.")
            self.msgBox.setIcon(QtWidgets.QMessageBox.Information)
            self.msgBox.exec()
        
    def fn_Ejecutar_Debuguer(self):
        print("ejecutando debuguer")
        global tsDebug, printListDebug, instructionsDebug, conttadorIns, printPases
        Augus.resize(1500, 616)
        
        try:
            execute.contador = 4  #for grapho   
            execute.currentAmbit = 'main'   #current ambit
            execute.currentParams = []  #list of parameters that the current function will have
            execute.semanticErrorList = []
            execute.tsGlobal = {}
            execute.lecturasRead = []       #sera modificada desde gui
            execute.la = 0
            execute.co = 0 
            execute.pasadas = 0
            tsDebug = {}
            printListDebug[:] = []
            instructionsDebug[:] = []
            conttadorIns = 0
            printPases[:] = []

            #region creations of reports
            fgraph = open('../reports/ast.dot','w+') #creamos el archivo
            fgraph.write("graph \"\"{ node [shape=box];\n")          
            fgraph.close()

            fgraph = open('../reports/graph.dot','w+') #creamos el archivo
            fgraph.write("graph \"\" {")
            fgraph.close()
            #endregion

            content = self.tabWidget.currentWidget().findChild(QtWidgets.QTextEdit,"textEdit").toPlainText()
            content += '\n'
            result = grammar.parse(content)
            instructionsDebug = result[:]   #copio las instrucciones a la lista global

            # si exists errores lexicos o sintacticos traera una lista vacia            
            global data, dataS, dataSema, dataTs
            if len(result) == 0:
                self.msgBox = QtWidgets.QMessageBox()
                self.msgBox.setText("Este archivo contiene errores lexicos o sintacticos.")
                self.msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                self.msgBox.exec()

                if len(grammar.LexicalErrosList) > 0:                    
                    data = [("LEXEMA", "COLUMNA", "LINEA")]
                    for i in grammar.LexicalErrosList:
                        data.append((str(i.lexema), str(i.column), str(i.line)))
                
                if len(grammar.sintacticErroList) > 0:                    
                    dataS = [("LEXEMA", "COLUMNA", "LINEA")]
                    for i in grammar.sintacticErroList:
                        dataS.append((str(i.lexema), str(i.column), str(i.line)))
             
            #region end to report
            fgraph = open('../reports/ast.dot','a') #agregamos al archivo '}'
            fgraph.write("}")
            fgraph.flush() 
            fgraph.close()

            fgraph = open('../reports/graph.dot','a') #agregamos al archivo '}'
            fgraph.write("}")
            fgraph.flush()
            fgraph.close()
          
            sys.stdout.flush()
            #endregion
            
        except:
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setIcon(QtWidgets.QMessageBox.Critical)
            self.msgBox.setText("Area Vacia.")
            self.msgBox.exec()

    def fn_Ejecutar_Ascendente(self):
        #try:
            #region creations of reports
            execute.contador = 4  #for grapho   
            execute.currentAmbit = 'main'   #current ambit
            execute.currentParams = []  #list of parameters that the current function will have
            execute.semanticErrorList = []
            execute.tsGlobal = {}
            execute.lecturasRead = []       #sera modificada desde gui
            execute.la = 0
            execute.co = 0 
            execute.pasadas = 0
            fgraph = open('../reports/ast.dot','w+') #creamos el archivo
            fgraph.write("graph \"\"{ node [shape=box];\n")          
            fgraph.close()

            fgraph = open('../reports/graph.dot','w+') #creamos el archivo
            fgraph.write("graph \"\" {")
            fgraph.close()
            #endregion

            content = self.tabWidget.currentWidget().findChild(QtWidgets.QTextEdit,"textEdit").toPlainText()
            content += '\n'
            result = grammar.parse(content)

            # si exists errores lexicos o sintacticos traera una lista vacia            
            global data, dataS, dataSema, dataTs
            if len(result) == 0:
                self.msgBox = QtWidgets.QMessageBox()
                self.msgBox.setText("Este archivo contiene errores lexicos o sintacticos.")
                self.msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                self.msgBox.exec()

                if len(grammar.LexicalErrosList) > 0:                    
                    data = [("LEXEMA", "COLUMNA", "LINEA")]
                    for i in grammar.LexicalErrosList:
                        data.append((str(i.lexema), str(i.column), str(i.line)))
                
                if len(grammar.sintacticErroList) > 0:                    
                    dataS = [("LEXEMA", "COLUMNA", "LINEA")]
                    for i in grammar.sintacticErroList:
                        dataS.append((str(i.lexema), str(i.column), str(i.line)))
            else:
                #not exist errors                            
                printList = execute.execute(result)

                print("\nConsole:")
                self.textEditConsole.setText("")
                self.textEditConsole.setPlainText("CONSOLE:\n")
                textoLinea = '> '
                for element in printList:
                    if element == "\\n" or element == '\\n':
                        self.textEditConsole.append(textoLinea +"\n")
                        textoLinea = '> '          
                    else:
                        textoLinea += str(element)
                        #self.textEditConsole.append("> " + str(element))
                        print( "> " + str(element))
                self.textEditConsole.append(textoLinea +"\n")
                textoLinea = '> '
                
                if len(execute.semanticErrorList) == 0:
                    
                    self.msgBox = QtWidgets.QMessageBox()
                    self.msgBox.setText("Analisis correcto.")
                    self.msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    self.msgBox.exec()
                
                else:                   
                    dataSema = [("DESCRIPCION", "COLUMNA", "LINEA")]
                    for i in execute.semanticErrorList:
                        dataSema.append((str(i.description), str(i.column), str(i.line)))
                    
                    self.msgBox = QtWidgets.QMessageBox()
                    self.msgBox.setText("Existen errores semanticos.")
                    self.msgBox.setIcon(QtWidgets.QMessageBox.Information)
                    self.msgBox.exec()

            #region end to report
            fgraph = open('../reports/ast.dot','a') #agregamos al archivo '}'
            fgraph.write("}")
            fgraph.flush() 
            fgraph.close()

            fgraph = open('../reports/graph.dot','a') #agregamos al archivo '}'
            fgraph.write("}")
            fgraph.flush()
            fgraph.close()
          
            sys.stdout.flush()
            #endregion
            
        #except:
            #self.msgBox = QtWidgets.QMessageBox()
            #self.msgBox.setIcon(QtWidgets.QMessageBox.Critical)
            #self.msgBox.setText("Area Vacia.")
            #self.msgBox.exec()
    
    def fn_Ejecutar_Descendente(self):
        try:
            content = self.tabWidget.currentWidget().findChild(QtWidgets.QTextEdit,"textEdit").toPlainText()
            print("contenido a ejecutar de manera descendente: " + content)        
        except:
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("Empty Area.")
            self.msgBox.exec()

    def fn_Guardar(self):
        #content to save
        content = self.tabWidget.currentWidget().findChild(QtWidgets.QTextEdit,"textEdit").toPlainText()
        path = self.tabWidget.tabText(self.tabWidget.currentIndex())
        #print(path)
        print("writing to file.")
        f=open(path,"w")
        f.write(content)
        f.close()
    
    def fn_Guardar_Como(self):
        try:
            content = self.tabWidget.currentWidget().findChild(QtWidgets.QTextEdit,"textEdit").toPlainText()
            filename = QFileDialog.getSaveFileName(None)
            path = filename[0]
            
            print("writing to file.")
            f=open(path,"w+")
            f.write(content)
            f.close()

            #updating title on the tab
            self.tabWidget.setTabText(self.tabWidget.currentIndex(), path)
        except:
            print("closing file dialog")

    def fn_Cerrar(self):
        self.tabWidget.removeTab(self.tabWidget.currentIndex())
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText("Closed Table.")
        self.msg.exec()

    def fn_Salir(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText("¡Good Bye!")
        self.msg.exec()
        sys.exit(1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Augus = QtWidgets.QMainWindow()
    ui = Ui_Augus()
    ui.setupUi(Augus)
    Augus.show()
    sys.exit(app.exec_())

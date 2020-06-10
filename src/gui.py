# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import grammar
import reportGenerator as rg
import execute
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
#from PyQt5.QtGui import QColor

contadorVentanas = 0
cantidadEjecuciones = 0
lineasBefore = 0
lines = 0
data = []
dataS = []
result = []
class Ui_Augus(object):
    def setupUi(self, Augus):        
        Augus.setObjectName("Augus")
        Augus.resize(898, 616)
        self.centralwidget = QtWidgets.QWidget(Augus)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 471, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.textEditConsole = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditConsole.setGeometry(QtCore.QRect(510, 20, 361, 541))
        self.textEditConsole.setObjectName("textEditConsole")
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
        self.actionCambiar_color_de_fondo = QtWidgets.QAction(Augus)
        self.actionCambiar_color_de_fondo.setObjectName("actionCambiar_color_de_fondo")
        self.actionAyuda = QtWidgets.QAction(Augus)
        self.actionAyuda.setObjectName("actionAyuda")
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuReportes.addAction(self.actionReporteLexico)
        self.menuReportes.addAction(self.actionReporteSintactico)
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
        self.actionGuardar.triggered.connect(lambda : self.fn_Guardar())
        self.actionGuardar_Como.triggered.connect(lambda : self.fn_Guardar_Como())
        self.actionCerrar.triggered.connect(lambda : self.fn_Cerrar())
        self.actionSalir.triggered.connect(lambda : self.fn_Salir())
        self.actionReporteLexico.triggered.connect(lambda : self.fn_repLexico())
        self.actionReporteSintactico.triggered.connect(lambda : self.fn_repSintactico())


        self.textEditConsole.setStyleSheet('''background-color: rgb(33, 33, 33);
                                            border-color: rgb(18, 18, 18);
                                            color: rgb(51, 252, 255);
                                            font: 15pt \"consolas\";''' )
        self.textEditConsole.setPlainText("CONSOLE:\n")

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
                                            font: 15pt \"consolas\";''' )
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
                                            font: 15pt \"consolas\";''' )
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

    def fn_repSintactico(self):
        print("reportando sintactico")
        global dataS
        try:
            rg.export_to_pdf(dataS,2)
            dataS[:] = []
            grammar.sintacticErroList[:] = []           

            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("deployment report")
            self.msgBox.exec()
            import os
            os.startfile('..\\reports\\sintacticReport.pdf')
        except:
            print("error")
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("please close report sintactic.")
            self.msgBox.exec()
            dataS[:] = []
            grammar.sintacticErroList[:] = []
    
    def fn_repLexico(self):
        print("reportando lexico")
        global data
        try:
            rg.export_to_pdf(data,1)
            data[:] = []
            grammar.LexicalErrosList[:] = []           

            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("deployment report")
            self.msgBox.exec()
            import os
            os.startfile('..\\reports\\lexicalReport.pdf')
        except:
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("please close report lexical.")
            self.msgBox.exec()
            data[:] = []
            grammar.LexicalErrosList[:] = []
        
    def fn_Ejecutar_Ascendente(self):
        try:            
            fgraph = open('../reports/ast.dot','w+') #creamos el archivo
            fgraph.write("graph \"\"{ node [shape=box];\n")          
            fgraph.close()

            fgraph = open('../reports/graph.dot','w+') #creamos el archivo
            fgraph.write("graph \"\" {")
            fgraph.close()
            lines = 0
            content = self.tabWidget.currentWidget().findChild(QtWidgets.QTextEdit,"textEdit").toPlainText()
            words = content.split('\n')
            lines = len(words)
            auxLine = lines

            result = grammar.parse(content)

            # si exists errores lexicos o sintacticos traera una lista vacia
            if len(result) == 0:
                self.msgBox = QtWidgets.QMessageBox()
                self.msgBox.setText("this file contains lexical or syntactical errors.")
                self.msgBox.exec()

                if len(grammar.LexicalErrosList) > 0:
                    global lineasBefore, data, dataS
                    print("Errores Lexicos: "+ str(grammar.LexicalErrosList))
                    aux = lineasBefore

                    if lineasBefore != lines and lineasBefore != 0:
                        if lineasBefore < lines :
                            for i in grammar.LexicalErrosList:
                                i.line = i.line - (lines - lineasBefore)
                        else:
                            for i in grammar.LexicalErrosList:
                                i.line = i.line + (lineasBefore - lines)

                    can = grammar.LexicalErrosList[0].line / lines
                    if can >= 1:
                        lines = lines * can

                    result = grammar.LexicalErrosList
                    data = [("LEXEMA", "COLUMNA", "LINEA")]
                    for i in result:
                        line = i.line
                        if (i.line - (lines-1)) > 0:
                            line = round(i.line-(lines-1))
                        data.append((str(i.lexema), str(i.column), str(line)))
                
                if len(grammar.sintacticErroList) > 0:
                    lines = auxLine
                    aux = lineasBefore
                    if lineasBefore != lines and lineasBefore != 0:
                        if lineasBefore < lines :
                            for i in grammar.sintacticErroList:
                                i.line = i.line - (lines - lineasBefore)
                        else:
                            for i in grammar.sintacticErroList:
                                i.line = i.line + (lineasBefore - lines)
                    can = 0
                    can = (grammar.sintacticErroList[0].line +1) / (lines)
                    if can >= 1:
                        lines = (lines) * can

                    #print(str(grammar.sintacticErroList))
                    result = grammar.sintacticErroList
                    dataS = [("LEXEMA", "COLUMNA", "LINEA")]
                    for i in result:                        
                        line = i.line
                        if ((i.line) - (lines-2)) > 0:
                            line = round((i.line)-(lines-2)+1)
                        dataS.append((str(i.lexema), str(i.column), str(line)))

                    lineasBefore = auxLine
                    lines = auxLine
                
            else:
                #not exist errors
                printList = execute.execute(result)

                print("\nConsole:")
                self.textEditConsole.setText("")
                self.textEditConsole.setPlainText("CONSOLE:\n")
                for element in printList:                
                    self.textEditConsole.append("> " + str(element) + "\n")
                    print( "> " + str(element))
                
                self.msgBox = QtWidgets.QMessageBox()
                self.msgBox.setText("Correct Analysis.")
                self.msgBox.exec()

            #creat to report
            fgraph = open('../reports/ast.dot','a') #agregamos al archivo '}'
            fgraph.write("}")
            fgraph.flush() 
            fgraph.close()

            fgraph = open('../reports/graph.dot','a') #agregamos al archivo '}'
            fgraph.write("}")
            fgraph.flush()
            fgraph.close()

            import os
            os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
            #os.system('dot -Tpng ../reports/graph.dot -o ../reports/graph.png')
            #os.system('dot -Tpng ../reports/ast.dot -o ../reports/ast.png')

            sys.stdout.flush()
            
        except:
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setText("Empty Area.")
            self.msgBox.exec()
    
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

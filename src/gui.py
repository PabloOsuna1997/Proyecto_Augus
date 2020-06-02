# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

contadorVentanas = 0
class Ui_Augus(object):
    def setupUi(self, Augus):
        Augus.setObjectName("Augus")
        Augus.resize(877, 757)
        self.centralwidget = QtWidgets.QWidget(Augus)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 471, 541))
        self.tabWidget.setObjectName("tabWidget")
        Augus.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Augus)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuEjecutar = QtWidgets.QMenu(self.menubar)
        self.menuEjecutar.setObjectName("menuEjecutar")
        self.menuOpciones = QtWidgets.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        Augus.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Augus)
        self.statusbar.setObjectName("statusbar")
        Augus.setStatusBar(self.statusbar)
        self.actionNuevo = QtWidgets.QAction(Augus)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionAbrir = QtWidgets.QAction(Augus)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionGuardar = QtWidgets.QAction(Augus)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_Como = QtWidgets.QAction(Augus)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionCerrar = QtWidgets.QAction(Augus)
        self.actionCerrar.setObjectName("actionCerrar")
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
        self.actionCambiar_color_de_fondo = QtWidgets.QAction(Augus)
        self.actionCambiar_color_de_fondo.setObjectName("actionCambiar_color_de_fondo")
        self.actionAyuda = QtWidgets.QAction(Augus)
        self.actionAyuda.setObjectName("actionAyuda")
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addAction(self.actionCerrar)
        self.menuEditar.addAction(self.actionCopiar)
        self.menuEditar.addAction(self.actionPegar)
        self.menuEditar.addAction(self.actionCortar)
        self.menuEditar.addAction(self.actionBuscar)
        self.menuEjecutar.addAction(self.actionAscendente)
        self.menuOpciones.addAction(self.actionCambiar_color_de_fondo)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuEjecutar.menuAction())
        self.menubar.addAction(self.menuOpciones.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(Augus)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Augus)


        #actions
        self.actionNuevo.triggered.connect(lambda : self.fn_Nuevo())
        self.actionAbrir.triggered.connect(lambda : self.fn_Abrir())
        self.actionAscendente.triggered.connect(lambda : self.fn_Ejecutar())

    def retranslateUi(self, Augus):
        _translate = QtCore.QCoreApplication.translate
        Augus.setWindowTitle(_translate("Augus", "Augus"))
        self.menuArchivo.setTitle(_translate("Augus", "Archivo"))
        self.menuEditar.setTitle(_translate("Augus", "Editar"))
        self.menuEjecutar.setTitle(_translate("Augus", "Ejecutar"))
        self.menuOpciones.setTitle(_translate("Augus", "Opciones"))
        self.menuAyuda.setTitle(_translate("Augus", "Ayuda"))
        self.actionNuevo.setText(_translate("Augus", "Nuevo"))
        self.actionAbrir.setText(_translate("Augus", "Abrir"))
        self.actionGuardar.setText(_translate("Augus", "Guardar"))
        self.actionGuardar_Como.setText(_translate("Augus", "Guardar Como"))
        self.actionCerrar.setText(_translate("Augus", "Cerrar"))
        self.actionCopiar.setText(_translate("Augus", "Copiar"))
        self.actionPegar.setText(_translate("Augus", "Pegar"))
        self.actionCortar.setText(_translate("Augus", "Cortar"))
        self.actionBuscar.setText(_translate("Augus", "Buscar"))
        self.actionAscendente.setText(_translate("Augus", "Ascendente"))
        self.actionCambiar_color_de_fondo.setText(_translate("Augus", "Cambiar color de fondo"))
        self.actionAyuda.setText(_translate("Augus", "Ayuda"))

    def fn_Nuevo(self):
        global contadorVentanas
        contadorVentanas += 1
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(0,0,440,500))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(
            self.tab,"Tab "+ str(contadorVentanas)
        )
        self.tabWidget.setCurrentIndex(self.tabWidget.count()-1)    #para poner el focus en la nueva pestaña

    def fn_Abrir(self):
        filename = QFileDialog.getOpenFileName(None,' Open document',r"c:\\Users\\", "All Files (*)")
        path = filename[0]
        print(path)
        with open(path, 'r') as f:
            data = f.read()
           
            #creating a new tab
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName("tab")
            self.textEdit = QtWidgets.QTextEdit(self.tab)
            self.textEdit.setGeometry(QtCore.QRect(0,0,440,500))
            self.textEdit.setObjectName("textEdit")
            self.textEdit.setPlainText(data)
            self.tabWidget.addTab(
                self.tab,path
            )
            self.tabWidget.setCurrentIndex(self.tabWidget.count()-1)    #para poner el focus en la nueva pestaña

            #close the file
            f.close()

    def fn_Ejecutar(self):
        content = self.tabWidget.currentWidget().findChild(QtWidgets.QTextEdit,"textEdit").toPlainText()
        print("contenido a ejecutar: " + content)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Augus = QtWidgets.QMainWindow()
    ui = Ui_Augus()
    ui.setupUi(Augus)
    Augus.show()
    sys.exit(app.exec_())

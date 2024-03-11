# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import codecs
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 441, 331))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(510, 80, 271, 331))
        self.textEdit_2.setObjectName("textEdit_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 450, 441, 81))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 450, 251, 81))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.analizar_contenido)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 761, 31))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(540, 420, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def analizar_contenido(self):

        if(self.checkBox.isChecked()):
            contenido = self.textEdit.toPlainText()
            with open("C:/Users/MIGUEL ALFONSO/Pictures/Prueba Analizador/Ruby/Ejecutable.rb", "w") as myfile:
                myfile.write(contenido)

            test = 'C:/Users/MIGUEL ALFONSO/PycharmProjects/Analizador LSS Ruby y Julia/Analizador_Ruby/parser.out'
            fp = codecs.open(test, "r", "utf-8")
            cadena = fp.read()
            fp.close()

            try:
                # Ejecuta el archivo mi_script.py y captura la salida
                resultado_bytes = subprocess.check_output(["python", "Analizador_Ruby/Analizador_Sintactico_Ruby.py"])
                # Decodifica los bytes a una cadena de texto (UTF-8 por defecto)
                resultado = resultado_bytes.decode("utf-8")
                print("Resultados obtenidos:")
                print(resultado)
                self.textEdit_2.setText(resultado)
                self.textEdit_2.setEnabled(True)
                self.plainTextEdit.setPlainText(cadena)
                self.plainTextEdit.setEnabled(True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")
        else:
            contenido = self.textEdit.toPlainText()
            with open("C:/Users/MIGUEL ALFONSO/Pictures/Prueba Analizador/Julia/Ejecutable.jl", "w") as myfile:
                myfile.write(contenido)

            test = 'C:/Users/MIGUEL ALFONSO/PycharmProjects/Analizador LSS Ruby y Julia/Analizador_Julia/parser.out'
            fp = codecs.open(test, "r", "utf-8")
            cadena = fp.read()
            fp.close()

            try:
                # Ejecuta el archivo mi_script.py y captura la salida
                resultado_bytes = subprocess.check_output(["python", "Analizador_Julia/Analizador_Sintactico_Julia.py"])
                # Decodifica los bytes a una cadena de texto (UTF-8 por defecto)
                resultado = resultado_bytes.decode("utf-8")
                print("Resultados obtenidos:")
                print(resultado)
                self.textEdit_2.setText(resultado)
                self.textEdit_2.setEnabled(True)
                self.plainTextEdit.setPlainText(cadena)
                self.plainTextEdit.setEnabled(True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el archivo: {e}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Ejecutar"))
        self.label.setText(_translate("MainWindow", "Analizador Léxico Sintáctico y Semántico de Julia y Ruby"))
        self.checkBox.setText(_translate("MainWindow", "Ruby"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

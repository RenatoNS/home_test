import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets

import re

global arq_csv

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1252, 814)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.btnNumeral = QtWidgets.QPushButton(self.centralwidget)
        self.btnNumeral.setObjectName("btnNumeral")
        self.gridLayout_10.addWidget(self.btnNumeral, 7, 4, 1, 1)
        self.scrollAreaListDetalhe = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaListDetalhe.setWidgetResizable(True)
        self.scrollAreaListDetalhe.setObjectName("scrollAreaListDetalhe")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 838, 91))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidgetDetalhe = QtWidgets.QListWidget(self.scrollAreaWidgetContents_4)
        self.listWidgetDetalhe.setDragEnabled(False)
        self.listWidgetDetalhe.setDragDropOverwriteMode(False)
        self.listWidgetDetalhe.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidgetDetalhe.setObjectName("listWidgetDetalhe")
        self.gridLayout_5.addWidget(self.listWidgetDetalhe, 0, 0, 1, 1)
        self.scrollAreaListDetalhe.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_10.addWidget(self.scrollAreaListDetalhe, 5, 5, 1, 1)
        self.btnProduto = QtWidgets.QPushButton(self.centralwidget)
        self.btnProduto.setObjectName("btnProduto")
        self.gridLayout_10.addWidget(self.btnProduto, 4, 4, 1, 1)
        self.btnMontar = QtWidgets.QPushButton(self.centralwidget)
        self.btnMontar.setObjectName("btnMontar")
        self.gridLayout_10.addWidget(self.btnMontar, 11, 0, 1, 1)
        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvar.setObjectName("btnSalvar")
        self.gridLayout_10.addWidget(self.btnSalvar, 11, 1, 1, 1)
        self.scrollAreaListEscolha = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaListEscolha.setWidgetResizable(True)
        self.scrollAreaListEscolha.setObjectName("scrollAreaListEscolha")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 274, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidgetEscolha = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidgetEscolha.setDragEnabled(False)
        self.listWidgetEscolha.setDragDropOverwriteMode(False)
        self.listWidgetEscolha.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidgetEscolha.setObjectName("listWidgetEscolha")
        self.gridLayout.addWidget(self.listWidgetEscolha, 0, 0, 1, 1)
        self.scrollAreaListEscolha.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_10.addWidget(self.scrollAreaListEscolha, 4, 0, 6, 4)
        self.btnNA = QtWidgets.QPushButton(self.centralwidget)
        self.btnNA.setObjectName("btnNA")
        self.gridLayout_10.addWidget(self.btnNA, 9, 4, 1, 1)
        self.scrollAreaListNumeral = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaListNumeral.setWidgetResizable(True)
        self.scrollAreaListNumeral.setObjectName("scrollAreaListNumeral")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 838, 91))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.listWidgetNumeral = QtWidgets.QListWidget(self.scrollAreaWidgetContents_6)
        self.listWidgetNumeral.setDragEnabled(False)
        self.listWidgetNumeral.setDragDropOverwriteMode(False)
        self.listWidgetNumeral.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidgetNumeral.setObjectName("listWidgetNumeral")
        self.gridLayout_7.addWidget(self.listWidgetNumeral, 0, 0, 1, 1)
        self.scrollAreaListNumeral.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_10.addWidget(self.scrollAreaListNumeral, 7, 5, 1, 1)
        self.btnDetalhe = QtWidgets.QPushButton(self.centralwidget)
        self.btnDetalhe.setObjectName("btnDetalhe")
        self.gridLayout_10.addWidget(self.btnDetalhe, 5, 4, 1, 1)
        self.scrollAreaListNA = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaListNA.setWidgetResizable(True)
        self.scrollAreaListNA.setObjectName("scrollAreaListNA")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 838, 91))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listWidgetNA = QtWidgets.QListWidget(self.scrollAreaWidgetContents_9)
        self.listWidgetNA.setDragEnabled(False)
        self.listWidgetNA.setDragDropOverwriteMode(False)
        self.listWidgetNA.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidgetNA.setObjectName("listWidgetNA")
        self.gridLayout_4.addWidget(self.listWidgetNA, 0, 0, 1, 1)
        self.scrollAreaListNA.setWidget(self.scrollAreaWidgetContents_9)
        self.gridLayout_10.addWidget(self.scrollAreaListNA, 9, 5, 1, 1)
        self.scrollAreaListMarca = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaListMarca.setWidgetResizable(True)
        self.scrollAreaListMarca.setObjectName("scrollAreaListMarca")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 838, 91))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.listWidgetMarca = QtWidgets.QListWidget(self.scrollAreaWidgetContents_8)
        self.listWidgetMarca.setDragEnabled(False)
        self.listWidgetMarca.setDragDropOverwriteMode(False)
        self.listWidgetMarca.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidgetMarca.setObjectName("listWidgetMarca")
        self.gridLayout_8.addWidget(self.listWidgetMarca, 0, 0, 1, 1)
        self.scrollAreaListMarca.setWidget(self.scrollAreaWidgetContents_8)
        self.gridLayout_10.addWidget(self.scrollAreaListMarca, 6, 5, 1, 1)
        self.scrollAreaListJson = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaListJson.setWidgetResizable(True)
        self.scrollAreaListJson.setObjectName("scrollAreaListJson")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1215, 91))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidgetJson = QtWidgets.QListWidget(self.scrollAreaWidgetContents_3)
        self.listWidgetJson.setObjectName("listWidgetJson")
        self.gridLayout_3.addWidget(self.listWidgetJson, 0, 0, 1, 1)
        self.scrollAreaListJson.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_10.addWidget(self.scrollAreaListJson, 10, 0, 1, 6)
        self.scrollAreaListUnidade = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaListUnidade.setWidgetResizable(True)
        self.scrollAreaListUnidade.setObjectName("scrollAreaListUnidade")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, -10, 838, 91))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.listWidgetUnidade = QtWidgets.QListWidget(self.scrollAreaWidgetContents_5)
        self.listWidgetUnidade.setDragEnabled(False)
        self.listWidgetUnidade.setDragDropOverwriteMode(False)
        self.listWidgetUnidade.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidgetUnidade.setObjectName("listWidgetUnidade")
        self.gridLayout_6.addWidget(self.listWidgetUnidade, 0, 0, 1, 1)
        self.scrollAreaListUnidade.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_10.addWidget(self.scrollAreaListUnidade, 8, 5, 1, 1)
        self.scrollAreaListProduto = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaListProduto.setWidgetResizable(True)
        self.scrollAreaListProduto.setObjectName("scrollAreaListProduto")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 838, 91))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_10)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.listWidgetProduto = QtWidgets.QListWidget(self.scrollAreaWidgetContents_10)
        self.listWidgetProduto.setDragEnabled(False)
        self.listWidgetProduto.setDragDropOverwriteMode(False)
        self.listWidgetProduto.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidgetProduto.setObjectName("listWidgetProduto")
        self.gridLayout_9.addWidget(self.listWidgetProduto, 0, 0, 1, 1)
        self.scrollAreaListProduto.setWidget(self.scrollAreaWidgetContents_10)
        self.gridLayout_10.addWidget(self.scrollAreaListProduto, 4, 5, 1, 1)
        self.scrollAreaListCSV = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaListCSV.setWidgetResizable(True)
        self.scrollAreaListCSV.setObjectName("scrollAreaListCSV")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1215, 91))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidgetCSV = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.listWidgetCSV.setDragEnabled(False)
        self.listWidgetCSV.setDragDropOverwriteMode(False)
        self.listWidgetCSV.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.listWidgetCSV.setObjectName("listWidgetCSV")
        self.gridLayout_2.addWidget(self.listWidgetCSV, 0, 0, 1, 1)
        self.scrollAreaListCSV.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_10.addWidget(self.scrollAreaListCSV, 1, 0, 1, 6)
        self.btnLimpar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpar.setObjectName("btnLimpar")
        self.gridLayout_10.addWidget(self.btnLimpar, 2, 3, 1, 1)
        self.btnEscolherEntradaCSV = QtWidgets.QPushButton(self.centralwidget)
        self.btnEscolherEntradaCSV.setObjectName("btnEscolherEntradaCSV")
        self.gridLayout_10.addWidget(self.btnEscolherEntradaCSV, 0, 0, 1, 1)
        self.btnProximo = QtWidgets.QPushButton(self.centralwidget)
        self.btnProximo.setObjectName("btnProximo")
        self.gridLayout_10.addWidget(self.btnProximo, 2, 0, 1, 1)
        self.btnMarca = QtWidgets.QPushButton(self.centralwidget)
        self.btnMarca.setObjectName("btnMarca")
        self.gridLayout_10.addWidget(self.btnMarca, 6, 4, 1, 1)
        self.btnUnidade = QtWidgets.QPushButton(self.centralwidget)
        self.btnUnidade.setObjectName("btnUnidade")
        self.gridLayout_10.addWidget(self.btnUnidade, 8, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NER"))
        self.btnNumeral.setText(_translate("MainWindow", "Numeral Unidade"))
        self.btnProduto.setText(_translate("MainWindow", "Produto"))
        self.btnMontar.setText(_translate("MainWindow", "Montar"))
        self.btnMontar.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.btnSalvar.setText(_translate("MainWindow", "Salvar"))
        self.btnSalvar.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.btnNA.setText(_translate("MainWindow", "N/A"))
        self.btnDetalhe.setText(_translate("MainWindow", "Detalhe"))
        self.btnLimpar.setText(_translate("MainWindow", "Limpar"))
        self.btnLimpar.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.btnEscolherEntradaCSV.setText(_translate("MainWindow", "Escolher CSV"))
        self.btnProximo.setText(_translate("MainWindow", "Próximo"))
        self.btnMarca.setText(_translate("MainWindow", "Marca"))
        self.btnUnidade.setText(_translate("MainWindow", "Unidade"))






class NerJson(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherEntradaCSV.clicked.connect(self.abrir_csv)
        self.btnProximo.clicked.connect(self.split_item)
        self.btnProduto.clicked.connect(self.add_produto)
        self.btnMarca.clicked.connect(self.add_marca)
        self.btnNumeral.clicked.connect(self.add_numeral)
        self.btnUnidade.clicked.connect(self.add_unidade)
        self.btnDetalhe.clicked.connect(self.add_detalhe)
        self.btnNA.clicked.connect(self.add_na)
        self.btnSalvar.clicked.connect(self.salvar_json)
        self.btnMontar.clicked.connect(self.montar)
        self.btnLimpar.clicked.connect(self.limpar)



    def abrir_csv(self):
        global arq_csv
        arq_csv, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir CSV", (QtCore.QDir.homePath()), "CSV (*.csv *.tsv)")

        if arq_csv:
            data = open(str(arq_csv), 'r+')
            dataList = data.readlines()

            self.listWidgetCSV.clear()

            for cadaLinha in dataList:
                if len(cadaLinha.strip()) != 0:
                    self.listWidgetCSV.addItem(cadaLinha.strip())


    def split_item(self):
        x = [self.listWidgetCSV.currentItem().text()]
        x = str(x).split(" ")
        for y, j in enumerate(x):
            x[y] = re.sub(u'[^a-z A-Z áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ:]', '', x[y])
            self.listWidgetEscolha.addItem(x[y])
        x = [self.listWidgetCSV.currentItem().text()]
        x = str(x).split(" ")
        for y, j in enumerate(x):
            x[y] = re.sub(u'[^0-9:]', '', str(x[y]))
            if x[y].isdigit():
                self.listWidgetEscolha.addItem(x[y])
        # self.listWidgetCSV.takeItem(self.listWidgetCSV.currentRow())


    def salvar_json(self):
        global arq_csv
        nome = QtWidgets.QFileDialog.getSaveFileName(self, "Salvar arquivo", (QtCore.QDir.homePath()), '.json (*.json)')[0]
        file = open(nome, 'a+')

        for i in range(self.listWidgetJson.count()):
            x = self.listWidgetJson.item(i).text()
            text = '\n'+str(x)
            file.write(text)
        file.close()
        self.listWidgetJson.clear()


        # Modifica o arquivo CSV de origem
        file_csv = open(arq_csv, 'w+')

        for j in range(self.listWidgetCSV.count()):
            y = self.listWidgetCSV.item(j).text()
            text_csv =str(y) + '\n'
            file_csv.write(text_csv)


    def limpar(self):
        self.listWidgetEscolha.clear()
        self.listWidgetProduto.clear()
        self.listWidgetMarca.clear()
        self.listWidgetNumeral.clear()
        self.listWidgetUnidade.clear()
        self.listWidgetDetalhe.clear()
        self.listWidgetNA.clear()





    def montar(self):
        ultimo_digito = str(0)
        fr = r'"'

        # Produto
        if self.listWidgetProduto.count() > 0:
            palavra_prod = []
            for prod_cont in range(self.listWidgetProduto.count()):
                if prod_cont <= 0:
                    palavra_prod = self.listWidgetProduto.item(prod_cont).text()
                elif prod_cont > 0:
                    palavra_prod += self.listWidgetProduto.item(prod_cont).text()
            prod_ult = len(palavra_prod) + int(ultimo_digito)
            prod_ult_plus = prod_ult + 1
            finalProd = str('[' + str(ultimo_digito) + ',' + str(prod_ult) + fr + ',' + "produto" + fr + "]" + ",")
            ultimo_digito = prod_ult_plus
        else:
            finalProd = ''



        # Marca
        if self.listWidgetMarca.count() > 0:
            palavra_marca = []
            for marca_cont in range(self.listWidgetMarca.count()):
                if marca_cont <= 0:
                    palavra_marca = self.listWidgetMarca.item(marca_cont).text()
                elif marca_cont > 0:
                    palavra_marca += self.listWidgetMarca.item(marca_cont).text()
            marca_ult = len(palavra_marca) + int(ultimo_digito)
            marca_ult_plus = marca_ult + 1
            finalMarca = str('[' + str(ultimo_digito) + ',' + str(marca_ult) + fr + ',' + "marca" + fr + "]" + ",")
            ultimo_digito = marca_ult_plus
        else:
            finalMarca = ''



        # Numeral
        if self.listWidgetNumeral.count() > 0:
            palavra_numeral = []
            for numeral_cont in range(self.listWidgetNumeral.count()):
                if numeral_cont <= 0:
                    palavra_numeral = self.listWidgetNumeral.item(numeral_cont).text()
                elif numeral_cont > 0:
                    palavra_numeral += self.listWidgetNumeral.item(numeral_cont).text()
            numeral_ult = len(palavra_numeral) + int(ultimo_digito)
            numeral_ult_plus = numeral_ult + 1
            finalNumeral = str('[' + str(ultimo_digito) + ',' + str(numeral_ult) + fr + ',' + "numeral" + fr + "]" + ",")
            ultimo_digito = numeral_ult_plus

        else:
            finalNumeral = ''



        # Unidade
        if self.listWidgetUnidade.count() > 0:
            palavra_unidade = []
            for unidade_cont in range(self.listWidgetUnidade.count()):
                if unidade_cont <= 0:
                    palavra_unidade = self.listWidgetUnidade.item(unidade_cont).text()
                elif unidade_cont > 0:
                    palavra_unidade += self.listWidgetUnidade.item(unidade_cont).text()
            unidade_ult = len(palavra_unidade) + int(ultimo_digito)
            unidade_ult_plus = unidade_ult + 1
            finalUnidade = str('[' + str(ultimo_digito) + ',' + str(unidade_ult) + fr + ',' + "unidade" + fr + "]" + ",")
            ultimo_digito = unidade_ult_plus

        else:
            finalUnidade = ''



        # Detalhe
        if self.listWidgetDetalhe.count() > 0:
            palavra_detalhe = []
            for detalhe_cont in range(self.listWidgetDetalhe.count()):
                if detalhe_cont <= 0:
                    palavra_detalhe = self.listWidgetDetalhe.item(detalhe_cont).text()
                elif detalhe_cont > 0:
                    palavra_detalhe += self.listWidgetDetalhe.item(detalhe_cont).text()
            detalhe_ult = len(palavra_detalhe) + int(ultimo_digito)
            detalhe_ult_plus = detalhe_ult + 1
            finalDetalhe = str('[' + str(ultimo_digito) + ',' + str(detalhe_ult) + fr + ',' + "detalhe" + fr + "]" + ",")
            ultimo_digito = detalhe_ult_plus

        else:
            finalDetalhe = ''



        # NA
        if self.listWidgetNA.count() > 0:
            palavra_na = []
            for na_cont in range(self.listWidgetNA.count()):
                if na_cont <= 0:
                    palavra_na = self.listWidgetNA.item(na_cont).text()
                elif na_cont > 0:
                    palavra_na += self.listWidgetNA.item(na_cont).text()
            na_ult = len(palavra_na) + int(ultimo_digito)
            na_ult_plus = na_ult + 1
            finalNA = str('[' + str(ultimo_digito) + ',' + str(na_ult) + fr + ',' + "n-a" + fr + "]" + ",")
            ultimo_digito = na_ult_plus

        else:
            finalNA = ''



        a = self.listWidgetCSV.currentItem().text()
        b = r',{"entities": ['
        c = fr + a + fr + b
        self.listWidgetCSV.takeItem(self.listWidgetCSV.currentRow())
        d = (finalProd + finalMarca + finalNumeral + finalUnidade + finalDetalhe + finalNA)
        e = "[" + c + d + "]}],"
        self.listWidgetJson.addItem(e)


        self.listWidgetProduto.clear()
        self.listWidgetMarca.clear()
        self.listWidgetNumeral.clear()
        self.listWidgetUnidade.clear()
        self.listWidgetDetalhe.clear()
        self.listWidgetNA.clear()




    def add_produto(self):
        y = self.listWidgetEscolha.currentItem()
        self.listWidgetProduto.addItem(y.text())
        self.listWidgetEscolha.takeItem(self.listWidgetEscolha.currentRow())



    def add_marca(self):
        y = self.listWidgetEscolha.currentItem()
        self.listWidgetMarca.addItem(y.text())
        self.listWidgetEscolha.takeItem(self.listWidgetEscolha.currentRow())



    def add_numeral(self):
        y = self.listWidgetEscolha.currentItem()
        self.listWidgetNumeral.addItem(y.text())
        self.listWidgetEscolha.takeItem(self.listWidgetEscolha.currentRow())



    def add_unidade(self):
        y = self.listWidgetEscolha.currentItem()
        self.listWidgetUnidade.addItem(y.text())
        self.listWidgetEscolha.takeItem(self.listWidgetEscolha.currentRow())



    def add_detalhe(self):
        y = self.listWidgetEscolha.currentItem()
        self.listWidgetDetalhe.addItem(y.text())
        self.listWidgetEscolha.takeItem(self.listWidgetEscolha.currentRow())



    def add_na(self):
        y = self.listWidgetEscolha.currentItem()
        self.listWidgetNA.addItem(y.text())
        self.listWidgetEscolha.takeItem(self.listWidgetEscolha.currentRow())




if __name__ == '__main__':
    qt = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ner_json = NerJson()
    ner_json.show()
    qt.exec_()

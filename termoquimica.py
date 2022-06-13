#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 23:57:47 2021

@author: marcio
"""

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QFileDialog, QMainWindow, QMessageBox, QPushButton,
 QLabel, QApplication, QRadioButton, QMenu, QAction, QLineEdit, QGroupBox, QTextEdit)
from PyQt5.QtCore import  QRect# pyqtSlot
from PyQt5.QtGui import QIcon#, QClipboard
import modulo as termo ## módulo que cálcula as funções termodinâmicas
import Idioma_gui_en as lang ## módulo com os textos da interface
import config
import os
path = os.path.dirname(os.path.realpath(__file__))
##############################################################################
class Window(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle(lang.title)
        self.setFixedSize(1200, 680)
        self.setStyleSheet("background:#808080")
        self.setWindowIcon(QIcon(path+"/temps/ico2.png"))
        self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
        ## Barra de menu ####
        self.menubar = self.menuBar()
        self.arquivo = self.menubar.addMenu(lang.file)
        self.ajuda = self.arquivo.addAction(lang.ajuda)
        self.ajuda.triggered.connect(self.AjudaDef)
        self.ajuda.setShortcut("F2")
        self.sobre = self.arquivo.addAction(lang.sobre)
        self.sobre.triggered.connect(self.SobreDef)
        self.sobre.setShortcut("F3")
        self.fechar = self.arquivo.addAction(lang.fecha)
        self.fechar.triggered.connect(self.FecharDef)
        self.fechar.setShortcut("F4")

        self.ferramentas = self.menubar.addMenu(lang.ferramentas)
        self.language = self.ferramentas.addMenu(lang.language)
        self.En_US = QAction('En_US', self)
        self.Pt_Br = QAction('Pt_Br', self)
        self.En_US.triggered.connect(self.En) # muda interface para inglês
        self.Pt_Br.triggered.connect(self.Pt) # interface em portugues
        self.language.addAction(self.En_US)
        self.language.addAction(self.Pt_Br)

        self.simetria = self.ferramentas.addAction(lang.simetria)
        self.simetria.triggered.connect(self.SimetriaDef)
        self.simetria.setShortcut("F5")
        self.convert = self.ferramentas.addAction(lang.conv)
        self.convert.triggered.connect(self.ConvertDef)
        self.convert.setShortcut("F6")
        self.exibir = self.menubar.addMenu(lang.exibir)
        self.tempU = self.exibir.addAction(lang.tempU)
        self.tempU.triggered.connect(self.SetarU)
        self.tempU.setShortcut("F7")
        self.tempS = self.exibir.addAction(lang.tempS)
        self.tempS.triggered.connect(self.SetarS)
        self.tempS.setShortcut("F8")
        self.tempH = self.exibir.addAction(lang.tempH)
        self.tempH.triggered.connect(self.SetarH)
        self.tempH.setShortcut("F9")
        self.tempG = self.exibir.addAction(lang.tempG)
        self.tempG.triggered.connect(self.SetarG)
        self.tempG.setShortcut("F10")
        self.tempA = self.exibir.addAction(lang.tempA)
        self.tempA.triggered.connect(self.SetarA)
        self.tempA.setShortcut("F11")
        self.menubar.setStyleSheet("background:#A9A9A9")
        self.messageBox = QMessageBox()

#-------------------Entrada de dados------------------------------------------
        self.scf = QLabel(self,text=lang.path_scf)
        self.scf.setGeometry(10, 60, 400, 30)
        self.scf.setStyleSheet("color:black;font-size:16px")
        self.dym = QLabel(self,text=lang.path_dyn)
        self.dym.setGeometry(10, 140, 400, 30)
        self.dym.setStyleSheet("color:black;font-size:16px")
        self.line_scf = QLineEdit(self)
        self.line_scf.setGeometry(10, 90, 400, 30)
        self.line_scf.setStyleSheet("background:#BDBDBD")
        self.btn1 = QPushButton(self)
        self.btn1.setIcon(QIcon(path+"/temps/lupa.png"))
        self.btn1.setGeometry(QRect(415, 90, 40, 30))
        self.btn1.clicked.connect(self.open_scf)
        self.btn1.setToolTip("Pesquisar")
        self.line_dynmat = QLineEdit(self)
        self.line_dynmat.setGeometry(10, 170, 400, 30)
        self.line_dynmat.setStyleSheet("background:#BDBDBD")
        self.btn2 = QPushButton(self)
        self.btn2.setIcon(QIcon(path+"/temps/lupa.png"))
        self.btn2.setGeometry(QRect(415, 170, 40, 30))
        self.btn2.setToolTip("Pesquisar")
        self.btn2.clicked.connect(self.open_dynmat)
#--------------------------bloco de temperaturas------------------------------
        self.grupT = QGroupBox(self)
        self.grupT.setGeometry(10,250,450,100)
        self.grupT.setStyleSheet("background:#757580")
        self.tempew = QLabel(self.grupT,text=lang.tK)
        self.tempew.setGeometry(10, 0, 400, 30)
        self.tempew.setStyleSheet("color:black;font-size:16px")
        #temperatura min
        self.temperatura1 = QLabel(self.grupT,text=lang.tmin)
        self.temperatura1.setGeometry(10, 35, 400, 30)
        self.temperatura1.setStyleSheet("color:black;font-size:14px")
        self.T_min = QLineEdit(self.grupT)
        self.T_min.setAlignment(QtCore.Qt.AlignRight)
        self.T_min.setGeometry(10, 60, 100, 30)
        self.T_min.setText('298.15')
        self.T_min.setStyleSheet("background:#BDBDBD")
        #temperatura máx
        self.temperatura2 = QLabel(self.grupT,text=lang.tmax)
        self.temperatura2.setGeometry(180, 35, 400, 30)
        self.temperatura2.setStyleSheet("color:black;font-size:14px")
        self.T_max = QLineEdit(self.grupT)
        self.T_max.setAlignment(QtCore.Qt.AlignRight)
        self.T_max.setGeometry(180, 60, 100, 30)
        self.T_max.setText('600.15')
        self.T_max.setStyleSheet("background:#BDBDBD")
        #delta
        self.delta = QLabel(self.grupT,text=lang.tD)
        self.delta.setGeometry(340, 35, 400, 30)
        self.delta.setStyleSheet("color:black;font-size:14px")
        self.deltaT = QLineEdit(self.grupT)
        self.deltaT.setAlignment(QtCore.Qt.AlignRight)
        self.deltaT.setGeometry(340, 60, 100, 30)
        self.deltaT.setStyleSheet("background:#BDBDBD")
        self.deltaT.setText('10') ## temperatura máxima
#---------------------tipo de estruturas--------------------------------------
        self.grupo1 = QGroupBox(self)
        self.grupo1.setGeometry(10,380,150,100)
        self.grupo1.setStyleSheet("background:#757580")
        self.molecule = QRadioButton(self.grupo1, text=lang.mol)
        self.molecule.move(10, 0)
        self.solids = QRadioButton(self.grupo1, text=lang.sol)
        self.solids.move(10, 30)
        self.solids.setChecked(True)#mantém solidos selciondados
        self.molecule.toggled.connect(self.G1)
        self.solids.toggled.connect(self.G2)
#---------------------variáveis moleculares-----------------------------------
        self.grupo2 = QGroupBox(self)
        self.grupo2.setGeometry(170, 380, 290, 100)
        self.grupo2.setStyleSheet("background:#757580")
        self.grupo2.setCheckable(True)#### selector oculto
        self.grupo2.setChecked(False) ### desativa as variaveis moleculares
        self.nolinear = QRadioButton(self.grupo2, text=lang.poli)
        self.nolinear.move(2, 0)
        self.linear = QRadioButton(self.grupo2, text=lang.line)
        self.linear.move(2, 30)
        self.mono = QRadioButton(self.grupo2, text=lang.mono)
        self.mono.move(2, 60)
        self.mono.toggled.connect(self.G3)
        self.nolinear.setChecked(True) ### poliatomico selcionado
        self.sym = QLabel(self.grupo2,text=lang.Nsym)
        self.sym.setGeometry(150, 0, 120, 20)
        self.Press = QLabel(self.grupo2,text=lang.Pres)
        self.Press.setGeometry(150, 45, 120, 25)
        self.line_sym = QLineEdit(self.grupo2)
        self.line_sym.setAlignment(QtCore.Qt.AlignRight)
        self.line_sym.setGeometry(150, 20, 120, 25)
        self.line_sym.setText('1')
        self.line_sym.setStyleSheet("background:#BDBDBD")
        self.line_Press = QLineEdit(self.grupo2)
        self.line_Press.setAlignment(QtCore.Qt.AlignRight)
        self.line_Press.setGeometry(150, 70, 120, 25)
        self.line_Press.setStyleSheet("background:#BDBDBD")
        self.line_Press.setText('1') # pressão padrão 1 atm
#-------------------------botões----------------------------------------------
        self.btn3 = QPushButton(self,text=lang.calcule)  ## botão calcular
        self.btn3.setGeometry(QRect(10, 510, 100, 40))
        self.btn3.clicked.connect(self.Print) ## conecta a função print
        self.btn3.setStyleSheet("font-size:16px")
        self.btn3.setToolTip(lang.calcule1)
        self.btn4 = QPushButton(self,text=lang.save)  ## botão salvar
        self.btn4.setGeometry(QRect(130, 510, 100, 40))
        self.btn4.clicked.connect(self.Salvar) ## conecta a função salvar
        self.btn4.setStyleSheet("font-size:16px")
        self.btn4.setToolTip(lang.save1)
        self.btn6 = QPushButton(self,text=lang.edit)  ## botão editar
        self.btn6.setGeometry(QRect(250, 510, 100, 40))
        self.btn6.clicked.connect(self.Editar) ## conecta a função editar
        self.btn6.setStyleSheet("font-size:16px")
        self.btn6.setToolTip(lang.edit1)
        self.btn7 = QPushButton(self,text=lang.copy)  ## botão editar
        self.btn7.setGeometry(QRect(370, 510, 100, 40))
        self.btn7.clicked.connect(self.Copiar) ## conecta a função editar
        self.btn7.setStyleSheet("font-size:16px")
        self.btn7.setToolTip(lang.copy1)
#-------------------área de texto---------------------------------------------
        self.texto = QTextEdit(self)
        self.texto.setGeometry(475,30,720,640)
        self.texto.setStyleSheet("background:white")
        self.texto.setReadOnly(True)
        self.texto.setPlaceholderText(lang.f2)
##############################################################################
###  FUNÇÕES PARA ATIVAR/DESATIVAR AS VARIÁVEIS MOLECULARES
    def G1(self):
        self.grupo2.setCheckable(True)
        self.nolinear.setEnabled(True)
        self.linear.setEnabled(True)
        self.line_sym.setEnabled(True)
        self.mono.setChecked(False)
    def G2(self):
        self.grupo2.setChecked(False)
        self.mono.setChecked(False)
    def G3(self):
        if self.mono.isChecked():
            self.line_sym.setEnabled(False)
            self.sym.setEnabled(False)
        else:
            self.line_sym.setEnabled(True)
            self.sym.setEnabled(True)
#-----------------Aqui termina a interface------------------------------------
##############################################################################
    def open_scf(self): # pesquisar arquivos
        self.file_scf, _ = QFileDialog.getOpenFileName(self, lang.abrir, "","*.out")
        if self.file_scf:
            self.line_scf.setText(self.file_scf)
    def open_dynmat(self): # pesquisar arquivos
        self.fileDynmat, _ = QFileDialog.getOpenFileName(self, lang.abrir, "","*.out")
        if self.fileDynmat:
            self.line_dynmat.setText(self.fileDynmat)
    def Salvar(self):
        self.fileName, _ = QFileDialog.getSaveFileName(self, lang.saveas, ".dat","*.dat")
        with open (self.fileName, 'w') as saida:
            saida.write(self.texto.toPlainText())
#--------------------Cálculos termodinâmicos----------------------------------
    def Calcular(self): ## função que retorna resultados termodinâmicos
        if self.line_scf.text() != '' and self.line_dynmat.text() != '': #
#----------------------------Sólidos------------------------------------------
            self.texto.setReadOnly(True)
            if self.solids.isChecked(): # computar solidos
                tipo = 'solido'
                dados = [tipo, # formato da resposta
                         self.line_scf.text(), # path scf.out
                         self.line_dynmat.text(), # path mat.out
                         self.T_min.text(), # temperatura mínima
                         self.T_max.text(), # temperatura máxima
                         0, # pressão
                         0, # número de simetria
                         None, #
                         self.deltaT.text()] # Delta
                return termo.Termo(dados)
#----------------------------Moléculas----------------------------------------
            elif self.molecule.isChecked():# computar sistemas moleculares
#----------------------------poliatômico--------------------------------------
                if self.nolinear.isChecked(): # poliatomico
                    tipo = 'molecula'
                    lin = 'nolinear'
                    dados = [tipo, # formato da resposta
                             self.line_scf.text(), # path scf.out
                             self.line_dynmat.text(), # path mat.out
                             self.T_min.text(), # temperatura mínima
                             self.T_max.text(), # temperatura máxima
                             self.line_Press.text(), # pressão
                             self.line_sym.text(), # número de simetria
                             lin, # poliatomico
                             self.deltaT.text()] # Delta T
                    return termo.Termo(dados)
#-----------------------------------------------------------------------------
#----------------------------linear-------------------------------------------
                elif self.linear.isChecked(): # linear
                    tipo = 'molecula'
                    lin = 'linear'
                    dados = [tipo, # formato da resposta
                             self.line_scf.text(), # path scf.out
                             self.line_dynmat.text(), # path mat.out
                             self.T_min.text(), # temperatura mínima
                             self.T_max.text(), # temperatura máxima
                             self.line_Press.text(), # pressão
                             self.line_sym.text(), # número de simetria
                             lin, # poliatomico
                             self.deltaT.text()] # Delta T
                    return termo.Termo(dados)
#-----------------------------------------------------------------------------
#----------------------------monoatômico--------------------------------------
                elif self.mono.isChecked(): # computar atomos no vácuo
                    tipo = 'molecula'
                    lin = 'atomo'
                    dados = [tipo, # formato da resposta
                             self.line_scf.text(), # path scf.out
                             self.line_dynmat.text(), # path mat.out
                             self.T_min.text(), # temperatura mínima
                             self.T_max.text(), # temperatura máxima
                             self.line_Press.text(), # pressão
                             1, # número de simetria self.line_sym.text()
                             lin, # monoatomico
                             self.deltaT.text()] # Delta T
                    return termo.Termo(dados)
        else:
            self.messageBox.about(self,lang.erro, lang.erro1)
#-----------------------------------------------------------------------------
#---------------função para plotar os resultados na tela----------------------
    def Print(self):
        if self.Calcular() != None:
            self.texto.setText(str(self.Calcular()))
        else:
            pass
##############################################################################
#--------------------------- I D I O M A S ------------------------------------
    def Pt(self):
        config.Pt()
        self.messageBox.about(self, 'Warning', 'Restart the interface')
        #self.close()
    def En(self):
        config.En()
        self.messageBox.about(self, 'Atenção', 'Reinicie a interface')
        #self.close()

#-----------------------------------------------------------------------------
    def AjudaDef(self):
        self.messageBox.about(self, lang.ajuda, lang.texto)
    def FecharDef(self):
        self.close()
    def Editar(self):
        self.texto.setReadOnly(False)
    def Copiar(self):
        if self.texto.toPlainText() != '':
            cb = QApplication.clipboard()
            cb.setText(self.texto.toPlainText())
            self.messageBox.about(self,lang.warning, lang.info1)
        else:
            self.messageBox.about(self,lang.erro, lang.info2)
    def SimetriaDef(self):
        self.messageBox.about(self, lang.simetria, lang.texto2)
    def ConvertDef(self):
        self.messageBox.about(self, lang.conv, lang.texto3)
    def SobreDef(self):
        self.messageBox.about(self, lang.sobre, lang.info)
    def Leitura(self):
        self.texto.setReadOnly(True)
        T = [] # lista para armazenar as temperaturas
        U = [] # lista para armazenar energias internas
        S = [] # lista para armazenar entropia
        H = [] # lista para armazenar entalpia
        G = [] # lista para armazenar energias Gibbs
        A = [] # lista para armazenar energias de Helmholtz
        with open(path+'/temps/temp.nyp', 'r') as data:
            for lines in data:
                if lang.controle in lines:
                    data.readline()#, data.readline()
                    break
            try:
                for lines in data:
                    d = lines.split()
                    T.append(d[0]), U.append(d[1]), S.append(d[2])
                    H.append(d[3]), G.append(d[4]), A.append(d[5])
            except:
                pass
        return T, U, S, H, G, A
#----------------------Temperatura x Energia interna--------------------------
    def SetarU(self):
        if self.Calcular() != None:
            T = self.Leitura()[0] # lista para armazenar as temperaturas
            U = self.Leitura()[1] # lista para armazenar energias internas
            res = []
            for  x, y in zip (T, U):
                res.append(str(f'{x:^5}\t{y:^15}\n'))
            resultado ="".join(map(str,res))
            self.texto.clear()
            self.texto.setText(resultado)
#--------------------Temperatura x entropia-----------------------------------
    def SetarS(self):
        if self.Calcular() != None:
            T = self.Leitura()[0] # lista para armazenar as temperaturas
            S = self.Leitura()[2] # lista para armazenar entropias
            res = []
            for  x, y in zip (T, S):
                res.append(str(f'{x:^5}\t{y:^15}\n'))
            resultado ="".join(map(str,res))
            self.texto.clear()
            self.texto.setText(resultado)
#-------------------Temperatura x entalpia------------------------------------
    def SetarH(self):
        if self.Calcular() != None:
            T = self.Leitura()[0] # lista para armazenar as temperaturas
            H = self.Leitura()[3] # lista para armazenar entalpias
            res = []
            for  x, y in zip (T, H):
                res.append(str(f'{x:^5}\t{y:^15}\n'))
            resultado ="".join(map(str,res))
            self.texto.clear()
            self.texto.setText(resultado)
#------------------Temperatura x enegia de Gibbs------------------------------
    def SetarG(self):
        if self.Calcular() != None:
            T = self.Leitura()[0] # lista para armazenar as temperaturas
            G = self.Leitura()[4] # lista para armazenar energias Gibbs
            res = []
            for  x, y in zip (T, G):
                res.append(str(f'{x:^5}\t{y:^15}\n'))
            resultado ="".join(map(str,res))
            self.texto.clear()
            self.texto.setText(resultado)
#-----------------Temperatura x energia de Helmholtz--------------------------
    def SetarA(self):
        if self.Calcular() != None:
            T = self.Leitura()[0] # lista para armazenar as temperaturas
            A = self.Leitura()[5] # lista para armazenar energias Helmholtz
            res = []
            for  x, y in zip (T, A):
                res.append(str(f'{x:^5}\t{y:^15}\n'))
            resultado ="".join(map(str,res))
            self.texto.clear()
            self.texto.setText(resultado)
##############################################################################
if __name__ == '__main__':
    App = QApplication(sys.argv)
    gui = Window()
    gui.show()
    App.exec_()

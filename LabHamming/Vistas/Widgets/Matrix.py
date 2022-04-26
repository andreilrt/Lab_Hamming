import random
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import Vistas.ViewFuntion.Common as Common
from Vistas.Widgets.IngresoData import IngresoData
from Vistas.Widgets.Texto import Texto
from Vistas.Widgets.Boton import Boton

class Matrix:
    tamano = 0
    fondo = ''
    Matrix = None
    matrix = []
    matrixI = []
    matrixR = []
    textos = []

    def __init__(self, tamano, colorFondo, frame):
        super().__init__()
        self.Matrix = Frame(frame)
        self.tamano = tamano
        self.fondo = colorFondo

    def generarInputs(self, x, y):
        self.Matrix.config(bg=self.fondo, width=x, height=y)
        self.matrixI = []
        for i in range(self.tamano):
            self.matrixI.append([])
            for j in range(self.tamano):
                self.matrixI[i].append(IngresoData(self.Matrix, j*(1/self.tamano), (i*0.08), (1/self.tamano)-0.02))
        for i in self.matrixI:
            for tx in i:
                tx.ingreso()
        self.Matrix.pack()

    def generarText(self, x, y, mat):
        self.Matrix.config(bg=self.fondo, width=x, height=y)
        x = 0
        for i in range(len(mat)):
            self.matrixR.append([])
            for j in range(len(mat[0])):
                self.matrixR[i].append(self.textos.append([Texto(self.Matrix,mat[i][j], self.fondo, 14), j*(1/self.tamano), (i*0.08)]))
                x+=1
        Common.generarTextos(self.textos)
        self.Matrix.pack()

    def obtenerMatrix(self):
        self.matrix = []
        for i in range(self.tamano):
            self.matrix.append([])
            for j in range(self.tamano):
                self.matrix[i].append(self.matrixI[i][j].getData())
        if self.isInteger():
            return self.matrix
        else:
            return 1
                

    def isInteger(self):
        try:
            for i in range(self.tamano):
                    for j in range(self.tamano):              
                        self.matrix[i][j] = int(self.matrix[i][j])
            return 1
        except:
            self.Limpiar()
            return 0

    def Limpiar(self):
        for i in range(self.tamano):
                for j in range(self.tamano):
                    self.matrixI[i][j].Limpiar()

    def destruir(self):
        self.Matrix.destroy()
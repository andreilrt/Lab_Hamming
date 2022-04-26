import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from Vistas.Widgets.Texto import Texto
from Vistas.Widgets.Boton import Boton
from Vistas.Widgets.Matrix import Matrix
from Vistas.ViewFuntion import Common
from Controlador.Controlador import Controlador


class MatrizSec:
    resultados = None
    controlador = Controlador()

    def __init__(self, root, colorBotones, colorFondo):
        self.MatrizSec = Frame(root)
        self.color = colorBotones
        self.fondo = colorFondo

    def setFrames(self, result):
        self.resultados = result

    def generar(self):
        self.MatrizSec.config(bg=self.fondo, width=1000, height=720)
        # Matrix
        fp = self.controlador.getFPs()
        l = len(fp[0])
        mat = Matrix(l, self.fondo, self.MatrizSec)
        mat.generarText(700, 700, fp)
        # Botones
        botonAtras = Boton(self.MatrizSec, self.color, self.fondo, .1, .85, 'Atras', lambda event: {
                           self.isHiden(), self.resultados.isVisible()})
        botonAtras.generarCuadrado()

    def isVisible(self):
        self.MatrizSec.pack()

    def isHiden(self):
        self.MatrizSec.pack_forget()

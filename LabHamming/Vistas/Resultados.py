import tkinter as tk
from tkinter import *
from Vistas.Widgets.Boton import Boton
from Vistas.Widgets.Texto import Texto
import Vistas.ViewFuntion.Common as Common
from Controlador.Controlador import Controlador

class Resultados:
    inicio = None
    matSec = None
    textos = []
    controlador = Controlador()

    def __init__(self, root, colorBotones, colorFondo):
        self.resultados = Frame(root)
        self.fondo = colorFondo
        self.color = colorBotones

    def setFrames(self, inicio, matSec):
        self.inicio = inicio
        self.matSec = matSec

    def generar(self):
        self.resultados.config(bg=self.fondo, width='1020', heigh='1000')
        # Textos
        self.textos.append(
            [Texto(self.resultados, 'Trama Binaria', self.fondo, 20), .4, .1])
        self.textos.append(
            [Texto(self.resultados, self.controlador.getTrama(), self.fondo, 14), .3, .2])
        Common.generarTextos(self.textos)
        botonSalir = Boton(self.resultados, self.color, self.fondo, .7, .85, 'Salir', lambda event:{exit(0)})
        botonSalir.generarCuadrado()
        botonMatSec = Boton(self.resultados, self.color, self.fondo, .2, .85, 'FP', lambda event:{self.isOculto(), self.matSec.generar(), self.matSec.isVisible()})
        botonMatSec.generarCuadrado()
        
    def isVisible(self):
        self.resultados.pack()

    def isOculto(self):
        self.resultados.pack_forget()



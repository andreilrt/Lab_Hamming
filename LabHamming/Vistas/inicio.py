import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from Vistas.Widgets.Texto import Texto
from Vistas.Widgets.Boton import Boton
from Vistas.Widgets.Listas import Listas
from Vistas.Widgets.IngresoData import IngresoData
from Vistas.ViewFuntion import Common
from Controlador.Controlador import Controlador
import Modelo.hamming as hamming

class Inicio:
    fondo = ''
    color = ''
    controlador = Controlador()
    inicio = None
    creditos = None
    resultados = None
    resultados2 = None
    tipo = ''
    mensaje = ''

    def __init__(self, root, colorBotones, colorFondo):
        super().__init__()
        self.inicio = Frame(root)
        self.color = colorBotones
        self.fondo = colorFondo

    def setFrames(self, credit, result, result2):
        self.creditos = credit
        self.resultados = result
        self.resultados2 = result2

    def generar(self):
        self.inicio.config(bg=self.fondo, width=1000, height=720)
        # Textos
        textos = []
        textos.append(
            [Texto(self.inicio, 'Codificación Hamming', self.fondo, 30), .3, .1])
        textos.append(
            [Texto(self.inicio, 'Digite la trama que se quiere codificar : ', self.fondo, 20), .2, .25])
        textos.append([Texto(self.inicio, 'Tipo de trama', self.fondo, 20), .4, .45])
        Common.generarTextos(textos)
        # Entry
        self.mensaje = IngresoData(self.inicio, .1, .35, .8)
        self.mensaje.ingreso()
        # listas
        def setParametro1(event):
            self.tipo = self.comboTamano.get()
            print(self.tipo)
        self.comboTamano = Listas(self.inicio, .4, .55, ['A Codificar', 'Con Errror'], setParametro1)
        self.comboTamano.Generar()
        # Botones
        def Calcular():
            self.isHiden()
            self.controlador.setMensaje(self.mensaje.getData())
            print(self.controlador.getMensaje())
            if self.tipo == 'A Codificar':
                hamming.fpFinal(self.controlador.getMensaje())
                self.resultados.generar()
                self.resultados.isVisible()
            else:
                self.controlador.setTrama(self.controlador.getMensaje())
                hamming.verify(self.controlador.getMensaje())
                self.resultados2.generar()
                self.resultados2.isVisible()

        botonCalcular = Boton(
            self.inicio, self.color, self.fondo, .4, .75, 'Calcular', lambda event: {Calcular()})
        botonCalcular.generarOvalado()
        botonCreditos = Boton(self.inicio, self.color, self.fondo, .1, .85, 'Creditos', lambda event: {
                              self.isHiden(), self.creditos.isVisible()})
        botonCreditos.generarCuadrado()
        botonSalir = Boton(self.inicio, self.color,
                           self.fondo, .7, .85, 'Salir', lambda event: {exit(0)})
        botonSalir.generarCuadrado()

    def isVisible(self):
        self.inicio.pack()

    def isHiden(self):
        self.inicio.pack_forget()

import tkinter as tk
from tkinter import *
from Vistas.inicio import Inicio
from Vistas.Creditos import Creditos
from Vistas.Resultados import Resultados
from Vistas.Resultados2 import Resultados2
from Vistas.MatrizSec import MatrizSec

raiz = Tk()
raiz.geometry('1000x1000')

ColorBotones = '#B134E3'
ColorFondo = '#FFFFFF'
inicio = Inicio(raiz, ColorBotones, ColorFondo)
creditos = Creditos(raiz,ColorBotones, ColorFondo)
result = Resultados(raiz, ColorBotones, ColorFondo)
result2 = Resultados2(raiz, ColorBotones, ColorFondo)
macsec = MatrizSec(raiz, ColorBotones, ColorFondo)

inicio.setFrames(creditos,result,result2)
result.setFrames(inicio, macsec)
result2.setFrames(inicio, macsec)
macsec.setFrames(result)
creditos.setFrames(inicio)

inicio.generar()
creditos.generar()
inicio.isVisible()
raiz.mainloop()
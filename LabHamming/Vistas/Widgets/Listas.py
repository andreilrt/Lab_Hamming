import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

class Listas:
    lista = None
    raiz = None
    x = 0
    y = 0
    values = []
    func = None

    def __init__(self, root, x, y, valores, funcion):
        super().__init__()
        self.raiz = root
        self.x = x
        self.y = y
        self.values = valores
        self.func = funcion

    def Generar(self):
        self.lista = ttk.Combobox(self.raiz, state='readonly')
        self.lista.place(relx=self.x, rely=self.y)
        self.lista['values'] = self.values
        self.lista.bind("<<ComboboxSelected>>", self.func)

    def get(self):
        return self.lista.get()
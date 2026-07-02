from abc import ABC, abstractmethod
from tkinter import *
from classe_Figura import *

class Linha(Figura):
    def __init__(self, coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)

    def desenhar(self, canvas):
        canvas.create_line(self.coordenadas[0], self.coordenadas[1], self.coordenadas[2], self.coordenadas[3], fill= self.corBorda, dash= self.dash)
    
    def atualizar(self, novoX, novoY):
        self.coordenadas = [self.coordenadas[0], self.coordenadas[1], novoX, novoY]
        
    def finalizar(self):
        self.dash = ''
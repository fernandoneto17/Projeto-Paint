from figura import Figura
from tkinter import *

class Elipse(Figura):
    def __init__(self, coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)

    def desenhar(self, canvas):
        canvas.create_oval(self.coordenadas[0], self.coordenadas[1], self.coordenadas[2], self.coordenadas[3], outline= self.corBorda,fill= self.corPreenchimento, dash= self.dash)

    def atualizar(self, novoX, novoY):
        self.coordenadas = [self.coordenadas[0], self.coordenadas[1], novoX, novoY]

    def verificarFig(self):
        if abs(self.coordenadas[2] - self.coordenadas[0]) > 2 and abs(self.coordenadas[3] - self.coordenadas[1]) > 2:
            return True
        else:
            return False
        
    def finalizar(self):
        self.dash = ''

from abc import ABC, abstractmethod
from tkinter import *
from classe_Figura import *

class Linha(Figura):
    #Para criar uma linha, precisamos de 2 pontos(cada ponto possui 2 coordenadas) e as características da classe mãe, por isso nosso construtor está assim:
    def __init__(self, coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)

    #Criei uma linha utilizando as coordenadas dos pontos. O canvas é onde o desenho ocorre.
    def desenhar(self, canvas):
        canvas.create_line(self.coordenadas[0], self.coordenadas[1], self.coordenadas[2], self.coordenadas[3], fill= self.corBorda, dash= self.dash)
    
    #Isso aqui serve para quando eu desenhar uma linha e querer desenhar outra.
    def atualizar(self, novoX, novoY):
        self.coordenadas = [self.coordenadas[0], self.coordenadas[1], novoX, novoY]
    
    def verificarFig(self):
        if self.coordenadas[0] == self.coordenadas[2] and self.coordenadas[1] == self.coordenadas[3]:
            return False
        else:
            return True
        
    #Foi necessário criar este método para que, ao soltar o mouse, a linha fique contínua, e não desenhe tracejada igual ao rascunho.
    def finalizar(self):
        self.dash = ''
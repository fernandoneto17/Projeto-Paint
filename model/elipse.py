from .figura import Figura
from tkinter import *

# Classe filha da Figura
class Elipse(Figura):
    # Inicializa os atributos herdados
    def _init_(self, coordenadas, corBorda, corPreenchimento, dash):
        super()._init_(coordenadas, corBorda, corPreenchimento, dash)

    # Atualiza o ponto final da figura
    def atualizar(self, novoX, novoY):
        self.coordenadas = [self.coordenadas[0], self.coordenadas[1], novoX, novoY]

    # Verifica se a figura tem tamanho válido
    def verificarFig(self):
        if abs(self.coordenadas[2] - self.coordenadas[0]) > 2 and abs(self.coordenadas[3] - self.coordenadas[1]) > 2:
            return True
        else:
            return False
        
    # Finaliza a figura removendo o tracejado
    def finalizar(self):
        self.dash = ''

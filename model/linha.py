from .figura import *
from .figura import Figura

class Linha(Figura):
    #Para criar uma linha, precisamos de 2 pontos(cada ponto possui 2 coordenadas) e as características da classe mãe, por isso nosso construtor está assim:
    def __init__(self, coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)

   
    #Isso aqui serve para quando eu desenhar uma linha e querer desenhar outra.
    def atualizar(self, novoX, novoY):
        self.coordenadas = [self.coordenadas[0], self.coordenadas[1], novoX, novoY]
    
    #Esse método serve para conferirmos se a linha não vai ser um ponto. 
    def verificarFig(self):
        if self.coordenadas[0] == self.coordenadas[2] and self.coordenadas[1] == self.coordenadas[3]:
            return False
        else:
            return True
        
    #Foi necessário criar este método para que, ao soltar o mouse, a linha fique contínua, e não desenhe tracejada igual ao rascunho.
    def finalizar(self):
        self.dash = ''
    
    def contem_ponto(self, x, y):
        # Verifica se o ponto (x, y) está na linha usando a equação da linha
        x1, y1, x2, y2 = self.coordenadas
        if x1 == x2:  # Linha vertical
            return x == x1 and min(y1, y2) <= y <= max(y1, y2)
        elif y1 == y2:  # Linha horizontal
            return y == y1 and min(x1, x2) <= x <= max(x1, x2)
        else:
            # Verifica se o ponto está na linha usando a equação da linha
            return (y - y1) * (x2 - x1) == (y2 - y1) * (x - x1) and min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)
        
    def calcular_distancia(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    def mover(self, dx, dy):
        self.coordenadas[0] += dx
        self.coordenadas[1] += dy
        self.coordenadas[2] += dx
        self.coordenadas[3] += dy
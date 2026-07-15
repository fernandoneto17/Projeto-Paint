from .figura import Figura
# Essa classe serve para criarmos os "rabiscos"(mão livre)
class Rabisco(Figura):
    def __init__(self, coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)

    # Esse método modifica em tempo real as coordenadas para acompanhar a posição do ponteiro do mouse
    def atualizar(self,novoX,novoY):
        self.coordenadas.extend([novoX,novoY])

    # Método de verificação, verifica se o rabisco tem tamanho suficiente para nao ser apenas um ponto
    def verificarFig(self):
        if len(self.coordenadas) > 4:
            return True
        else:
            return False

    # Remove o traçado do desenho
    def finalizar(self):
        self.dash = ''
    
    def contem_ponto(self, x, y):
        # Verifica se o ponto (x, y) está próximo de algum ponto do rabisco
        for i in range(0, len(self.coordenadas), 2):
            px = self.coordenadas[i]
            py = self.coordenadas[i + 1]
            if abs(px - x) <= 2 and abs(py - y) <= 2:
                return True
        return False

    def calcular_distancia(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def mover(self, dx, dy):
        for i in range(0, len(self.coordenadas), 2):
            self.coordenadas[i] += dx
            self.coordenadas[i + 1] += dy
from .figura import Figura
import math

class Pentagono(Figura):
    def __init__(self, coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)
        self.xInicial = coordenadas[0]
        self.yInicial = coordenadas[1]

    def atualizar(self, novo_x, novo_y):
        xEsquerda = min(self.xInicial, novo_x)
        xDireita = max(self.xInicial, novo_x)
        yTopo = min(self.yInicial, novo_y)
        yBase = max(self.yInicial, novo_y)

        centroX = (xEsquerda + xDireita) / 2
        centroY = (yTopo + yBase) / 2
        raioX = (xDireita - xEsquerda) / 2
        raioY = (yBase - yTopo) / 2

        pontos = []

        for i in range(5):
            angulo = math.radians(-90 + i * 72)
            xVertice = centroX + raioX * math.cos(angulo)
            yVertice = centroY + raioY * math.sin(angulo)
            pontos.extend([int(xVertice), int(yVertice)])

        self.coordenadas = pontos

    def verificarFig(self):
        xs = self.coordenadas[::2]
        ys = self.coordenadas[1::2]
        largura = max(xs) - min(xs)
        altura = max(ys) - min(ys)
        return largura > 2 and altura > 2

    def finalizar(self):
        self.dash = ''

    def contem_ponto(self, x, y):
        pontos = list(zip(self.coordenadas[::2], self.coordenadas[1::2]))
        dentro = False
        j = len(pontos) - 1

        for i in range(len(pontos)):
            xi, yi = pontos[i]
            xj, yj = pontos[j]

            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 0.000001) + xi):
                dentro = not dentro

            j = i

        return dentro

    def calcular_distancia(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def mover(self, dx, dy):
        self.xInicial += dx
        self.yInicial += dy
        for i in range(0, len(self.coordenadas), 2):
            self.coordenadas[i] += dx
            self.coordenadas[i + 1] += dy
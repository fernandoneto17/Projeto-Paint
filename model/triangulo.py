from .figura import Figura

class Triangulo(Figura):
    # Inicializa os atributos herdados
    def __init__(self, coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)

    # Atualiza os 3 vértices do triângulo a partir do clique inicial e do arrasto do mouse
    def atualizar(self, novoX, novoY):
        x1 = self.coordenadas[0]
        y1 = self.coordenadas[1]
        x2 = novoX
        y2 = novoY

        x_esquerda = min(x1, x2)
        x_direita = max(x1, x2)
        y_topo = min(y1, y2)
        y_base = max(y1, y2)
        x_meio = (x_esquerda + x_direita) // 2

        self.coordenadas = [
            x_esquerda, y_base,
            x_direita, y_base,
            x_meio, y_topo
        ]

    # Verifica se o triângulo tem tamanho válido
    def verificarFig(self):
        base = abs(self.coordenadas[2] - self.coordenadas[0])
        altura = abs(self.coordenadas[5] - self.coordenadas[1])
        if base > 2 and altura > 2:
            return True
        else:
            return False

    # Finaliza a figura removendo o tracejado
    def finalizar(self):
        self.dash = ''

    def contem_ponto(self, x, y):
        x1, y1, x2, y2, x3, y3 = self.coordenadas

        area_total = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)
        area1 = abs((x*(y2-y3) + x2*(y3-y) + x3*(y-y2)) / 2)
        area2 = abs((x1*(y-y3) + x*(y3-y1) + x3*(y1-y)) / 2)
        area3 = abs((x1*(y2-y) + x2*(y-y1) + x*(y1-y2)) / 2)

        return abs(area_total - (area1 + area2 + area3)) < 1

    def calcular_distancia(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def mover(self, dx, dy):
        for i in range(0, len(self.coordenadas), 2):
            self.coordenadas[i] += dx
            self.coordenadas[i + 1] += dy
from .figura import Figura

# Classe filha da Figura
class Retangulo(Figura):
    # Inicializa os atributos herdados
    def __init__(self,coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)
    
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

    def contem_ponto(self, x, y):
        x1, y1, x2, y2 = self.coordenadas
        return x1 <= x <= x2 and y1 <= y <= y2
    
    def calcular_distancia(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    def mover(self, dx, dy):
        self.coordenadas[0] += dx
        self.coordenadas[1] += dy
        self.coordenadas[2] += dx
        self.coordenadas[3] += dy

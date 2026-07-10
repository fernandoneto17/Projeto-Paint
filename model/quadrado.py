# Para fazer a classe quadrado, utilizaremos a mesma base da classe retangulo.

from .figura import Figura

# Classe filha da Figura
class Quadrado(Figura):
    # Inicializa os atributos herdados
    def __init__(self,coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)
    
    # Atualiza o ponto final da figura
    def atualizar(self, novoX, novoY):
        x1 = self.coordenadas[0]
        y1 = self.coordenadas[1]
        # Calcula a diferença entre as coordenadas iniciais e finais
        delta_X = abs(novoX - x1)
        delta_Y = abs(novoY - y1)

        lado = max(delta_X, delta_Y)  # Determina o lado do quadrado como o maior delta
        sinal_x = 1 if novoX >= x1 else -1  # Determina o sinal para a coordenada X
        sinal_y = 1 if novoY >= y1 else -1  # Determina o sinal para a coordenada Y

        x2 = x1 + lado * sinal_x  # Calcula a coordenada X final
        y2 = y1 + lado * sinal_y  # Calcula a coordenada Y final
        self.coordenadas = [x1, y1, x2, y2]  # Atualiza as coordenadas do quadrado
       

    # Verifica se a figura tem tamanho válido
    def verificarFig(self):
        if abs(self.coordenadas[2] - self.coordenadas[0]) > 2 and abs(self.coordenadas[3] - self.coordenadas[1]) > 2:
            return True
        else:
            return False

    # Finaliza a figura removendo o tracejado
    def finalizar(self):
        self.dash = ''
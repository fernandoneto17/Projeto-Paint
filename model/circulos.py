from .figura import Figura

# Essa classe servirá de molde para os círculos que desenharmos
class Circulo(Figura):

    def __init__(self, coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)
    
        # Os itens indicados pelos indices 0,1,2,3 da lista coordenadas serao respectivamente x inicial,y inicial, x final, y final
        # Então iremos declarar novas variaveis para melhorar legibilidade

        self.ini_x = self.coordenadas[0]
        self.ini_y = self.coordenadas[1]
        self.fim_x = self.coordenadas[2]
        self.fim_y = self.coordenadas[3]

        self.raio = ( (self.ini_x - self.fim_x)**2 + (self.ini_y - self.fim_y)**2 ) ** 0.5

    # Metodo utilizado para criar um novo circulo
    def atualizar(self, novoX, novoY):
        self.coordenadas = [self.ini_x, self.ini_y, novoX, novoY]
        self.fim_x = novoX
        self.fim_y = novoY
        self.raio = ( (self.ini_x - self.fim_x)**2 + (self.ini_y - self.fim_y)**2 ) ** 0.5
        self.coordenadas = [self.ini_x - self.raio, self.ini_y - self.raio, self.ini_x + self.raio, self.ini_y + self.raio]

    # Metodo utilizado para verificar se a figura é um circulo ou nao
    def verificarFig(self):
        # Se o ponto inicial é o mesmo do final, ou seja, se(ini_x,ini_y) == (fim_x,fim_y),essa figura nao devera ser um circulo
        if (self.ini_x,self.ini_y) == (self.fim_x,self.fim_y):
            return False
        else:
            return True

    # Metodo para tirar o tracejado no desenho
    def finalizar(self):
        self.dash = ''

    def contem_ponto(self, x, y): 
        # Verifica se o ponto (x, y) está dentro do círculo usando a equação do círculo
        return (x - self.ini_x) ** 2 + (y - self.ini_y) ** 2 <= self.raio ** 2
    
    def calcular_distancia(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    def mover(self, dx, dy):
        self.ini_x += dx
        self.ini_y += dy
        self.fim_x += dx
        self.fim_y += dy
        # Atualiza as coordenadas do círculo após o movimento, da mesma maneira que definimos as coordenadas na linha 25
        self.coordenadas = [self.ini_x - self.raio, self.ini_y - self.raio, self.ini_x + self.raio, self.ini_y + self.raio]
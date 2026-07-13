from .linha import Linha
from .rabisco import Rabisco
from .elipse import Elipse
from .circulos import Circulo
from .retangulos import Retangulo
from .quadrado import Quadrado
from controller.estados.estadoLinha import EstadoLinha


class DesenhoModel:
    def __init__(self):
        self.figuraAtual = None
        self.desenhos = []
        self.estadoAtual = EstadoLinha()

        # Criação de dicionario para associar uma figura e chamar a função dessa figura a partir dos parametros dados:
        self.dicionarioFiguras = {
            'Linha': lambda coordenadas, corBorda, corPreenchimento: Linha(coordenadas, corBorda, corPreenchimento, dash=(4,2)),
            'Rabisco': lambda coordenadas, corBorda, corPreenchimento: Rabisco(coordenadas, corBorda, corPreenchimento, dash=''),
            'Elipse': lambda coordenadas, corBorda, corPreenchimento: Elipse(coordenadas, corBorda, corPreenchimento, dash=(4,2)),
            'Circulo': lambda coordenadas, corBorda, corPreenchimento: Circulo(coordenadas, corBorda, corPreenchimento, dash=(4,2)),
            'Retangulo': lambda coordenadas, corBorda, corPreenchimento: Retangulo(coordenadas, corBorda, corPreenchimento, dash=(4,2)),
            'Quadrado': lambda coordenadas, corBorda, corPreenchimento: Quadrado(coordenadas, corBorda, corPreenchimento, dash=(4,2))
        }

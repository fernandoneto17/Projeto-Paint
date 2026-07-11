from .linha import Linha
from .rabisco import Rabisco
from .elipse import Elipse
from .circulos import Circulo
from .retangulos import Retangulo
from .quadrado import Quadrado
from controller.estados.estadosLinha import EstadoLinha


class DesenhoModel:
    def __init__(self):
        self.figuraAtual = None
        self.desenhos = []
        self.ferramenta_atual = 'Linha'
        self.estado_atual = EstadoLinha()

        # Criação de dicionario para associar uma figura e chamar a função dessa figura a partir dos parametros dados:
        self.dicionario_figuras = {
            'Linha': lambda coordenadas, corBorda, corPreenchimento: Linha(coordenadas, corBorda, corPreenchimento, dash=(4,2)),
            'Rabisco': lambda coordenadas, corBorda, corPreenchimento: Rabisco(coordenadas, corBorda, corPreenchimento, dash=''),
            'Elipse': lambda coordenadas, corBorda, corPreenchimento: Elipse(coordenadas, corBorda, corPreenchimento, dash=(4,2)),
            'Círculo': lambda coordenadas, corBorda, corPreenchimento: Circulo(coordenadas, corBorda, corPreenchimento, dash=(4,2)),
            'Retângulo': lambda coordenadas, corBorda, corPreenchimento: Retangulo(coordenadas, corBorda, corPreenchimento, dash=(4,2)),
            'Quadrado': lambda coordenadas, corBorda, corPreenchimento: Quadrado(coordenadas, corBorda, corPreenchimento, dash=(4,2))
        }

        self.ferramentaAtual = 'Linha'
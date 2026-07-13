from .linha import Linha
from .rabisco import Rabisco
from .elipse import Elipse
from .circulos import Circulo
from .retangulos import Retangulo
from .quadrado import Quadrado
from controller.estados.estadoLinha import EstadoLinha
import pickle

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


    #Função do pickle para salvar arquivos
    def salvar_em_arquivo(self, caminho_arquivo):
        with open(caminho_arquivo, "wb") as arquivo:
            pickle.dump(self.desenhos, arquivo, protocol=pickle.HIGHEST_PROTOCOL)


    #Função do pickle para acessar arquivos
    def abrir_de_arquivo(self, caminho_arquivo):
        with open(caminho_arquivo, "rb") as arquivo:
            self.desenhos = pickle.load(arquivo)
        self.figuraAtual = None






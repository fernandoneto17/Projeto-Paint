from abc import ABC, abstractmethod

#Essa classe é a classe mãe, a qual julgamos que precisa ter esses 4 atributos gerais, pois serão comum a todas às figuras (filhas).
class Figura(ABC):
    def __init__(self, coordenadas, corBorda, corPreenchimento, dash):
        self.coordenadas = coordenadas
        self.corBorda = corBorda
        self.corPreenchimento = corPreenchimento
        self.dash = dash

#Esses são os métodos que TODAS as classes filhas precisam ter obrigatoriamente, por isso o uso de métodos abstratos.

    @abstractmethod
    def atualizar(self):
        pass

    @abstractmethod
    def verificarFig(self):
        pass

    @abstractmethod
    def finalizar(self):
        pass
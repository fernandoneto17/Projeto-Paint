from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, coordenadas, corBorda, corPreenchimento):
        self.coordenadas = coordenadas
        self.corBorda = corBorda
        self.corPreenchimento = corPreenchimento

    @abstractmethod
    def desenhar(self):
        pass

    @abstractmethod
    def atualizar(self):
        pass


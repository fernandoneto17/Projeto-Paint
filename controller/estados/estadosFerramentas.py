from abc import ABC, abstractmethod

class EstadoFerramenta(ABC):
    @abstractmethod
    def pressionar(self, controller, event):
        pass

    @abstractmethod
    def arrastar(self, controller, event):
        pass

    @abstractmethod
    def soltar(self, controller, event):
        pass
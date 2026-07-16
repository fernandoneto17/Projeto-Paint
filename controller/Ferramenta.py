from abc import ABC, abstractmethod

class Ferramenta(ABC):

    @abstractmethod
    def iniciar_figura_nova(self, event, executor):
        pass

    @abstractmethod
    def atualizar_figura_nova(self, event, executor):
        pass

    @abstractmethod
    def incluir_figura_nova(self, event, executor):
        pass
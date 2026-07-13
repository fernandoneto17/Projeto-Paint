from abc import ABC

class EstadoFerramenta(ABC):
    tipoFigura = None

    def pressionar(self, controller, event):
        controller.iniciar_figura_nova(event)

    def arrastar(self, controller, event):
        controller.atualizar_figura_nova(event)

    def soltar(self, controller, event):
        controller.incluir_figura_nova(event)
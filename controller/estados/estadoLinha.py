from .estadosFerramentas import EstadoFerramenta

class EstadoLinha(EstadoFerramenta):
        def pressionar_mouse(self, controller, event):
            controller.iniciar_figura_nova(event)
        
        def arrastar_mouse(self, controller, event):
            controller.atualizar_figura_nova(event)

        def soltar_mouse(self, controller, event):
            controller.incluir_figura_atual(event)

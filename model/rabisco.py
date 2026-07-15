from .figura import Figura
# Essa classe serve para criarmos os "rabiscos"(mão livre)
class Rabisco(Figura):
    def __init__(self, coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)

    # Esse método modifica em tempo real as coordenadas para acompanhar a posição do ponteiro do mouse
    def atualizar(self,novoX,novoY):
        self.coordenadas.extend([novoX,novoY])

    # Método de verificação, verifica se o rabisco tem tamanho suficiente para nao ser apenas um ponto
    def verificarFig(self):
        if len(self.coordenadas) > 4:
            return True
        else:
            return False

    # Remove o traçado do desenho
    def finalizar(self):
        self.dash = ''

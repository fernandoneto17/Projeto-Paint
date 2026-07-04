from figura import Figura

class Rabisco(Figura):
    def __init__(self, coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)

    def desenhar(self,canvas):
        canvas.create_line(self.coordenadas,fill=self.corBorda,dash = self.dash)
    
    def atualizar(self,novoX,novoY):
        self.coordenadas.extend([novoX,novoY])
    
    def verificarFig(self):
        if len(self.coordenadas) > 4:
            return True
        else:
            return False

    def finalizar(self):
        self.dash = ''

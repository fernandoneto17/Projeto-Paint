from figura import Figura

class Rabisco(Figura):
    def __init__(self, coordenadas, corBorda, corPreenchimento, dash):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)

    def desenhar(self,canvas):
        canvas.create_line(self.coordenadas,fill=self.corBorda,dash = self.dash)
    
    def atualizar(self,novoX,novoY):
        self.coordenadas.append((novoX,novoY))
    
    def verificarFig(self):
        return len(self.coordenadas > 1)

    def finalizar(self):
        self.dash = ''

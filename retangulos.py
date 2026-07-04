from figura import Figura


class Retangulo(Figura):
    def __init__(self,coordenadas, x_inicial, y_inicial, corBorda="black", corPreenchimento="", dash=None):
        super().__init__(coordenadas, corBorda, corPreenchimento, dash)
        coordenadas = [x_inicial, y_inicial, x_inicial, y_inicial]
        

    def desenhar(self, canvas):
        x1, y1, x2, y2 = self.coordenadas
        canvas.create_rectangle(
            x1, y1, x2, y2,
            outline=self.corBorda,
            fill=self.corPreenchimento,
            dash=self.dash
        )

    def atualizar(self, event):
        self.coordenadas[2] = event.x
        self.coordenadas[3] = event.y

    def verificarFig(self):
        x1, y1, x2, y2 = self.coordenadas
        return abs(x2 - x1) > 2 and abs(y2 - y1) > 2

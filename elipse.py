from figura import Figura

class Elipse(Figura):
    def _init_(self, coordenadas, x_inicial, y_inicial, corBorda="black", corPreenchimento="", dash=None):
        super()._init_(coordenadas, corBorda, corPreenchimento, dash)
        coordenadas = [x_inicial, y_inicial, x_inicial, y_inicial]

    def desenhar(self, canvas):
        centro_x, centro_y, raio_x, raio_y  = self.coordenadas
        canvas.create_oval(centro_x, centro_y, raio_x, raio_y,outline=self.corBorda,fill=self.corPreenchimento,dash=self.dash)

    def atualizar(self, event):
        self.coordenadas[2] = event.x
        self.coordenadas[3] = event.y

    def verificarFig(self):
        centro_x, centro_y, raio_x, raio_y = self.coordenadas
        return abs(raio_x- centro_x) > 2 and abs(raio_y - centro_y) > 2

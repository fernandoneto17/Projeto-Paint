from model.linha import Linha
from model.elipse import Elipse
from model.circulos import Circulo
from model.retangulos import Retangulo
from model.rabisco import Rabisco
from model.quadrado import Quadrado

class Executor:
    def __init__(self, interface):
        self.interface = interface
        self.xInicial = 0
        self.yInicial = 0
        self.figuraAtual = None
        self.desenhos = []

        # Ajustando os cliques do mouse:
        self.interface.canvas.bind('<ButtonPress-1>', self.iniciar_figura_nova)
        self.interface.canvas.bind('<B1-Motion>', self.atualizar_figura_nova)
        self.interface.canvas.bind('<ButtonRelease-1>', self.incluir_figura_nova)

    def iniciar_figura_nova(self, event): 
        self.xInicial = event.x
        self.yInicial = event.y
        tipoFigura = self.interface.tipoFiguraVar.get()
        corBorda = self.interface.cores_borda.get(self.interface.corBordaVar.get())
        corPreenchimento = self.interface.cores_preenchimento.get(self.interface.corPreenchimentoVar.get())

        coordenadas = [self.xInicial, self.yInicial, self.xInicial, self.yInicial]

        # O Controller cria os Models:
        if tipoFigura == 'Linha':
            self.figuraAtual = Linha(coordenadas, corBorda, corPreenchimento, dash=(4,2))
        elif tipoFigura == 'Rabisco':
            self.figuraAtual = Rabisco(coordenadas, corBorda, corPreenchimento, dash='')
        elif tipoFigura == 'Retângulo':
            self.figuraAtual = Retangulo(coordenadas, corBorda, corPreenchimento, dash=(4,2))
        elif tipoFigura == 'Elipse':
            self.figuraAtual = Elipse(coordenadas, corBorda, corPreenchimento, dash=(4,2))
        elif tipoFigura == 'Círculo':
            self.figuraAtual = Circulo(coordenadas, corBorda, corPreenchimento, dash=(4,2))
        elif tipoFigura == 'Quadrado':
            self.figuraAtual = Quadrado(coordenadas, corBorda, corPreenchimento, dash=(4,2))

        # O Controller manda a View desenhar o modelo atual:
        if self.figuraAtual:
            self.interface.desenhar_figura(self.figuraAtual)

    def atualizar_figura_nova(self, event):
        if self.figuraAtual is not None:
            self.interface.limpar_canvas()

            # Redesenhando o histórico usando a View:
            for desenho in self.desenhos:
                self.interface.desenhar_figura(desenho)

            # Atualiza o Model e renderiza pela View:
            self.figuraAtual.atualizar(event.x, event.y)
            self.interface.desenhar_figura(self.figuraAtual)
                
    def incluir_figura_nova(self, event):
        if self.figuraAtual is not None:
            self.interface.canvas.delete("all")

            for desenho in self.desenhos:
                self.interface.desenhar_figura(desenho)
            
            if self.figuraAtual.verificarFig():
                self.figuraAtual.finalizar()
                self.interface.desenhar_figura(self.figuraAtual)
                self.desenhos.append(self.figuraAtual)

            self.figuraAtual = None

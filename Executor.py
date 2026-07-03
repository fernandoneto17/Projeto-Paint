from classe_Linha import Linha


class Executor:
    def __init__(self, interface):
        # O Executor guarda a interface para poder ler as cores e usar o canvas depois.
        self.interface = interface

        # Variáveis para guardar as coordenadas de onde o mouse clicou e a figura que está sendo desenhada:
        self.xInicial = 0
        self.yInicial = 0
        self.figuraAtual = None
        self.desenhos = []

        #Ajustando os cliques do mouse:
        self.interface.canvas.bind('<ButtonPress-1>', self.iniciar_figura_nova)
        self.interface.canvas.bind('<B1-Motion>', self.atualizar_figura_nova)
        self.interface.canvas.bind('<ButtonRelease-1>', self.incluir_figura_nova)

    def iniciar_figura_nova(self, event): 
        self.xInicial = event.x
        self.yInicial = event.y
        tipoFigura = self.interface.tipoFiguraVar.get()
        corBorda = self.interface.tradutorCores[self.interface.corBordaVar.get()]
        corPreenchimento = self.interface.tradutorCores[self.interface.corPreenchimentoVar.get()]

        if tipoFigura == 'Linha':
            coordenadas = [self.xInicial, self.yInicial, self.xInicial, self.yInicial]
            self.figuraAtual = Linha(coordenadas, corBorda, corPreenchimento, dash= (4,2))
            self.figuraAtual.desenhar(self.interface.canvas)
        elif tipoFigura == 'Rabisco':
            pass
        elif tipoFigura == 'Retângulo':
            coordenadas = [self.xInicial, self.yInicial, self.xInicial, self.yInicial]
            self.figuraAtual = Retangulo(coordenadas, corBorda, corPreenchimento, dash= (4,2))
            self.figuraAtual.desenhar(self.interface.canvas)
        elif tipoFigura == 'Elipse':
            coordenadas = [self.xInicial, self.yInicial, self.xInicial, self.yInicial]
            self.figuraAtual = Elipse(coordenadas, corBorda, corPreenchimento, dash= (4,2))
            self.figuraAtual.desenhar(self.interface.canvas)
        elif tipoFigura == 'Círculo':
            coordenadas = [self.xInicial, self.yInicial, self.xInicial, self.yInicial]
            self.figuraAtual = Circulo(coordenadas, corBorda, corPreenchimento, dash= (4,2))
            self.figuraAtual.desenhar(self.interface.canvas)

    def atualizar_figura_nova(self, event):
        if self.figuraAtual is not None:
            self.interface.canvas.delete("all")

            for desenho in self.desenhos:
                desenho.desenhar(self.interface.canvas)
        
            self.figuraAtual.atualizar(event.x, event.y)
            self.figuraAtual.desenhar(self.interface.canvas)
                
    def incluir_figura_nova(self, event):
        if self.figuraAtual is not None:
            self.interface.canvas.delete("all")

            for desenho in self.desenhos:
                desenho.desenhar(self.interface.canvas)
            
            if self.figuraAtual.verificarFig() == True:
                self.figuraAtual.finalizar()
                self.figuraAtual.desenhar(self.interface.canvas)
                self.desenhos.append(self.figuraAtual)

            self.figuraAtual = None
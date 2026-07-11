from model.linha import Linha
from model.elipse import Elipse
from model.circulos import Circulo
from model.retangulos import Retangulo
from model.rabisco import Rabisco
from model.quadrado import Quadrado

class Executor:
    def __init__(self, interface, model):
        self.interface = interface
        self.model = model
        self.xInicial = 0
        self.yInicial = 0
        
        
        # Ajustando os cliques do mouse:
        self.interface.canvas.bind('<ButtonPress-1>', self.iniciar_figura_nova)
        self.interface.canvas.bind('<B1-Motion>', self.atualizar_figura_nova)
        self.interface.canvas.bind('<ButtonRelease-1>', self.incluir_figura_nova)

    def iniciar_figura_nova(self, event): 
        self.xInicial = event.x
        self.yInicial = event.y
        self.model.ferramenta = self.interface.tipoFiguraVar.get()
        tipoFigura = self.model.ferramenta
        corBorda = self.interface.cores_borda.get(self.interface.corBordaVar.get())
        corPreenchimento = self.interface.cores_preenchimento.get(self.interface.corPreenchimentoVar.get())
    
        coordenadas = [self.xInicial, self.yInicial, self.xInicial, self.yInicial]
        # chamando a função para criar o onjeto a partir do clique do mouse
        self.criar_figura_atual(tipoFigura, coordenadas, corBorda, corPreenchimento)
        
    def criar_figura_atual(self, tipoFigura, coordenadas, corBorda, corPreenchimento):
        self.model.figuraAtual = self.model.dicionarios_figuras[tipoFigura](coordenadas, corBorda, corPreenchimento)

        
       
        # O Controller manda a View desenhar o modelo atual:
        if self.model.figuraAtual:
            self.interface.desenhar_figura(self.model.figuraAtual)

    def atualizar_figura_nova(self, event):
        if self.model.figuraAtual is not None:
            self.interface.limpar_canvas()

            # Redesenhando o histórico usando a View:
            for desenho in self.desenhos:
                self.interface.desenhar_figura(desenho)

            # Atualiza o Model e renderiza pela View:
            self.model.figuraAtual.atualizar(event.x, event.y)
            self.interface.desenhar_figura(self.model.figuraAtual)
                
    def incluir_figura_nova(self, event):
        if self.model.figuraAtual is not None:
            self.interface.canvas.delete("all")

            for desenho in self.desenhos:
                self.interface.desenhar_figura(desenho)
            
            if self.model.figuraAtual.verificarFig():
                self.model.figuraAtual.finalizar()
                self.interface.desenhar_figura(self.model.figuraAtual)
                self.desenhos.append(self.model.figuraAtual)

            self.model.figuraAtual = None
    
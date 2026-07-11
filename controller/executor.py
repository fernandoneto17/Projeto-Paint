from .estadoLinha import EstadoLinha
from .estadoRetangulo import EstadoRetangulo
from .estadoElipse import EstadoElipse
from .estadoQuadrado import EstadoQuadrado
from .estadoCirculo import EstadoCirculo
from .estadoRabisco import EstadoRabisco

class Executor:
    def __init__(self, interface):
        self.interface = interface
        self.figuraAtual = None
        self.desenhos = []

        self.estados = {
            'Linha': EstadoLinha(),
            'Retângulo': EstadoRetangulo(),
            'Quadrado': EstadoQuadrado(),
            'Elipse': EstadoElipse(),
            'Círculo': EstadoCirculo(),  
            'Rabisco': EstadoRabisco()
        }
        self.estadoAtual = None

        # Ajustando os cliques do mouse:
        self.interface.canvas.bind('<ButtonPress-1>', self.iniciar_figura_nova)
        self.interface.canvas.bind('<B1-Motion>', self.atualizar_figura_nova)
        self.interface.canvas.bind('<ButtonRelease-1>', self.incluir_figura_nova)

    #Criando o método que encontra a classe:
    def acharEstadoAtual(self):
        tipoAtual = self.interface.tipoFiguraVar.get()
        return self.estados.get(tipoAtual)
    
    #Criando o método que elimina os ifs:
    def mudarEstado(self):
        self.estadoAtual = self.acharEstadoAtual()

    def iniciar_figura_nova(self, event): 
        #Atualizando o estado:
        self.mudarEstado()
        if self.estadoAtual is not None:
            # Passamos o evento e o próprio Executor (self) para o Estado ter acesso aos dados.
            self.estadoAtual.iniciar_figura_nova(event, self)

    #Repetindo o processo com as outras funções:
    def atualizar_figura_nova(self, event):
        if self.estadoAtual is not None:
            self.estadoAtual.atualizar_figura_nova(event, self)

                
    def incluir_figura_nova(self, event):
        if self.estadoAtual is not None:
            self.estadoAtual.incluir_figura_nova(event, self)

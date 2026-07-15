from .estados.estadoLinha import EstadoLinha
from .estados.estadoRabisco import EstadoRabisco
from .estados.estadoCirculo import EstadoCirculo
from .estados.estadoElipse import EstadoElipse
from .estados.estadoRetangulo import EstadoRetangulo
from .estados.estadoQuadrado import EstadoQuadrado
from tkinter import messagebox


class Executor:
    def __init__(self, interface, model):
        self.interface = interface
        self.model = model
        self.interface.controlador = self  # Passa a referência do Executor para a InterfaceGrafica, permitindo que a View chame os métodos do Controller.
        self.xInicial = 0
        self.yInicial = 0

        # Tabela de mapeamento entre o nome escolhido na interface e a classe de estado correspondente. Isso permite trocar de ferramenta sem usar if/elif.
        self.mapeamentoEstados = {
        'Linha': EstadoLinha,
        'Rabisco': EstadoRabisco,
        'Circulo': EstadoCirculo,
        'Elipse': EstadoElipse,
        'Retangulo': EstadoRetangulo,
        'Quadrado': EstadoQuadrado,
    }
        
        # Associa os eventos do mouse que ocorrem no canvas da View aos métodos de tratamento definidos no Controller.
        self.interface.canvas.bind('<ButtonPress-1>', self.ao_pressionar_mouse)
        self.interface.canvas.bind('<B1-Motion>', self.ao_arrastar_mouse)
        self.interface.canvas.bind('<ButtonRelease-1>', self.ao_soltar_mouse)

    # Inicia a criação da figura atual a partir do ponto em que o mouse foi pressionado.
    def iniciar_figura_nova(self, event): 
        self.xInicial = event.x
        self.yInicial = event.y

        corBorda = self.interface.cores.get(self.interface.corBordaVar.get())
        corPreenchimento = self.interface.cores.get(self.interface.corPreenchimentoVar.get())

        coordenadas = [self.xInicial, self.yInicial, self.xInicial, self.yInicial]

        # O tipo da figura vem do estado atual. Isso evita condicionais e faz o comportamento depender do objeto de estado.
        tipoFigura = self.model.estadoAtual.tipoFigura

        # Solicita a criação da figura atual no Model com base no tipo informado pelo estado ativo e nos dados coletados da View.
        self.criar_figura_atual(tipoFigura, coordenadas, corBorda, corPreenchimento)
        
    # Cria no Model a figura que está sendo desenhada neste momento. 
    def criar_figura_atual(self, tipoFigura, coordenadas, corBorda, corPreenchimento):
        self.model.figuraAtual = self.model.dicionarioFiguras[tipoFigura](coordenadas, corBorda, corPreenchimento)

        # O Controller manda a View desenhar o modelo atual:
        if self.model.figuraAtual:
            self.interface.desenhar_figura(self.model.figuraAtual)

    # Atualiza a figura em construção enquanto o mouse está sendo arrastado.
    def atualizar_figura_nova(self, event):
        # Só atualiza se já existir uma figura em processo de criação.
        if self.model.figuraAtual is not None:
            self.interface.limpar_canvas()


            # Redesenhando o histórico usando a View:
            for desenho in self.model.desenhos:
                self.interface.desenhar_figura(desenho)


            # Atualiza o Model e renderiza pela View:
            self.model.figuraAtual.atualizar(event.x, event.y)
            self.interface.desenhar_figura(self.model.figuraAtual)

    # Finaliza a figura quando o botão do mouse é solto e a adiciona ao histórico permanente do Model.        
    def incluir_figura_nova(self, event):
        if self.model.figuraAtual is not None:
            self.interface.limpar_canvas()


            for desenho in self.model.desenhos:
                self.interface.desenhar_figura(desenho)
           
            if self.model.figuraAtual.verificarFig():
                self.model.figuraAtual.finalizar()
                self.interface.desenhar_figura(self.model.figuraAtual)
                self.model.desenhos.append(self.model.figuraAtual)

            self.model.figuraAtual = None
    
    # Sincroniza o estado atual com a ferramenta selecionada na View. O nome escolhido na interface é convertido na classe de estado correspondente.
    def atualizar_estado_ferramenta(self):
        ferramentaEscolhida = self.interface.tipoFiguraVar.get()
        classeEstado = self.mapeamentoEstados[ferramentaEscolhida]
        self.model.estadoAtual = classeEstado()

    # Antes de iniciar o desenho, atualiza o estado conforme a ferramenta escolhida e delega o tratamento do evento ao estado atual.
    def ao_pressionar_mouse(self, event):
        self.atualizar_estado_ferramenta()
        self.model.estadoAtual.pressionar(self, event)

    # Delega ao estado atual o comportamento durante o arraste do mouse.
    def ao_arrastar_mouse(self, event):
        self.model.estadoAtual.arrastar(self, event)

    # Delega ao estado atual o comportamento de finalização do desenho.
    def ao_soltar_mouse(self, event):
        self.model.estadoAtual.soltar(self, event)


    #Salva o desenho como arquivo.pkl
    def salvar_desenho(self):
        caminho = self.interface.pedir_caminho_salvar()
        if not caminho:
            return


         #Testa se está salvando os desenhos
        try:
            self.model.salvar_em_arquivo(caminho)
            messagebox.showinfo("Salvar", "Desenho salvo com sucesso.")
        except Exception as erro:
            messagebox.showerror("Erro", f"Não foi possível salvar o desenho.\n{erro}")


    #Abre desenhos com extensão .pkl
    def abrir_desenho(self):
        caminho = self.interface.pedir_caminho_abrir()
        if not caminho:
            return


        #Testa se está recuperando os desenhos
        try:
            self.model.abrir_de_arquivo(caminho)
            self.interface.limpar_canvas()


            for desenho in self.model.desenhos:
                self.interface.desenhar_figura(desenho)


            messagebox.showinfo("Abrir", "Desenho carregado com sucesso.")
        except Exception as erro:
            messagebox.showerror("Erro", f"Não foi possível abrir o desenho.\n{erro}")
   




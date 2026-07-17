from .estados.estadoLinha import EstadoLinha
from .estados.estadoRabisco import EstadoRabisco
from .estados.estadoCirculo import EstadoCirculo
from .estados.estadoElipse import EstadoElipse
from .estados.estadoRetangulo import EstadoRetangulo
from .estados.estadoQuadrado import EstadoQuadrado
from .estados.estadoTriangulo import EstadoTriangulo
from .estados.estadoLosango import EstadoLosango
from .estados.estadoPentagono import EstadoPentagono
from .estados.estadoHexagono import EstadoHexagono
from tkinter import messagebox
from .estados.estadoSelecionar import EstadoSelecionar


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
        'Triangulo': EstadoTriangulo,
        'Losango': EstadoLosango,
        'Pentagono': EstadoPentagono,
        'Hexagono': EstadoHexagono,
        'Selecionar': EstadoSelecionar,
    }
        
        # Associa os eventos do mouse que ocorrem no canvas da View aos métodos de tratamento definidos no Controller.
        self.interface.canvas.bind('<ButtonPress-1>', self.ao_pressionar_mouse)
        self.interface.canvas.bind('<B1-Motion>', self.ao_arrastar_mouse)
        self.interface.canvas.bind('<ButtonRelease-1>', self.ao_soltar_mouse)

        # Atalhos de teclado para a ferramenta de Seleção:
        self.interface.root.bind("<Delete>", self.apagar_figura)
        self.interface.root.bind("<Control-c>", self.copiar_figura)
        self.interface.root.bind("<Control-v>", self.colar_figura)
        # As 4 direções para controlar as camadas:
        self.interface.root.bind("<Up>", self.mover_para_topo)
        self.interface.root.bind("<Down>", self.mover_para_fundo)
        self.interface.root.bind("<Right>", self.mover_para_frente)
        self.interface.root.bind("<Left>", self.mover_para_tras)

        #Sempre que a variável de cor da View mudar (write), chamamos as funções de atualizar:
        self.interface.corBordaVar.trace_add('write', self.atualiza_cor_linha)
        self.interface.corPreenchimentoVar.trace_add('write', self.atualiza_cor_preenchimento)

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
        self.model.figuraAtual = self.model.dicionarioFiguras[tipoFigura](
            coordenadas, corBorda, corPreenchimento
    )

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

            self.model.figuraAtual.atualizar(event.x, event.y)

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
   
    def apagar_tudo(self):
        # Limpa a lista de desenhos no Model
        self.model.desenhos.clear()
        self.model.figuraSelecionada = None  # Reseta a figura selecionada
        self.interface.limpar_canvas()  # Limpa o canvas na View


    #Função auxiliar para limpar e redesenhar tudo rapidamente(similar a redesenhar_tudo da classe estadoSelecionar):
    def atualizar_tela(self):
        self.interface.limpar_canvas()
        for desenho in self.model.desenhos:
            self.interface.desenhar_figura(desenho)

    def apagar_figura(self, event):
        #Chama a função de apagar do model e atualiza a tela
        self.model.apagar_selecionada()
        self.atualizar_tela()

    def copiar_figura(self, event):
        #Chama a função de copiar do model e obviamente não precisa atualizar a tela, pois estamos copiando apenas.
        self.model.copiar_selecionada()

    #Repetindo o processo de chamar a função do model e atualizar a tela:
    def colar_figura(self, event):
        self.model.colar()
        self.atualizar_tela()

    def mover_para_frente(self, event=None):
        self.model.subir_uma_camada()
        self.atualizar_tela()

    def mover_para_tras(self, event=None):
        self.model.abaixar_uma_camada()
        self.atualizar_tela()

    def mover_para_topo(self, event=None):
        self.mover_para_frente()

    def mover_para_fundo(self, event=None):
        self.mover_para_tras()

    #Parte da view:
    def atualiza_cor_linha(self, *args):
        #Barreira contra um executor fantasma (criado pela view) para impedir um erro de deixar objeto sem tipo/atributo:
        if self.model is None:
            return
        
        #Pegando a figura selecionada:
        figura = self.model.selecionada() 
        if figura is not None:
            #Pegando o nome em português (ex: "Preto"):
            nomeCorPT = self.interface.corBordaVar.get()
            #Traduzindo para inglês usando o dicionário da View (ex: "black"):
            corIngles = self.interface.cores.get(nomeCorPT)
            
            #Atualizando a figura e redesenhando a tela:
            figura.corBorda = corIngles
            self.atualizar_tela()
    
    #Repetindo o processo:
    def atualiza_cor_preenchimento(self, *args):
        #Barreira contra um executor fantasma (criado pela view) para impedir um erro de deixar objeto sem tipo/atributo:
        if self.model is None:
            return 
        
        figura = self.model.selecionada() 
        if figura is not None:
            nomeCorPT = self.interface.corPreenchimentoVar.get()
            corIngles = self.interface.cores.get(nomeCorPT)
            
            figura.corPreenchimento = corIngles
            self.atualizar_tela()

    #Criação do método selecionarFigura para a view:
    def selecionar_figura(self):
        #Mudando a ferramenta ativa para 'Selecionar':
        self.interface.tipoFiguraVar.set('Selecionar')
        #Atualizando o Estado atual para o EstadoSelecionar:
        self.atualizar_estado_ferramenta()

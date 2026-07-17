from tkinter import *
from tkinter import filedialog, messagebox
from controller.executor import Executor
import os


class InterfaceGrafica:
    def __init__(self, root):
        #Recebendo o root como atributo. Por que apenas ele? Porque precisamos de uma janela para poder criarmos o restante da parte gráfica, ou seja, precisamos dele pronto.
        self.root = root
        self.frame = Frame(root)
        #Criando onde desenha:
        self.canvas = Canvas(self.frame, bg='white', width=1280, height=550)
        self.canvas.pack()

        #Criando as variáveis especiais que guardam a escolha do usuário:
        self.corBordaVar = StringVar()
        self.corPreenchimentoVar = StringVar()
        self.tipoFiguraVar = StringVar()
        self.tipoFiguraVar.set('Linha')
        self.corBordaVar.set('Preto')
        self.corPreenchimentoVar.set('Branco')

        #Objeto do controlador que será usado para chamar os métodos do Controller. Ele é criado aqui para que a View possa chamar os métodos do Controller.
        self.controlador = Executor(self, None )  # Passando self (InterfaceGrafica) e None (DesenhoModel) para o Executor. O DesenhoModel será passado posteriormente no Main.py.   

        pastaView = os.path.dirname(os.path.abspath(__file__))  # Obtém o diretório do arquivo atual
        pastaProjeto = os.path.dirname(pastaView)  # Obtém o diretório pai (projeto)
        pastaImagens = os.path.join(pastaProjeto, 'figuras')  # Caminho completo para a pasta de imagens

        #Criando o dicionário das cores, assim como foi feito no hiperativo:
        self.cores = {
                            'Branco': 'white',
                            'Preto': 'black',
                            'Azul': 'blue',
                            'Amarelo': 'yellow',
                            'Vermelho': 'red',
                            'Verde': 'green',
                            'Rosa': 'pink',
                            'Laranja': 'orange',
                            'Roxo': 'purple',
                            'Cinza': 'gray',
                            'Marrom': 'brown',
                            'Ciano': 'cyan',
                            'Magenta': 'magenta',
                            'Dourado': '#FFD700',
                            'Prata': '#C0C0C0',
                            'Turquesa': '#40E0D0',
                            'Violeta': '#8A2BE2',
                            'Verde Limão': '#32CD32',
                            'Rosa Choque': '#FF69B4',
                            'Azul Claro': '#ADD8E6',
                            'Vermelho Escuro': "#5C0000",
                            }


        self.figuraImagem = [
        ('Linha', 'linha.png'),
        ('Rabisco', 'rabisco.png'),
        ('Retangulo', 'retangulo.png'),
        ('Circulo', 'circulo.png'),
        ('Elipse', 'elipse.png'),
        ('Quadrado','quadrado.png'),
        ('Triangulo','triangulo.png'),
        ('Losango','losango.png'),
        ('Pentagono','pentagono.png'),
        ('Hexagono','hexagono.png')
        ]


        #Criando um frame para os botões, que ficará acima do canvas:
        self.frameBotoes = Frame(root)
        self.frameBotoes.pack(side = TOP, fill = X)
        Label(self.frameBotoes, font=("Arial", 10, "bold"), text="Formas:").grid(row=0, column=0, padx=14, pady=10, sticky="w")
        
        for i, (nome, arquivo) in enumerate(self.figuraImagem):
            caminhoImagem = os.path.join(pastaImagens, arquivo)#Para acessar as imagens da pasta figuras(o caminho está no trecho de código no inicio da classe)
            imagem = PhotoImage(file=caminhoImagem)
            botao = Button(
                self.frameBotoes,
                image=imagem,
                activebackground="#CFCFCF",
                activeforeground="#000000",
                relief="ridge",
                overrelief="raised",
                padx=6,
                pady=5,
                cursor="hand2",
                command=lambda n=nome: self.tipoFiguraVar.set(n)
            )
            botao.image = imagem
            botao.grid(column=i + 1, row=0, padx=5, pady=5, sticky=W)

        
        self.botaoSalvar = Button(self.frameBotoes,
            text="💾 Salvar arquivo",
            bg="#E9E9E9",
            fg="#222222",
            activebackground="#CFCFCF",
            activeforeground="#000000",
            font=("Arial", 10, "bold"),
            bd=1,
            relief="ridge",
            overrelief="raised",
            highlightthickness=0,
            padx=6,
            pady=5,
            cursor="hand2", 
            command=lambda: self.controlador.salvar_desenho())
        
        self.botaoSalvar.grid(row=0, column=len(self.figuraImagem) + 2, padx=10, pady=3)

        self.botaoAbrir = Button(self.frameBotoes,
            text="📂 Abrir",
            bg="#E8E8E8",
            fg="#222222",
            activebackground="#CFCFCF",
            activeforeground="black",
            font=("Arial", 10, "bold"),
            bd=1,
            relief="ridge",
            overrelief="raised",
            padx=6,
            pady=5,
            cursor="hand2", command=lambda: self.controlador.abrir_desenho())
        self.botaoAbrir.grid(row=0, column=len(self.figuraImagem) + 3, padx=10, pady=3)

        self.botaoLimpar = Button(self.frameBotoes,
            text="🧹 Limpar tela",
            bg="#F2F2F2",
            fg="#333333",
            activebackground="#CFCFCF",
            activeforeground="#111111",
            font=("Arial", 10, "bold"),
            bd=1,
            relief="ridge",
            overrelief="raised",
            highlightthickness=0,
            padx=6,
            pady=5,
            cursor="hand2",
            command=lambda: self.controlador.apagar_tudo())
        self.botaoLimpar.grid(row=0, column=len(self.figuraImagem) + 4, padx=10, pady=3)

        self.selecionarFigura = Button(self.frameBotoes,
            text="🔍 Selecionar figura",
            bg="#E6E6E6",
            fg="#1F1F1F",
            activebackground="#CFCFCF",
            activeforeground="#000000",
            font=("Arial", 10, "bold"),
            bd=1,
            relief="ridge",
            overrelief="raised",
            highlightthickness=0,
            padx=6,
            pady=5,
            cursor="hand2", command=lambda: self.controlador.selecionar_figura())
        self.selecionarFigura.grid(row=0, column=len(self.figuraImagem) + 5, padx=10, pady=3, sticky="w")

       # Frame pai para manter os dois grupos na mesma linha
        self.frameCores = Frame(self.root)
        self.frameCores.pack(side=TOP, fill=X, padx=5, pady=5)

        # Frame das cores da borda
        self.frameCoresBorda = Frame(self.frameCores)
        self.frameCoresBorda.grid(row=0, column=0, padx=0, pady=5, sticky="w")

        Label(self.frameCoresBorda, font=("Arial", 10, "bold"), text="Cor da borda:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

        for i, (nomeCor, corbg) in enumerate(self.cores.items()):
            if i < 7:
                linha = 0
                coluna = i + 1
            elif i < 14:
                linha = 1
                coluna = i - 6
            else:
                linha = 2
                coluna = i - 13

            Button(
                self.frameCoresBorda,
                bg=corbg,
                width=2,
                height=1,
                activebackground="#CFCFCF",
                activeforeground="#000000",
                relief="ridge",
                overrelief="raised",
                padx=6,
                pady=5,
                cursor="hand2",
                command=lambda cor=nomeCor: self.corBordaVar.set(cor)
            ).grid(row=linha, column=coluna, padx=3, pady=3)

        # Frame das cores do preenchimento
        self.frameCoresFill = Frame(self.frameCores)
        self.frameCoresFill.grid(row=0, column=1, padx=15, pady=5, sticky="w")

        Label(self.frameCoresFill, font=("Arial", 10, "bold"), text="Cor do preenchimento:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

        for i, (nomeCorFill, corBg) in enumerate(self.cores.items()):
            if i < 7:
                linha = 0
                coluna = i + 1
            elif i < 14:
                linha = 1
                coluna = i - 6
            else:
                linha = 2
                coluna = i - 13

            Button(
                self.frameCoresFill,
                bg=corBg,
                width=2,
                height=1,
                activebackground="#CFCFCF",
                activeforeground="#000000",
                relief="ridge",
                overrelief="raised",
                padx=6,
                pady=5,
                cursor="hand2", 
                command=lambda cor=nomeCorFill: self.corPreenchimentoVar.set(cor)
            ).grid(row=linha, column=coluna, padx=3, pady=3)


        #Dicionário do espaçamento (margens) dos elementos, feito inicialmente por Khalil.
        self.paddings = {'padx': 5, 'pady': 5}

       
        #Posicionado o layout do frame principal da tela e do canvas(parte onde desenha):
        self.frame.pack(side=TOP,fill=BOTH, expand=True)
        self.canvas.grid(column=0, row=1, columnspan=6, sticky=W ,**self.paddings)
        self.canvas.place(relx=0.5, rely=0.5, anchor='center')


    def desenhar_figura(self, figura):
        tipo = figura.__class__.__name__
       
        if tipo == 'Linha' or tipo == 'Rabisco':
            self.canvas.create_line(figura.coordenadas, smooth=True,        # <-- Ativa a suavização
                splinesteps=36, fill=figura.corBorda, dash=figura.dash)
        elif tipo == 'Triangulo' or tipo == 'Losango' or tipo == 'Pentagono' or tipo == 'Hexagono':
            self.canvas.create_polygon(*figura.coordenadas,outline=figura.corBorda,fill=figura.corPreenchimento,dash=figura.dash,width=2)

        elif tipo == 'Retangulo' or tipo == 'Quadrado':
            self.canvas.create_rectangle(*figura.coordenadas, outline=figura.corBorda, fill=figura.corPreenchimento, dash=figura.dash)
           
        elif tipo == 'Elipse' or tipo == 'Circulo':
            self.canvas.create_oval(figura.coordenadas, outline=figura.corBorda, fill=figura.corPreenchimento, dash=figura.dash)


    def limpar_canvas(self):
        self.canvas.delete("all")


    #Permite escolher local de onde salvar o arquivo (criar o caminho do arquivo)
    def pedir_caminho_salvar(self):
        return filedialog.asksaveasfilename(title="Salvar desenho", defaultextension=".pkl",filetypes=[("Arquivo Pickle", "*.pkl")] )


    #Permite escolher local de onde o arquivo está (acessar o caminho do arquivo)
    def pedir_caminho_abrir(self):
        return filedialog.askopenfilename( title="Abrir desenho", filetypes=[("Arquivo Pickle", "*.pkl")])

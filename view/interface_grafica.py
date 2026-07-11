from tkinter import *
import os

class InterfaceGrafica:
    def __init__(self, root):
        #Recebendo o root como atributo. Por que apenas ele? Porque precisamos de uma janela para poder criarmos o restante da parte gráfica, ou seja, precisamos dele pronto.
        self.root = root
        self.frame = Frame(root)


        pasta_view = os.path.dirname(os.path.abspath(__file__))  # Obtém o diretório do arquivo atual
        pasta_projeto = os.path.dirname(pasta_view)  # Obtém o diretório pai (projeto)
        pasta_imagens = os.path.join(pasta_projeto, 'figuras')  # Caminho completo para a pasta de imagens
        #Criando frame(moldura) para organizar todos os elementos visuais:

        #Criando o dicionário das cores, assim como foi feito no hiperativo:
        self.cores_preenchimento = {
                            'Preto': 'black',
                            'Azul': 'blue',
                            'Amarelo': 'yellow',
                            'Vermelho': 'red',
                            'Verde': 'green',
                            'Branco': 'white',

                            }
        self.cores_borda = {          
                            'Preto': 'black',
                            'Azul': 'blue',
                            'Amarelo': 'yellow',
                            'Vermelho': 'red',
                            'Verde': 'green',
                            'Branco': 'white',
                            }
        

        self.figura_imagem = [
        ('Linha', 'linha.png'),
        ('Rabisco', 'curva.png'),
        ('Retângulo', 'retangulo.png'),
        ('Círculo', 'circulo.png'),
        ('Elipse', 'elipse.png'),
        ('Quadrado','quadrado.png')
        ]

        #Criando um frame para os botões, que ficará acima do canvas:
        self.frame_botoes = Frame(root)
        self.frame_botoes.pack(side = TOP, fill = X)
        Label(self.frame_botoes, text="Formas:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        for i, (nome, arquivo) in enumerate(self.figura_imagem):
            caminho_imagem = os.path.join(pasta_imagens, arquivo)#Para acessar as imagens da pasta figuras(o caminho está no trecho de código no inicio da classe)
            imagem = PhotoImage(file=caminho_imagem)
            botao = Button(
                self.frame_botoes,
                image=imagem,
                command=lambda n=nome: self.tipoFiguraVar.set(n)
            )
            botao.image = imagem
            botao.grid(column=i + 1, row=0, padx=2, pady=2, sticky=W)


        #Criando os botões de cores da borda, que ficarão acima do canvas:
        self.frame_cores_borda = Frame(self.root)
        self.frame_cores_borda.pack(side = TOP, fill = X, padx=5, pady=5)


        Label(self.frame_cores_borda, text="Cor da borda:").grid(row=1, column=0, padx=10, pady=10, sticky="w")

        for i, (nome_cor, cor_bg) in enumerate(self.cores_borda.items()):
            Button(
                self.frame_cores_borda,
                bg=cor_bg,
                width=4,
                height=1,
                command=lambda cor=nome_cor: self.corBordaVar.set(cor)
            ).grid(row=1, column=i + 1, padx=3, pady=3)


        #Criando os botões de cores da borda, que ficarão acima do canvas:
        self.frame_cores_fill = Frame(self.root)
        self.frame_cores_fill.pack(side = TOP, fill = X, padx=5, pady=5)


        Label(self.frame_cores_fill, text="Cor do preenchimento:").grid(row=2, column=0, padx=10, pady=10, sticky="w")

        for i, (nome_cor_fill, cor_bg) in enumerate(self.cores_preenchimento.items()):
            Button(
                self.frame_cores_fill,
                bg=cor_bg,
                width=4,
                height=1,
                command=lambda cor=nome_cor_fill: self.corPreenchimentoVar.set(cor)
            ).grid(row=2, column=i + 1, padx=3, pady=3)


        #Criando as variáveis especiais que guardam a escolha do usuário:
        self.corBordaVar = StringVar()
        self.corPreenchimentoVar = StringVar()
        self.tipoFiguraVar = StringVar()

        #Dicionário do espaçamento (margens) dos elementos, feito inicialmente por Khalil.
        self.paddings = {'padx': 5, 'pady': 5} 

        #Criando onde desenha:
        self.canvas = Canvas(self.frame, bg='white', width=1280, height=720)

        
        #Posicionado o layout do frame principal da tela e do canvas(parte onde desenha):
        self.frame.pack(side=TOP,fill=BOTH, expand=True)
        self.canvas.grid(column=0, row=1, columnspan=6, sticky=W ,**self.paddings)
        self.canvas.place(relx=0.5, rely=0.5, anchor='center')


        #Esse trecho serve para deixar os botões com esse texto aparecendo, se não, o botão inicalizaria em branco e precisaria clicar para aparecer suas opções.
        self.tipoFiguraVar.set('Linha')
        self.corBordaVar.set('Preto')
        self.corPreenchimentoVar.set('Sem preenchimento')

        #Lembrar de colocar o .mainloop() no arquivo de execução.

    def desenhar_figura(self, figura):
        # Descobre qual é a classe do modelo (ex: 'Retangulo', 'Linha', etc.)
        tipo = figura.__class__.__name__
        
        if tipo == 'Linha' or tipo == 'Rabisco':
            self.canvas.create_line(figura.coordenadas, smooth=True,        # <-- Ativa a suavização
                splinesteps=36, fill=figura.corBorda, dash=figura.dash)
            
        elif tipo == 'Retangulo' or tipo == 'Quadrado':
            self.canvas.create_rectangle(*figura.coordenadas, outline=figura.corBorda, fill=figura.corPreenchimento, dash=figura.dash)
            
        elif tipo == 'Elipse' or tipo == 'Circulo':
            self.canvas.create_oval(figura.coordenadas, outline=figura.corBorda, fill=figura.corPreenchimento, dash=figura.dash)
    def limpar_canvas(self):
        self.canvas.delete("all")
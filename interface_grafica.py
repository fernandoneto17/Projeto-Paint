from tkinter import *
from tkinter import ttk

class InterfaceGrafica:
    def __init__(self, root):
        #Recebendo o root como atributo. Por que apenas ele? Porque precisamos de uma janela para poder criarmos o restante da parte gráfica, ou seja, precisamos dele pronto.
        self.root = root
        
        #Criando frame(moldura) para organizar todos os elementos visuais:
        self.frame = Frame(root)

        #Criando as variáveis especiais que guardam a escolha do usuário:
        self.corBordaVar = StringVar()
        self.corPreenchimentoVar = StringVar()
        self.tipoFiguraVar = StringVar()

        #Dicionário do espaçamento (margens) dos elementos, feito inicialmente por Khalil.
        self.paddings = {'padx': 5, 'pady': 5} 

        #Criando onde desenha:
        self.canvas = Canvas(self.frame, bg='white', width=600, height=600)

        #Criando o dicionário das cores, assim como foi feito no hiperativo:
        self.tradutorCores = {
                            'Preto': 'black',
                            'Azul': 'blue',
                            'Amarelo': 'yellow',
                            'Vermelho': 'red',
                            'Verde': 'green',
                            'Branco': 'white',
                            'Sem preenchimento': ''
                            }
        
        #Posicionado o layout do frame principal da tela e do canvas(parte onde desenha):
        self.frame.grid(column=0, row=0, sticky=W, **self.paddings)
        self.canvas.grid(column=0, row=1, columnspan=6, sticky=W, **self.paddings)

        #Label e Menu do programa, onde fica a parte das figuras:
        Label(self.frame, text='Figura:').grid(column=1, row=0, sticky=W, **self.paddings)
        menuOpcoes = ['Linha', 'Rabisco', 'Retângulo', 'Círculo', 'Elipse']
        OptionMenu(self.frame, self.tipoFiguraVar, *menuOpcoes).grid(column=2, row=0, sticky=W, **self.paddings)

        #Label e Menu da parte da cor da borda:
        Label(self.frame, text='Cor da borda:').grid(column=3, row=0, sticky=W, **self.paddings)
        OptionMenu(self.frame, self.corBordaVar, *list(self.tradutorCores)).grid(column=4, row=0, sticky=W, **self.paddings)
        
        #Label e Menu da parte da cor do preenchimento:
        Label(self.frame, text='Cor do preenchimento:').grid(column=5, row=0, sticky=W, **self.paddings)
        OptionMenu(self.frame, self.corPreenchimentoVar, *list(self.tradutorCores)).grid(column=6, row=0, sticky=W, **self.paddings)

        #Esse trecho serve para deixar os botões com esse texto aparecendo, se não, o botão inicalizaria em branco e precisaria clicar para aparecer suas opções.
        self.tipoFiguraVar.set('Linha')
        self.corBordaVar.set('Preto')
        self.corPreenchimentoVar.set('Sem preenchimento')

        #Lembrar de colocar o .mainloop() no arquivo de execução.

from classe_Linha import Linha

class Executor:
    def __init__(self, interface):
        # O Executor guarda a interface para poder ler as cores e usar o canvas depois.
        self.interface = interface

        # Variáveis para guardar as coordenadas de onde o mouse clicou, figura que está sendo desenhada e a lista de desenhos:
        self.xInicial = 0
        self.yInicial = 0
        self.figuraAtual = None
        self.desenhos = []

        #Ajustando os cliques do mouse:
        self.interface.canvas.bind('<ButtonPress-1>', self.iniciar_figura_nova)
        self.interface.canvas.bind('<B1-Motion>', self.atualizar_figura_nova)
        self.interface.canvas.bind('<ButtonRelease-1>', self.incluir_figura_nova)

    def iniciar_figura_nova(self, event): 
        #Atribuindo os valores necessários para as variáveis que precisamos usar nos desenhos.
        self.xInicial = event.x
        self.yInicial = event.y
        tipoFigura = self.interface.tipoFiguraVar.get()
        corBorda = self.interface.tradutorCores[self.interface.corBordaVar.get()]
        corPreenchimento = self.interface.tradutorCores[self.interface.corPreenchimentoVar.get()]

        #Criando os ifs, assim como no código hiperativo.
        if tipoFigura == 'Linha':
            #Aqui criamos os atributos das classses filhas, passamos eles e usamos o método desenhar que estão nelas.
            coordenadas = [self.xInicial, self.yInicial, self.xInicial, self.yInicial]
            self.figuraAtual = Linha(coordenadas, corBorda, corPreenchimento, dash= (4,2))
            self.figuraAtual.desenhar(self.interface.canvas)
        elif tipoFigura == 'Rabisco':
            pass
        elif tipoFigura == 'Retângulo':
            #Repetindo o que fizemos em Linha.
            coordenadas = [self.xInicial, self.yInicial, self.xInicial, self.yInicial]
            self.figuraAtual = Retangulo(coordenadas, corBorda, corPreenchimento, dash= (4,2))
            self.figuraAtual.desenhar(self.interface.canvas)
        elif tipoFigura == 'Elipse':
            #Repetindo o que fizemos em Linha.
            coordenadas = [self.xInicial, self.yInicial, self.xInicial, self.yInicial]
            self.figuraAtual = Elipse(coordenadas, corBorda, corPreenchimento, dash= (4,2))
            self.figuraAtual.desenhar(self.interface.canvas)
        elif tipoFigura == 'Círculo':
            #Repetindo o que fizemos em Linha.
            coordenadas = [self.xInicial, self.yInicial, self.xInicial, self.yInicial]
            self.figuraAtual = Circulo(coordenadas, corBorda, corPreenchimento, dash= (4,2))
            self.figuraAtual.desenhar(self.interface.canvas)

    def atualizar_figura_nova(self, event):
        #Verificando se tem alguma figura:
        if self.figuraAtual is not None:
            #Limpando para evitar repetição do desenho enquanto o mouse se move.
            self.interface.canvas.delete("all")

            #Como limpamos todo o canvas, precisamos desenhar os desenhos antigos:
            for desenho in self.desenhos:
                desenho.desenhar(self.interface.canvas)

            #Utilizando dos métodos da classe para ir atualizando as informações enquanto movemos o mouse.
            self.figuraAtual.atualizar(event.x, event.y)
            self.figuraAtual.desenhar(self.interface.canvas)
                
    def incluir_figura_nova(self, event):
        #Verificando se tem alguma figura:
        if self.figuraAtual is not None:
            #Repetindo o processo que fizemos na função de atualizarFigNova.
            self.interface.canvas.delete("all")

            for desenho in self.desenhos:
                desenho.desenhar(self.interface.canvas)
            
            #Esse if é para evitar o problema que Kalil reclamou da elipse virar uma linha, por exemplo.
            if self.figuraAtual.verificarFig() == True:
                #Aqui a gente atualiza o dash para vazio, para que o desenho não fique tracejado.
                self.figuraAtual.finalizar()
                #Desenhando a figura:
                self.figuraAtual.desenhar(self.interface.canvas)
                #Adicionando o desenho na lista:
                self.desenhos.append(self.figuraAtual)

            #Deixando sem figura nenhuma para repetir o processo no próximo desenho:
            self.figuraAtual = None
from .linha import Linha
from .rabisco import Rabisco
from .elipse import Elipse
from .circulos import Circulo
from .retangulos import Retangulo
from .quadrado import Quadrado
from controller.estados.estadoLinha import EstadoLinha
import pickle
import copy 

class DesenhoModel:
    def __init__(self):
        self.figuraAtual = None
        self.desenhos = []
        self.estadoAtual = EstadoLinha()
        
        self.figuraSelecionada = None 
        self.buffer = None # Aqui guardaremos a figura quando der o CTRL+C

        # Criação de dicionario para associar uma figura e chamar a função:
        self.dicionarioFiguras = {
            'Linha': lambda coordenadas, corBorda, corPreenchimento: Linha(coordenadas, corBorda, corPreenchimento, dash=(4,2)),
            'Rabisco': lambda coordenadas, corBorda, corPreenchimento: Rabisco(coordenadas, corBorda, corPreenchimento, dash=''),
            'Elipse': lambda coordenadas, corBorda, corPreenchimento: Elipse(coordenadas, corBorda, corPreenchimento, dash=(4,2)),
            'Circulo': lambda coordenadas, corBorda, corPreenchimento: Circulo(coordenadas, corBorda, corPreenchimento, dash=(4,2)),
            'Retangulo': lambda coordenadas, corBorda, corPreenchimento: Retangulo(coordenadas, corBorda, corPreenchimento, dash=(4,2)),
            'Quadrado': lambda coordenadas, corBorda, corPreenchimento: Quadrado(coordenadas, corBorda, corPreenchimento, dash=(4,2))
        }

    # Metodos de selecao e movimento de mouse
    def selecionar_figura_pelo_clique(self, xMouse, yMouse):
        for figura in reversed(self.desenhos): # Como no nosso modelo, cada figura desenhada fica por cima da anterior, precisamos percorrer a lista de desenhos de trás pra frente, para selecionar a ultima figura da lista, que representa a ultima figura desenhada
            if figura.contem_ponto(xMouse, yMouse):
                self.figuraSelecionada = figura
                return # Se encontrou uma figura, estabelece a figura selecionada como aquela e sai do método
        self.figuraSelecionada = None # Se não encontrou nenhuma figura, estabelece a figura selecionada como None

    def mover_figura_selecionada(self, dx, dy):
        if self.figuraSelecionada is not None: # Se existe uma figura selecionada, chamamos o método mover da figura selecionada, passando os deslocamentos dx e dy
            self.figuraSelecionada.mover(dx, dy)

    
    def copiar_selecionada(self):
        if self.figuraSelecionada is not None:
            # Usamos deepcopy para não criarmos um link de memória, e sim um Clone perfeito.
            self.buffer = copy.deepcopy(self.figuraSelecionada)

    def colar(self):
        if self.buffer is not None:
            # Clonamos o buffer (assim podemos colar várias vezes seguidas)
            novaFigura = copy.deepcopy(self.buffer)
            
            # Movemos a figura colada um pouquinho pro lado (10 pixels) para ela não ficar camuflada
            novaFigura.mover(10, 10)
            
            # Adicionamos o clone na nossa lista de desenhos (ele vai direto pro topo)
            self.desenhos.append(novaFigura)
            
            # Opcional: A figura colada já passa a ser a nova figura selecionada!
            self.figuraSelecionada = novaFigura
            
            # Atualizamos o buffer para que, se colarmos de novo, ande mais 10 pixels
            self.buffer = copy.deepcopy(novaFigura)

    def apagar_selecionada(self):
        # Se tem figura selecionada E ela existe na lista
        if self.figuraSelecionada is not None and self.figuraSelecionada in self.desenhos:
            self.desenhos.remove(self.figuraSelecionada)
            self.figuraSelecionada = None 
    
    def trazer_para_topo(self):
        # Seta pra Cima: Sobrepõe todos. Jogamos ela para o final da lista.
        if self.figuraSelecionada is not None and self.figuraSelecionada in self.desenhos:
            self.desenhos.remove(self.figuraSelecionada)
            self.desenhos.append(self.figuraSelecionada)

    def enviar_para_fundo(self):
        # Seta pra Baixo: Fica atrás de todos. Jogamos ela para o índice 0.
        if self.figuraSelecionada is not None and self.figuraSelecionada in self.desenhos:
            self.desenhos.remove(self.figuraSelecionada)
            self.desenhos.insert(0, self.figuraSelecionada)

    def subir_uma_camada(self):
        # Seta pra Direita: Troca de lugar com a figura que está "uma casa acima" na lista.
        if self.figuraSelecionada is not None and self.figuraSelecionada in self.desenhos:
            index = self.desenhos.index(self.figuraSelecionada)
            if index < len(self.desenhos) - 1: # Se já não for a última
                # Faz a troca entre as posições na lista
                self.desenhos[index], self.desenhos[index + 1] = self.desenhos[index + 1], self.desenhos[index]

    def abaixar_uma_camada(self):
        # Seta pra Esquerda: Troca de lugar com a figura que está "uma casa abaixo" na lista.
        if self.figuraSelecionada is not None and self.figuraSelecionada in self.desenhos:
            index = self.desenhos.index(self.figuraSelecionada)
            if index > 0: # Se já não for a primeira (fundo)
                self.desenhos[index], self.desenhos[index - 1] = self.desenhos[index - 1], self.desenhos[index]

        # Metodos de salvar e abrir arquivos
    def salvar_em_arquivo(self, caminho_arquivo):
        with open(caminho_arquivo, "wb") as arquivo:
            pickle.dump(self.desenhos, arquivo, protocol=pickle.HIGHEST_PROTOCOL)

    def abrir_de_arquivo(self, caminho_arquivo):
        with open(caminho_arquivo, "rb") as arquivo:
            self.desenhos = pickle.load(arquivo)
            self.figuraSelecionada = None # Reseta a seleção ao abrir um novo arquivo

    def limpa_selecao(self):
        #Desmarca qualquer figura que estivesse selecionada.
        self.figuraSelecionada = None

    def selecionada(self):
        #Retorna a figura que está selecionada no momento, ou None.
        return self.figuraSelecionada

    def seleciona(self, px, py):
        #Percorre os desenhos de trás para a frente (para pegar a que está por cima) e seleciona a primeira que contiver o ponto clicado.
        self.figuraSelecionada = None #Limpa antes de tentar selecionar.
        
        #O reversed faz com que ele olhe primeiro para a última figura desenhada
        for figura in reversed(self.desenhos):
            if figura.contem_ponto(px, py):
                self.figuraSelecionada = figura
                break #Achou a figura, para de procurar.
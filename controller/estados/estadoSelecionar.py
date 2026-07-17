from .estadosFerramentas import EstadoFerramenta

class EstadoSelecionar(EstadoFerramenta) :
    def __init__(self):
        tipoFigura = 'Selecionar'
        #Inicializa as variáveis para guardar a posição do último clique
        self.ult_x = 0
        self.ult_y = 0

    def pressionar(self, controller, event):
        self.ult_x = event.x
        self.ult_y = event.y

        #Acessando o Model através do controller:
        controller.model.limpa_selecao()
        controller.model.selecionar_figura_pelo_clique(event.x, event.y)

        #Redesenhando a tela:
        self.redesenhar_tudo(controller)

    def arrastar(self, controller, event):
        figSel = controller.model.selecionada()
        if figSel :         
            #Calculando o deslocamento(dx, dy):
            dx = event.x - self.ult_x
            dy = event.y - self.ult_y
            
            #Movendo a figura usando o método do Model:
            figSel.mover(dx, dy)
            
            #Atualizando a última posição do mouse:
            self.ult_x = event.x
            self.ult_y = event.y
            
            #Redesenhando a tela em tempo real
            self.redesenhar_tudo(controller)

    def soltar(self, controller, event):
        pass

    #Função auxiliar para limpar e redesenhar tudo usando a estrutura que está no executor:
    def redesenhar_tudo(self, controller):
        #Limpa a tela usando a View (interface):
        controller.interface.limpar_canvas()
    
        #Percorre o histórico de desenhos do Model e manda a View desenhar cada um:
        for desenho in controller.model.desenhos:
            controller.interface.desenhar_figura(desenho)

    #obs: preciso que criem no Model: limpa_selecao(), seleciona(), selecionada(), contem(), mover().
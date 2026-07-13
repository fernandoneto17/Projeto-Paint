from model.linha import Linha
from .Ferramenta import Ferramenta

class EstadoLinha(Ferramenta):
    #Basicamente, o código que estava no método dos ifs:
    def iniciar_figura_nova(self, event, executor):
        #Pegando as cores da interface (que está no executor):
        corBorda = executor.interface.cores_borda.get(executor.interface.corBordaVar.get())
        corPreenchimento = executor.interface.cores_preenchimento.get(executor.interface.corPreenchimentoVar.get())
        
        #Criando as coordenadas iniciais:
        coordenadas = [event.x, event.y, event.x, event.y]
        
        #O Estado cria a linha, mas guarda no Executor.
        executor.figuraAtual = Linha(coordenadas, corBorda, corPreenchimento, dash=(4,2))

    def atualizar_figura_nova(self, event, executor):
        if executor.figuraAtual is not None:
            #Apagando o canvas e redesenha o histórico:
            executor.interface.limpar_canvas()
            for desenho in executor.desenhos:
                executor.interface.desenhar_figura(desenho)
            
            #Atualizando e desenhando a figura atual:
            executor.figuraAtual.atualizar(event.x, event.y)
            executor.interface.desenhar_figura(executor.figuraAtual)

    def incluir_figura_nova(self, event, executor):
        if executor.figuraAtual is not None:
            #Finalizando a linha (tira o tracejado - dash):
            executor.figuraAtual.finalizar()
            
            #Guardando a linha na lista de desenhos do Executor:
            if executor.figuraAtual.verificarFig():
                executor.desenhos.append(executor.figuraAtual)
            
            #Redesenhando a versão final:
            executor.interface.limpar_canvas()
            for desenho in executor.desenhos:
                executor.interface.desenhar_figura(desenho)
                
            #Limpando a figura atual do Executor para o próximo clique:
            executor.figuraAtual = None
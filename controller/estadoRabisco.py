from model.rabisco import Rabisco
from .Ferramenta import Ferramenta

class EstadoRabisco(Ferramenta):
    #Basicamente, o código que estava no método dos ifs:
    def iniciar_figura_nova(self, event, executor):
        #Pegando as cores da interface (que está no executor):
        corBorda = executor.interface.cores_borda.get(executor.interface.corBordaVar.get())
        corPreenchimento = executor.interface.cores_preenchimento.get(executor.interface.corPreenchimentoVar.get())
        
        #O rabisco começa com um ponto inicial apenas
        coordenadas = [event.x, event.y]
        
         #O Estado cria o rabisco, mas guarda no Executor. (Obs: Rabisco não tem dash, então passamos como None).
        executor.figuraAtual = Rabisco(coordenadas, corBorda, corPreenchimento, dash=None)

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
                executor.figuraAtual.finalizar()
            
            #Guardando o rabisco na lista de desenhos do Executor:
            if executor.figuraAtual.verificarFig():
                executor.desenhos.append(executor.figuraAtual)
            
            #Redesenhando a versão final:
            executor.interface.limpar_canvas()
            for desenho in executor.desenhos:
                executor.interface.desenhar_figura(desenho)
                
            #Limpando a figura atual do Executor para o próximo clique:
            executor.figuraAtual = None
from tkinter import *
from classe_InterfaceGráfica import InterfaceGrafica
from Executor import Executor  

def main():
    #Criamos a janela principal (a raiz do Tkinter):
    root = Tk()
    root.title('App de desenho')
    
    #Criamos o objeto real da Interface, passando a janela 'root' para ela:
    tela = InterfaceGrafica(root)
    
    #Passamos a tela como atributo para o construtor (o self.interface):
    executor = Executor(tela)
    
    #Mantemos a janela aberta e escutando os cliques do utilizador (como foi lembrado na classe da InterfaceGráfica):
    root.mainloop()

main()
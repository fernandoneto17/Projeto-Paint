from tkinter import *
from view.interface_grafica import InterfaceGrafica
from controller.executor import Executor  

def main():
    #Criamos a janela principal (a raiz do Tkinter):
    root = Tk()
    root.title('App de desenho')
    root.minsize(width=1152, height=648)
    #Criamos o objeto real da Interface, passando a janela 'root' para ela:
    tela = InterfaceGrafica(root)
    
    #Passamos a tela como atributo para o construtor (o self.interface):
    executor = Executor(tela)
    
    #Mantemos a janela aberta e escutando os cliques do utilizador (como foi lembrado na classe da InterfaceGráfica):
    root.mainloop()

main()

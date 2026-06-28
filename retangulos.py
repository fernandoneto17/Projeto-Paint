#Fazer retangulos
#A largura será a reta definida pela distância entre a posição x inicial e final
#A altura segue a mesma lógica da largura

from tkinter import *


# Quando o mouse é pressionado
def inicia_retangulo(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y


# Quando o mouse é movido com o botão pressionado
def atualiza_retangulo(event):
    global fim_x, fim_y
    fim_x = event.x
    fim_y = event.y
    desenhar()  # redesenha os retângulos já finalizados
    # Desenha a prévia do retângulo atual
    x1, y1 = min(ini_x, fim_x), min(ini_y, fim_y)
    x2, y2 = max(ini_x, fim_x), max(ini_y, fim_y)
    canvas.create_rectangle(x1, y1, x2, y2)

# Quando o mouse é solto
def finaliza_retangulo(event):
    global fim_x, fim_y
    fim_x = event.x
    fim_y = event.y
    # Normaliza coordenadas (canto superior-esquerdo e inferior-direito)
    x1, y1 = min(ini_x, fim_x), min(ini_y, fim_y)
    x2, y2 = max(ini_x, fim_x), max(ini_y, fim_y)
    retangulos.append((x1, y1, x2, y2))
    desenhar()


def desenhar():
    canvas.delete("all")
    for ret in retangulos:
        x1, y1, x2, y2 = ret
        canvas.create_rectangle(x1, y1, x2, y2)




#******* MAIN *******#


# Todos os retângulos desenhados são armazenados aqui
retangulos = []

root = Tk()


canvas = Canvas(root, bg='white', width=600, height=600)
canvas.pack()


ini_x = None
ini_y = None
fim_x = None
fim_y = None


canvas.bind('<ButtonPress-1>', inicia_retangulo)
canvas.bind('<B1-Motion>', atualiza_retangulo)
canvas.bind('<ButtonRelease-1>', finaliza_retangulo)

root.mainloop()
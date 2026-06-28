#Criando ovais
#O oval é composto por um centro, um raio na vertical(y) e um raio na horizontal(x)

from tkinter import *


def inicia_oval(event):
    global cx, cy
    cx, cy = event.x, event.y  # centro fixo no clique


def atualiza_oval(event):
    global rx, ry
    rx = abs(event.x - cx)  # raio horizontal = distância x
    ry = abs(event.y - cy)  # raio vertical   = distância y
    desenhar()
    # prévia
    canvas.create_oval(cx - rx, cy - ry, cx + rx, cy + ry)


def finaliza_oval(event):
    global rx, ry
    rx = abs(event.x - cx) #valores em modulo, pois nao existe raio negativo
    ry = abs(event.y - cy)
    ovais.append((cx, cy, rx, ry)) # guarda centro + raios
    desenhar()


def desenhar():
    canvas.delete("all")
    for oval in ovais:
        cx_, cy_, rx_, ry_ = oval
        canvas.create_oval(cx_ - rx_, cy_ - ry_, cx_ + rx_, cy_ + ry_)


# MAIN
ovais = []
cx = cy = rx = ry = None


root = Tk()
canvas = Canvas(root, bg='white', width=600, height=600)
canvas.pack()


canvas.bind('<ButtonPress-1>',inicia_oval)
canvas.bind('<B1-Motion>',atualiza_oval)
canvas.bind('<ButtonRelease-1>',finaliza_oval)


root.mainloop()




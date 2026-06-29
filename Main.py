from tkinter import *

#******* MAIN *******#

# Todas os círuculos desenhados são armazenados aqui
circulos = []
raio = None

root = Tk()

canvas = Canvas(root, bg='white', width=600, height=600)
canvas.pack()

ini_x = None
ini_y = None
fim_x = None
fim_y = None
canvas.bind('<ButtonPress-1>', inicia_linha)
canvas.bind('<B1-Motion>', atualiza_linha)
canvas.bind('<ButtonRelease-1>', incluir_linha)

root.mainloop()

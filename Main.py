from tkinter import *
from tkinter import ttk

#******* MAIN *******#

figuras = []       # todas as figuras desenhadas
figura_nova = None # figura que está sendo desenhada

root = Tk()
root.title("App de Desenho")
frame = Frame(root)

paddings = {'padx': 5, 'pady': 5} 

# Label
label = ttk.Label(frame,  text='Ferramenta:')
label.grid(column=0, row=0, sticky=W, **paddings)

tipo_figura_var = StringVar(root)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Elipse', 'Círculo', 'Retângulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
from tkinter import *
from tkinter import ttk


# ---------- ESTADO ----------
figuras = []           # listas de tuplas imutáveis
figura_nova = None     # tupla sendo desenhada (preview)
cx = cy = None         # centro/ponto inicial fixo


# ---------- HANDLERS ----------
def iniciar_figura_nova(event):
    global figura_nova, cx, cy
    cx, cy = event.x, event.y
    tipo = tipo_figura_var.get()
    cor  = tipo_cor_var.get()
    if tipo == "retangulo":
        figura_nova = ("retangulo", cx, cy, cx, cy, cor)  # x1=y1=x2=y2 no início
    elif tipo == "circulo":
        figura_nova = ("circulo", cx, cy, 0, cor)         # raio 0
    else:  # oval
        figura_nova = ("oval", cx, cy, 0, 0, cor)         # rx=ry=0


def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova is None:
        return
    tipo = figura_nova[0]
    cor  = tipo_cor_var.get()
    x, y = event.x, event.y


    if tipo == "retangulo":
        # normaliza cantos
        x1, y1 = min(cx, x), min(cy, y)
        x2, y2 = max(cx, x), max(cy, y)
        figura_nova = ("retangulo", x1, y1, x2, y2, cor)


    elif tipo == "circulo":
        r = int(((x - cx)**2 + (y - cy)**2)**0.5)
        figura_nova = ("circulo", cx, cy, r, cor)


    else:  # oval
        rx = abs(x - cx)
        ry = abs(y - cy)
        figura_nova = ("oval", cx, cy, rx, ry, cor)


    desenhar_todas_figuras()


def incluir_figura_nova(event):
    global figura_nova
    if figura_nova:
        figuras.append(figura_nova)  # tupla imutável → safe
        figura_nova = None
        desenhar_todas_figuras()


# ---------- DESENHO ----------
def desenhar_todas_figuras():
    canvas.delete("all")
    # figuras finalizadas
    for figura in figuras:
        desenhar_uma_figura(figura, tracejado=False)
    # preview da figura atual
    if figura_nova:
        desenhar_uma_figura(figura_nova, tracejado=True)


def desenhar_uma_figura(figura, tracejado):
    tipo = figura[0]
    kwargs = {"outline": figura[-1], "dash": (4,2)} if tracejado else {"outline": figura[-1]}
    if tipo == "retangulo":
        _, x1, y1, x2, y2, _ = figura
        canvas.create_rectangle(x1, y1, x2, y2, **kwargs)
    elif tipo == "circulo":
        _, cx, cy, r, _ = figura
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, **kwargs)
    else:  # oval
        _, cx, cy, rx, ry, _ = figura
        canvas.create_oval(cx-rx, cy-ry, cx+rx, cy+ry, **kwargs)


# ---------- MAIN ----------
root = Tk()
frame = Frame(root)
frame.pack(padx=10, pady=10)


# Toolbar
tipo_figura_var = StringVar(value="retangulo")
tipo_cor_var    = StringVar(value="black")


ttk.Label(frame, text="Ferramentas:").grid(row=0, column=0, sticky=W, padx=5, pady=5)
ttk.OptionMenu(frame, tipo_figura_var, "retangulo", "retangulo", "circulo", "oval")\
    .grid(row=0, column=1, sticky=W, padx=5)
ttk.OptionMenu(frame, tipo_cor_var, "black", "black", "blue", "red", "yellow", "white", "green")\
    .grid(row=0, column=2, sticky=W, padx=5)


canvas = Canvas(frame, bg="white", width=600, height=600)
canvas.grid(row=1, column=0, columnspan=3, pady=5)


# Bindings
canvas.bind("<ButtonPress-1>",   iniciar_figura_nova)
canvas.bind("<B1-Motion>",       atualizar_figura_nova)
canvas.bind("<ButtonRelease-1>", incluir_figura_nova)


root.mainloop()




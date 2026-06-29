# Este arquivo contém, além da tarefa de cor de preenchimento, todas as tarefas anteriores. Caso queira testar se todas as funcionabilidades funcionam em conjunto, teste este arquivo.
from tkinter import *
from tkinter import ttk


# ---------- ESTADO ----------
figuras = []
figura_nova = None
cx = cy = None


# ---------- HANDLERS ----------
def iniciar_figura_nova(event):
    global figura_nova, cx, cy
    cx, cy = event.x, event.y
    tipo = tipo_figura_var.get()
    cor_borda = tipo_cor_var.get()
    cor_fill = tipo_fill_var.get()
    if tipo == "retangulo":
        figura_nova = ("retangulo", cx, cy, cx, cy, cor_borda, cor_fill)
    elif tipo == "circulo":
        figura_nova = ("circulo", cx, cy, 0, cor_borda, cor_fill)
    else:
        figura_nova = ("oval", cx, cy, 0, 0, cor_borda, cor_fill)


def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova is None:
        return
    tipo = figura_nova[0]
    cor_borda = tipo_cor_var.get()
    cor_fill = tipo_fill_var.get()
    x, y = event.x, event.y


    if tipo == "retangulo":
        x1, y1 = min(cx, x), min(cy, y)
        x2, y2 = max(cx, x), max(cy, y)
        figura_nova = ("retangulo", x1, y1, x2, y2, cor_borda, cor_fill)
    elif tipo == "circulo":
        r = int(((x - cx)**2 + (y - cy)**2)**0.5)
        figura_nova = ("circulo", cx, cy, r, cor_borda, cor_fill)
    else:
        rx, ry = abs(x - cx), abs(y - cy)
        figura_nova = ("oval", cx, cy, rx, ry, cor_borda, cor_fill)


    desenhar_todas_figuras()


def incluir_figura_nova(event):
    global figura_nova
    if figura_nova:
        figuras.append(figura_nova)
        figura_nova = None
        desenhar_todas_figuras()


# ---------- DESENHO ----------
def desenhar_todas_figuras():
    canvas.delete("all")
    for f in figuras:
        desenhar_uma_figura(f, tracejado=False)
    if figura_nova:
        desenhar_uma_figura(figura_nova, tracejado=True)


def desenhar_uma_figura(figura, tracejado):
    tipo = figura[0]
    cor_borda, cor_fill = figura[-2], figura[-1]
    kwargs = {"outline": cor_borda, "fill": cor_fill if cor_fill else ""}
    if tracejado:
        kwargs["dash"] = (4, 2)          # ← preview tracejado


    if tipo == "retangulo":
        _, x1, y1, x2, y2, _, _ = figura   # 7 itens
        canvas.create_rectangle(x1, y1, x2, y2, **kwargs)
    elif tipo == "circulo":
        _, cx, cy, r, _, _ = figura        # 6 itens
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, **kwargs)
    else:
        _, cx, cy, rx, ry, _, _ = figura   # 7 itens
        canvas.create_oval(cx-rx, cy-ry, cx+rx, cy+ry, **kwargs)


# ---------- MAIN ----------
root = Tk()
frame = Frame(root)
frame.pack(padx=10, pady=10)


# Cores em INGLÊS
tipo_fill_var    = StringVar(value="")
tipo_figura_var  = StringVar(value="retangulo")
tipo_cor_var     = StringVar(value="black")


ttk.Label(frame, text="Ferramentas:").grid(row=0, column=0, sticky=W, padx=5, pady=5)


ttk.OptionMenu(frame, tipo_figura_var, "retangulo", "retangulo", "circulo", "oval")\
    .grid(row=0, column=1, sticky=W, padx=5)
ttk.OptionMenu(frame, tipo_cor_var, "black", "black", "blue", "red", "yellow", "white", "green")\
    .grid(row=0, column=2, sticky=W, padx=5)
ttk.OptionMenu(frame, tipo_fill_var, "", "", "black", "blue", "red", "yellow", "white", "green")\
    .grid(row=0, column=3, sticky=W, padx=5)


canvas = Canvas(frame, bg="white", width=600, height=600)
canvas.grid(row=1, column=0, columnspan=4, pady=5)


canvas.bind("<ButtonPress-1>",   iniciar_figura_nova)
canvas.bind("<B1-Motion>",       atualizar_figura_nova)
canvas.bind("<ButtonRelease-1>", incluir_figura_nova)


root.mainloop()




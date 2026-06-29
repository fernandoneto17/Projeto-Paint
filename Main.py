from tkinter import *
from tkinter import ttk

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

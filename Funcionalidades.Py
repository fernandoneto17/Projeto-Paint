from tkinter import *
from tkinter import ttk

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    tipo = tipo_figura_var.get()
    borda = tradutor_cores[corBordaVar.get()]
    preenchimento = tradutor_cores[corPreenchimentorVar.get()]
    
    if tipo == 'Linha':
        figura_nova = ('linha', (event.x, event.y, event.x, event.y), borda, preenchimento)
    elif tipo == 'Elipse':
        figura_nova = ('elipse', (event.x, event.y, event.x, event.y), borda, preenchimento)
    elif tipo == 'Círculo':
        # Para o círculo, guardamos o centro (x, y) e o raio inicial que é 0
        figura_nova = ('circulo', (event.x, event.y, 0), borda, preenchimento)
    elif tipo == 'Retângulo':
        figura_nova = ('retangulo', (event.x, event.y, event.x, event.y), borda, preenchimento)
    else: # Rabisco
        figura_nova = ('rabisco', [(event.x, event.y)], borda, preenchimento)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova

    if figura_nova is None: 
        return
    
    tipo, values, borda, preenchimento = figura_nova

    #figuranova é uma tupla do tipo e das coordenadas, então os ifs precisam ser nas coordenadas, pois as atualizaremos a medida que o mouse é movido
    if tipo == 'rabisco':
        #no caso do rabisco, a tupla da figuranova é composta pelo tipo e uma lista das coordenadas, então podemos dar apenas .append
        values.append((event.x, event.y))
        figura_nova = ('rabisco', values, borda, preenchimento)
    elif tipo == 'linha':
        #nos outros casos, a tupla da figuranova é composta pelo tipo e uma tupla de coordenadas, então precisamos atualizar as tuplas
        figura_nova = ('linha', (values[0], values[1], event.x, event.y), borda, preenchimento)
    elif tipo == 'elipse':
        figura_nova = ('elipse', (values[0], values[1], event.x, event.y), borda, preenchimento)
    elif tipo == 'circulo':
        # pega o centro original que foi salvo no clique
        xDoCentro, yDoCentro = values[0], values[1]
        # calcula o raio usando a fórmula de distância dada por Kalil
        raio = ((xDoCentro - event.x)**2 + (yDoCentro - event.y)**2) ** 0.5
        figura_nova = ('circulo', (xDoCentro, yDoCentro, raio), borda, preenchimento)
    elif tipo == 'retangulo':
        figura_nova = ('retangulo', (values[0], values[1], event.x, event.y), borda, preenchimento)

    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event):
    global figura_nova 
    #conferindo se a fig é válida, assim como foi feito no exemplo dado por Kalil
    if not incompleta(figura_nova): 
        figuras.append(figura_nova) 
    figura_nova = None
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values, borda, preenchimento in figuras: #esse for já percorre os 4 elementos da tupla, p n ter q fazer separado
        if fig == 'linha':
            canvas.create_line(values[0], values[1], values[2], values[3], fill= borda)
        elif fig == 'elipse':
            canvas.create_oval(values[0], values[1], values[2], values[3], outline= borda, fill= preenchimento,)
        elif fig == 'circulo':
            xDoCentro, yDoCentro, r = values
            canvas.create_oval(xDoCentro - r, yDoCentro - r, xDoCentro + r, yDoCentro + r, outline= borda, fill= preenchimento,)
        elif fig == 'rabisco':
            canvas.create_line(values, fill= borda)
        elif fig == 'retangulo':
            canvas.create_rectangle(values[0], values[1], values[2], values[3], outline= borda, fill= preenchimento,)


def desenhar_figura_nova():
    if figura_nova is None: 
        return
    
    fig, values, borda, preenchimento = figura_nova

    if fig == 'linha':
        canvas.create_line(values[0], values[1], values[2], values[3], fill= borda, dash=(4, 2))
    elif fig == 'elipse':
        canvas.create_oval(values[0], values[1], values[2], values[3], outline= borda, fill= preenchimento, dash=(4, 2))
    elif fig == 'circulo':
        xDoCentro, yDoCentro, r = values
        canvas.create_oval(xDoCentro - r, yDoCentro - r, xDoCentro + r, yDoCentro + r, outline= borda, fill= preenchimento, dash=(4, 2))
    elif fig == 'rabisco':
        canvas.create_line(values, fill= borda, dash=(4, 2))
    elif fig == 'retangulo':
        canvas.create_rectangle(values[0], values[1], values[2], values[3], outline= borda, fill= preenchimento, dash=(4, 2))

    #o dash serve apenas para mostrar o rascunho

def incompleta(figura):
    fig, values, _, _ = figura
    #a condição da elipse pode ser a mesma da linha porque ela não depende do raio, mas sim de 2 pontos (focos), assim como uma linha precisa de 2 pontos tbm (msm coisa p ret)
    if fig == 'linha' or fig == 'elipse' or fig == 'retangulo':
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == 'circulo':
        return values[2] == 0  # incompleto se o raio for zero
    else: # rabisco
        return len(values) <= 1

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

#Cores:
#Borda:
labelBorda = ttk.Label(frame, text='Cor da borda:')
labelBorda.grid(column=2, row=0, sticky=W, **paddings)
corBordaVar = StringVar(root)
menuBorda = ttk.OptionMenu(frame, corBordaVar, 'Azul', 'Azul', 'Amarelo', 'Vermelho', 'Verde', 'Preto', 'Branco')
menuBorda.grid(column=3, row=0, sticky=W, **paddings)
#Preenchimento:
labelPreenchimento = ttk.Label(frame, text='Cor do preenchimento:')
labelPreenchimento.grid(column=4, row=0, sticky=W, **paddings)
corPreenchimentorVar = StringVar(root)
menuPreenchimento = ttk.OptionMenu(frame, corPreenchimentorVar, 'Sem preenchimento','Sem preenchimento', 'Azul', 'Amarelo', 'Vermelho', 'Verde', 'Preto', 'Branco')
menuPreenchimento.grid(column=5, row=0, sticky=W, **paddings)

tradutor_cores = {
    'Preto': 'black',
    'Azul': 'blue',
    'Amarelo': 'yellow',
    'Vermelho': 'red',
    'Verde': 'green',
    'Branco': 'white',
    'Sem preenchimento': ''
}

# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=6, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
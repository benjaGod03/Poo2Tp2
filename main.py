import networkx as nx
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import openpyxl as op

class Grafo:
    def __init__(self, nombre):
        ws = op.load_workbook(nombre)
        wb = ws.active
        self.g = nx.Graph()
        agregar = [wb.cell(row=i, column=1).value for i in range(1, wb.max_row +1)]
        if agregar[wb.max_row-1] is None:
            agregar.remove(agregar[wb.max_row-1])
        self.g.add_nodes_from(agregar)
        j = 1
        while wb['A{}'.format(j)].value is not None:
            values = [wb.cell(row=j, column=c).value for c in range(1, wb.max_column + 1)]
            nodo = values[0]
            p = 1
            while values[p] != None:
                if self.g.has_edge(nodo, values[p]) == False :
                    if self.g.has_node(values[p]) == True :
                        self.g.add_edge(nodo, values[p], amistad=values[p+1])
                if (p+2 >= values.__len__()):
                    break
                p += 2
            j += 1
    def getGraph(self):
        return self.g

a1 = Grafo('Prueba.xlsx')

G=a1.getGraph()


grado_de_amistad = {"amigo personal" : 3, "conocido" : 2, "compañero" : 1}

for u, v, data in G.edges(data = True):
    data["valor"] = grado_de_amistad[data["amistad"]]

def distancia_de_amistad (G, source, target):
    try:
        distancia = nx.shortest_path_length(G, source=source, target=target, weight="valor")
        return distancia
    except nx.NetworkXNoPath:
        return float("inf")


def mostrar_grafo():
    fig, ax = plt.subplots(figsize=(8, 6))  

    pos = nx.spring_layout(G, seed=42)   


    node_colors = [G.degree(n) for n in G.nodes()]    
    node_sizes = [700 + 100 * G.degree(n) for n in G.nodes()]  

    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes,  
            cmap=plt.cm.viridis, font_weight='bold', edge_color='gray', ax=ax)


    labels = nx.get_edge_attributes(G, 'valor') 
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', ax=ax)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafo)  
    canvas.draw()
    canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=1)



def calcular_distancia():
    nombre1 = entry_nombre1.get().capitalize()  
    nombre2 = entry_nombre2.get().capitalize()
    distancia = distancia_de_amistad(G, nombre1, nombre2) 
    label_resultado.configure(text=f"La distancia de amistad entre {nombre1} y {nombre2} es: {distancia}")



ventana = ctk.CTk()
ventana.title("Distancia de Amistad")  

frame_entrada = ctk.CTkFrame(ventana)  
frame_entrada.pack(pady=20, padx=20, fill="both", expand=True)

label_nombre1 = ctk.CTkLabel(frame_entrada, text="Introduce un nombre:")
label_nombre1.pack(pady=5)

entry_nombre1 = ctk.CTkEntry(frame_entrada)
entry_nombre1.pack(pady=5)

label_nombre2 = ctk.CTkLabel(frame_entrada, text="Introduce otro nombre:") 
label_nombre2.pack(pady=5)

entry_nombre2 = ctk.CTkEntry(frame_entrada)
entry_nombre2.pack(pady=5)

button_calcular = ctk.CTkButton(frame_entrada, text="Calcular distancia", command=calcular_distancia)
button_calcular.pack(pady=10)   

label_resultado = ctk.CTkLabel(frame_entrada, text="") 
label_resultado.pack(pady=10)

frame_grafo = ctk.CTkFrame(ventana)
frame_grafo.pack(pady=20, padx=20, fill="both", expand=True)




mostrar_grafo()

ventana.mainloop()


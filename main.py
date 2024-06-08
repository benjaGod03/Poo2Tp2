#librerias que usé
#a ver
import networkx as nx
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

#grafo que me inventé

#nodoNahuel = {"Nahuel" : ["Benja" ,"Kevin" ,"Mati"]}
#nodoBenja = {"Benja" : ["Cande", "Kevin"]}
#nodoKevin = {"Kevin" : ["Cande" ,"Mateo" ,"Mati"]}
#nodoMati = {"Mati" : ["Mateo" ,"Ezequiel"]}
#nodoMateo = {"Mateo" : ["elMago" ,"Ezequiel"]}
#nodoCande = {"Cande" : ["Mateo" ,"elMago"]}
#nodoEzequiel = {"Ezequiel" : ["elMago"]}
#nodoElMago = {"elMago" : "-"}


#diccionario con el valor de cada nivel de amistad
grado_de_amistad = {"amigo personal" : 3, "conocido" : 2, "compañero" : 1}

#creo un grafo dirigido
G = nx.Graph()

#agrego los nodos
G.add_nodes_from(["Nahuel", "Benja", "Kevin", "Mati", "Cande", "Mateo", "Ezequiel", "elMago"])
#agrego las aristas
G.add_edge("Nahuel", "Benja", amistad = "conocido")
G.add_edge("Nahuel", "Kevin", amistad = "compañero")
G.add_edge("Nahuel", "Mati", amistad = "amigo personal")
G.add_edge("Benja", "Cande", amistad = "conocido")
G.add_edge("Benja", "Kevin", amistad = "amigo personal")
G.add_edge("Kevin", "Cande", amistad = "compañero")
G.add_edge("Kevin", "Mateo", amistad = "amigo personal")
G.add_edge("Kevin", "Mati", amistad = "conocido")
G.add_edge("Mati", "Mateo", amistad = "amigo personal")
G.add_edge("Mati", "Ezequiel", amistad = "compañero")
G.add_edge("Mateo", "elMago", amistad = "conocido")
G.add_edge("Mateo", "Ezequiel", amistad = "amigo personal")
G.add_edge("Cande", "Mateo", amistad = "conocido")
G.add_edge("Cande", "elMago", amistad = "amigo personal")
G.add_edge("Ezequiel", "elMago", amistad = "compañero")

#almaceno en "valor" el grado de amistad en numero
for u, v, data in G.edges(data = True):
    data["valor"] = grado_de_amistad[data["amistad"]]

#uso la funcion de Nx para el camino de mayor costo
def distancia_de_amistad (G, source, target):
    try:
        distancia = nx.shortest_path_length(G, source = source, target = target, weight = "valor")
        return distancia
    except nx.NetworkXNoPath:
        return float("inf")

#si quieren mostrar en consola usan esto:
#print("introduce un nombre: ")
#nombre1 = input()
#print("Introduce otro nombre: ")
#nombre2 = input()
#print("la distancia de amistad entre esas dos personas es: ", distancia_de_amistad(G, nombre1, nombre2))



def mostrar_grafo():
    fig, ax = plt.subplots(figsize=(8, 6))  #creo la figura usando matplotlib, el tamaño es en pulgadas ojo

    pos = nx.spring_layout(G, seed=42)   #aca se puede cambiar el layout


    node_colors = [G.degree(n) for n in G.nodes()]     #segun el grado de nodo uso un color diferente, esto lo pueden sacar si quieren
    node_sizes = [700 + 100 * G.degree(n) for n in G.nodes()]  #esto hace que los nodos sean mas grandes segun el grado, tmb lo sacan si quieren

    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=node_sizes,  #dibuja el grafo G utilizando las pociones "Pos"
            cmap=plt.cm.viridis, font_weight='bold', edge_color='gray', ax=ax)


    labels = nx.get_edge_attributes(G, 'valor') #obtiene un diccionario de etiquetas para las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', ax=ax)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafo)  #genera un widget para la GUI
    canvas.draw()
    canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=1)



def calcular_distancia():
    nombre1 = entry_nombre1.get().capitalize()  #obtiene lo ingresado en nombre1 y 2
    nombre2 = entry_nombre2.get().capitalize()
    distancia = distancia_de_amistad(G, nombre1, nombre2) #llama a la funcion de la distancia minima
    label_resultado.configure(text=f"La distancia de amistad entre {nombre1} y {nombre2} es: {distancia}")



ventana = ctk.CTk()
ventana.title("Distancia de Amistad")  #titulo de la ventana


frame_entrada = ctk.CTkFrame(ventana)  #crea un marco dentro de la ventana principal
frame_entrada.pack(pady=20, padx=20, fill="both", expand=True)

label_nombre1 = ctk.CTkLabel(frame_entrada, text="Introduce un nombre:") #crea este texto en el marco nuevo
label_nombre1.pack(pady=5)

entry_nombre1 = ctk.CTkEntry(frame_entrada)
entry_nombre1.pack(pady=5)

label_nombre2 = ctk.CTkLabel(frame_entrada, text="Introduce otro nombre:") #otro texto
label_nombre2.pack(pady=5)

entry_nombre2 = ctk.CTkEntry(frame_entrada)
entry_nombre2.pack(pady=5)

button_calcular = ctk.CTkButton(frame_entrada, text="Calcular distancia", command=calcular_distancia)
button_calcular.pack(pady=10)   #crea un boton q al presionarlo llama a la funcion calcular distancia

label_resultado = ctk.CTkLabel(frame_entrada, text="") #muestra el resultado dentro de eso
label_resultado.pack(pady=10)

frame_grafo = ctk.CTkFrame(ventana)
frame_grafo.pack(pady=20, padx=20, fill="both", expand=True)



#muestra el grafo
mostrar_grafo()

#genera un loop para q no se cierre la ventana
ventana.mainloop()


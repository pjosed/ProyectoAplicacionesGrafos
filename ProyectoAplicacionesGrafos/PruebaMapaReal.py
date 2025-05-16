import tkinter as tk
from tkinter import messagebox

import osmnx as ox
import networkx as nx

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.image as mpimg

# Inicializar ventana Tkinter
root = tk.Tk()
root.title("Mapa de la Universidad - Click para seleccionar origen y destino")

# Crear figura de matplotlib
fig, ax = plt.subplots(figsize=(10, 7))

# Descargar grafo de la Uninorte
G = ox.graph_from_place('Universidad del Norte, Barranquilla, Colombia', network_type='walk')

# Obtener posiciones de los nodos
pos = {node: (data['x'], data['y']) for node, data in G.nodes(data=True)}

# Cargar imagen del mapa
imagen_fondo = mpimg.imread('MapaUninorte.png')  # Asegúrate de tener la imagen en el mismo directorio

# Obtener límites de los nodos manualmente
x_values = [data['x'] for node, data in G.nodes(data=True)]
y_values = [data['y'] for node, data in G.nodes(data=True)]
west, east = min(x_values), max(x_values)
south, north = min(y_values), max(y_values)

# Dibujar la imagen de fondo con los bounds del grafo
ax.imshow(imagen_fondo, extent=[west, east + (east - west) * 0.7, south, north], zorder=0)

# Guardar límites originales del eje
limites_originales = ax.axis()

# Variables globales
origen = None
destino = None

# Función para encontrar el nodo más cercano
def obtener_nodo_mas_cercano(x_click, y_click):
    trans = ax.transData.inverted()
    xdata, ydata = trans.transform((x_click, y_click))
    closest_node = ox.distance.nearest_nodes(G, X=xdata, Y=ydata)
    return closest_node

# Función para manejar click en mapa
def click_en_mapa(event):
    global origen, destino
    nodo_cercano = obtener_nodo_mas_cercano(event.x, event.y)

    if origen is None:
        origen = nodo_cercano
        messagebox.showinfo("Origen seleccionado", "Origen seleccionado. Ahora selecciona el destino.")
    elif destino is None:
        destino = nodo_cercano
        mostrar_camino_mas_corto()

# Función para mostrar el camino más corto
def mostrar_camino_mas_corto():
    global origen, destino
    try:
        if origen not in G.nodes or destino not in G.nodes:
            messagebox.showerror("Error", "Selecciona nodos válidos.")
            return
        
        shortest_path = nx.dijkstra_path(G, source=origen, target=destino, weight='length')

        ax.clear()
        ax.imshow(imagen_fondo, extent=[west, east + (east - west) * 0.7, south, north], zorder=0)
        nx.draw(G, pos, ax=ax, node_size=10, node_color='blue', edge_color='gray', with_labels=False)

        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=3, ax=ax)

        # Restaurar límites originales
        ax.axis(limites_originales)

        canvas.draw()

        origen = None
        destino = None

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
        origen = None
        destino = None

# Botón para limpiar selección
def limpiar_seleccion():
    global origen, destino
    origen = None
    destino = None
    ax.clear()
    ax.imshow(imagen_fondo, extent=[west, east + (east - west) * 0.7, south, north], zorder=0)
    nx.draw(G, pos, ax=ax, node_size=10, node_color='blue', edge_color='gray', with_labels=False)

    # Restaurar límites originales
    ax.axis(limites_originales)

    canvas.draw()

# Integrar matplotlib en Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill="both", expand=True)

# Conectar click
canvas.mpl_connect('button_press_event', click_en_mapa)

# Botón para limpiar
limpiar_button = tk.Button(root, text="Limpiar Selección", command=limpiar_seleccion)
limpiar_button.pack()

# Mostrar mapa inicial
nx.draw(G, pos, ax=ax, node_size=10, node_color='blue', edge_color='gray', with_labels=False)
canvas.draw()

# Mostrar ventana
root.mainloop()

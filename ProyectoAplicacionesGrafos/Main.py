import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
import numpy as np

# Crear grafo
universidad = nx.Graph()

# Cargar el mapa real de fondo
map_image = np.array(Image.open("MapaUninorte.png"))

# Mostrar imagen de fondo
fig, ax = plt.subplots(figsize=(12, 10))
ax.imshow(map_image, extent=[0, 1800, 0, 1200])

# Agregar nodos
nodos = [
    'CasaEstudio', 'Biblioteca', 'BloqueA', 'BloqueB', 'BloqueC', 'BloqueD',
    'BloqueE', 'BloqueF', 'BloqueG', 'CentroMedico',
    'BloqueI', 'BloqueJ', 'BloqueK', 'BloqueL', 'BloqueM',
    'Puerta7', 'Puerta4', 'Coliseo', 'Puerta11B',
    'BambúJ', 'BambúColaboradores', 'OficinaDelEgresado'
]

universidad.add_nodes_from(nodos)

# Conectar todos los nodos con todos los demás (grafo completo)

pesos = {
    ('BloqueA', 'BloqueB'): 6,
    ('BloqueB', 'BloqueC'): 3,
    ('BloqueC', 'BloqueD'): 2,
    ('BloqueD', 'BloqueE'): 2,
    ('Coliseo', 'BloqueF'): 2,
    ('Biblioteca', 'BloqueG'): 2,
    ('BloqueA', 'CentroMedico'): 2,
    ('BloqueA', 'BloqueI'): 2,
    ('BloqueA', 'BloqueJ'): 2,
    ('BloqueA', 'BloqueK'): 2,
    ('BloqueA', 'BloqueL'): 2,
    ('BloqueA', 'BloqueM'): 2,
    ('Puerta4', 'BloqueC'): 4,
    ('BambúColaboradores', 'OficinaDelEgresado'): 1,
    ('BambúJ', 'BambúColaboradores'): 1,
    ('BambúJ', 'OficinaDelEgresado'): 1,
    ('Biblioteca', 'BambúColaboradores'): 1,
    ('Biblioteca', 'BambúJ'): 1,
    ('Biblioteca', 'BloqueA'): 1,
    ('Biblioteca', 'BloqueB'): 1,
    ('Biblioteca', 'BloqueC'): 1,
    ('Biblioteca', 'BloqueD'): 1,
    ('Biblioteca', 'BloqueE'): 1,
    ('Biblioteca', 'BloqueF'): 1,
    ('Biblioteca', 'BloqueG'): 2,
    ('Biblioteca', 'BloqueI'): 1,
    ('Biblioteca', 'BloqueJ'): 1,
    ('Biblioteca', 'BloqueK'): 1,
    ('Biblioteca', 'BloqueL'): 1,
    ('Biblioteca', 'BloqueM'): 1,
    ('Biblioteca', 'CentroMedico'): 1,
    ('Biblioteca', 'Coliseo'): 1,
    ('Biblioteca', 'OficinaDelEgresado'): 1,
    ('Biblioteca', 'Puerta11B'): 1,
    ('Biblioteca', 'Puerta4'): 1,
    ('Biblioteca', 'Puerta7'): 1,
    ('BloqueA', 'BambúColaboradores'): 1,
    ('BloqueA', 'BambúJ'): 1,
    ('BloqueA', 'BloqueB'): 6,
    ('BloqueA', 'BloqueC'): 1,
    ('BloqueA', 'BloqueD'): 1,
    ('BloqueA', 'BloqueE'): 1,
    ('BloqueA', 'BloqueF'): 1,
    ('BloqueA', 'BloqueG'): 1,
    ('BloqueA', 'BloqueI'): 2,
    ('BloqueA', 'BloqueJ'): 2,
    ('BloqueA', 'BloqueK'): 2,
    ('BloqueA', 'BloqueL'): 2,
    ('BloqueA', 'BloqueM'): 2,
    ('BloqueA', 'CentroMedico'): 2,
    ('BloqueA', 'Coliseo'): 1,
    ('BloqueA', 'OficinaDelEgresado'): 1,
    ('BloqueA', 'Puerta11B'): 1,
    ('BloqueA', 'Puerta4'): 1,
    ('BloqueA', 'Puerta7'): 1,
    ('BloqueB', 'BambúColaboradores'): 1,
    ('BloqueB', 'BambúJ'): 1,
    ('BloqueB', 'BloqueC'): 3,
    ('BloqueB', 'BloqueD'): 1,
    ('BloqueB', 'BloqueE'): 1,
    ('BloqueB', 'BloqueF'): 1,
    ('BloqueB', 'BloqueG'): 1,
    ('BloqueB', 'BloqueI'): 1,
    ('BloqueB', 'BloqueJ'): 1,
    ('BloqueB', 'BloqueK'): 1,
    ('BloqueB', 'BloqueL'): 1,
    ('BloqueB', 'BloqueM'): 1,
    ('BloqueB', 'CentroMedico'): 1,
    ('BloqueB', 'Coliseo'): 1,
    ('BloqueB', 'OficinaDelEgresado'): 1,
    ('BloqueB', 'Puerta11B'): 1,
    ('BloqueB', 'Puerta4'): 1,
    ('BloqueB', 'Puerta7'): 1,
    ('BloqueC', 'BambúColaboradores'): 1,
    ('BloqueC', 'BambúJ'): 1,
    ('BloqueC', 'BloqueD'): 2,
    ('BloqueC', 'BloqueE'): 1,
    ('BloqueC', 'BloqueF'): 1,
    ('BloqueC', 'BloqueG'): 1,
    ('BloqueC', 'BloqueI'): 1,
    ('BloqueC', 'BloqueJ'): 1,
    ('BloqueC', 'BloqueK'): 1,
    ('BloqueC', 'BloqueL'): 1,
    ('BloqueC', 'BloqueM'): 1,
    ('BloqueC', 'CentroMedico'): 1,
    ('BloqueC', 'Coliseo'): 1,
    ('BloqueC', 'OficinaDelEgresado'): 1,
    ('BloqueC', 'Puerta11B'): 1,
    ('BloqueC', 'Puerta7'): 1,
    ('BloqueD', 'BambúColaboradores'): 1,
    ('BloqueD', 'BambúJ'): 1,
    ('BloqueD', 'BloqueE'): 2,
    ('BloqueD', 'BloqueF'): 1,
    ('BloqueD', 'BloqueG'): 1,
    ('BloqueD', 'BloqueI'): 1,
    ('BloqueD', 'BloqueJ'): 1,
    ('BloqueD', 'BloqueK'): 1,
    ('BloqueD', 'BloqueL'): 1,
    ('BloqueD', 'BloqueM'): 1,
    ('BloqueD', 'CentroMedico'): 1,
    ('BloqueD', 'Coliseo'): 1,
    ('BloqueD', 'OficinaDelEgresado'): 1,
    ('BloqueD', 'Puerta11B'): 1,
    ('BloqueD', 'Puerta4'): 1,
    ('BloqueD', 'Puerta7'): 1,
    ('BloqueE', 'BambúColaboradores'): 1,
    ('BloqueE', 'BambúJ'): 1,
    ('BloqueE', 'BloqueF'): 1,
    ('BloqueE', 'BloqueG'): 1,
    ('BloqueE', 'BloqueI'): 1,
    ('BloqueE', 'BloqueJ'): 1,
    ('BloqueE', 'BloqueK'): 1,
    ('BloqueE', 'BloqueL'): 1,
    ('BloqueE', 'BloqueM'): 1,
    ('BloqueE', 'CentroMedico'): 1,
    ('BloqueE', 'Coliseo'): 1,
    ('BloqueE', 'OficinaDelEgresado'): 1,
    ('BloqueE', 'Puerta11B'): 1,
    ('BloqueE', 'Puerta4'): 1,
    ('BloqueE', 'Puerta7'): 1,
    ('BloqueF', 'BambúColaboradores'): 1,
    ('BloqueF', 'BambúJ'): 1,
    ('BloqueF', 'BloqueG'): 1,
    ('BloqueF', 'BloqueI'): 1,
    ('BloqueF', 'BloqueJ'): 1,
    ('BloqueF', 'BloqueK'): 1,
    ('BloqueF', 'BloqueL'): 1,
    ('BloqueF', 'BloqueM'): 1,
    ('BloqueF', 'CentroMedico'): 1,
    ('BloqueF', 'OficinaDelEgresado'): 1,
    ('BloqueF', 'Puerta11B'): 1,
    ('BloqueF', 'Puerta4'): 1,
    ('BloqueF', 'Puerta7'): 1,
    ('BloqueG', 'BambúColaboradores'): 1,
    ('BloqueG', 'BambúJ'): 1,
    ('BloqueG', 'BloqueI'): 1,
    ('BloqueG', 'BloqueJ'): 1,
    ('BloqueG', 'BloqueK'): 1,
    ('BloqueG', 'BloqueL'): 1,
    ('BloqueG', 'BloqueM'): 1,
    ('BloqueG', 'CentroMedico'): 1,
    ('BloqueG', 'Coliseo'): 1,
    ('BloqueG', 'OficinaDelEgresado'): 1,
    ('BloqueG', 'Puerta11B'): 1,
    ('BloqueG', 'Puerta4'): 1,
    ('BloqueG', 'Puerta7'): 1,
    ('BloqueI', 'BambúColaboradores'): 1,
    ('BloqueI', 'BambúJ'): 1,
    ('BloqueI', 'BloqueJ'): 1,
    ('BloqueI', 'BloqueK'): 1,
    ('BloqueI', 'BloqueL'): 1,
    ('BloqueI', 'BloqueM'): 1,
    ('BloqueI', 'Coliseo'): 1,
    ('BloqueI', 'OficinaDelEgresado'): 1,
    ('BloqueI', 'Puerta11B'): 1,
    ('BloqueI', 'Puerta4'): 1,
    ('BloqueI', 'Puerta7'): 1,
    ('BloqueJ', 'BambúColaboradores'): 1,
    ('BloqueJ', 'BambúJ'): 1,
    ('BloqueJ', 'BloqueK'): 1,
    ('BloqueJ', 'BloqueL'): 1,
    ('BloqueJ', 'BloqueM'): 1,
    ('BloqueJ', 'Coliseo'): 1,
    ('BloqueJ', 'OficinaDelEgresado'): 1,
    ('BloqueJ', 'Puerta11B'): 1,
    ('BloqueJ', 'Puerta4'): 1,
    ('BloqueJ', 'Puerta7'): 1,
    ('BloqueK', 'BambúColaboradores'): 1,
    ('BloqueK', 'BambúJ'): 1,
    ('BloqueK', 'BloqueL'): 1,
    ('BloqueK', 'BloqueM'): 1,
    ('BloqueK', 'Coliseo'): 1,
    ('BloqueK', 'OficinaDelEgresado'): 1,
    ('BloqueK', 'Puerta11B'): 1,
    ('BloqueK', 'Puerta4'): 1,
    ('BloqueK', 'Puerta7'): 1,
    ('BloqueL', 'BambúColaboradores'): 1,
    ('BloqueL', 'BambúJ'): 1,
    ('BloqueL', 'BloqueM'): 1,
    ('BloqueL', 'Coliseo'): 1,
    ('BloqueL', 'OficinaDelEgresado'): 1,
    ('BloqueL', 'Puerta11B'): 1,
    ('BloqueL', 'Puerta4'): 1,
    ('BloqueL', 'Puerta7'): 1,
    ('BloqueM', 'BambúColaboradores'): 1,
    ('BloqueM', 'BambúJ'): 1,
    ('BloqueM', 'Coliseo'): 1,
    ('BloqueM', 'OficinaDelEgresado'): 1,
    ('BloqueM', 'Puerta11B'): 1,
    ('BloqueM', 'Puerta4'): 1,
    ('BloqueM', 'Puerta7'): 1,
    ('CasaEstudio', 'BambúColaboradores'): 1,
    ('CasaEstudio', 'BambúJ'): 1,
    ('CasaEstudio', 'Biblioteca'): 1,
    ('CasaEstudio', 'BloqueA'): 1,
    ('CasaEstudio', 'BloqueB'): 1,
    ('CasaEstudio', 'BloqueC'): 1,
    ('CasaEstudio', 'BloqueD'): 1,
    ('CasaEstudio', 'BloqueE'): 1,
    ('CasaEstudio', 'BloqueF'): 1,
    ('CasaEstudio', 'BloqueG'): 1,
    ('CasaEstudio', 'BloqueI'): 1,
    ('CasaEstudio', 'BloqueJ'): 1,
    ('CasaEstudio', 'BloqueK'): 1,
    ('CasaEstudio', 'BloqueL'): 1,
    ('CasaEstudio', 'BloqueM'): 1,
    ('CasaEstudio', 'CentroMedico'): 1,
    ('CasaEstudio', 'Coliseo'): 1,
    ('CasaEstudio', 'OficinaDelEgresado'): 1,
    ('CasaEstudio', 'Puerta11B'): 1,
    ('CasaEstudio', 'Puerta4'): 1,
    ('CasaEstudio', 'Puerta7'): 1,
    ('CentroMedico', 'BambúColaboradores'): 1,
    ('CentroMedico', 'BambúJ'): 1,
    ('CentroMedico', 'BloqueI'): 1,
    ('CentroMedico', 'BloqueJ'): 1,
    ('CentroMedico', 'BloqueK'): 1,
    ('CentroMedico', 'BloqueL'): 1,
    ('CentroMedico', 'BloqueM'): 1,
    ('CentroMedico', 'Coliseo'): 1,
    ('CentroMedico', 'OficinaDelEgresado'): 1,
    ('CentroMedico', 'Puerta11B'): 1,
    ('CentroMedico', 'Puerta4'): 1,
    ('CentroMedico', 'Puerta7'): 1,
    ('Coliseo', 'BambúColaboradores'): 1,
    ('Coliseo', 'BambúJ'): 1,
    ('Coliseo', 'BloqueF'): 2,
    ('Coliseo', 'OficinaDelEgresado'): 1,
    ('Coliseo', 'Puerta11B'): 1,
    ('Puerta11B', 'BambúColaboradores'): 1,
    ('Puerta11B', 'BambúJ'): 1,
    ('Puerta11B', 'OficinaDelEgresado'): 1,
    ('Puerta4', 'BambúColaboradores'): 1,
    ('Puerta4', 'BambúJ'): 1,
    ('Puerta4', 'BloqueC'): 4,
    ('Puerta4', 'Coliseo'): 1,
    ('Puerta4', 'OficinaDelEgresado'): 1,
    ('Puerta4', 'Puerta11B'): 1,
    ('Puerta7', 'BambúColaboradores'): 1,
    ('Puerta7', 'BambúJ'): 1,
    ('Puerta7', 'Coliseo'): 1,
    ('Puerta7', 'OficinaDelEgresado'): 1,
    ('Puerta7', 'Puerta11B'): 1,
    ('Puerta7', 'Puerta4'): 850,
}

# Crear las conexiones a partir del diccionario de pesos
for (nodo1, nodo2), peso in pesos.items():
    universidad.add_edge(nodo1, nodo2, weight=peso)

# Coordenadas manuales
pos = {
    'CasaEstudio': (610, 182),
    'Biblioteca': (650, 265),
    'BloqueA': (483, 400),
    'BloqueB': (491, 465),
    'BloqueC': (500, 535),
    'BloqueD': (693, 350),
    'BloqueE': (686, 428),
    'BloqueF': (679, 500),
    'BloqueG': (759, 711),
    'CentroMedico': (276, 495),
    'BloqueI': (523, 677),
    'BloqueJ': (318, 969),
    'BloqueK': (422, 823),
    'BloqueL': (330, 591),
    'BloqueM': (1120, 832),
    'Puerta7': (783, 593),
    'Puerta4': (601, 134),
    'Puerta11B': (345, 1000),
    'Coliseo': (612, 842),
    'BambúJ': (210, 975),
    'BambúColaboradores': (212, 240),
    'OficinaDelEgresado': (260, 409)
}

def mostrar_camino_mas_corto(G, positions):
    origen = origen_combobox.get()
    destino = destino_combobox.get()

    if origen not in G.nodes or destino not in G.nodes:
        messagebox.showerror("Error", "Selecciona nodos válidos.")
        return

    try:
        shortest_path = nx.dijkstra_path(G, source=origen, target=destino, weight='weight')
    except nx.NetworkXNoPath:
        messagebox.showerror("Sin conexión", "No existe un camino entre los nodos seleccionados.")
        return

    # Limpiar el canvas
    ax.clear()

    # Dibujar la imagen del mapa
    ax.imshow(map_image, extent=[0, 1800, 0, 1200])

    # Mostrar etiquetas de los nodos
    nx.draw_networkx_labels(G, positions, ax=ax, font_size=7)

    # Extraer aristas del camino más corto
    path_edges = list(zip(shortest_path, shortest_path[1:]))

    # Dibujar aristas del camino
    nx.draw_networkx_edges(G, positions, edgelist=path_edges, ax=ax, edge_color='black', width=2.5)

    # Dibujar pesos de las aristas
    edge_labels = {(u, v): G[u][v]['weight'] for u, v in path_edges}
    nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels, ax=ax, font_size=7, font_color='blue')

    # Colorear nodos del camino
    if len(shortest_path) > 2:
        intermedios = shortest_path[1:-1]
    else:
        intermedios = []

    # Origen en verde
    nx.draw_networkx_nodes(G, positions, nodelist=[origen], ax=ax, node_color='green', node_size=300)

    # Destino en rojo
    nx.draw_networkx_nodes(G, positions, nodelist=[destino], ax=ax, node_color='red', node_size=300)

    # Intermedios en naranja
    if intermedios:
        nx.draw_networkx_nodes(G, positions, nodelist=intermedios, ax=ax, node_color='brown', node_size=300)

    # Actualizar el canvas
    canvas.draw()


# Obtener etiquetas de distancias
labels = nx.get_edge_attributes(universidad, 'weight')

# Crear el frame para los controles
root = tk.Tk()
root.title("Rutas Uninorte")
control_frame = tk.Frame(root)
control_frame.pack(side=tk.TOP, pady=10)

tk.Label(control_frame, text="Origen:").grid(row=0, column=0, padx=5)
origen_combobox = ttk.Combobox(control_frame, values=list(universidad.nodes))
origen_combobox.grid(row=0, column=1, padx=5)

tk.Label(control_frame, text="Destino:").grid(row=0, column=2, padx=5)
destino_combobox = ttk.Combobox(control_frame, values=list(universidad.nodes))
destino_combobox.grid(row=0, column=3, padx=5)

buscar_button = tk.Button(
    control_frame,
    text="Buscar Ruta",
    command=lambda: mostrar_camino_mas_corto(universidad, pos)
)
buscar_button.grid(row=0, column=4, padx=10)

# Dibujar el grafo
#nx.draw(universidad, pos, with_labels=True, node_color='red', node_size=200, font_size=6)
#nx.draw_networkx_edge_labels(universidad, pos, edge_labels=labels, font_size=4)

# Dibujar solo los nodos (vértices), sin aristas
nx.draw_networkx_nodes(universidad, pos, ax=ax, node_color='brown', node_size=300)
nx.draw_networkx_labels(universidad, pos, ax=ax, font_size=7, font_color='black')

# Mostrar figura en tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


plt.title("Mapa de la universidad")
root.mainloop()
#plt.show()









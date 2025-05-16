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
    ('BloqueB', 'BloqueC'): 14,
    ('BloqueC', 'BloqueD'): 450,
    ('BloqueD', 'BloqueE'): 33,
    ('Coliseo', 'BloqueF'): 240,
    ('Biblioteca', 'BloqueG'): 240,
    ('BloqueA', 'CentroMedico'): 25,
    ('BloqueA', 'BloqueI'): 140,
    ('BloqueA', 'BloqueJ'): 400,
    ('BloqueA', 'BloqueK'): 360,
    ('BloqueA', 'BloqueL'): 120,
    ('BloqueA', 'BloqueM'): 600,
    ('Puerta4', 'BloqueC'): 350,
    ('BambúColaboradores', 'OficinaDelEgresado'): 34,
    ('BambúJ', 'BambúColaboradores'): 450,
    ('BambúJ', 'OficinaDelEgresado'): 410,
    ('Biblioteca', 'BambúColaboradores'): 170,
    ('Biblioteca', 'BambúJ'): 700,
    ('Biblioteca', 'BloqueA'): 230,
    ('Biblioteca', 'BloqueB'): 350,
    ('Biblioteca', 'BloqueC'): 400,
    ('Biblioteca', 'BloqueD'): 25,
    ('Biblioteca', 'BloqueE'): 55,
    ('Biblioteca', 'BloqueF'): 80,
    ('Biblioteca', 'BloqueG'): 220,
    ('Biblioteca', 'BloqueI'): 350,
    ('Biblioteca', 'BloqueJ'): 600,
    ('Biblioteca', 'BloqueK'): 550,
    ('Biblioteca', 'BloqueL'): 290,
    ('Biblioteca', 'BloqueM'): 450,
    ('Biblioteca', 'CentroMedico'): 240,
    ('Biblioteca', 'Coliseo'): 260,
    ('Biblioteca', 'OficinaDelEgresado'): 150,
    ('Biblioteca', 'Puerta11B'): 602,
    ('Biblioteca', 'Puerta4'): 20,
    ('Biblioteca', 'Puerta7'): 160,
    ('BloqueA', 'BambúColaboradores'): 61,
    ('BloqueA', 'BambúJ'): 400,
    ('BloqueA', 'BloqueB'): 29,
    ('BloqueA', 'BloqueC'): 55,
    ('BloqueA', 'BloqueD'): 60,
    ('BloqueA', 'BloqueE'): 80,
    ('BloqueA', 'BloqueF'): 100,
    ('BloqueA', 'BloqueG'): 450,
    ('BloqueA', 'BloqueI'): 150,
    ('BloqueA', 'BloqueJ'): 370,
    ('BloqueA', 'BloqueK'): 330,
    ('BloqueA', 'BloqueL'): 69,
    ('BloqueA', 'BloqueM'): 324.84,
    ('BloqueA', 'CentroMedico'): 99.06,
    ('BloqueA', 'Coliseo'): 259.22,
    ('BloqueA', 'OficinaDelEgresado'): 94.53,
    ('BloqueA', 'Puerta11B'): 296.72,
    ('BloqueA', 'Puerta4'): 135.25,
    ('BloqueA', 'Puerta7'): 189.28,
    ('BloqueB', 'BambúColaboradores'): 121.23,
    ('BloqueB', 'BambúJ'): 249.9,
    ('BloqueB', 'BloqueC'): 27.64,
    ('BloqueB', 'BloqueD'): 121.23,
    ('BloqueB', 'BloqueE'): 114.86,
    ('BloqueB', 'BloqueF'): 103.8,
    ('BloqueB', 'BloqueG'): 166.45,
    ('BloqueB', 'BloqueI'): 82.43,
    ('BloqueB', 'BloqueJ'): 253.48,
    ('BloqueB', 'BloqueK'): 154.06,
    ('BloqueB', 'BloqueL'): 99.49,
    ('BloqueB', 'BloqueM'): 297.06,
    ('BloqueB', 'CentroMedico'): 94.28,
    ('BloqueB', 'Coliseo'): 217.88,
    ('BloqueB', 'OficinaDelEgresado'): 114.26,
    ('BloqueB', 'Puerta11B'): 261.74,
    ('BloqueB', 'Puerta4'): 164.3,
    ('BloqueB', 'Puerta7'): 193.23,
    ('BloqueC', 'BambúColaboradores'): 152.4,
    ('BloqueC', 'BambúJ'): 236.5,
    ('BloqueC', 'BloqueD'): 128.96,
    ('BloqueC', 'BloqueE'): 119.45,
    ('BloqueC', 'BloqueF'): 111.5,
    ('BloqueC', 'BloqueG'): 153.96,
    ('BloqueC', 'BloqueI'): 76.33,
    ('BloqueC', 'BloqueJ'): 229.97,
    ('BloqueC', 'BloqueK'): 131.39,
    ('BloqueC', 'BloqueL'): 82.78,
    ('BloqueC', 'BloqueM'): 287.53,
    ('BloqueC', 'CentroMedico'): 99.98,
    ('BloqueC', 'Coliseo'): 191.71,
    ('BloqueC', 'OficinaDelEgresado'): 135.2,
    ('BloqueC', 'Puerta11B'): 243.61,
    ('BloqueC', 'Puerta7'): 156.28,
    ('BloqueD', 'BambúColaboradores'): 211.36,
    ('BloqueD', 'BambúJ'): 364.59,
    ('BloqueD', 'BloqueE'): 59.18,
    ('BloqueD', 'BloqueF'): 90.48,
    ('BloqueD', 'BloqueG'): 190.17,
    ('BloqueD', 'BloqueI'): 171.19,
    ('BloqueD', 'BloqueJ'): 350.0,
    ('BloqueD', 'BloqueK'): 246.0,
    
    ('BloqueD', 'BloqueL'): 239,
    ('BloqueD', 'BloqueM'): 296,
    ('BloqueD', 'CentroMedico'): 272,
    ('BloqueD', 'Coliseo'): 224,
    ('BloqueD', 'OficinaDelEgresado'): 189,		
    ('BloqueD', 'Puerta11B'): 399,
    ('BloqueD', 'Puerta4'): 94.6,
    ('BloqueD', 'Puerta7'): 175,
    ('BloqueE', 'BambúColaboradores'): 269,
    ('BloqueE', 'BambúJ'): 402,
    ('BloqueE', 'BloqueF'): 16.7,
    ('BloqueE', 'BloqueG'): 141,
    ('BloqueE', 'BloqueI'): 168,
    ('BloqueE', 'BloqueJ'): 330,
    ('BloqueE', 'BloqueK'): 252,
    ('BloqueE', 'BloqueL'): 203,
    ('BloqueE', 'BloqueM'): 241,
    ('BloqueE', 'CentroMedico'): 176,
    ('BloqueE', 'Coliseo'): 172,
    ('BloqueE', 'OficinaDelEgresado'): 227,
    ('BloqueE', 'Puerta11B'): 333,
    ('BloqueE', 'Puerta4'): 135,
    ('BloqueE', 'Puerta7'): 124,
    ('BloqueF', 'BambúColaboradores'): 263,
    ('BloqueF', 'BambúJ'): 359,
    ('BloqueF', 'BloqueG'): 115,
    ('BloqueF', 'BloqueI'): 122,
    ('BloqueF', 'BloqueJ'): 320,
    ('BloqueF', 'BloqueK'): 219,
    ('BloqueF', 'BloqueL'): 179,
    ('BloqueF', 'BloqueM'): 205,
    ('BloqueF', 'CentroMedico'):205,
    ('BloqueF', 'OficinaDelEgresado'): 230,
    ('BloqueF', 'Puerta11B'): 317,
    ('BloqueF', 'Puerta4'): 146,
    ('BloqueF', 'Puerta7'): 106,
    ('BloqueG', 'BambúColaboradores'): 394,
    ('BloqueG', 'BambúJ'): 314,
    ('BloqueG', 'BloqueI'): 84.9,
    ('BloqueG', 'BloqueJ'): 227,
    ('BloqueG', 'BloqueK'): 230,
    ('BloqueG', 'BloqueL'): 218,
    ('BloqueG', 'BloqueM'): 183,
    ('BloqueG', 'CentroMedico'): 297,
    ('BloqueG', 'Coliseo'): 77.8,
    ('BloqueG', 'OficinaDelEgresado'): 336,
    ('BloqueG', 'Puerta11B'): 247,
    ('BloqueG', 'Puerta4'): 251,
    ('BloqueG', 'Puerta7'): 57,
    
    ('BloqueI', 'BambúColaboradores'): 223.78,
    ('BloqueI', 'BambúJ'): 198.66,
    ('BloqueI', 'BloqueJ'): 180.06,
    ('BloqueI', 'BloqueK'): 93.87,
    ('BloqueI', 'BloqueL'): 67.72,
    ('BloqueI', 'BloqueM'): 239.11,
    ('BloqueI', 'Coliseo'): 23.73,
    ('BloqueI', 'OficinaDelEgresado'): 170.06,
    ('BloqueI', 'Puerta11B'): 182.86,
    ('BloqueI', 'Puerta4'): 233.26,
    ('BloqueI', 'Puerta7'): 130.0,
    ('BloqueJ', 'BambúColaboradores'): 324.65,
    ('BloqueJ', 'BambúJ'): 35.27,
    ('BloqueJ', 'BloqueK'): 101.53,
    ('BloqueJ', 'BloqueL'): 162.32,
    ('BloqueJ', 'BloqueM'): 325.31,
    ('BloqueJ', 'Coliseo'): 134.23,
    ('BloqueJ', 'OficinaDelEgresado'): 256.53,
    ('BloqueJ', 'Puerta11B'): 8.24,
    ('BloqueJ', 'Puerta4'): 391.54,
    ('BloqueJ', 'Puerta7'): 297.70,
    ('BloqueK', 'BambúColaboradores'): 264.70,
    ('BloqueK', 'BambúJ'): 126.53,
    ('BloqueK', 'BloqueL'): 84.29,
    ('BloqueK', 'BloqueM'): 275.85,
    ('BloqueK', 'Coliseo'): 65.03,
    ('BloqueK', 'OficinaDelEgresado'): 181.23,
    ('BloqueK', 'Puerta11B'): 119.06,
    ('BloqueK', 'Puerta4'): 292.30,
    ('BloqueK', 'Puerta7'): 207.42,
    ('BloqueL', 'BambúColaboradores'): 147.27,
    ('BloqueL', 'BambúJ'): 177.36,
    ('BloqueL', 'BloqueM'): 296.44,
    ('BloqueL', 'Coliseo'): 119.88,
    ('BloqueL', 'OficinaDelEgresado'): 63.24,
    ('BloqueL', 'Puerta11B'): 221.05,
    ('BloqueL', 'Puerta4'): 205.09,
    ('BloqueL', 'Puerta7'): 217.25,
    ('BloqueM', 'BambúColaboradores'): 428.40,
    ('BloqueM', 'BambúJ'): 397.96,
    ('BloqueM', 'Coliseo'): 174.49,
    ('BloqueM', 'OficinaDelEgresado'): 371.83,
    ('BloqueM', 'Puerta11B'): 362.88,
    ('BloqueM', 'Puerta4'): 344.04,
    ('BloqueM', 'Puerta7'): 107.39,
    ('CasaEstudio', 'BambúColaboradores'): 185.08,
    ('CasaEstudio', 'BambúJ'): 588.10,
    ('CasaEstudio', 'Biblioteca'): 12.2,
    ('CasaEstudio', 'BloqueA'): 100.89,

('CasaEstudio', 'BloqueB'): 260,
    ('CasaEstudio', 'BloqueC'): 350,
    ('CasaEstudio', 'BloqueD'): 130,
    ('CasaEstudio', 'BloqueE'): 240,
    ('CasaEstudio', 'BloqueF'): 190,
    ('CasaEstudio', 'BloqueG'): 300,
    ('CasaEstudio', 'BloqueI'): 400,
    ('CasaEstudio', 'BloqueJ'): 550,
    ('CasaEstudio', 'BloqueK'): 500,
    ('CasaEstudio', 'BloqueL'): 350,
    ('CasaEstudio', 'BloqueM'): 450,
    ('CasaEstudio', 'CentroMedico'): 270,
    ('CasaEstudio', 'Coliseo'): 500,
    ('CasaEstudio', 'OficinaDelEgresado'): 300,
    ('CasaEstudio', 'Puerta11B'): 550,
    ('CasaEstudio', 'Puerta4'): 30,
    ('CasaEstudio', 'Puerta7'): 260,
    ('CentroMedico', 'BambúColaboradores'): 60,
    ('CentroMedico', 'BambúJ'): 350,
    ('CentroMedico', 'BloqueI'): 120,
    ('CentroMedico', 'BloqueJ'): 300,
    ('CentroMedico', 'BloqueK'): 220,
    ('CentroMedico', 'BloqueL'): 90,
    ('CentroMedico', 'BloqueM'): 400,
    ('CentroMedico', 'Coliseo'): 300,
    ('CentroMedico', 'OficinaDelEgresado'): 40,
    ('CentroMedico', 'Puerta11B'): 320,
    ('CentroMedico', 'Puerta4'): 270,
    ('CentroMedico', 'Puerta7'): 300,
    ('Coliseo', 'BambúColaboradores'): 320,
    ('Coliseo', 'BambúJ'): 220,
    ('Coliseo', 'BloqueF'): 300,
    ('Coliseo', 'OficinaDelEgresado'): 280,
    ('Coliseo', 'Puerta11B'): 200,
    ('Puerta11B', 'BambúColaboradores'): 300,
    ('Puerta11B', 'BambúJ'): 50,
    ('Puerta11B', 'OficinaDelEgresado'): 280,
    ('Puerta4', 'BambúColaboradores'): 230,
    ('Puerta4', 'BambúJ'): 650,
    ('Puerta4', 'BloqueC'): 200,
    ('Puerta4', 'Coliseo'): 480,
    ('Puerta4', 'OficinaDelEgresado'): 250,
    ('Puerta4', 'Puerta11B'): 600,
    ('Puerta7', 'BambúColaboradores'): 320,
    ('Puerta7', 'BambúJ'): 430,
    ('Puerta7', 'Coliseo'): 220,
    ('Puerta7', 'OficinaDelEgresado'): 300,
    ('Puerta7', 'Puerta11B'): 390,
    ('Puerta7', 'Puerta4'): 260,

}

# Crear las conexiones a partir del diccionario de pesos
for (nodo1, nodo2), peso in pesos.items():
    universidad.add_edge(nodo1, nodo2, weight=peso)

# Coordenadas manuales en el mapa de la U
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

# Obtener etiquetas de distancias (pesos)
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


# Dibujar algunas aristas específicas
aristas_a_dibujar = [
    ('BloqueB', 'BloqueC'),
    ('BloqueC', 'BloqueD'),
    ('Biblioteca', 'BloqueA'),
    ('BloqueA', 'BloqueL'),
    ('BloqueA', 'CentroMedico'),
    ('BambúJ', 'OficinaDelEgresado'),
    ('BloqueM', 'Puerta11B'),
    ('BloqueK', 'Coliseo'),
    ('BambúColaboradores', 'Puerta4'),
    ('BloqueE', 'Puerta7'),
    ('OficinaDelEgresado', 'CasaEstudio'),
    ('BloqueM', 'BloqueD'),
    ('BloqueI', 'BloqueF'),
    ('BloqueK', 'BloqueB'),
    ('BloqueM', 'Puerta4'),
    ('Coliseo', 'BloqueG'),
    ('BloqueL', 'BloqueJ'),
    ('BloqueI', 'BloqueG'),
    ('BambúColaboradores', 'OficinaDelEgresado'),
    ('BloqueG', 'BloqueM'),

]

# Dibujar las aristas seleccionadas
nx.draw_networkx_edges(universidad, pos, edgelist=aristas_a_dibujar, ax=ax, edge_color='black')
# Filtrar solo los labels de las aristas a dibujar
edge_labels_completos = nx.get_edge_attributes(universidad, 'weight')
edge_labels_filtrados = {arista: peso for arista, peso in edge_labels_completos.items() if arista in aristas_a_dibujar or (arista[1], arista[0]) in aristas_a_dibujar}
nx.draw_networkx_edge_labels(universidad, pos, edge_labels=edge_labels_filtrados, font_size=8, ax=ax)

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
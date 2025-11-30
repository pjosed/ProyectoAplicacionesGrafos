# 🗺️ UniPathFinder — Shortest Path Finder usando teoría de grafos

**Python | Graph Theory | NetworkX | OSMnx | Tkinter | GUI | Pathfinding**

UniPathFinder es una herramienta interactiva que aplica conceptos de teoría de grafos para resolver un problema de la vida real:

> ⭐ **Encontrar el camino mínimo entre dos lugares dentro de la Universidad del Norte.**

El proyecto cuenta con **dos implementaciones**, ambas con interfaz gráfica intuitiva.

---

## 🚀 Overview

UniPathFinder permite al usuario seleccionar dos puntos del campus y visualizar la ruta más corta entre ellos.  
Incluye:

### 🌍 Versión basada en mapa real (OSMnx)
Usa **OSMnx + NetworkX + Matplotlib** para extraer el grafo real del campus desde OpenStreetMap y calcular rutas reales basadas en calles y senderos.

### 🏫 Versión con distancias manuales
Construye un grafo propio a partir de mediciones hechas manualmente en el campus, permitiendo control total sobre:

- Pesos  
- Nodos  
- Conexiones  
- Distancias  

Ambas versiones utilizan una GUI hecha con Tkinter para seleccionar origen, destino y mostrar el camino.

---

## 🧠 Conceptos fundamentales aplicados:

- ✔ Algoritmos de grafos  
- ✔ Cálculo de distancias mínimas (Dijkstra / A*)  
- ✔ Modelado de nodos y aristas  
- ✔ Manipulación de grafos reales (OSMnx)  
- ✔ Visualización dinámica sobre mapas  

---

## 🧭 Features

### 🌍 Versión 1 — Grafo Real (OSMnx)
Esta versión:

- Descarga o carga el grafo del campus desde OSMnx  
- Simplifica nodos y caminos  
- Calcula rutas con NetworkX  
- Dibuja el mapa y la ruta calculada  
- Muestra errores o mensajes emergentes (messagebox)

## 🏫 Versión 2 — Grafo Manual

Esta implementación crea un grafo completamente personalizado para modelar la Universidad del Norte, permitiendo control total sobre la lógica de rutas:

- Nodos representando puntos clave del campus  
- Pesos medidos manualmente entre ubicaciones  
- Grafo construido desde cero (edge lists o listas de adyacencia)  
- Algoritmo de Dijkstra implementado manualmente  
- Visualización de la ruta sobre el mapa base **MapaUninorte.png**  
- GUI intuitiva para seleccionar origen y destino  

---

  ## 🎨 Interfaz gráfica (GUI)

Ambas versiones incluyen una interfaz construida con Tkinter que permite:

- ✔ Menús simples y organizados  
- ✔ Selección de nodos mediante listas o ComboBox  
- ✔ Mapa visual del campus como fondo  
- ✔ Dibujo del camino más corto directamente sobre el canvas  
- ✔ Mensajes de validación y manejo de errores  
- ✔ Botones para calcular y limpiar rutas  
- ✔ Integración fluida con Matplotlib para renderizar mapas  

---

## 🧱 Architecture

### 📂 Versión OSMnx

**main_osmnx.py**  
- Descarga y configuración del grafo del campus  
- Construcción de la GUI en Tkinter  
- Render del mapa con Matplotlib  
- Función `calcular_camino()` usando NetworkX  

### 📂 Versión Manual

**main_manual.py**  
- Clase **Grafo** (nodos, aristas, pesos)  
- Algoritmo de **Dijkstra** implementado a mano  
- Carga del mapa base: `MapaUninorte.png`  
- Canvas y funciones para dibujar rutas sobre la imagen  

---

## 📚 Technologies Used

| Tecnología      | Uso                                      |
|-----------------|-------------------------------------------|
| **Python**      | Lógica principal del proyecto             |
| **NetworkX**    | Cálculo de rutas, pesos y grafos          |
| **OSMnx**       | Descarga del mapa real para la versión 1  |
| **Tkinter**     | Interfaz gráfica del usuario              |
| **Matplotlib**  | Visualización del mapa y las rutas        |
| **PIL / mpimg** | Carga de imágenes (mapa del campus)       |
| **Data Structures** | Nodos, aristas y grafos personalizados |

---

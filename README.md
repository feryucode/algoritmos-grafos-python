# Algoritmos de Grafos en Python

Este repositorio contiene la implementacion en Python de cuatro algoritmos clasicos y fundamentales de la teoria de grafos. El proyecto tiene un enfoque educativo, por lo que cada script imprime en consola la ejecucion paso a paso, mostrando tablas de costos, matrices y la toma de decisiones del algoritmo, ideal para comprender su funcionamiento interno.

## Algoritmos Incluidos

1. Algoritmo de Dijkstra (1_dijkstra.py)
Encuentra la ruta mas corta (de menor costo) desde un nodo origen hacia todos los demas nodos en un grafo ponderado con pesos positivos. Utiliza una estrategia voraz (Greedy) apoyada por una cola de prioridad.

2. Algoritmo de Floyd (2_floyd.py)
Resuelve el problema del camino mas corto entre todos los pares de nodos simultaneamente. Utiliza programacion dinamica para construir y actualizar una matriz de costos minimos, probando cada nodo como un posible puente intermedio.

3. Algoritmo de Warshall (3_warshall.py)
Calcula la clausura transitiva de un grafo dirigido. Mediante el uso de algebra booleana (0 y 1), determina si existe un camino (alcanzabilidad) directo o indirecto entre cualquier par de nodos en la red.

4. Algoritmo de Kruskal (4_kruskal.py)
Construye el Arbol de Expansion Minima (MST) de un grafo no dirigido y conexo. Conecta todos los nodos al menor costo total posible utilizando una estrategia voraz y la estructura de datos Union-Find para evitar la formacion de ciclos.

## Requisitos Previos

Para ejecutar estos scripts, solo necesitas tener Python instalado en tu computadora. No se requiere la instalacion de bibliotecas externas (pip install), ya que todo el codigo utiliza unicamente la biblioteca estandar de Python (como la libreria `heapq`).

- Python 3.6 o superior recomendado.

## Instrucciones de Ejecucion

1. Clona este repositorio en tu maquina local:
   git clone https://github.com/TU_USUARIO/algoritmos-grafos-python.git

2. Navega al directorio del proyecto:
   cd algoritmos-grafos-python

3. Ejecuta cada script individualmente desde la terminal. Por ejemplo:
   python 1_dijkstra.py
   python 2_floyd.py
   python 3_warshall.py
   python 4_kruskal.py

Cada programa mostrara en la consola el proceso de evaluacion, los pasos intermedios y el resultado final con tablas estructuradas.

## Estructura del Codigo

Cada archivo es independiente y contiene:
- Una implementacion limpia del algoritmo.
- Una funcion dedicada a imprimir los resultados en consola con formato de tabla.
- Un bloque `if __name__ == "__main__":` con un grafo de prueba basado en estados de la Republica Mexicana para facilitar la comprension del problema.

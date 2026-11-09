import heapq


def dijkstra(grafo, origen):
  # 1. Inicializar distancias en infinito y el origen en 0
  distancias = {nodo: float("inf") for nodo in grafo}
  distancias[origen] = 0
  predecesores = {nodo: None for nodo in grafo}
  visitados = set()

  # Cola de prioridad: almacena tuplas (costo_acumulado, nodo_actual)
  cola_prioridad = [(0, origen)]
  paso = 1

  print("=" * 72)
  print(f" EJECUCIÓN PASO A PASO - ALGORITMO DE DIJKSTRA (Origen: {origen})")
  print("=" * 72)

  while cola_prioridad:
    costo_actual, u = heapq.heappop(cola_prioridad)

    if u in visitados:
      continue
    visitados.add(u)

    print(f"\n[Paso {paso}] Visitando estado '{u}' (Costo acumulado: ${costo_actual})")
    paso += 1

    # 2. Relajación de las aristas vecinas
    for vecino, peso in grafo[u].items():
      if vecino not in visitados:
        nuevo_costo = costo_actual + peso
        if nuevo_costo < distancias[vecino]:
          anterior = (
              "∞" if distancias[vecino] == float("inf") else f"${distancias[vecino]}"
          )
          distancias[vecino] = nuevo_costo
          predecesores[vecino] = u
          heapq.heappush(cola_prioridad, (nuevo_costo, vecino))
          print(
              f"   ✔ Mejora encontrada hacia {vecino:<10}: {anterior} ->"
              f" ${nuevo_costo} (vía {u})"
          )
        else:
          print(
              f"   • Sin mejora hacia {vecino:<10}: costo actual"
              f" ${distancias[vecino]} <= ${nuevo_costo}"
          )

  return distancias, predecesores


def reconstruir_camino(predecesores, destino):
  camino = []
  actual = destino
  while actual is not None:
    camino.append(actual)
    actual = predecesores[actual]
  return camino[::-1]


if __name__ == "__main__":
  # Grafo ponderado de 6 estados de México
  grafo_mexico = {
      "CDMX": {"Puebla": 130, "Veracruz": 400, "Oaxaca": 460},
      "Puebla": {"CDMX": 130, "Veracruz": 280, "Oaxaca": 340},
      "Veracruz": {"CDMX": 400, "Puebla": 280, "Oaxaca": 310, "Tabasco": 480},
      "Oaxaca": {"CDMX": 460, "Puebla": 340, "Veracruz": 310, "Chiapas": 520},
      "Tabasco": {"Veracruz": 480, "Chiapas": 260},
      "Chiapas": {"Oaxaca": 520, "Tabasco": 260},
  }

  nodo_inicial = "CDMX"
  distancias, predecesores = dijkstra(grafo_mexico, nodo_inicial)

  print("\n" + "=" * 72)
  print(f" TABLA FINAL DE CAMINOS MÁS CORTOS DESDE {nodo_inicial}")
  print("=" * 72)
  print(f"{'Destino':<12} | {'Costo Mínimo':<14} | {'Ruta Óptima'}")
  print("-" * 72)
  for destino in grafo_mexico:
    ruta = " -> ".join(reconstruir_camino(predecesores, destino))
    print(f"{destino:<12} | ${distancias[destino]:<13} | {ruta}")
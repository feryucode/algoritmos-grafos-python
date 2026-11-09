class UnionFind:
  """Estructura de Conjuntos Disjuntos para detectar ciclos eficientemente."""

  def __init__(self, nodos):
    self.padre = {nodo: nodo for nodo in nodos}
    self.rango = {nodo: 0 for nodo in nodos}

  def encontrar(self, nodo):
    if self.padre[nodo] != nodo:
      self.padre[nodo] = self.encontrar(self.padre[nodo])  # Compresión de ruta
    return self.padre[nodo]

  def unir(self, u, v):
    raiz_u = self.encontrar(u)
    raiz_v = self.encontrar(v)

    if raiz_u == raiz_v:
      return False  # Ya están conectados: agregar la arista formaría un ciclo

    if self.rango[raiz_u] < self.rango[raiz_v]:
      self.padre[raiz_u] = raiz_v
    elif self.rango[raiz_u] > self.rango[raiz_v]:
      self.padre[raiz_v] = raiz_u
    else:
      self.padre[raiz_v] = raiz_u
      self.rango[raiz_u] += 1
    return True


def kruskal(nodos, aristas):
  # 1. Ordenar todas las aristas de menor a mayor costo
  aristas_ordenadas = sorted(aristas, key=lambda item: item[2])
  uf = UnionFind(nodos)

  mst = []
  costo_total = 0

  print("=" * 74)
  print(" EVALUACIÓN DE ARISTAS ORDENADAS POR COSTO - ALGORITMO DE KRUSKAL")
  print("=" * 74)
  print(f"{'Arista (Conexión)':<26} | {'Costo':<8} | {'Decisión del Algoritmo'}")
  print("-" * 74)

  # 2. Evaluar aristas en orden voraz (Greedy)
  for u, v, costo in aristas_ordenadas:
    conexion = f"{u} <-> {v}"
    if uf.unir(u, v):
      mst.append((u, v, costo))
      costo_total += costo
      print(f"{conexion:<26} | ${costo:<7} | ✔ ACEPTADA (Conecta nuevos estados)")
    else:
      print(f"{conexion:<26} | ${costo:<7} | ✖ DESCARTADA (Formaría un ciclo)")

  print("\n" + "=" * 74)
  print(" ÁRBOL DE EXPANSIÓN MÍNIMA (MST) RESULTANTE")
  print("=" * 74)
  for i, (u, v, costo) in enumerate(mst, 1):
    print(f"  {i}. {u:<10} <===> {v:<10}  (Costo: ${costo})")
  print("-" * 74)
  print(f"  Nodos totales: {len(nodos)} | Aristas del árbol (V - 1): {len(mst)}")
  print(f"  COSTO MÍNIMO TOTAL PARA CONECTAR TODOS LOS ESTADOS: ${costo_total}")
  print("=" * 74)

  return mst, costo_total


if __name__ == "__main__":
  estados = ["CDMX", "Puebla", "Veracruz", "Oaxaca", "Tabasco", "Chiapas"]
  carreteras = [
      ("CDMX", "Puebla", 130),
      ("Tabasco", "Chiapas", 260),
      ("Puebla", "Veracruz", 280),
      ("Veracruz", "Oaxaca", 310),
      ("Puebla", "Oaxaca", 340),
      ("CDMX", "Veracruz", 400),
      ("CDMX", "Oaxaca", 460),
      ("Veracruz", "Tabasco", 480),
      ("Oaxaca", "Chiapas", 520),
  ]

  kruskal(estados, carreteras)
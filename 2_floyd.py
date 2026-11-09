INF = float("inf")


def imprimir_matriz_costos(matriz, nodos, titulo):
  print(f"\n{titulo}")
  print("-" * 66)
  encabezado = f"{'Origen/Dest':<12} | " + " ".join(f"{n[:7]:>8}" for n in nodos)
  print(encabezado)
  print("-" * 66)
  for i, fila in enumerate(matriz):
    valores = " ".join(f"{'∞':>8}" if v == INF else f"{v:>8}" for v in fila)
    print(f"{nodos[i]:<12} | {valores}")


def floyd(nodos, aristas):
  n = len(nodos)
  idx = {nodo: i for i, nodo in enumerate(nodos)}

  # 1. Inicializar matriz de distancias y matriz de reconstrucción de rutas
  dist = [[0 if i == j else INF for j in range(n)] for i in range(n)]
  sig = [[None for _ in range(n)] for _ in range(n)]

  for u, v, peso in aristas:
    i, j = idx[u], idx[v]
    dist[i][j] = peso
    dist[j][i] = peso
    sig[i][j] = j
    sig[j][i] = i

  imprimir_matriz_costos(
      dist, nodos, "1. MATRIZ INICIAL DE COSTOS DIRECTOS (FLOYD)"
  )

  print("\n" + "=" * 66)
  print(" MEJORAS DESCUBIERTAS AL USAR NODOS INTERMEDIOS (k)")
  print("=" * 66)

  # 2. Triple ciclo de programación dinámica (k = intermedio, i = origen, j = destino)
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][k] + dist[k][j] < dist[i][j]:
          anterior = "∞" if dist[i][j] == INF else f"${dist[i][j]}"
          nuevo = dist[i][k] + dist[k][j]
          print(
              f" • Vía {nodos[k]:<8}: Ruta {nodos[i]} -> {nodos[j]} mejora de"
              f" {anterior} a ${nuevo}"
          )
          dist[i][j] = nuevo
          sig[i][j] = sig[i][k]

  imprimir_matriz_costos(
      dist, nodos, "2. MATRIZ FINAL DE COSTOS MÍNIMOS ENTRE TODOS LOS PARES"
  )
  return dist, sig


if __name__ == "__main__":
  estados = ["CDMX", "Puebla", "Veracruz", "Oaxaca", "Tabasco"]
  carreteras = [
      ("CDMX", "Puebla", 130),
      ("CDMX", "Veracruz", 420),
      ("Puebla", "Veracruz", 250),
      ("Puebla", "Oaxaca", 340),
      ("Veracruz", "Tabasco", 480),
      ("Oaxaca", "Tabasco", 650),
  ]

  floyd(estados, carreteras)

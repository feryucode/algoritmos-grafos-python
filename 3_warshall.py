def imprimir_matriz_booleana(matriz, nodos, titulo):
  print(f"\n{titulo}")
  print("-" * 62)
  encabezado = f"{'Nodo':<12} | " + " ".join(f"{n[:7]:>8}" for n in nodos)
  print(encabezado)
  print("-" * 62)
  for i, fila in enumerate(matriz):
    valores = " ".join(f"{val:>8}" for val in fila)
    print(f"{nodos[i]:<12} | {valores}")


def warshall(nodos, vuelos_dirigidos):
  n = len(nodos)
  idx = {nodo: i for i, nodo in enumerate(nodos)}

  # 1. Construir matriz booleana inicial (0 = sin ruta, 1 = conexión directa)
  clausura = [[0 for _ in range(n)] for _ in range(n)]
  for u, v in vuelos_dirigidos:
    clausura[idx[u]][idx[v]] = 1

  imprimir_matriz_booleana(
      clausura, nodos, "1. MATRIZ DE ADYACENCIA BOOLEANA INICIAL (WARSHALL)"
  )

  print("\n" + "=" * 62)
  print(" NUEVAS CONEXIONES INDIRECTAS DESCUBIERTAS (CLAUSURA TRANSITIVA)")
  print("=" * 62)

  # 2. Triple ciclo con álgebra booleana: W[i][j] = W[i][j] OR (W[i][k] AND W[k][j])
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if clausura[i][j] == 0 and (clausura[i][k] == 1 and clausura[k][j] == 1):
          clausura[i][j] = 1
          print(
              f" ✔ Camino descubierto: {nodos[i]:<9} ===> {nodos[j]:<9} (usando"
              f" puente en {nodos[k]})"
          )

  imprimir_matriz_booleana(
      clausura, nodos, "2. MATRIZ FINAL DE CLAUSURA TRANSITIVA (ALCANZABILIDAD)"
  )
  return clausura


if __name__ == "__main__":
  # Grafo dirigido (ejemplo: rutas aéreas de un solo sentido)
  estados = ["CDMX", "Puebla", "Veracruz", "Tabasco", "Yucatán"]
  vuelos = [
      ("CDMX", "Puebla"),
      ("Puebla", "Veracruz"),
      ("Veracruz", "Tabasco"),
      ("Tabasco", "Yucatán"),
  ]

  warshall(estados, vuelos)

def generar_cuadrado_espiral(n):
    matriz = [[0] * n for _ in range(n)]
    x, y, dx, dy = 0, 0, 1, 0
    
    for valor in range(1, n * n + 1):
        matriz[y][x] = valor
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and matriz[ny][nx] == 0:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    
    max_valor_length = len(str(n * n))
    for fila in matriz:
        print(" ".join(f"{x:>{max_valor_length}}" for x in fila))

tamaño = int(input("Ingrese el tamaño del cuadrado: "))
generar_cuadrado_espiral(tamaño)



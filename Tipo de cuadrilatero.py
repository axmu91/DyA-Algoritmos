def identificar_cuadrilatero(lados):
    # Ordenar los lados de menor a mayor
    lados_ordenados = sorted(lados)
    
    # Identificar el tipo de cuadrilátero
    if len(set(lados)) == 1:  # Si todos los lados son iguales, es un cuadrado
        return "Cuadrado"
    elif len(set(lados)) == 2:  # Si solo hay dos longitudes diferentes, es un rectángulo
        return "Rectángulo"
    elif lados_ordenados[0] == lados_ordenados[1] and lados_ordenados[2] == lados_ordenados[3]:  # Si tiene dos pares de lados iguales, es un rombo
        return "Rombo"
    else:  # En cualquier otro caso, es solo un cuadrilátero
        return "Cuadrilátero"


def main():
    print("Ingrese las medidas de los 4 lados del cuadrilátero:")
    lados = []
    for i in range(4):
        lado = float(input(f"Ingrese la medida del lado {i+1}: "))
        lados.append(lado)

    tipo_cuadrilatero = identificar_cuadrilatero(lados)
    print(f"El cuadrilátero ingresado es un {tipo_cuadrilatero}.")


if __name__ == "__main__":
    main()
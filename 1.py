# Rellenar una matriz de 4x4. Imprimirla en su orden y obtener e imprimir el producto y el promedio por cada fila de la matriz

matriz = [[0] * 4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input(f"Ingrese el numero en la posicionn ({i+1}, {j+1}): "))

print("Matriz:")
for fila in matriz:
    print(fila)

for fila in matriz:
    producto = 1
    for elemento in fila:
        producto *= elemento
    promedio = sum(fila) / len(fila)
    print(f"Producto {producto}, Promedio {promedio}")
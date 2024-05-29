# Crear una matriz de 10x10. Luego, pedir un entero y una posicion de la matriz al final deberan sustituir el entero en la posición nueva introducida. Visualizar la matriz resultante

matriz = [[0] * 10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input(f"Ingrese el numero en la posicionn ({i+1}, {j+1}): "))
        
print("Matriz:")
for fila in matriz:
    print(fila)
    
nuevo_numero = int(input("Ingrese un nuevo numero: "))
posicion = input("Ingrese la posicion en la matriz (fila,columna): ")
posicion = posicion.split(",")
fila = int(posicion[0]) - 1
columna = int(posicion[1]) - 1
matriz[fila][columna] = nuevo_numero

print("Matriz:")
for fila in matriz:
    print(fila)

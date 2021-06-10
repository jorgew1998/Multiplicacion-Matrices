fila1=int(input("Filas matriz 1: "))
colum1=int(input("Columnas matriz 1: "))
colum2=int(input("Columnas matriz 2: "))
print("")
print("Generando Matriz 1 vacia")
matrizA=[]
for a in range(fila1):
    matrizA.append([0]*colum1)
print("")
for a in range(fila1):
    print(matrizA[a])
print("")
print("Genrando Matriz 2 vacia")
matrizB=[]
for b in range(colum1):
    matrizB.append([0]*colum2)
print("")    
for a in range(colum1):
    print(matrizB[b])
print("")
print("Pidiendo datos matriz 1")
for i in range(fila1):
    for j in range(colum1):
        matrizA[i][j]=float(input("Introduzca componente (%d,%d): " % (i,j)))
print("")        
print("Pidiendo datos matriz 2")
for i in range(colum1):
    for j in range(colum2):
        matrizB[i][j]=float(input("Introduzca componente (%d,%d): " % (i,j)))
print("")    
print("Matriz 1:")
for a in range (fila1):
    print(matrizA[a])
print("")    
print("Matriz 2:")
for b in range (colum1):
    print(matrizB[b])
print("")
print("Generando matriz final vacia")
matrizC=[]
for i in range(fila1):
    matrizC.append([0]*colum2)
for i in range(fila1):
    print(matrizC[i])
print("")
for i in range(fila1):
    for j in range(colum2):
        for k in range(colum1):
            matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
print("Multiplicacion y visualizacion de matriz final")
for i in range(fila1):
    result=[]
    for j in range(colum2):
            result.append(matrizC[i][j])
    print(result)

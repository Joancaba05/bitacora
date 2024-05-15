import random
def Llenarvector(arreglo):
    for i in range(10):
        r = random.randint(1,100)
        """print("Ingrese un número: ")
        num = int(input())"""
        arreglo.append(r)
    return arreglo

def Promedio(arreglo):
    sumatoria = 0
    for valor in arreglo:
        sumatoria+= valor
    sumatoria = sumatoria/len(arreglo)
    return sumatoria

def Paresimpares(arreglo):
    sumapar = 0
    sumaimpar = 0
    for i in range(len(arreglo)):
        if i%2 == 0:
            sumapar+=arreglo[i]
        else:
            sumaimpar+=arreglo[i]
    print('La suma de las posiciones pares es de: ', sumapar)
    print('La suma de las posiciones impares es de: ', sumaimpar)

print("Semana 16: Ejercicio 1")
vector = []
vector = Llenarvector(vector)
print(vector)
print("El promedio es: ", Promedio(vector))
print('La longitud del vector es: ', len(vector))
Paresimpares(vector)

# Ejercicio #2
def ContarParImpar(matriz):
    par1 = 0
    impar1 = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] %2 == 0:
                par1+=1
            else:
                impar1+=1
    print('Cantidad de números pares es de: ', par1)
    print('Cantidad de números impares es de: ', impar1)

def Nummayormenor(matriz):
    may = 0
    men = 1001
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > may:
                may = matriz[i][j]
            if matriz[i][j] < men:
                men = matriz[i][j]
    print('El número mayor es: ', may)
    print('El número menor es: ', men)

print()
print("Semana 16: Ejercicio 2")
filas = int(input('Ingrese cantidad de filas: '))
columnas = int(input('Ingrese cantidad de columnas: '))
matriz = []
for a in range(filas):
    temp = []
    for e in range(columnas):
        r = random.randint(0,1001)
        temp.append(r)
    matriz.append(temp)
print(matriz)
ContarParImpar(matriz)
Nummayormenor(matriz)
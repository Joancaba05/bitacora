#Actividad No.1
import math
def Atriangulo(b,h):
    atria = (b*h)/2
    print(f'El área del triangulo es: {atria}')
    return atria

def Acuadrado(l):
    acua = l**2
    print(f'El área del cuadrado es: {acua}')
    return acua

def Arectangulo(b,h):
    arec = b*h
    print(f'El área del rectángulo es: {arec}')
    return arec

def Acirculo(r):
    acir = math.pi*(r**2)
    print('El área del círculo es:',"{0:.2f}".format(acir))
    return acir

#Actividad No.2
X = 0
Y = 0
def MoverHaciaArriba():
    global Y
    Y += 1

def MoverHaciaAbajo():
    global Y
    Y -= 1

def MoverHaciaLaDerecha():
    global X
    X += 1

def MoverHaciaIzquierda():
    global X
    X -= 1

ac = 1
while ac==1:
    print('Elija que actividad trabajar: ')
    print('1 - Actividad No.1')
    print('2 - Actividad No.2')
    print('3 - Salir del ciclo')
    menu = int(input('Opción '))
    if menu == 1:
        print("Semana No. 12: Ejercicio 1")
        ac1 = 1
        while ac1==1:
            print()
            print("Elija opción a calcular:")
            print("1 - Área de triángulo")
            print("2 - Área de cuadrado")
            print("3 - Área de rectángulo")
            print("4 - Área de círculo")
            print("5 - Salir del ciclo")
            menu1 =int(input("Opción:  "))
            if menu1 == 1: 
                print('Ingrese el valor de la base del triángulo:')
                b1 = int(input())
                print('Ingrese el valor de la altura del triángulo:')
                h1 = int(input())
                Atriangulo(b1,h1)
            elif menu1 == 2:
                print('Ingrese el valor del lado del cuadrado:')
                l1 = int(input())
                Acuadrado(l1)
            elif menu1 == 3:
                print('Ingrese el valor de la base del rectángulo:')
                b2 = int(input())
                print('Ingrese el valor de la altura del rectángulo:')
                h2 = int(input())
                Arectangulo(b2,h2)
            elif menu1 == 4:
                print('Ingrese el valor del radio del círculo:')
                r1 = int(input())
                Acirculo(r1)
            elif menu1 == 5: 
                menu = 0 
                ac1 = 0 
                print()      
            else:       
                print('Opción no definida, intente de nuevo')
                print()
        
    elif menu == 2:
        print("Semana No. 12: Ejercicio 2")
        ac2 = 1
        while ac2==1:
            print()
            print("Elija opción a calcular:")
            print("a - Sube")
            print("b - Baja")
            print("c - Izquierda")
            print("d - Derecha")
            print("e - Salir del ciclo")
            menu2 =input('Opción:').lower()
            if menu2 == 'a': 
                MoverHaciaArriba()
            elif menu2 == 'b':
                MoverHaciaAbajo()
            elif menu2 == 'c':
                MoverHaciaIzquierda()
            elif menu2 == 'd':
                MoverHaciaLaDerecha()
            elif menu2 == 'e': 
                menu = 0 
                ac2 = 0
                print(f'Corrdenadas finales del personaje: ({X},{Y})')   
                print()     
            else:       
                print('Opción no definida, intente de nuevo')
                print()

    elif menu == 0 and menu1==5 or menu == 0 and menu2=='e':
        menu = 0
    elif menu == 3:
        ac = 0
        print('Gracias por probar el código :)') 
    else:
        print('Opción no definida')
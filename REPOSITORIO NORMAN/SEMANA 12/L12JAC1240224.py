print ("Semana 12: Ejercicio 1")
print("a. Sumatoria ")
print ("b. Factorial ")
print("c. Tablas de multiplicar")
print("d. Números perfectos ")

opcion=input("Elija una opción a calcular: ")

match(opcion):
    case "a":
        N=0
        while N<=0:
            N=int(input("Ingrese un número entero positivo: "))
            if N<=0:
                print("El númerop ingresado debe ser entero positivo. ")
            sumatoria=0
            for cont in range (1,N+1):
                sumatoria+=cont 
            print ("La sumatoria es:" , sumatoria)
    
    
    case "b":
        N=0
        while N<=0:
            N=int(input("Ingrese un número entero positivo: "))
            if N<=0:
                print("El númerop ingresado debe ser entero positivo. ")
            factorial=1
            for cont in range (1,N+1):
                factorial*=cont 
                print("La factorial es: ", factorial)
    case "c":
        for i in range (1,11):
            for j in range (1,11):
                print (i*j, "\t" , end='')
            print()
    case "d":
        N=0
        while N<=0:
            N=int(input("Ingrese un número entero positivo: "))
            if N<=0:
                print("El númerop ingresado debe ser entero positivo. ")
            acumulador=0
            for factor in range (1,N):
                if N%factor==0:
                    acumulador+=factor
            if N== acumulador:
                print("Es perfecto")
            else:
                print("No es perfecto")

    case _:
        print("Elija una opción válida")



          
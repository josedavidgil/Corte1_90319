print("+---------------------------------------------------------------------------------------------------------+\n"
      "                                                MENÚ\n"
      " \n"
      "1. Números impares desde el 1 hasta su número.\n"
      "2. Factorial del número que ingrese.\n"
      "3. Indicar si su número es primo e indicar todos los números primos desde el 1 hasta su número.\n"
      "+---------------------------------------------------------------------------------------------------------+")
opc=int(input("Ingrese la opción que desea realizar: "))
if opc==1:
    n = int(input("Ingrese un número entero positivo: "))
    for i in range(1, n+1, 2):
        if i == 1:
            print(i, end="")
        else:
            print(",", i, end="")
elif opc==2:
    n= int(input("Ingrese un número entero positivo: "))
    f=1
    for i in range(1,n+1):
        f*=i
    print("El resultado es", f)
elif opc==3:
    n = int(input("Ingrese un número entero positivo: "))
    es_primo = True

    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num,end=",")

    if es_primo:
        print("El número ingresado es primo.")
    else:
        print("El número ingresado no es primo.")

else:
    print("Ingrese una opción válida.")
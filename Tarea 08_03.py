def Saludo():
    nombre = input("Ingrese su nombre: ")
    print("Hola " + nombre + "!")

Saludo() #Invocación




def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Ingrese el número total de elementos (n): "))
r = int(input("Ingrese el número de muestras sin orden (r): "))
comb = factorial(n) / (factorial(r) * factorial(n-r))

print("El número de combinaciones binomiales es:", comb)
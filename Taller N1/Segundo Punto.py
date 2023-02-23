#Realice un programa que calcule el índice de masa corporal de una persona, donde le solicite al usuario la estatura en cm y el peso en Kg. Después imprima como resultado el índice de masa corporal mediante un mensaje que diga “Su IMC es <valor>” redondeado con dos decimales.
stat=float(input("Ingrese su estatura en centímetros: "))
peso=float(input("Ingrese su peso en kilogramos: "))
imc=(peso)/((stat/100)**2)
print("Su IMC es", round(imc,2))
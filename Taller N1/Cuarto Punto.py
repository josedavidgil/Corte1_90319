#Realice un programa que permita calcular el costo anual del consumo de combustible de un vehículo, si el usuario ingresa la distancia recorrida (Km) anual, el consumo de combustible (L / 100Km) anual y el costo promedio anual del combustible por litros recorridos ($ / L)
d_rec=float(input("Ingrese la distancia recorrida anual en kilómetros (Km): "))
c_anual=float(input("Ingrese el consumo de combustible anual (L/100km): "))
c_prom=float(input("Ingrese el costo del combustible anual por litros recorridos ($/L): "))
print("El costo anual del consumo de combustible del vehículo es de:$",(d_rec/ 100)*c_anual*c_prom)
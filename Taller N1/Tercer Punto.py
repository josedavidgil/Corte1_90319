#Realice un programa donde se solicite al usuario escribir el precio final de un artículo o producto, con el que después calculará e imprimirá en pantalla el valor del IVA y el valor bruto (precio antes de IVA) del artículo o producto.
precio=float(input("Ingrese el precio final de un artículo o producto (sin puntos ni comas): "))
iva=(precio*19)/100
final=((precio*19)/100)+precio
print("Su artículo tiene un valor bruto de",precio,"$, y con el IVA del 19% (",iva,") su valor es de",final,"$")
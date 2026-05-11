#Ticket de tienda
#Declarar articulo e imprimir costo
art=input("Ingrese nombre del artículo deseado: ")
ct=int(input("Ingrese la cantidad de unidades de compra: "))
prc=float(input("Ingrese el precio por unidad del articulo de compra: "))
total= ct*prc
print("Usted compro",art,",unidades de",ct,".Total a pagar es:",total)
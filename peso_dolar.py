print("1.PESO A DOLAR")
print("2.DOLAR A PESO")
dolar = 18
opcion = int(input("Elige una opcion(1 o 2): "))
if opcion == 1:
    pesos = float(input("Ingresa la cantidad de pesos que desea convertir a dolar: "))
    dolares = pesos/dolar
    print("Tu conversion es de",dolares,"dolares")

elif opcion == 2:
    dolares = float(input("Ingresa la cantidad de dolares que desea convertir a pesos: "))
    pesos = dolares * dolar
    print("Tu conversion es de",pesos,"pesos")
else:
    print("OPCION INVALIDA")

#Ejercicio N°4 
# Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0
#item N°1

numero=int(input("Ingrese un numero: "))

if numero > 0:
    print(f"El numero {numero} es positivo")
elif numero == 0:
    print(f"El numero es 0")
else:
    print(f"El numero {numero} es negativo")

#item N°2 while
numero = int(input("Ingrese numero: "))
while numero < 3:
    numero += 1
    print(numero)

#item N°3 do-while

    while True:
        numero = int(input("Ingrese numero: "))
        numero += 1
        print(numero)


#bucle for

numero = 1

for numero in range(3):
    if numero < 3:
        numero += 1
        print(numero)
    elif numero >= 3:
        break



estacion = int(input("ingrese temperatura del dia: "))

if 22 >= estacion< 44:
    print("Estas en verano")
elif 16<=estacion< 22: 
     print("Estas en primavera")
elif 10<=estacion<16:
    print("Esta en otono")
elif -5==estacion<10:
    print("Estas en invierno")
else:
    print("temperatura invalidad para esta zona")

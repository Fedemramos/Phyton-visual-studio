"""
#Primera parte

def sumar_numeros(num1, num2, num3):
    return (num1 + num2 + num3)

resultado_suma = sumar_numeros(7,4,12)
print(resultado_suma)

#Segunda Parte

class coche:
    puertas = 4

    def cantidad_puertas(self, n):
       self.puertas = n
       print(f'El auto tiene: {self.puertas} puertas')

miCoche = coche()

miCoche.cantidad_puertas(4)
miCoche.cantidad_puertas(2)

"""
#ejercicio semana 22 
""""
numeros = (0,100)

for numero in range(100):
    if (numero %3 == 0) and (numero %5 == 0):
        print("fizzbuzz")
    elif numero %3 == 0:
        print ("fizz")
    elif numero %5 == 0:
        print("buzz")
    else:
        print(numero)
"""

# Hace un anagrama semama 23

""""
def anagrama(palabra, palabra2):
    if sorted(palabra) == sorted(palabra2):
        print("La palabra es un anagrama")
    else:
        print("no es un anagrama")

anagrama("amor","roma")
anagrama("delira","lidera")    

"""


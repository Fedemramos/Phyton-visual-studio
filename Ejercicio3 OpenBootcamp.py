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
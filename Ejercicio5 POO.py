# Para practicar la encapsulación:

# Crear clase Persona.
# Crear variables las privadas edad, nombre y telefono de la clase Persona.
# Crear gets y sets de cada propiedad.
# Crear un objeto persona en el main.
# Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola

class Persona:
    
    def __init__(self, nombre, edad, telefono):
        
        self.__nombre= nombre
        self.__edad = edad
        self.__telefono = telefono
#get
    def get_nombre(self):
        return (f'nombre: {self.__nombre}')

    def get_edad(self):
        return (f'edad: {self.__edad}')

    def get_telefono(self):
        return (f'numero de telefono: {self.__telefono}')

#set
    def set_telefono(self, telefono):
        self.__telefono = telefono
    
    def set_edad(self, edad):
        self.__edad = edad

ejemplo = Persona("Rodrigo", 28 , "xxx-0008-1000")

print(ejemplo.get_nombre())
print(ejemplo.get_edad())
ejemplo.set_edad(32)
print(ejemplo.get_edad())
print(ejemplo.get_telefono())







#Crea una clase Persona con las siguientes variables:
#La edad
#El nombre
#El teléfono

#Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable credito solo para esa clase.

#Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.

#Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo tenga la clase Trabajador.

class Persona:
    
    def __init__(self, nombre, edad, telefono):
        
        self.nombre= nombre
        self.edad = edad
        self.telefono = telefono

    def presentacion(self):
        print (f'mi nombre es {self.nombre}, tenmgo {self.edad} y mi telefono es {self.telefono}')

class Cliente(Persona):
    def __init__(self, nombre, edad, telefono, credito):
        super().__init__(nombre, edad, telefono)
        self.tucredito = credito

    def infocliente(self):
        print(f'Nombre: {self.nombre}, edad: {self.edad}, telefono: {self.telefono}')
        print(f'Tu credito es de: {self.tucredito}')

class Trabajador(Persona):
    def __init__(self, nombre, edad, telefono, salario):
        super().__init__(nombre, edad, telefono)
        self.tusalario = salario
    
    def infotrabajador(self):
        print(f'Nombre: {self.nombre}, edad: {self.edad}, telefono: {self.telefono}')
        print(f'Tu credito es de: {self.tusalario}')


usuario = Cliente("Rodrigo", 22, "xxx-3000-2800", 12000)
usuario2 = Persona("Julian", 21 , "xxx-2400-1231")

usuario.infocliente()
usuario2.presentacion()


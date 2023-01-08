from abc import ABC, abstractmethod
from clinica import Clinica
class persona(ABC):
    @abstractmethod
    def __init__(self, nombre,edad, cedula, telefono,direccion):
        self.nombre = nombre
        self.edad= edad
        self.cedula = cedula
        self.telefono = telefono
        self.direccion= direccion
    def mostrar_datos(self):
        print("Nombre:",self.nombre,"/", "Edad:",self.edad, "/", "Cedula:",self.cedula, "/", "Telefono:", self.telefono, "/", "Direccion:",self.direccion)

class mostrar_paciente(persona):
    def __init__(self, nombre, edad, cedula, telefono, direccion):
        super().__init__(nombre, edad, cedula, telefono, direccion)

class mostrar_enfermeros(persona):
    def __init__(self, nombre, edad, cedula, telefono, direccion):
        super().__init__(nombre, edad, cedula, telefono, direccion)

class mostrar_doctor(persona):
    def __init__(self, nombre, edad, cedula, telefono, direccion):
        super().__init__(nombre, edad, cedula, telefono, direccion)








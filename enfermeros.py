from persona import mostrar_enfermeros
class enfermero(mostrar_enfermeros):
    def __init__(self, nombre, edad, cedula, telefono, direccion, area,turno):
        super().__init__(nombre, edad, cedula, telefono, direccion)
        self.area = area
        self.turno = turno

    def mostrar_info(self):
        print("=/"*50)
        print("                   Enfermera")
        print("=/"*50)
        print("Enfermera:",self.nombre)
        print("Edad:",self.edad)
        print("Cedula:",self.cedula)
        print("Telefono:",self.telefono)
        print("Direccion:",self.direccion)
        print("Area:", self.area)
        print("Turno:", self.turno)
    
    def receta(self, medicamentos, dosis):
        receta = f"Tome {dosis} de {medicamentos} cada 8 horas"
        return receta

    def administrar_medicamentos(self, medicamentos, dosis):
        receta = self.receta(medicamentos, dosis)
        print("Administración:", receta)


enf = enfermero("Jennifer Muñoz",20, 987463698, 899654793, "Santiago", "Cuidados Intensivos", "Nocturno")
enf.mostrar_info()
enf.administrar_medicamentos("Aspirina", "500 mg")
from persona import mostrar_doctor
class doc(mostrar_doctor):
    def __init__(self, nombre, edad, cedula, telefono, direccion, area,turno):
        super().__init__(nombre, edad, cedula, telefono, direccion)
        self.area = area
        self.turno = turno

    def mostrar_info(self):
        print("=/"*50)
        print("                   Doctor")
        print("=/"*50)
        print("Doctor:",self.nombre)
        print("Edad:",self.edad)
        print("Cedula:",self.cedula)
        print("Telefono:",self.telefono)
        print("Direccion:",self.direccion)
        print("Especialidad:", self.area)
        print("Experiencia:", self.turno)
    
    def receta(self, medicamentos, dosis):
        receta = f"Recomienda tomar {dosis} de {medicamentos} cada 8 horas en caso de fiebre"
        return receta

    def diagnostico(self, medicamentos, dosis):
        receta = self.receta(medicamentos, dosis)
        print("Diagnostico:", receta)


doct = doc("Anderson Merchán",22, 984726066, 157794324, "Guayaquil", "Cardiologia", "5 años")
doct.mostrar_info()
doct.diagnostico("Aspirina", "500 mg")
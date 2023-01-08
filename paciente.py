from persona import mostrar_paciente
class paciente(mostrar_paciente):
    def __init__(self, nombre, edad, cedula, telefono, direccion):
        super().__init__(nombre, edad, cedula, telefono, direccion)

    def mostrar_info(self):
        print("=/"*30)
        print("                   Paciente")
        print("=/"*30)
        print("Paciente:",self.nombre)
        print("Edad:",self.edad)
        print("Cedula:",self.cedula)
        print("Telefono:",self.telefono)
        print("Direccion:",self.direccion)
    

paci = paciente("Dary Pincay",20, 987463698, 899654793, "Sauses")
paci.mostrar_info()





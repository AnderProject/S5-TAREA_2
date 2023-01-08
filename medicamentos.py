from clinica import Clinica
class Medicamento:
    def __init__(self, nombre, dosis, fabricante, fecha_vencimiento):
        self.nombre = nombre
        self.dosis = dosis
        self.fabricante = fabricante
        self.fecha_vencimiento = fecha_vencimiento

    def mostrar_informacion(self):
        print("Medicamentos")
        print("-"*50)
        print(f"Nombre: {self.nombre}")
        print(f"Dosis: {self.dosis}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Fecha de vencimiento: {self.fecha_vencimiento}")
    
    def actualizar_dosis(self, nueva_dosis):
        self.dosis = nueva_dosis
medicamento = Medicamento("Aspirina", "500 mg", "Bayer", "01/01/2023")
medicamento.mostrar_informacion()
medicamento.actualizar_dosis("1000 mg")

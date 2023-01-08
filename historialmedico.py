from persona import mostrar_paciente
class HistorialMedico(mostrar_paciente):
    def __init__(self, nombre,edad, cedula, telefono,direccion, numero_ficha, grupo_sangre, alergias, sintomas, antecedentes, citas):
        super().__init__(nombre, edad, cedula, telefono, direccion)
        self.numero_ficha = numero_ficha
        self.grupo_sangre = grupo_sangre
        self.alergias = alergias
        self.sintomas = sintomas
        self.antecedentes = antecedentes
        self.cita = citas

    def mostrar_informacion(self):
        print("                 HISTORIAL MEDICO")
        print("="*50)
        print("Nombre de Paciente:", self.nombre)
        print(f"Número de ficha: {self.numero_ficha}")
        print(f"Grupo de sangre: {self.grupo_sangre}")
        print(f"Alergias: {self.alergias}")
        print(f"Síntomas: {self.sintomas}")
        print(f"Antecedentes: {self.antecedentes}")
        print(f"Cita: {self.cita}")

    def agregar_alergia(self, alergia):
        self.alergias.append(alergia)

    def agregar_sintoma(self, sintoma):
        self.sintomas.append(sintoma)

    def agregar_antecedente(self, antecedente):
        self.antecedentes.append(antecedente)

    def agregar_cita(self, cita):
        self.cita.append(cita)

Historial = HistorialMedico("Dary Pincay", 21, 945896325, 912348596, "Guayaquil",789,"O Positivo",["penicilina"],["fiebre", "tos"],["gripe"],["01/01/2023"])
Historial.mostrar_informacion()
Historial.agregar_alergia("mariscos")
Historial.agregar_sintoma("dolor de cabeza")
Historial.agregar_antecedente("esguince de tobillo")
Historial.agregar_cita("01/02/2023")

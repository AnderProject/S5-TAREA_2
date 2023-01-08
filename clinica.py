class Clinica:
    def __init__(self, nombre="Clinica MedicPochita", telefono="055-555-555", ruc="123-456-789", direccion="Milagro"):
        self.nombre = nombre
        self.telefono = telefono
        self.ruc = ruc
        self.direccion = direccion


clin=Clinica()
if __name__ == '__main__':  
    print("=" * 50)
    print(" " * 15 + clin.nombre)
    print("=" * 50)
    print("Teléfono:", clin.telefono)
    print("RUC:", clin.ruc)
    print("Dirección:", clin.direccion)
    print("=" * 50)



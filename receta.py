from datetime import date
from clinica import Clinica
from persona import mostrar_doctor, mostrar_paciente

class medicamento:
    _secuencia=0
    def __init__(self,des,pre,sto):
        medicamento._secuencia += 1
        self.__codigo = medicamento._secuencia
        self.descripcion = des
        self.precio = pre
        self.stock = sto
    
    @property
    def codigo(self):
        return self.__codigo
        
    def mostrar_medicamento(self):
        print(self.codigo,self.descripcion)
        

class RecetaMedica:
    _linea=0
    def __init__(self,medicina,cantidad):
        RecetaMedica._linea += 1
        self.linea = RecetaMedica._linea
        self.medicina = medicina
        self.precio = medicina.precio
        self.cantidad = cantidad
        
class Consulta:
    _nroFicha=0
    _costoConsulta=12.00
    def __init__(self,paciente):
        Consulta._nroFicha = Consulta._nroFicha + 1
        self.ficha = "Nro "+str(Consulta._nroFicha)
        self.fecha = date.today()
        self.paciente = paciente
        self.subtotal = 0
        self.costoConsulta = 0
        self.total = 0
        self.detalleVenta = []

    
    def agregarDetalle(self,medicina,cantidad):
        detalle = RecetaMedica(medicina,cantidad)
        self.subtotal += round(detalle.precio*detalle.cantidad,2)
        self.costoConsulta = round(self.subtotal*Consulta._costoConsulta,2)
        self.total = round(self.subtotal+self._costoConsulta,2)
        self.detalleVenta.append(detalle)
    
    def mostrarConsulta(self,clinicanombre,clinicaruc):
        print("="*100)
        print("Clinica: {:17} Ruc:{}".format(clinicanombre,clinicaruc))    
        print("Ficha:{:11}Fecha:  {}".format(self.ficha,self.fecha))
        self.paciente.mostrar_datos()
        print("="*100)
        print("Lista de Medicinas                  Precio Cantidad Subtotal")
        for det in self.detalleVenta:
            print("{} {:35} {}  {:6}  {:7}".format(det.linea,det.medicina.descripcion,det.precio,det.cantidad,det.precio*det.cantidad))
        print("="*100)    
        print( "Diagnostico: administrarse 1 Aspirina de 500 mg cada 8 horas")
        print( "Diagnostico: administrarse 1 Paracetamol cada 8 horas")
        print( "Diagnostico: administrarse 1 Desloratadina cada 24 horas")
        print("="*100)
        print("                                                                         ","Subtotal => ",f"    $ {self.subtotal}")    
        print( "                                                                         ","Consulta =>", f"     $ {self.costoConsulta}")
        print( "                                                                         ","Total => ",  f"       $ {self.total} ")   

clinica = Clinica()
paciente = mostrar_paciente("Dary Pincay",20, 987463698, 899654793, "Sauses")      
medi1 = medicamento("Aspirina",3,100)
medi2 = medicamento("Paracetamol",1,200)
medi3 = medicamento("Umbral",1,300)
medi4 = medicamento("Desloratadina",2,100)
consu = Consulta(paciente)
consu.agregarDetalle(medi1,3)
consu.agregarDetalle(medi2,2)
consu.agregarDetalle(medi3,1)
consu.agregarDetalle(medi4,2)
consu.mostrarConsulta(clinica.nombre,clinica.ruc)

from modelo import Modelo
from vista import Vista

class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista(self)

    def crear_archivo(self, texto, nombre_archivo):
        datos = self.modelo.hacer_texto(texto)
        mensaje = self.modelo.crear_archivo(datos, nombre_archivo)
        return mensaje

    def leer_archivo(self, nombre_archivo):
        datos = self.modelo.leer_archivo(nombre_archivo)
        return datos

    def iniciar(self):
        self.vista.iniciar()

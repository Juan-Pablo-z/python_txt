import json

class Modelo:
    def hacer_texto(self, texto):
        return {"contenido": texto}

    def crear_archivo(self, datos, nombre_archivo):
        nombre_archivo += ".txt"
        with open(nombre_archivo, "w") as archivo_json:
            json.dump(datos, archivo_json)
            return "Documento creado..."

    def leer_archivo(self, nombre_archivo):
        nombre_archivo += ".txt"
        try:
            with open(nombre_archivo, "r") as archivo_json:
                datos = json.load(archivo_json)
                return datos
        except FileNotFoundError:
            return None
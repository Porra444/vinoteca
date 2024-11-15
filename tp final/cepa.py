from entidadvineria import EntidadVineria

class Cepa(EntidadVineria):
    def __init__(self, id, nombre: str):
        super().__init__(id, nombre)

    def obtenerVinos(self):
        from vinoteca import Vinoteca
        return Vinoteca.obtenerVinosPorCepa(self.id)
    
    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "vinos": [vino.obtenerNombre() + " (" + vino.obtenerBodega().obtenerNombre() + ")" for vino in self.obtenerVinos()]
        }

    def convertirAJSONFull(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "vinos": self.obtenerVinos()
        }
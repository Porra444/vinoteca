from entidadvineria import EntidadVineria

class Bodega(EntidadVineria):
    def __init__(self, id, nombre: str):
        super().__init__(id, nombre)

    def obtenerVinos(self):
        from vinoteca import Vinoteca
        return Vinoteca.obtenerVinos(self.id)
    
    def obtenerCepas(self):
        from vinoteca import Vinoteca 
        return list(Vinoteca.obtenerCepas())
    
    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cepas": [cepa.obtenerNombre() for cepa in self.obtenerCepas()],
            "vinos": [vino.obtenerNombre() for vino in self.obtenerVinos()]
        }
    
    def convertirAJSONFull(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cepas": self.obtenerCepas(),
            "vinos:": self.obtenerVinos()
        }
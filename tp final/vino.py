from entidadvineria import EntidadVineria

class Vino(EntidadVineria):
    def __init__(self, id, nombre: str, bodega: str, cepas: list, partidas: list):
        super().__init__(id, nombre)
        self.bodega = bodega
        self.cepas = cepas
        self.partidas = partidas

    def establecerBodega(self, bodega: str):
        self.bodega = bodega

    def establecerCepas(self, cepas: list):
        self.cepas = cepas

    def establecerPartidas(self, partidas: list):
        self.partidas = partidas

    def obtenerBodega(self):
        from vinoteca import Vinoteca
        return Vinoteca.buscarBodega(self.bodega)

    def obtenerCepas(self):
        from vinoteca import Vinoteca
        return [Vinoteca.buscarCepa(cepa) for cepa in self.cepas]

    def convertirAJSON(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "bodega": self.bodega,
            "cepas": self.cepas,
            "partidas": self.partidas
        }

    def convertirAJSONFull(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.obtenerCepas(),
            "partidas": self.partidas
        }

import json
from bodega import Bodega  
from cepa import Cepa  
from vino import Vino

class Vinoteca:
    archivoDeDatos = "vinoteca.json"
    bodegas = []
    cepas = []
    vinos = []

    @classmethod
    def inicializar(cls):
        data = cls.__parsearArchivoDeDatos()
        cls.__convertirJsonAListas(data)

    @classmethod
    def __parsearArchivoDeDatos(cls):
        with open(cls.archivoDeDatos, "r") as file:
            data = json.load(file)
        return data
    
    @classmethod
    def __convertirJsonAListas(cls, listas):
        cls.bodegas = [Bodega(**bodega) for bodega in listas.get('bodegas', [])]
        cls.cepas = [Cepa(**cepa) for cepa in listas.get('cepas', [])]
        cls.vinos = [Vino(**vino) for vino in listas.get('vinos', [])]

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso='no'):
        bodegas = cls.bodegas.copy()
        if orden:
            bodegas.sort(key=lambda x: getattr(x, orden), reverse=(reverso == 'si'))
        return bodegas ##add
    
    @classmethod
    def obtenerCepas(cls, orden=None, reverso='no'):
        cepas = cls.cepas.copy()
        if orden:
            cepas.sort(key=lambda x: getattr(x, orden), reverse=(reverso == 'si'))
        return cepas
    
    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso='no'):
        vinos = cls.vinos.copy()
        if anio is not None:
            vinos = [vino for vino in vinos if anio in vino.partidas]
        if orden:
            vinos.sort(key=lambda x: getattr(x, orden), reverse=(reverso == 'si'))
        return vinos
    
    @classmethod
    def buscarBodega(cls, id):
        for bodega in cls.bodegas:
            if bodega.obtenerID() == id:
                return bodega
        return None
    
    @classmethod
    def buscarCepa(cls, id):
        for cepa in cls.cepas:
            if cepa.obtenerID() == id:
                return cepa
        return None
    
    @classmethod
    def buscarVino(cls, id):
        for vino in cls.vinos:
            if vino.obtenerID() == id:
                return vino
        return None
    
    @classmethod
    def obtenerVinosPorBodega(cls, id_bodega):
        return [vino for vino in cls.vinos if vino.bodega == id_bodega]
    
    @classmethod
    def obtenerVinosPorCepa(cls, id_cepa):
        return [vino for vino in cls.vinos if id_cepa in vino.cepas]
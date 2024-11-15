from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    def __init__(self, id, nombre: str):
        self.id = id
        self.nombre = nombre

    def establecerNombre(self, nombre: str):
        self.nombre = nombre

    def obtenerID(self) -> str:
        return self.id
    
    def obtenerNombre(self) -> str:
        return self.nombre
    
    def __eq__(self, other):
        if isinstance(other, EntidadVineria):
            return self.id == other.id
        return False
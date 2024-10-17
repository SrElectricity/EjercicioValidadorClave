from abc import ABC, abstractclassmethod, abstractmethod
from typing import Protocol


class ReglaValidacion(ABC):

    def __init__(self, clave: str):
        self.clave: str = clave

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > 5

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)


class ReglaValidacionGanimedes(ReglaValidacion, ABC):
    pass


class ReglaValidacionCalisto(ReglaValidacion, ABC):
    pass


class Validador:
    def __init__(self, regla: ReglaValidacion):
        pass

    def _es_valida(self, clave: str) -> bool:
        pass

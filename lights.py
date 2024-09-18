from MathLib import *

class Luz:
    def __init__(self, intensidad=1.0, color=[1.0, 1.0, 1.0]):
        self.intensidad = intensidad
        self.color = color


class LuzDireccional(Luz):
    def __init__(self, direccion=[0, -1, 0], intensidad=1.0, color=[1.0, 1.0, 1.0]):
        super().__init__(intensidad, color)
        self.direccion = normalize_vector(direccion)

    def calcular_iluminacion(self, punto, normal):
        iluminacion = max(dot(self.direccion, normal), 0) * self.intensidad
        return [iluminacion * c for c in self.color]


class LuzPuntual(Luz):
    def __init__(self, posicion=[0, 0, 0], intensidad=1.0, color=[1.0, 1.0, 1.0]):
        super().__init__(intensidad, color)
        self.posicion = posicion

    def calcular_iluminacion(self, punto, normal):
        direccion_luz = restar_elementos(self.posicion, punto)
        direccion_luz = normalize_vector(direccion_luz)

        iluminacion = max(dot(direccion_luz, normal), 0) * self.intensidad
        return [iluminacion * c for c in self.color]


class LuzAmbiente(Luz):
    def __init__(self, intensidad=0.2, color=[1.0, 1.0, 1.0]):
        super().__init__(intensidad, color)

    def calcular_iluminacion(self):
        return [self.intensidad * c for c in self.color]


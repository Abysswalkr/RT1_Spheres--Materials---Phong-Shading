from Interception import Interception
from MathLib import restar_elementos, dot, suma_vectores, normalize_vector
from math import sqrt

class Figura:
    def __init__(self, posicion, material):
        self.posicion = posicion
        self.material = material

    def intersectar_rayo(self, origen, direccion):
        return None

class Esfera(Figura):
    def __init__(self, centro, radio, material):
        super().__init__(centro, material)
        self.radio = radio

    def intersectar_rayo(self, origen, direccion):
        L = restar_elementos(self.posicion, origen)
        tca = dot(L, direccion)
        magnitud_L2 = dot(L, L)

        d2 = magnitud_L2 - tca ** 2
        if d2 > self.radio ** 2:
            return None

        thc = sqrt(self.radio ** 2 - d2)

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None

        punto_interseccion = suma_vectores(origen, [direccion[i] * t0 for i in range(len(direccion))])

        normal_interseccion = normalize_vector(restar_elementos(punto_interseccion, self.posicion))

        return Interception(punto_interseccion, normal_interseccion, t0, self)


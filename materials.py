class Material:
    def __init__(self, color=[1.0, 1.0, 1.0], difuso=1.0, especular=0.5, reflectividad=0.5):
        self.color = color
        self.difuso = difuso
        self.especular = especular
        self.reflectividad = reflectividad

    def calcular_luz_difusa(self, intensidad_luz, angulo):
        return [self.color[i] * intensidad_luz * self.difuso * max(0, angulo) for i in range(3)]

    def calcular_luz_especular(self, intensidad_luz, angulo, brillo=32):
        return [intensidad_luz * self.especular * (max(0, angulo) ** brillo) for i in range(3)]

    def calcular_reflejo(self, color_reflejado, nivel_reflejo):
        return [self.color[i] * (1 - self.reflectividad) + color_reflejado[i] * self.reflectividad for i in range(3)]

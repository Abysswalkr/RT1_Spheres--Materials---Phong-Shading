# Snowman Raytracer

**Snowman Raytracer** es un proyecto de trazado de rayos desarrollado en Python que renderiza un muñeco de nieve 3D utilizando Pygame. El proyecto implementa un motor de trazado de rayos (Ray Tracing) básico, que calcula la intersección de rayos con objetos geométricos para generar una escena con iluminación, materiales y sombras.

![Muñeco de nieve renderizado](SnowMan.png)

## Características

- **Motor de Ray Tracing**: Implementación de un trazador de rayos que calcula la interacción de rayos con objetos en 3D.
- **Objetos 3D**: Renderización de esferas que forman el muñeco de nieve, incluyendo su cuerpo, ojos, nariz y botones.
- **Iluminación**: Se incluye iluminación direccional desde distintos ángulos, incluida luz proveniente desde abajo, con soporte para luz ambiental.
- **Materiales**: Se utilizan propiedades de materiales como color base, brillo y reflectividad para dar un acabado realista.
- **Fácil Ajuste**: Permite personalizar el tamaño y la posición de los elementos del muñeco de nieve, así como modificar la fuente de luz.
- **Soporte para Anti-Aliasing**: Mejora la nitidez y suavidad de los bordes para evitar efectos pixelados en la escena.

## Requisitos Previos

Necesitarás tener instalados **Python 3.x** y **Pygame** en tu sistema para ejecutar este proyecto.

## Instalación

1. Clona este repositorio y navega al directorio del proyecto:

    ```sh
    git clone https://github.com/tu-usuario/snowman-raytracer.git
    cd snowman-raytracer
    ```

2. Instala las dependencias necesarias:

    ```sh
    pip install pygame
    ```

## Uso

Para ejecutar el renderizador y ver el muñeco de nieve:

```sh
python Raytracer.py
```

Esto abrirá una ventana de Pygame en la que se renderizará el muñeco de nieve 3D con iluminación personalizada y efectos de sombreado.

## Estructura del Proyecto

- **Raytracer.py**: Componente principal que inicia el renderizado y configura la escena.
- **gl.py**: Implementa la lógica del trazador de rayos, la proyección, y la generación del framebuffer.
- **lights.py**: Define las fuentes de luz, incluida la luz direccional y la luz ambiental.
- **materials.py**: Maneja las propiedades de los materiales, como el color base, brillo y reflectividad.
- **figures.py**: Contiene las clases geométricas, como las esferas que representan las partes del muñeco de nieve.
- **camera.py**: Implementa la configuración de la cámara en la escena 3D.
- **MathLib.py**: Funciones matemáticas para vectores, normales, y cálculo de intersecciones de rayos.

## Personalización

Puedes modificar los siguientes aspectos del proyecto para personalizar la escena:

1. **Tamaño y Posición de los Botones y Ojos**: Ajusta el tamaño o posición de los botones y ojos modificando los valores de **radio** y **posición** en `Raytracer.py`.

2. **Iluminación**: Cambia la dirección, intensidad o color de las luces modificando los parámetros en `lights.py`. Ejemplo:
    ```python
    rt.lights.append(Sunlight(directionVector=[0, 1, 0], brightness=0.8))  # Luz desde abajo hacia arriba
    ```

3. **Resolución**: Mejora la nitidez aumentando la resolución de la ventana de Pygame. Ajusta los valores de `width` y `height` en `Raytracer.py`.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas agregar nuevas características o mejoras al trazador de rayos, por favor abre un **issue** o crea un **pull request**.

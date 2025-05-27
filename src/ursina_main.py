from ursina import *

app = Ursina()

# Crea una entidad tipo cubo
cube = Entity(
    model='cube',
    color=color.azure,
    scale=2,
    position=(0, 0, 0)
)

# Cámara básica libre
EditorCamera()

app.run()

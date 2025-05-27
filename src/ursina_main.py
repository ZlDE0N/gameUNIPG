from ursina import *
from pathlib import Path

app = Ursina()

# ✅ Ajustar carpeta base de assets
application.asset_folder = Path('assets')

# 🧍 Modelo del caballero
player = Entity(
    model='models/player/low_poly_knight.glb',
    scale=0.05,
    position=(0, 0, 0),
    color=color.white,
)

print('🟢 Modelo cargado:', player.model)

# 🔴 Esfera de referencia en el centro
marker = Entity(
    model='sphere',
    color=color.red,
    scale=0.1,
    position=(0, 0, 0)
)

# ✅ Suelo verde
ground = Entity(
    model='plane',
    scale=(20, 1, 20),
    color=color.green,
    position=(0, -1, 0),
    collider='box'
)

# 💡 Luz básica
DirectionalLight().look_at(Vec3(1, -1, -1))

# 🎥 Cámara libre con mouse
EditorCamera()

# 🔁 Animación de rotación para verificar modelo
def update():
    player.rotation_y += time.dt * 30

app.run()
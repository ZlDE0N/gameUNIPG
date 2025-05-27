from ursina import *
from pathlib import Path

app = Ursina()

# ✅ Ajustar carpeta base de assets
application.asset_folder = Path('assets')

# Estado del juego
player_speed = 3

# 🧍 Modelo del caballero (jugador)
player = Entity(
    model='models/player/low_poly_knight.glb',
    scale=0.05,
    position=(0, 0, 0),
    color=color.white,
    collider='box'
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

# 💡 Luz direccional
DirectionalLight().look_at(Vec3(1, -1, -1))

# 🎥 Cámara libre con mouse
EditorCamera()

# 🔁 Lógica de movimiento por frame
def update():
    # Movimiento básico con WASD
    direction = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['s'] - held_keys['w']
    ).normalized()
    
    player.position += direction * time.dt * player_speed

    # Rotación animada (opcional)
    # player.rotation_y += time.dt * 30

app.run()
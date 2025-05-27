from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from model_loader import load_model, draw_model

class Player:
    def __init__(self):
        self.position = [0, 0, 0]
        self.speed = 0.2
        self.model = load_model("assets/models/player/low_poly_knight.glb")

    def draw(self):
        # Cubo rojo de prueba
        glPushMatrix()
        glTranslatef(0, 0, 0)
        glColor3f(1.0, 0.0, 0.0)
        glutSolidCube(2)
        glPopMatrix()

        # Modelo real cargado
        glPushMatrix()
        glTranslatef(self.position[0], self.position[1], self.position[2])
        glScalef(1.0, 1.0, 1.0)  # escala grande para ver el modelo
        glRotatef(-90, 1, 0, 0)
        glColor3f(0.6, 0.6, 1.0)
        draw_model(self.model)
        glPopMatrix()

    def update(self, keys):
        if keys[K_w]: self.position[2] -= self.speed
        if keys[K_s]: self.position[2] += self.speed
        if keys[K_a]: self.position[0] -= self.speed
        if keys[K_d]: self.position[0] += self.speed

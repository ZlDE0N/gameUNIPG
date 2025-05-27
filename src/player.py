from OpenGL.GL import *
from pygame.locals import *
from OpenGL.GLUT import glutSolidCube  # ✅ ESTA LÍNEA ES CLAVE


class Player:
    def __init__(self):
        self.position = [0, 0, 0]
        self.speed = 0.2

    def draw(self):
        x, y, z = self.position
        glPushMatrix()
        glTranslatef(x, y + 0.5, z)
        glColor3f(0.6, 0.3, 0.1)  # marrón simple
        glutSolidCube(1)
        glPopMatrix()

    def update(self, keys):
        if keys[K_w]: self.position[2] -= self.speed
        if keys[K_s]: self.position[2] += self.speed
        if keys[K_a]: self.position[0] -= self.speed
        if keys[K_d]: self.position[0] += self.speed

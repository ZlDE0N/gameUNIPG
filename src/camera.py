from OpenGL.GLU import *

class Camera:
    def __init__(self):
        pass

    def update(self, target_pos):
        gluLookAt(0, 5, 10,
                  0, 0, 0,
                  0, 1, 0)

    def handle_mouse(self):
        pass  # desactivado por ahora

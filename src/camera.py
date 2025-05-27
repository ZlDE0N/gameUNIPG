# src/camera.py
import pygame
import math
from OpenGL.GLU import *

class Camera:
    def __init__(self):
        self.distance = 10
        self.angle_x = 0
        self.angle_y = 30
        self.mouse_sensitivity = 0.3
        self.last_mouse_pos = None

    def update(self, target_pos):
        x_offset = self.distance * math.sin(math.radians(self.angle_x))
        z_offset = self.distance * math.cos(math.radians(self.angle_x))
        y_offset = self.distance * math.sin(math.radians(self.angle_y))

        eye_x = target_pos[0] + x_offset
        eye_y = target_pos[1] + y_offset
        eye_z = target_pos[2] + z_offset

        gluLookAt(eye_x, eye_y, eye_z,
                  target_pos[0], target_pos[1], target_pos[2],
                  0, 1, 0)

    def handle_mouse(self):
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:  # botón izquierdo presionado
            x, y = pygame.mouse.get_pos()
            if self.last_mouse_pos:
                dx = x - self.last_mouse_pos[0]
                dy = y - self.last_mouse_pos[1]
                self.angle_x += dx * self.mouse_sensitivity
                self.angle_y -= dy * self.mouse_sensitivity
                self.angle_y = max(5, min(80, self.angle_y))
            self.last_mouse_pos = (x, y)
        else:
            self.last_mouse_pos = None

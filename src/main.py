import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from camera import Camera
from player import Player

def draw_ground():
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.8, 0.5)
    glVertex3f(-20, 0, -20)
    glVertex3f( 20, 0, -20)
    glVertex3f( 20, 0,  20)
    glVertex3f(-20, 0,  20)
    glEnd()

def main():
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Legado de la Espada")
    glutInit()

    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glEnable(GL_DEPTH_TEST)
    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    clock = pygame.time.Clock()
    camera = Camera()
    player = Player()

    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or keys[K_ESCAPE]:
                running = False

        player.update(keys)
        camera.handle_mouse()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        camera.update(player.position)

        draw_ground()
        player.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

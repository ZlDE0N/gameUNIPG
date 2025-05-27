import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_ground():
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.8, 0.5)  # verde claro
    glVertex3f(-10, 0, -10)
    glVertex3f( 10, 0, -10)
    glVertex3f( 10, 0,  10)
    glVertex3f(-10, 0,  10)
    glEnd()

def main():
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Legado de la Espada")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glEnable(GL_DEPTH_TEST)
    glTranslatef(0.0, -1.5, -10)  # Aleja la cámara hacia atrás

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_ground()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

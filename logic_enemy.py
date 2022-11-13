from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x_enemy = -50
move = 1

def enemy():
    global x_enemy, move

    glPushMatrix()
    glColor3ub(255,255,255)

    if x_enemy>=150:
        move = -1
    elif x_enemy<-50:
        move = 1
    x_enemy = x_enemy+move
    glTranslated(x_enemy,0,0)

    glBegin(GL_POLYGON)
    glVertex2f(100, 50)
    glVertex2f(100, 100)
    glVertex2f(150, 100)
    glVertex2f(150, 50)
    glEnd()

    glPopMatrix()

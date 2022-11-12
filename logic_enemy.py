from win32api import GetSystemMetrics
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rn

w,h = 800,600
w_position,h_position = (GetSystemMetrics(0)/2)-(w/2), (GetSystemMetrics(1)/2)-(h/2)

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

        
    print(x_enemy)

    glBegin(GL_POLYGON)
    glVertex2f(100, 50)
    glVertex2f(100, 100)
    glVertex2f(150, 100)
    glVertex2f(150, 50)
    glEnd()

    glPopMatrix()



import ctypes
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h=1200,750
w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)

def map1():
    glScaled(.9,.9,0)
    glTranslated(0, 50, 0)
#kotak luar
    glColor3ub(240,25,10)
    glBegin(GL_POLYGON)
    glVertex2f(-350, -400)
    glVertex2f(-350, 300)
    glVertex2f(-350, 300)
    glVertex2f(350, 300)
    glVertex2f(350, 300)
    glVertex2f(350, -400)
    glVertex2f(350, -400)
    glVertex2f(-350, -400)
    glEnd()
#kotak dalam
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(-300, -350)
    glVertex2f(-300, 250)
    glVertex2f(-300, 250)
    glVertex2f(300, 250)
    glVertex2f(300, 250)
    glVertex2f(300, -350)
    glVertex2f(300, -350)
    glVertex2f(-300, -350)
    glEnd()
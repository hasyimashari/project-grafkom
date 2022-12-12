import ctypes
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def map4():
#kotak luar
    glColor3ub(250,0,0)
    glBegin(GL_POLYGON)
    # glBegin(GL_LINES)
    glVertex2f(-550, 300)
    glVertex2f(-550, -300)
    glVertex2f(-550, -300)
    glVertex2f(550, -300)
    glVertex2f(550, -300)
    glVertex2f(550, 300)
    glVertex2f(550, 300)
    glVertex2f(-550, 300)
    glEnd()

#kotak dalam horizontal
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    # glBegin(GL_LINES)
    glVertex2f(-500, 80)
    glVertex2f(-500, -80)
    glVertex2f(-500, -80)
    glVertex2f(500, -80)
    glVertex2f(500, -80)
    glVertex2f(500, 80)
    glVertex2f(500, 80)
    glVertex2f(-500, 80)
    glEnd()

#kotak dalam 1
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    # glBegin(GL_LINES)
    glVertex2f(-500, 250)
    glVertex2f(-500, -250)
    glVertex2f(-500, -250)
    glVertex2f(-300, -250)
    glVertex2f(-300, -250)
    glVertex2f(-300, 250)
    glVertex2f(-300, 250)
    glVertex2f(-500, 250)
    glEnd()

#kotak dalam 2
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    # glBegin(GL_LINES)
    glVertex2f(-200, 250)
    glVertex2f(-200, -250)
    glVertex2f(-200, -250)
    glVertex2f(-50, -250)
    glVertex2f(-50, -250)
    glVertex2f(-50, 250)
    glVertex2f(-50, 250)
    glVertex2f(-200, 250)
    glEnd()

#kotak dalam 3
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    # glBegin(GL_LINES)
    glVertex2f(50, 250)
    glVertex2f(50, -250)
    glVertex2f(50, -250)
    glVertex2f(200, -250)
    glVertex2f(200, -250)
    glVertex2f(200, 250)
    glVertex2f(200, 250)
    glVertex2f(50, 250)
    glEnd()

#kotak dalam 4
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    # glBegin(GL_LINES)
    glVertex2f(300, 250)
    glVertex2f(300, -250)
    glVertex2f(300, -250)
    glVertex2f(500, -250)
    glVertex2f(500, -250)
    glVertex2f(500, 250)
    glVertex2f(500, 250)
    glVertex2f(300, 250)
    glEnd()

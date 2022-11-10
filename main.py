from win32api import GetSystemMetrics
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rn

w,h = 800,600
w_position,h_position = (GetSystemMetrics(0)/2)-(w/2), (GetSystemMetrics(1)/2)-(h/2)

def linePos():
    glColor3ub(255,255,255)
    glBegin(GL_LINES)
    glVertex2f(w, 0)
    glVertex2f(-w, 0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0,h)
    glVertex2f(0,-h)
    glEnd()

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-(w/2), w/2, -(h/2), h/2, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    linePos()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(int(w_position), int(h_position))
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
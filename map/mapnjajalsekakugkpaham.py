import ctypes
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h=800,600

def map1():

    glColor3ub(240,25,10)
    glBegin(GL_POLYGON)
    glVertex2f(-500, -700)
    glVertex2f(-500, 600)
    glVertex2f(-500, 600)
    glVertex2f(400, 600)
    glVertex2f(400, 600)
    glVertex2f(400, -700)
    glVertex2f(400, -700)
    glVertex2f(-500, -700)
    glEnd()

    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(-300, -500)
    glVertex2f(-300, 400)
    glVertex2f(-300, 400)
    glVertex2f(200, 400)
    glVertex2f(200, 400)
    glVertex2f(200, -500)
    glVertex2f(200, -500)
    glVertex2f(-300, -500)
    glEnd()
    
def iterate():
    glViewport(0, 0, 800, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-800, 800, -600, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    map1()
    glutSwapBuffers()
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 600)
glutInitWindowPosition(0,0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

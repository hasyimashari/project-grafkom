from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h=2000,2000

def modelatas():
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(111, 261)
    glVertex2f(170, 200)
    glVertex2f(220, 240)
    glVertex2f(235, 263)
    glVertex2f(238, 284)
    glVertex2f(234, 302)
    glVertex2f(220, 314)
    glVertex2f(202, 315)
    glVertex2f(181, 312)
    glVertex2f(160, 300)
    glEnd()

    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(172, 288)
    glVertex2f(170, 282)
    glVertex2f(149, 268)
    glVertex2f(123, 248)
    glVertex2f(116, 255)
    glVertex2f(144, 275)
    glVertex2f(166, 290)
    glEnd()

def modelbawah():
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(111, 261)
    glVertex2f(170, 200)
    glVertex2f(120, 160)
    glVertex2f(102, 148)
    glVertex2f(77, 136)
    glVertex2f(52, 135)
    glVertex2f(36, 144)
    glVertex2f(31, 161)
    glVertex2f(34, 182)
    glVertex2f(44, 203)
    glVertex2f(60, 220)
    glEnd()
    
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1000, 1000, -1000, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    modelatas()
    modelbawah()
    glutSwapBuffers()
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0,0)
wind = glutCreateWindow("Player rek")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

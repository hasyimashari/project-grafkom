import ctypes
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h=2000,2000
# w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)

def modelatas():
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(111, 261)
    glVertex2f(170, 200)
    glVertex2f(170, 200)
    glVertex2f(220, 240)
    glVertex2f(240, 280)
    glVertex2f(240, 300)
    glVertex2f(220, 320)
    glVertex2f(200, 320)
    glVertex2f(160, 300)

    

    
    glEnd()

def modelbawah():
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(111, 261)
    glVertex2f(170, 200)
    glVertex2f(120, 160)
    glVertex2f(80, 140)
    glVertex2f(60, 140)
    glVertex2f(40, 160)
    glVertex2f(40, 180)
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

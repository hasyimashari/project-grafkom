import ctypes
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h=2000,2000
# w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)

def player():
    glColor3ub(0, 255, 0)
    glBegin(GL_POLYGON)
    glVertex2f(300, 100)
    glVertex2f(100, 200)
    glVertex2f(0, 300)
    glVertex2f(0, 500)
    glVertex2f(100, 600)
    glVertex2f(300, 700)
    glVertex2f(500, 700)
    glVertex2f(700, 600)
    glVertex2f(800, 500)
    glVertex2f(800, 300)
    glVertex2f(700, 200)
    glVertex2f(500, 100)
    

    
    glEnd()

def matakiri():
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(250,550)
    glVertex2f(200,500)
    glVertex2f(200,400)
    glVertex2f(250,350)
    glVertex2f(300,350)
    glVertex2f(350,400)
    glVertex2f(350,500)
    glVertex2f(300,550)
    
    glEnd()
def matakanan():
    glColor3ub(255,255,255)
    glBegin(GL_POLYGON)
    glVertex2f(500,550)
    glVertex2f(450,500)
    glVertex2f(450,400)
    glVertex2f(500,350)
    glVertex2f(550,350)
    glVertex2f(600,400)
    glVertex2f(600,500)
    glVertex2f(550,550)
    
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
    player()
    matakiri()
    matakanan()
    glutSwapBuffers()
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0,0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

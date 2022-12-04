import ctypes
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h=1200,800
w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)

def map1():

#kotak luar
    glColor3ub(250,0,0)
    glBegin(GL_POLYGON)
    # glBegin(GL_LINES)
    glVertex2f(-200, -150)
    glVertex2f(-550, -150)
    glVertex2f(-550, -150)
    glVertex2f(-550, 350)
    glVertex2f(-550, 350)
    glVertex2f(550, 350)
    glVertex2f(550, 350)
    glVertex2f(550, -150)
    glVertex2f(550, -150)
    glVertex2f(200, -150)
    glVertex2f(200, -150)
    glVertex2f(200, -350)
    glVertex2f(200, -350)
    glVertex2f(-200, -350)
    glVertex2f(-200, -350)
    glVertex2f(-200, -150)
    glEnd()

# kotak dalam
    glColor3ub(0,0,0)
    glBegin(GL_POLYGON)
    # glBegin(GL_LINES)
    glVertex2f(-150, -100)
    glVertex2f(-500, -100)
    glVertex2f(-500, -100)
    glVertex2f(-500, 300)
    glVertex2f(-500, 300)
    glVertex2f(500, 300)
    glVertex2f(500, 300)
    glVertex2f(500, -100)
    glVertex2f(500, -100)
    glVertex2f(150, -100)
    glVertex2f(150, -100)
    glVertex2f(150, -300)
    glVertex2f(150, -300)
    glVertex2f(-150, -300)
    glVertex2f(-150, -300)
    glVertex2f(-150, -100)
    glVertex2f(-150, -300)
    glVertex2f(-150, -100)
    glEnd()

# kotak dalam kiri
    glColor3ub(250,0,0)
    glBegin(GL_POLYGON)
    # glBegin(GL_LINES)
    glVertex2f(-200, 300)
    glVertex2f(-200, 100)
    glVertex2f(-200, 100)
    glVertex2f(-150, 100)
    glVertex2f(-150, 100)
    glVertex2f(-150, 300)
    glVertex2f(-150, 300)
    glVertex2f(-200, 300)
    glEnd()

# kotak dalam kanan
    glColor3ub(250,0,0)
    glBegin(GL_POLYGON)
    # glBegin(GL_LINES)
    glVertex2f(150, 300)
    glVertex2f(150, 100)
    glVertex2f(150, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 300)
    glVertex2f(200, 300)
    glVertex2f(150, 300)
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
    glColor3f(1.0, 0.0, 3.0)
    map1()
    glutSwapBuffers()
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(int(w_position), int(h_position))
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
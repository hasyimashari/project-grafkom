from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h=500,500

def player():
    glColor3ub(0, 255, 0)
    glBegin(GL_POLYGON)
    glVertex2f(200, 100)
    glVertex2f(100, 200)
    
    glVertex2f(100, 200)
    glVertex2f(100, 300)

    glVertex2f(100, 300)
    glVertex2f(200, 400)
    
    glVertex2f(200, 400)
    glVertex2f(300, 400)
    
    glVertex2f(300, 400)
    glVertex2f(400, 300)
    
    glVertex2f(400, 300)
    glVertex2f(400, 200)
    
    glVertex2f(400, 200)
    glVertex2f(300, 100)
    
    glVertex2f(300, 100)
    glVertex2f(200, 100)
    
    glEnd()
    
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-500, 500, -500, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    player()
    glutSwapBuffers()
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

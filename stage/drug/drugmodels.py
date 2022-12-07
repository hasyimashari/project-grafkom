from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h=2000,2000

def modelkanan():
    glColor3ub(255, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(55,20)
    glVertex2f(55,80)
    glVertex2f(70,80)
    glVertex2f(90,70)
    glVertex2f(100,60)
    glVertex2f(100,40)
    glVertex2f(90,30)
    glVertex2f(70,20)
    glEnd()
    
def letter():
    glPushMatrix()
    glColor3ub(0, 0, 0)
    glRasterPos2f(25,30)
    t=":D"
    for i in t:
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13,ord(i))
    glPopMatrix()
    

def modelkiri():
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(55,20)
    glVertex2f(55,80)
    glVertex2f(40,80)
    glVertex2f(20,70)
    glVertex2f(10,60)
    glVertex2f(10,40)
    glVertex2f(20,30)
    glVertex2f(40,20)

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
    modelkanan()
    modelkiri()
    letter()
    glutSwapBuffers()
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0,0)
wind = glutCreateWindow("Player rek")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()

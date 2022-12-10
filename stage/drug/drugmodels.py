from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h=2000,2000

def modelkanan():
    glScaled(.5,.5,0)
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


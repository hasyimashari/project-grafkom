from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h=2000,2000
#titik tengah 200,250
def Entity():
    glScaled(.1,.1,0)
    glColor3ub(175,0,0)
    glLineWidth(4)
    glBegin(GL_LINE_LOOP)
    glVertex2f(200, 300)
    glVertex2f(100, 400)
    glVertex2f(200, 350)
    glVertex2f(100, 600)
    glVertex2f(250, 400)
    glVertex2f(300, 500)
    glVertex2f(350, 400)
    glVertex2f(450, 600)
    glVertex2f(400, 350)
    glVertex2f(500, 400)
    glVertex2f(400, 300)
    glVertex2f(500, 100)
    glVertex2f(350, 200)
    glVertex2f(300, 100)
    glVertex2f(250, 200)
    glVertex2f(100, 100)
    glVertex2f(200, 300)
    glEnd()

    glColor3ub(232,14,14)
    glBegin(GL_TRIANGLES)
    glVertex2f(200, 300)
    glVertex2f(100, 400)
    glVertex2f(200, 350)

    glVertex2f(200, 350)
    glVertex2f(100, 600)
    glVertex2f(250, 400)

    glVertex2f(250, 400)
    glVertex2f(300, 500)
    glVertex2f(350, 400)

    glVertex2f(350, 400)
    glVertex2f(450, 600)
    glVertex2f(400, 350)

    glVertex2f(400, 350)
    glVertex2f(500, 400)
    glVertex2f(400, 300)

    glVertex2f(400, 300)
    glVertex2f(500, 100)
    glVertex2f(350, 200)

    glVertex2f(350, 200)
    glVertex2f(300, 100)
    glVertex2f(250, 200)

    glVertex2f(250, 200)
    glVertex2f(100, 100)
    glVertex2f(200, 300)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(200, 300)
    glVertex2f(200, 350)
    glVertex2f(200, 350)
    glVertex2f(250, 400)
    glVertex2f(250, 400)
    glVertex2f(350, 400)
    glVertex2f(350, 400)
    glVertex2f(400, 350)
    glVertex2f(400, 350)
    glVertex2f(400, 300)
    glVertex2f(400, 300)
    glVertex2f(350, 200)
    glVertex2f(350, 200)
    glVertex2f(250, 200)
    glVertex2f(250, 200)
    glVertex2f(200, 300)
    glEnd()
    
def mulut():
    glColor3ub(175,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(300,380)
    glVertex2f(350,350)
    glVertex2f(380,310)
    glVertex2f(350,250)
    glVertex2f(300,270)
    glVertex2f(250,250)
    glVertex2f(220,310)
    glVertex2f(250,350)
    glEnd()
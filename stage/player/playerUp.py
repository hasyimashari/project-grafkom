from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def player():
    glScaled(.1,.1,0)
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

    glColor3ub(30, 176, 30)
    glLineWidth(4)
    glBegin(GL_LINE_LOOP)
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

def lubang():
    glColor3ub(30, 176, 30)
    glBegin(GL_POLYGON)
    glVertex2f(73, 323)
    glVertex2f(66, 296)
    glVertex2f(87, 280)
    glVertex2f(110, 292)
    glVertex2f(107, 321)
    glVertex2f(91, 337)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(656, 290)
    glVertex2f(635, 269)
    glVertex2f(631, 237)
    glVertex2f(653, 227)
    glVertex2f(674, 244)
    glVertex2f(675, 271)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(194, 611)
    glVertex2f(173, 594)
    glVertex2f(174, 570)
    glVertex2f(195, 560)
    glVertex2f(216, 580)
    glVertex2f(216, 607)
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
    
def pusatmatakanan():
    glBegin(GL_POLYGON)
    glColor3ub(0,100,168)
    glVertex2f(500,550)
    glVertex2f(550,550)
    glVertex2f(550,450)
    glVertex2f(500,450)
    glEnd()

def pusatmatakiri():
    glBegin(GL_POLYGON)
    glColor3ub(0,100,168)
    glVertex2f(250,550)
    glVertex2f(300,550)
    glVertex2f(300,450)
    glVertex2f(250,450)
    glEnd()

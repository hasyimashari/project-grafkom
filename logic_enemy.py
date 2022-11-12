from win32api import GetSystemMetrics
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rn

w,h = 800,600
w_position,h_position = (GetSystemMetrics(0)/2)-(w/2), (GetSystemMetrics(1)/2)-(h/2)


def linePos():
    glColor3ub(255,255,255)
    glBegin(GL_LINES)
    glVertex2f(w, 0)
    glVertex2f(-w, 0)
    glVertex2f(0,h)
    glVertex2f(0,-h)
    glEnd()

geser = 0

def enemy():
    global geser

    glPushMatrix()
    glColor3ub(255,255,255)

    if geser>=248:
        geser=0
    else:
        geser+=1
    glTranslated(geser,0,0)

        
    print(geser)

    glBegin(GL_POLYGON)
    glVertex2f(100, 50)
    glVertex2f(100, 100)
    glVertex2f(150, 100)
    glVertex2f(150, 50)
    glEnd()

    glPopMatrix()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-(w/2), w/2, -(h/2), h/2, 0.0, 1.0)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    linePos()
    enemy()
    glFlush()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(50,update,0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(int(w_position), int(h_position))
    glutCreateWindow("Project Pacman Wannabe")
    glutDisplayFunc(showScreen)
    glutTimerFunc(10,update,0)
    init()
    glutMainLoop()

if __name__ == '__main__':
    main()
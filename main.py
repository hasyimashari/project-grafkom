from win32api import GetSystemMetrics
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rn
from logic_enemy import *

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

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-(w/2), w/2, -(h/2), h/2, 0.0, 1.0)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    linePos()
    enemy()
    glFlush()

def update(value):
    glutReshapeWindow(w,h)
    glutPositionWindow(int(w_position), int(h_position))
    glutPostRedisplay()
    glutTimerFunc(25,update,0)

# sementara
def resize_window(button, state, x,y):
    global w, h, w_position, h_position
    if button == GLUT_LEFT_BUTTON:
        w,h = 600,450
        w_position,h_position = (GetSystemMetrics(0)/2)-(w/2), (GetSystemMetrics(1)/2)-(h/2)
    elif button == GLUT_RIGHT_BUTTON:
        w,h = 800,600
        w_position,h_position = (GetSystemMetrics(0)/2)-(w/2), (GetSystemMetrics(1)/2)-(h/2)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(int(w_position), int(h_position))
    glutCreateWindow("Project Pacman Wannabe")
    glutDisplayFunc(showScreen)
    glutMouseFunc(resize_window)
    glutTimerFunc(10,update,0)
    init()
    glutMainLoop()

if __name__ == '__main__':
    main()
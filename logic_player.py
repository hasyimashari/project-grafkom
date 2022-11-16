from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

x_player = -150 #-100 sama dengan titik 0 x
y_player = 0    #-100 sama dengan titik 0 y
x_move = 0
y_move = 0

def player():
    global x_player, y_player, x_move, y_move
    w,h = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)

    glPushMatrix()
    glColor3ub(255,255,255)

    x_player = x_player+x_move
    y_player = y_player+y_move

    print(-(w/2)-95, x_player, "+", x_move, w/2-155, "|", -(h/2)-45, y_player, "+", y_move, h/2-105)
    
    if -(w/2)-95>x_player or x_player>w/2-155:
        x_move = 0
    if  -(h/2)-45>y_player or y_player>h/2-105:
        y_move = 0

    glTranslated(x_player+x_move,y_player+y_move,0)

    glBegin(GL_POLYGON)
    glVertex2f(100, 50)
    glVertex2f(100, 100)
    glVertex2f(150, 100)
    glVertex2f(150, 50)
    glEnd()

    glPopMatrix()

def input_keyboard_player(key,x,y):
    global x_player, y_player, x_move, y_move
    if key == GLUT_KEY_UP:
        x_move = 0
        y_move = 2
    elif key == GLUT_KEY_DOWN:
        x_move = 0
        y_move = -2
    elif key == GLUT_KEY_RIGHT:
        x_move = 2
        y_move = 0
    elif key == GLUT_KEY_LEFT:
        x_move = -2
        y_move = 0
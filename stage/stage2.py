import ctypes
import sys
sys.dont_write_bytecode = True
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import logic_player as lp
import logic_entity as le
from map import map2

w,h=1200, 768
w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)

def linepos():
    glColor3ub(255, 255, 255)
    glBegin(GL_LINES)
    glVertex2f(-(w/2), -120)
    glVertex2f(w/2, -120)
    glVertex2f(0, -(h/2))
    glVertex2f(0, h/2)
    glEnd()

def init():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-(w/2), w/2, -(h/2), h/2, 0.0, 1.0)

def update(value):
    glutReshapeWindow(w,h)
    glutPositionWindow(int(w_position), int(h_position))
    glutPostRedisplay()
    glutTimerFunc(25,update,0)

move = 1
le.move = move
posx, posy = -325,200

def stage_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init()
    linepos()

    glPushMatrix()
    map2.map2()
    glPopMatrix()

    glPushMatrix()
    pos_player = lp.player_move(posx,posy)
    posx_player = pos_player[0]
    posy_player = pos_player[1]
    if posx_player+40>=450-4 or posx_player-40<-450+4:
        lp.step_x=0

    if posy_player+35>134 and posx_player+40>135 and posx_player-40<180:
        lp.step_y=0
    if posy_player+35>=136 and posx_player+40>135-6 and posx_player-40<180+6:
        lp.step_x=0

    if posy_player+35>134 and posx_player+40>-180 and posx_player-40<-135:
        lp.step_y=0
    if posy_player+35>=136 and posx_player+40>-180-6 and posx_player-40<-135+6:
        lp.step_x=0

    if posy_player-35<=-90 and (posx_player-40<-135 or posx_player+40>135):
        lp.step_y = 0
    if posy_player-35<-94 and (posx_player-40<-135+4 or posx_player+40>135-4):
        lp.step_x = 0

    if posy_player+35>=315 or posy_player-35<=-270:
        lp.step_y=0
    glPopMatrix()

    glPushMatrix()
    pos_entity0 = le.RL(0,-50, move, 300)
    posx_entity0 = pos_entity0[0]
    posy_entity0 = pos_entity0[1]
    glPopMatrix()

    glPushMatrix()
    pos_entity05 = le.RL(0,100, move, 300)
    posx_entity05 = pos_entity05[0]
    posy_entity05 = pos_entity05[1]
    glPopMatrix()

    glPushMatrix()
    pos_entity1 = le.UD(325,100, move, 150)
    posx_entity1 = pos_entity1[0]
    posy_entity1 = pos_entity1[1]
    glPopMatrix()

    if posy_player+35 >= posy_entity0-25 and posy_player-35 <= posy_entity0+25 and posx_player+100 >= posx_entity0+40 and posx_player-100 <= posx_entity0-40:
        current_win = glutGetWindow()
        glutDestroyWindow(current_win)
        glutLeaveMainLoop()

    elif posy_player+35 >= posy_entity05-25 and posy_player-35 <= posy_entity05+25 and posx_player+100 >= posx_entity05+40 and posx_player-100 <= posx_entity05-40:
        current_win = glutGetWindow()
        glutDestroyWindow(current_win)
        glutLeaveMainLoop()

    elif posy_player+35 >= posy_entity1-25 and posy_player-35 <= posy_entity1+25 and posx_player+100 >= posx_entity1+40 and posx_player-100 <= posx_entity1-40:
        current_win = glutGetWindow()
        glutDestroyWindow(current_win)
        glutLeaveMainLoop()
        
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(w, h)
glutInitWindowPosition(int(w_position), int(h_position))
glutCreateWindow("Project Pacman Wannabe")
glutDisplayFunc(stage_screen)
glutSpecialFunc(lp.input_keyboard_player)
glutTimerFunc(10,update,0)
glutMainLoop()
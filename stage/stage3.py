import ctypes
import sys
sys.dont_write_bytecode = True
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import logic_player as lp
import logic_entity as le
import logic_drug as lg
from map import map3

w,h=1200, 750
w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)

def linepos():
    glColor3ub(255, 255, 255)
    glBegin(GL_LINES)
    glVertex2f(-(w/2), 0)
    glVertex2f(w/2, 0)
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
le.moveRL = move
le.moveUD = move

def stage_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init()
    linepos()

    glPushMatrix()
    map3.map3()
    glPopMatrix()

#==========================================

    glPushMatrix()
    pos_player = lp.player_move(-400,-35)
    posx_player = pos_player[0]
    posy_player = pos_player[1]
    glPopMatrix()

    if posy_player-35<146 and posx_player+40>-56 and posx_player-40<56  or posx_player+40>244 and posy_player-35>-100 or posx_player-40<-446 or posx_player+40>444:
        lp.step_x=0

    if posy_player+35>34 and posx_player-40<-244:
        lp.step_x=0
        
    if posy_player+35>30 and posx_player-40<-246 or posy_player-35<=-100 and posx_player+40<-46 or posy_player+35>=300 or posy_player-35<=-300:
        lp.step_y=0

    if posy_player-35<150 and posx_player+40>-50 and posx_player-40<50 or posy_player+35>-100 and posx_player+35>250:
        lp.step_y=0

#==========================================

    glPushMatrix()
    pos_drug0 = lg.drug_pos(-150,-35)
    posx_drug0 = pos_drug0[0]
    posy_drug0 = pos_drug0[1]
    glPopMatrix()

    if posy_player+35 >= posy_drug0+10 and posy_player-35 <= posy_drug0+40 and posx_player+80 >= posx_drug0+46 and posx_player-80 <= posx_drug0+10:
        current_win = glutGetWindow()
        glutDestroyWindow(current_win)
        glutLeaveMainLoop()

    glPushMatrix()
    pos_drug1 = lg.drug_pos(275,-215)
    posx_drug1 = pos_drug1[0]
    posy_drug1 = pos_drug1[1]
    glPopMatrix()

    if posy_player+35 >= posy_drug1+10 and posy_player-35 <= posy_drug1+40 and posx_player+80 >= posx_drug1+46 and posx_player-80 <= posx_drug1+10:
        current_win = glutGetWindow()
        glutDestroyWindow(current_win)
        glutLeaveMainLoop()

    glPushMatrix()
    pos_drug2 = lg.drug_pos(220,175)
    posx_drug2 = pos_drug2[0]
    posy_drug2 = pos_drug2[1]
    glPopMatrix()

    if posy_player+35 >= posy_drug2+10 and posy_player-35 <= posy_drug2+40 and posx_player+80 >= posx_drug2+46 and posx_player-80 <= posx_drug2+10:
        current_win = glutGetWindow()
        glutDestroyWindow(current_win)
        glutLeaveMainLoop()

    glPushMatrix()
    pos_drug3 = lg.drug_pos(-224,275)
    posx_drug3 = pos_drug3[0]
    posy_drug3 = pos_drug3[1]
    glPopMatrix()

    if posy_player+35 >= posy_drug3+10 and posy_player-35 <= posy_drug3+40 and posx_player+80 >= posx_drug3+46 and posx_player-80 <= posx_drug3+10:
        current_win = glutGetWindow()
        glutDestroyWindow(current_win)
        glutLeaveMainLoop()

#==========================================

    glPushMatrix()
    pos_entity0 = le.RL(0,180, move, 150)
    posx_entity0 = pos_entity0[0]
    posy_entity0 = pos_entity0[1]
    glPopMatrix()

    if posy_player+35 >= posy_entity0-35 and posy_player-35 <= posy_entity0+35 and posx_player+100 >= posx_entity0+30 and posx_player-100 <= posx_entity0-30:
        current_win = glutGetWindow()
        glutDestroyWindow(current_win)
        glutLeaveMainLoop()

    glPushMatrix()
    pos_entity1 = le.UD(-225,80, move, 150)
    posx_entity1 = pos_entity1[0]
    posy_entity1 = pos_entity1[1]
    glPopMatrix()

    if posy_player+35 >= posy_entity1-35 and posy_player-35 <= posy_entity1+35 and posx_player+100 >= posx_entity1+30 and posx_player-100 <= posx_entity1-30:
        current_win = glutGetWindow()
        glutDestroyWindow(current_win)
        glutLeaveMainLoop()

    glPushMatrix()
    pos_entity2 = le.UD(225,-110, move, 150)
    posx_entity2 = pos_entity2[0]
    posy_entity2 = pos_entity2[1]
    glPopMatrix()

    if posy_player+35 >= posy_entity2-35 and posy_player-35 <= posy_entity2+35 and posx_player+100 >= posx_entity2+30 and posx_player-100 <= posx_entity2-30:
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
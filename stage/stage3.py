import ctypes
import sys
sys.dont_write_bytecode = True
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from stage import logic_player3 as lp
from stage import logic_entity as le
from stage import logic_drug as lg 
from stage.map import map3
import helper_status

w,h=1280, 720
w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)

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

show_drug0 = True
show_drug1 = True
show_drug2 = True
show_drug3 = True

count_collect = 0

def stage_screen():
    global show_drug0, show_drug1, show_drug2, show_drug3, count_collect, game_over
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init()

    glPushMatrix()
    map3.map3()
    glPopMatrix()

#==========================================

    glPushMatrix()
    pos_player = lp.player_move(-400,-35)
    posx_player = pos_player[0]
    posy_player = pos_player[1]
    glPopMatrix()

    if posx_player-40<-446 or posx_player+40>444:
        lp.step_x=0

    if posy_player-35<146 and posx_player+40>-56 and posx_player-40<56:
        lp.step_x=0

    if posy_player+35>34 and posx_player-40<-244 or posy_player-35>-100 and posx_player+40>244:
        lp.step_x=0
        
    if posy_player+35>300 or posy_player-35<-300:
        lp.step_y=0

    if posy_player+35>30 and posx_player-40<-246 or posy_player-35<-100 and posx_player+40<-46:
        lp.step_y=0

    if posy_player-35<150 and posx_player+40>-50 and posx_player-40<50:
        lp.step_y=0

    if posy_player+35>-100 and posx_player+35>250:
        lp.step_y=0

#==========================================

    if show_drug0 == True:
        glPushMatrix()
        drug0 = lg.Drug(-150,-35)
        glPopMatrix()

        if drug0.get_col(posx_player+80, posx_player-80, posy_player+35, posy_player-35):
            show_drug0 = False
            count_collect+=1

    if show_drug1 == True:
        glPushMatrix()
        drug1 = lg.Drug(275,-215)
        glPopMatrix()

        if drug1.get_col(posx_player+80, posx_player-80, posy_player+35, posy_player-35):
            show_drug1 = False
            count_collect+=1

    if show_drug2 == True:
        glPushMatrix()
        drug2 = lg.Drug(220,175)
        glPopMatrix()

        if drug2.get_col(posx_player+80, posx_player-80, posy_player+35, posy_player-35):
            show_drug2 = False
            count_collect+=1

    if show_drug3 == True:
        glPushMatrix()
        drug3 = lg.Drug(-224,275)
        glPopMatrix()

        if drug3.get_col(posx_player+80, posx_player-80, posy_player+35, posy_player-35):
            show_drug3 = False
            count_collect+=1

#==========================================

    glPushMatrix()
    entity0 = le.EntityRL(0,180, move, 150)
    glPopMatrix()

    if entity0.get_col(posx_player+95, posx_player-95, posy_player+20, posy_player-20):
        helper_status.game_over = True

    glPushMatrix()
    entity1 = le.EntityUD(-225,80, move, 150)
    glPopMatrix()

    if entity1.get_col(posx_player+95, posx_player-95, posy_player+20, posy_player-20):
        helper_status.game_over = True

    glPushMatrix()
    entity2 = le.EntityUD(225,-110, move, 150)
    glPopMatrix()

    if entity2.get_col(posx_player+95, posx_player-95, posy_player+20, posy_player-20):
        helper_status.game_over = True

    glFlush()
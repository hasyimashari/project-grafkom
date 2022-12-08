from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Entity import entity

center_xRL,center_yRL = 0,0
moveRL, move_xRL,move_yRL = 0, center_xRL-30, center_yRL-35

center_xUD,center_yUD = 0,0
moveUD, move_xUD,move_yUD = 0, center_xUD-30, center_yUD-35

def RL(posx, posy, step, distance):
    global move_xRL, moveRL, center_xRL
    if center_xRL >= distance:
        moveRL = -step
    elif center_xRL <= -distance:
        moveRL = step
    move_xRL += moveRL
    center_xRL += moveRL
    glTranslated(move_xRL+posx, move_yRL+posy,0)
    entity.Entity()
    entity.mulut()
    return [posx+center_xRL, posy+center_yRL]

def UD(posx, posy, step, distance):
    global move_yUD, moveUD, center_yUD
    if center_yUD >= distance:
        moveUD = -step
    elif center_yUD <= -distance:
        moveUD = step
    move_yUD += moveUD
    center_yUD += moveUD
    glTranslated(move_xUD+posx, move_yUD+posy,0)
    entity.Entity()
    entity.mulut()
    return [posx+center_xUD, posy+center_yUD]

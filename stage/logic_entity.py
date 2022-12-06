from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Entity import entity

center_x,center_y = 0,0
move, move_x,move_y = 0, center_x-30, center_y-35

def RL(posx, posy, step, distance):
    global move_x, move, center_x
    move_y=-35
    if center_x>=distance:
        move=-step
    elif center_x<=-distance:
        move=step
    move_x+=move
    move_y+=0
    center_x+=move
    glTranslated(move_x+posx, move_y+posy,0)
    entity.Entity()
    entity.mulut()
    return [posx+move_x+30, posy+move_y+35]

def UD(posx, posy, step, distance):
    global move_y, move, center_y
    move_x=-30
    if center_y>=distance:
        move=-step
    elif center_y<=-distance:
        move=step
    move_x+=0
    move_y+=move
    center_y+=move
    glTranslated(move_x+posx, move_y+posy,0)
    entity.Entity()
    entity.mulut()
    return posx+move_x+30, posy+move_y+35

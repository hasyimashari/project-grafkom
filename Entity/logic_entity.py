import ctypes
import sys
sys.dont_write_bytecode = True
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import entity

center_x,center_y = 0,0
move, move_x,move_y = 0, center_x-30, center_y-35

def RL(posx, posy, step):
    global move_x, move, center_x
    move_y=-35
    if center_x+20>150:
        move=-step
    elif center_x-20<-150:
        move=step
    move_x+=move
    move_y+=0
    center_x+=move
    print(move_y, posy)
    glTranslated(move_x+posx, move_y+posy,0)
    entity.Entity()
    entity.mulut()

def UD(posx, posy, step):
    global move_y, move, center_y
    move_x=-30
    if center_y+20>150:
        move=-step
    elif center_y-20<-150:
        move=step
    move_x+=0
    move_y+=move
    center_y+=move
    glTranslated(move_x+posx, move_y+posy,0)
    entity.Entity()
    entity.mulut()
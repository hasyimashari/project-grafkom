import ctypes
import sys
sys.dont_write_bytecode = True
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from player import playerDown 
from player import playerLeft 
from player import playerRigh
from player import playerUp
from player import playerIdle

centerx,centery = 0,0
movex,movey = centerx-40,centery-40
step_x, step_y = 0,0

def player_idle():
    playerIdle.player()
    playerIdle.lubang()
    playerIdle.matakiri()
    playerIdle.matakanan()
    playerIdle.pusatmatakanan()
    playerIdle.pusatmatakiri()

def player_right():
    playerRigh.player()
    playerRigh.lubang()
    playerRigh.matakiri()
    playerRigh.matakanan()
    playerRigh.pusatmatakanan()
    playerRigh.pusatmatakiri()

def player_left():
    playerLeft.player()
    playerLeft.lubang()
    playerLeft.matakiri()
    playerLeft.matakanan()
    playerLeft.pusatmatakanan()
    playerLeft.pusatmatakiri()

def player_up():
    playerUp.player()
    playerUp.lubang()
    playerUp.matakiri()
    playerUp.matakanan()
    playerUp.pusatmatakanan()
    playerUp.pusatmatakiri()

def player_down():
    playerDown.player()
    playerDown.lubang()
    playerDown.matakiri()
    playerDown.matakanan()
    playerDown.pusatmatakanan()
    playerDown.pusatmatakiri()

def player_move(posx, posy):
    global movex, movey, centerx, centery, step_x, step_y
    
    movex+=step_x
    movey+=step_y
    centerx+=step_x
    centery+=step_y

    if posx+centerx+76>=300 or posy+centerx-76<-300:
        step_x=0
    if posx+centery+66>=300 or posy+centery-66<-300:
        step_y=0
    
    glTranslated(posx+movex, posy+movey, 0)
    
    if step_x==0 and step_y==0:
        player_idle()
    elif step_x==0 and step_y==2:
        player_up()
    elif step_x==0 and step_y==-2:
        player_down()
    elif step_x==2 and step_y==0:
        player_right()
    elif step_x==-2 and step_y==0:
        player_left()

    return [posx+centerx, posy+centery]

def input_keyboard_player(key,x,y):
    global step_x, step_y
    if key == GLUT_KEY_UP:
        step_x = 0
        step_y = 2
    elif key == GLUT_KEY_DOWN:
        step_x = 0
        step_y = -2
    elif key == GLUT_KEY_RIGHT:
        step_x = 2
        step_y = 0
    elif key == GLUT_KEY_LEFT:
        step_x = -2
        step_y = 0


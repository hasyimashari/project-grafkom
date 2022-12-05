import ctypes
import sys
sys.dont_write_bytecode = True
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import playerDown 
import playerLeft 
import playerRigh
import playerUp
import playerIdle

movex,movey = -40,-40
centerx,centery = 0,0
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

def player_move():
    global movex, movey, centerx, centery, step_x, step_y
    glTranslated(movex,movey,0)
    movex+=step_x
    movey+=step_y
    centerx+=step_x
    centery+=step_y
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
    glTranslated(movex, movey, 0)

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


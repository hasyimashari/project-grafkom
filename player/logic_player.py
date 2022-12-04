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

w,h = 800,600
w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)
movex,movey = -40,-40
centerx,centery = 0,0

def init():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-(w/2), w/2, -(h/2), h/2, 0.0, 1.0)
    print(centerx, centery)

def update(value):
    glutReshapeWindow(w,h)
    glutPositionWindow(int(w_position), int(h_position))
    glutPostRedisplay()
    glutTimerFunc(25,update,0)

def linepos():
    glColor3ub(255, 255, 255)
    glBegin(GL_LINES)
    glVertex2f(-(w/2), 0)
    glVertex2f(w/2, 0)
    glVertex2f(0, -(h/2))
    glVertex2f(0, h/2)
    glEnd()

def player_idle():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init()
    linepos()
    glTranslated(movex,movey,0)
    playerIdle.player()
    playerIdle.lubang()
    playerIdle.matakiri()
    playerIdle.matakanan()
    playerIdle.pusatmatakanan()
    playerIdle.pusatmatakiri()
    glFlush()

def player_right():
    global movex, movey, centerx, centery
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init()
    linepos()
    glTranslated(movex,movey,0)
    movex+=1.5
    movey+=0
    centerx+=1.5
    centery+=0
    playerRigh.player()
    playerRigh.lubang()
    playerRigh.matakiri()
    playerRigh.matakanan()
    playerRigh.pusatmatakanan()
    playerRigh.pusatmatakiri()
    glFlush()

def player_left():
    global movex, movey, centerx, centery
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init()
    linepos()
    glTranslated(movex,movey,0)
    movex-=1.5
    movey-=0
    centerx-=1.5
    centery-=0
    playerLeft.player()
    playerLeft.lubang()
    playerLeft.matakiri()
    playerLeft.matakanan()
    playerLeft.pusatmatakanan()
    playerLeft.pusatmatakiri()
    glFlush()

def player_up():
    global movex, movey, centerx, centery
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init()
    linepos()
    glTranslated(movex,movey,0)
    movex+=0
    movey+=1.5
    centerx+=0
    centery+=1.5
    playerUp.player()
    playerUp.lubang()
    playerUp.matakiri()
    playerUp.matakanan()
    playerUp.pusatmatakanan()
    playerUp.pusatmatakiri()
    glFlush()

def player_down():
    global movex, movey, centerx, centery    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init()
    linepos()
    glTranslated(movex,movey,0)
    movex-=0
    movey-=1.5
    centerx-=0
    centery-=1.5
    playerDown.player()
    playerDown.lubang()
    playerDown.matakiri()
    playerDown.matakanan()
    playerDown.pusatmatakanan()
    playerDown.pusatmatakiri()
    glFlush()

def player_move(key, x, y):
    if key == GLUT_KEY_RIGHT:
        glutDisplayFunc(player_right)
    elif key == GLUT_KEY_LEFT:
        glutDisplayFunc(player_left)
    elif key == GLUT_KEY_UP:
        glutDisplayFunc(player_up)
    elif key == GLUT_KEY_DOWN:
        glutDisplayFunc(player_down)

glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(w, h)
glutInitWindowPosition(int(w_position), int(h_position))
glutCreateWindow("Project Pacman Wannabe")
glutDisplayFunc(player_idle)
glutSpecialFunc(player_move)
glutTimerFunc(10,update,0)
glutMainLoop()

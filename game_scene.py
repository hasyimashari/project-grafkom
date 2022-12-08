import ctypes
import sys
sys.dont_write_bytecode = True
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from stage import logic_player as lp
from stage import logic_player2 as lp2
from stage import logic_player3 as lp3
from stage import logic_player4 as lp4
from stage import stage1
from stage import stage2
from stage import stage3
from stage import stage4


w,h=1200, 750
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



def display():
    init()
    if stage1.count_collect <= 4:
        glPushMatrix()
        stage1.stage_screen()
        glPopMatrix()
        glutSpecialFunc(lp.input_keyboard_player)
    if stage1.count_collect >= 4 and stage2.count_collect <= 4:
        stage1.count_collect+=1
        glPushMatrix()
        stage2.stage_screen()
        glPopMatrix()
        glutSpecialFunc(lp2.input_keyboard_player)
    if stage2.count_collect >= 4 and stage3.count_collect <= 4:
        stage2.count_collect+=1
        glPushMatrix()
        stage3.stage_screen()
        glPopMatrix()
        glutSpecialFunc(lp3.input_keyboard_player)
    if stage3.count_collect >= 4 and stage4.count_collect <= 4:
        stage3.count_collect+=1
        glPushMatrix()
        stage4.stage_screen()
        glPopMatrix()
        glutSpecialFunc(lp4.input_keyboard_player)
        

glutInit()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(w, h)
glutInitWindowPosition(int(w_position), int(h_position))
glutCreateWindow("Project Pacman Wannabe")
glutDisplayFunc(display)
glutTimerFunc(10,update,0)
glutMainLoop()


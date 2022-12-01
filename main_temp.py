import ctypes
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random as rn
import logic_enemy
import logic_player

w,h = 800,600
w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)
class Menu:
    def __init__(self, x, y):
        self.x1 = x
        self.x2 = self.x1 - 800
        self.x3 = self.x2
        self.x4 = self.x1
        self.y1 = y
        self.y2 = y
        self.y3 = self.y1 - 66
        self.y4 = self.y2 - 66

    def draw_MenuNotSelect(self):
        glColor3ub(255,255,255)
        glBegin(GL_QUADS)
        glVertex2f(self.x1, self.y1)
        glVertex2f(self.x2, self.y2)
        glVertex2f(self.x3, self.y3)
        glVertex2f(self.x4, self.y4)
        glEnd()

    def draw_MenuSelect(self):
        glColor3ub(255,255,255)
        glBegin(GL_QUADS)
        glVertex2f(self.x1, self.y1)
        glVertex2f(self.x2, self.y2)
        glVertex2f(self.x3, self.y3)
        glVertex2f(self.x4, self.y4)
        glEnd()

def linePos():
    glColor3ub(255,255,255)
    glBegin(GL_LINES)
    glVertex2f(w, 0)
    glVertex2f(-w, 0)
    glVertex2f(0,h)
    glVertex2f(0,-h)
    glEnd()

def menu_start_not_selected():
    menu = Menu(400, 100)
    menu.draw_MenuNotSelect()

def menu_option_not_selected():
    menu = Menu(400, 34)
    menu.draw_MenuNotSelect()

def menu_about_not_selected():
    menu = Menu(400, -32)
    menu.draw_MenuNotSelect()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-(w/2), w/2, -(h/2), h/2, 0.0, 1.0)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    menu_start_not_selected()
    menu_option_not_selected()
    menu_about_not_selected()
    glFlush()

def game_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    linePos()
    logic_enemy.enemy()
    logic_player.player()
    glFlush()

def update(value):
    glutReshapeWindow(w,h)
    glutPositionWindow(int(w_position), int(h_position))
    glutPostRedisplay()
    glutTimerFunc(25,update,0)

menu_pointer = 1

def key_func(key, x, y):
    global menu_pointer, w, h, w_position, h_position, main_win, game_win
    # if key == GLUT_KEY_UP:      # up
    #     w,h = 600,450
    #     w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)
    # elif key == GLUT_KEY_DOWN:    # down
    #     w,h = 800,600
    #     w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)
    if ord(key) == 13 and menu_pointer == 1:    
        glutDestroyWindow(main_win)
        glutLeaveMainLoop()
        game_win = glutCreateWindow("Project Pacman Wannabe")
        glutDisplayFunc(game_screen)
        glutSpecialFunc(logic_player.input_keyboard_player)
        glutKeyboardFunc(logic_player.exit_game)
        init()
        glutMainLoop()
    elif ord(key) == 13 and menu_pointer == 3:    
        glutDestroyWindow(main_win)
        glutLeaveMainLoop()       

def menu_func(key, x, y):
    global menu_pointer
    if key == GLUT_KEY_UP:
        menu_pointer = menu_pointer + 1 if menu_pointer < 3 else menu_pointer + 0
    elif key == GLUT_KEY_DOWN:
        menu_pointer = menu_pointer - 1 if menu_pointer > 1 else menu_pointer - 0
    print(menu_pointer)

def main():
    global main_win
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(int(w_position), int(h_position))
    main_win = glutCreateWindow("Project Pacman Wannabe")
    glutDisplayFunc(showScreen)
    glutSpecialFunc(menu_func)
    glutKeyboardFunc(key_func)
    glutTimerFunc(10,update,0)
    init()
    glutMainLoop()

if __name__ == '__main__':
    main()
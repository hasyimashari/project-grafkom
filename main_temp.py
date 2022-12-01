import ctypes
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import menu_ui
import logic_enemy
import logic_player

w,h = 800,600
w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-(w/2), w/2, -(h/2), h/2, 0.0, 1.0)

def game_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    logic_enemy.enemy()
    logic_player.player()
    glFlush()

def update(value):
    glutReshapeWindow(w,h)
    glutPositionWindow(int(w_position), int(h_position))
    glutPostRedisplay()
    glutTimerFunc(25,update,0)

menu_pointer = 1

def up_menu(key, x, y):
    global menu_pointer
    if key == GLUT_KEY_UP:
        menu_pointer = menu_pointer - 1 if menu_pointer > 1 else menu_pointer - 0
    elif key == GLUT_KEY_DOWN:
        menu_pointer = menu_pointer + 1 if menu_pointer < 3 else menu_pointer + 0
    print(menu_pointer)

def change_reso(key, x, y):
    global w, h, w_position, h_position
    if key == GLUT_KEY_UP:        
        w,h = 800,600
        w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)
    elif key == GLUT_KEY_DOWN:    
        w,h = 600,450 
        w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)
    print(w, h)

def back(key, x, y):
    if ord(key) == 27:
        glutHideWindow()
        main()

def menu_func(key, x, y):
    global w, h, w_position, h_position, main_win, game_win
    if ord(key) == 13 and menu_pointer == 1:    
        glutHideWindow()
        game_win = glutCreateWindow("Project Pacman Wannabe")
        glutDisplayFunc(game_screen)
        glutKeyboardFunc(back)
        glutSpecialFunc(logic_player.input_keyboard_player)
        init()
    elif ord(key) == 13 and menu_pointer == 2:
        glutHideWindow()
        setting_win = glutCreateWindow("Project Pacman Wannabe")
        glutDisplayFunc(menu_ui.showScreen)
        glutKeyboardFunc(back)
        glutSpecialFunc(change_reso)
        init()
    elif ord(key) == 13 and menu_pointer == 3:    
        glutDestroyWindow(main_win)
        glutLeaveMainLoop()       

def main():
    global main_win
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(int(w_position), int(h_position))
    main_win = glutCreateWindow("Project Pacman Wannabe")
    glutDisplayFunc(menu_ui.showScreen)
    glutKeyboardFunc(menu_func)
    glutSpecialFunc(up_menu)
    glutTimerFunc(10,update,0)
    init()
    glutMainLoop()

if __name__ == '__main__':
    main()
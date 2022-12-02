import ctypes
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import menu_ui
import logic_enemy
import logic_player

w,h = 800,600
w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)
menu_pointer = 1

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

def change_menu():
    if menu_pointer == 1:
        glutDisplayFunc(menu_ui.start)
    elif menu_pointer == 2:
        glutDisplayFunc(menu_ui.option)
    elif menu_pointer == 3:
        glutDisplayFunc(menu_ui.exit_game)

def up_menu(key, x, y):
    global menu_pointer
    if key == GLUT_KEY_UP:
        menu_pointer = menu_pointer - 1 if menu_pointer > 1 else menu_pointer - 0
    elif key == GLUT_KEY_DOWN:
        menu_pointer = menu_pointer + 1 if menu_pointer < 3 else menu_pointer + 0
    change_menu()

def escape(key, x, y):
    if ord(key) == 26+1:
        current_win = glutGetWindow()
        glutDestroyWindow(current_win)
        glutLeaveMainLoop()
        main_win()

# def change_res(key, x, y):
#     global w, h, w_position, h_position
#     if key == GLUT_KEY_UP: 
#         glutDisplayFunc(menu_ui.start)
#         w,h = 800,600
#         w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)
#     elif key == GLUT_KEY_DOWN: 
#         glutDisplayFunc(menu_ui.option)
#         w,h = 600,450 
#         w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)

def draw_text(text,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f(xpos, ypos)
    for i in text:
        if  i=='\n':
            line=line+1
            glRasterPos2f (xpos, ypos*line)
        else:
            glutBitmapCharacter(font_style, ord(i))

def menu_func(key, x, y):
    global w, h, w_position, h_position, main_win, game_win, setting_win
    if ord(key) == 13 and menu_pointer == 1:    
        current_win = glutGetWindow()
        glutDestroyWindow(current_win)
        game_win = glutCreateWindow("Project Pacman Wannabe")
        glutDisplayFunc(game_screen)
        glutKeyboardFunc(escape)
        glutSpecialFunc(logic_player.input_keyboard_player)
        init()
    elif ord(key) == 13 and menu_pointer == 2:
        pass
        # current_win = glutGetWindow()
        # glutDestroyWindow(current_win)
        # setting_win = glutCreateWindow("Project Pacman Wannabe")
        # glutDisplayFunc(menu_ui.start)
        # glutKeyboardFunc(escape)
        # glutSpecialFunc(change_res)
        # init()
    elif ord(key) == 13 and menu_pointer == 3:    
        glutDestroyWindow(main_win)
        glutLeaveMainLoop()       

def main_win():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(int(w_position), int(h_position))
    main_win = glutCreateWindow("Project Pacman Wannabe")
    change_menu()
    draw_text("test", -100, 250, 255, 255, 255)
    glutKeyboardFunc(menu_func)
    glutSpecialFunc(up_menu)
    glutTimerFunc(10,update,0)
    init()
    glutMainLoop()

if __name__ == '__main__':
    main_win()
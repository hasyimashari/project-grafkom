import ctypes
import sys
sys.dont_write_bytecode = True
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import menu.menu_ui as menu
from stage import logic_player as lp
from stage import logic_player2 as lp2
from stage import logic_player3 as lp3
from stage import logic_player4 as lp4
from stage import stage1
from stage import stage2
from stage import stage3
from stage import stage4

w,h = 1200, 750
w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)
menu_pointer = 1

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

def change_menu():
    if menu_pointer == 1:
        glutDisplayFunc(menu.start)
    elif menu_pointer == 2:
        glutDisplayFunc(menu.option)
    elif menu_pointer == 3:
        glutDisplayFunc(menu.quit_game)

def up_menu(key, x, y):
    global menu_pointer
    if key == GLUT_KEY_UP:
        menu_pointer = menu_pointer - 1 if menu_pointer > 1 else 3
    elif key == GLUT_KEY_DOWN:
        menu_pointer = menu_pointer + 1 if menu_pointer < 3 else 1
    change_menu()

def escape(key, x, y):
    if ord(key) == 26+1:
            change_menu()
            glutKeyboardFunc(menu_func)
            glutSpecialFunc(up_menu)

def game_screen():
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
        glutDisplayFunc(game_screen)
        glutKeyboardFunc(escape)
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
        current_win = glutGetWindow()
        glutDestroyWindow(current_win)
        glutLeaveMainLoop()       

def main_win():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(int(w_position), int(h_position))
    main_win = glutCreateWindow("Project Pacman Wannabe")
    change_menu()
    glutKeyboardFunc(menu_func)
    glutSpecialFunc(up_menu)
    glutTimerFunc(10,update,0)
    init()

if __name__ == '__main__':
    main_win()
    glutMainLoop()
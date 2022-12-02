from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

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
        glBegin(GL_LINES)
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

    # def draw_text(self, text):
    #     # color = (r, b, g)
    #     font_style = glut.GLUT_BITMAP_TIMES_ROMAN_24
    #     glColor3ub(255,255,255)
    #     line=0
    #     glRasterPos2f(self.x1-450, self.y1-33)
    #     for i in text:
    #         if  i=='\n':
    #             line=line+1
    #             glRasterPos2f (xpos, ypos*line)
    #         else:
    #             glutBitmapCharacter(font_style, ord(i))

def menu_start_not_selected():
    menu = Menu(400, 100)
    menu.draw_MenuNotSelect()
    # menu.draw_text("MENU")

def menu_option_not_selected():
    menu = Menu(400, 34)
    menu.draw_MenuNotSelect()

def menu_exit_not_selected():
    menu = Menu(400, -32)
    menu.draw_MenuNotSelect()

def menu_start_selected():
    menu = Menu(400, 100)
    menu.draw_MenuSelect()

def menu_option_selected():
    menu = Menu(400, 34)
    menu.draw_MenuSelect()

def menu_exit_selected():
    menu = Menu(400, -32)
    menu.draw_MenuSelect()

def start():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    menu_start_selected()
    menu_option_not_selected()
    menu_exit_not_selected()
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(100,100)
    glEnd()
    glFlush()

def option():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    menu_start_not_selected()
    menu_option_selected()
    menu_exit_not_selected()
    glFlush()

def exit_game():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    menu_start_not_selected()
    menu_option_not_selected()
    menu_exit_selected()
    glFlush()
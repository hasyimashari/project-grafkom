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

def menu_start_not_selected():
    menu = Menu(400, 100)
    menu.draw_MenuNotSelect()

def menu_option_not_selected():
    menu = Menu(400, 34)
    menu.draw_MenuNotSelect()

def menu_about_not_selected():
    menu = Menu(400, -32)
    menu.draw_MenuNotSelect()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    menu_start_not_selected()
    menu_option_not_selected()
    menu_about_not_selected()
    glFlush()
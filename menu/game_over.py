from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import main_temp

class Menu:
    def __init__(self, x, y):
        self.x1 = x
        self.y1 = y

    def draw_MenuSelect(self):
        glColor3ub(212,212,212)
        glBegin(GL_POLYGON)
        glVertex2f(self.x1-150, self.y1)
        glVertex2f(self.x1-150, self.y1-50)
        glVertex2f(self.x1-165, self.y1-66)
        glVertex2f(self.x1-650, self.y1-66)
        glVertex2f(self.x1-650, self.y1-10)
        glVertex2f(self.x1-640, self.y1)
        glEnd()

    def draw_MenuNotSelect(self):
        glColor3ub(0,0,0)
        glBegin(GL_POLYGON)
        glVertex2f(self.x1-200, self.y1-10)
        glVertex2f(self.x1-200, self.y1-40)
        glVertex2f(self.x1-210, self.y1-50)
        glVertex2f(self.x1-600, self.y1-50)
        glVertex2f(self.x1-600, self.y1-20)
        glVertex2f(self.x1-590, self.y1-10)
        glEnd()

        glColor3ub(212,212,212)
        glBegin(GL_LINES)
        glVertex2f(self.x1-200, self.y1-10)
        glVertex2f(self.x1-200, self.y1-40)
        glVertex2f(self.x1-200, self.y1-40)
        glVertex2f(self.x1-210, self.y1-50)
        glVertex2f(self.x1-210, self.y1-50)
        glVertex2f(self.x1-600, self.y1-50)
        glVertex2f(self.x1-600, self.y1-50)
        glVertex2f(self.x1-600, self.y1-20)
        glVertex2f(self.x1-600, self.y1-20)
        glVertex2f(self.x1-590, self.y1-10)
        glVertex2f(self.x1-590, self.y1-10)
        glVertex2f(self.x1-200, self.y1-10)
        glEnd()

    def draw_text(self,text,r,b,g):
        color = (r, b, g)
        font_style = GLUT_BITMAP_TIMES_ROMAN_24
        glColor3ub(color[0],color[1],color[2])
        line=0
        glRasterPos2f(self.x1-525, self.y1-33)
        for i in text:
            glutBitmapCharacter(font_style, ord(i))

def menu_back_selected():
    menu = Menu(400, 34)
    menu.draw_MenuSelect()
    menu.draw_text("press ESC to back to menu", 0, 0, 0)

def back():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    menu_back_selected()
    glFlush()

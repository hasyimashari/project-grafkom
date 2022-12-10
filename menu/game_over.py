from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Menu:
    def __init__(self, xcenter, ycenter):   #titik tengah dari kotak
        self.x = xcenter
        self.y = ycenter

    def draw_MenuSelect(self):
        glColor3ub(212,212,212)
        glBegin(GL_POLYGON)
        glVertex2f(self.x+220,self.y+55)
        glVertex2f(self.x+220,self.y+1)          
        glVertex2f(self.x+198,self.y-25)
        glVertex2f(self.x-220,self.y-25)
        glVertex2f(self.x-220,self.y+28)
        glVertex2f(self.x-198,self.y+55)
        glEnd()

    def draw_text(self,text,r,b,g):
        color = (r, b, g)
        font_style = GLUT_BITMAP_TIMES_ROMAN_24
        glColor3ub(color[0],color[1],color[2])
        glRasterPos2f(self.x-135, self.y+10)
        for i in text:
            glutBitmapCharacter(font_style, ord(i))

def menu_back():
    menu = Menu(0, 0)
    menu.draw_MenuSelect()
    menu.draw_text("press ESC to back to menu", 0, 0, 0)

def back():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    menu_back()
    glFlush()

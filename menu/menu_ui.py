from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#class untuk membuat tampilan menu
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

    def draw_MenuNotSelect(self):
        glColor3ub(212,212,212)
        glLineWidth(4)
        glBegin(GL_LINE_LOOP)
        glVertex2f(self.x+210,self.y+45)
        glVertex2f(self.x+210,self.y+5)
        glVertex2f(self.x+189,self.y-15)
        glVertex2f(self.x-210,self.y-15)
        glVertex2f(self.x-210,self.y+25)
        glVertex2f(self.x-189,self.y+45)
        glEnd()

    def draw_text(self,text,r,b,g):
        color = (r, b, g)
        font_style = GLUT_BITMAP_TIMES_ROMAN_24
        glColor3ub(color[0],color[1],color[2])
        glRasterPos2f(self.x-35, self.y+10)
        for i in text:
            glutBitmapCharacter(font_style, ord(i))

# membuat tampila menu
#jarak antar titik tengah kota = 90
def menu_start_not_selected():
    menu = Menu(0, 45)
    menu.draw_MenuNotSelect()
    menu.draw_text("Start", 255, 255, 255)

def menu_how_not_selected():
    menu = Menu(0, -45)
    menu.draw_MenuNotSelect()
    menu.draw_text("How to play", 255, 255, 255)

def menu_quit_not_selected():
    menu = Menu(0, -135)
    menu.draw_MenuNotSelect()
    menu.draw_text("Quit", 255, 255, 255)

def menu_start_selected():
    menu = Menu(0, 45)
    menu.draw_MenuSelect()
    menu.draw_text("Start", 0, 0, 0)

def menu_how_selected():
    menu = Menu(0, -45)
    menu.draw_MenuSelect()
    menu.draw_text("How to play", 0, 0, 0)

def menu_quit_selected():
    menu = Menu(0, -135)
    menu.draw_MenuSelect()
    menu.draw_text("Quit", 0, 0, 0)

# fungsi untuk menampilkan menu
def start():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    menu_start_selected()
    menu_how_not_selected()
    menu_quit_not_selected()
    glFlush()

def how():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    menu_start_not_selected()
    menu_how_selected()
    menu_quit_not_selected()
    glFlush()

def quit_game():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    menu_start_not_selected()
    menu_how_not_selected()
    menu_quit_selected()
    glFlush()
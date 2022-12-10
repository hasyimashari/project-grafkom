from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Menu:
    def __init__(self, xcenter, ycenter):   #titik tengah dari kotak
        self.x = xcenter
        self.y = ycenter

    def draw_MenuNotSelect(self):
        glColor3ub(212,212,212)
        glLineWidth(4)
        glBegin(GL_LINE_LOOP)
        glVertex2f(self.x+210+50,self.y+45)
        glVertex2f(self.x+210+50,self.y+5-134)
        glVertex2f(self.x+189+50,self.y-15-135)
        glVertex2f(self.x-210-50,self.y-15-135)
        glVertex2f(self.x-210-50,self.y+25)
        glVertex2f(self.x-189-50,self.y+45)
        glEnd()

    def draw_text(self,text,r,b,g):
        color = (r, b, g)
        font_style = GLUT_BITMAP_TIMES_ROMAN_24
        glColor3ub(color[0],color[1],color[2])
        line=0
        # glRasterPos2f(self.x-220, self.y+22)
        for i in text:
            if  i=='\n':
                line=line+1
                glRasterPos2f(self.x-220, (self.y+22)-(20*line))
            else:
                glutBitmapCharacter(font_style, ord(i))

def menu_how():
    global move_up
    menu = Menu(0, 0)
    menu.draw_MenuNotSelect()
    menu.draw_text("\nUse UP, DOWN, RIGHT, LEFT key to move\n\nEat all of drug to continue to next level\n\nYou touch enemy You die\n\nThere is NO save point :D", 255, 255, 255)

def how_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    menu_how()
    glFlush()
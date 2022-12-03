import ctypes
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h=800,600
w_position,h_position = (ctypes.windll.user32.GetSystemMetrics(0)/2)-(w/2), (ctypes.windll.user32.GetSystemMetrics(1)/2)-(h/2)

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-(w/2), w/2, -(h/2), h/2, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_text(text,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = GLUT_BITMAP_TIMES_ROMAN_24
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f(xpos, ypos)
    for i in text:
        glutBitmapCharacter(font_style, ord(i))

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    # draw_text("halo", 0, 0, 255, 255, 255)
    glColor3ub(255,255,255) # glColor3ub(0,0,0)
    glBegin(GL_POLYGON)     # glBegin(GL_POLYGON)

    # kanan atas (400, 100)         glVertex2f(250,100)     glVertex2f(200,90)
    #                                         (x-150,y)             (x-200,y-10)
    # kanan bawah (400, 100-66)     glVertex2f(250,50)      glVertex2f(200,60)
    #                                         (x-150,y-50)             (x-200,y-40)
    #                               glVertex2f(235,34)      glVertex2f(190,50)
    #                                         (x-165,y-66)             (x-210,y-50)
    # kiri bawah (400-800, 100-66)  glVertex2f(-250,34)     glVertex2f(-200,50)
    #                                         (x-650,y-66)             (x-600,y-50)

    #                               glVertex2f(-250,90)     glVertex2f(-200,80)
    #                                         (x-650,y-10)             (x-600,y-20)
    #kiri atas (400-800, 100)       glVertex2f(-240,100)    glVertex2f(-190,90)
    #                                         (x-640,y)               (x-590,y-10)
    glEnd()                 # glEnd()
    
    
    
    
    
    
    
    
    
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(int(w_position), int(h_position))
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()


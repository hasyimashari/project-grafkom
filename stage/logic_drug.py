from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from drug import drugmodels 

def drug_pos(posx, posy):
    glTranslated(posx-28, posy-25, 0)
    drugmodels.modelkanan()
    drugmodels.modelkiri()
    return [posx-28, posy-25]
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from stage.drug import drugmodels 

# class untuk drug
class Drug:
    def __init__(self,x,y): # titik tengah dari gambar drug
        glTranslated(x-28, y-25, 0)
        drugmodels.modelkanan()
        drugmodels.modelkiri()
        self.posx_drug = x-28
        self.posy_drug = y-25
    
    # mengecek collision
    def get_col(self,x1,x2,y1,y2):
        return y1 >= self.posy_drug+10 and y2 <= self.posy_drug+40 and x1 >= self.posx_drug+46 and x2 <= self.posx_drug+10
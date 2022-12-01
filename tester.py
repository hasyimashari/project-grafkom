# from OpenGL.GLUT import *
# import time

# DISPLAY_WIDTH, DISPLAY_HEIGHT = 800,600

# class TestEnv:
#     def __init__(self):
#         self.window = None
#         glutInit(sys.argv)
#         glutInitWindowSize(DISPLAY_WIDTH, DISPLAY_HEIGHT)
#         self.window = glutCreateWindow("TestEnv")

#     def close(self):
#         if self.window:
#             glutDestroyWindow(self.window)


# if __name__ == "__main__":
#     env = TestEnv()
#     env.close()
#     glutMainLoopEvent() # <--- handle events

class Test():
    def __init__(self):
        self.a = 1

    def print(self):
        print(self.a)

def panggil():
    global test
    test = Test()

panggil()
test.print()
import time

class Ant:
    def __init__(self, x, y, dire, mat):
        self.x = x
        self.y = y
        self.dire = dire
        self.mat = mat
    
    def move(self):
        square = self.mat[self.y][self.x]
        rot = (-1)**(square + 1) * 90
        self.dire = (self.dire + rot) % 360
        
        self.mat[self.y][self.x] = square ^ 1
        
        if self.dire == 0:
            self.y = self.y - 1
        if self.dire == 180:
            self.y = self.y + 1
        if self.dire == 90:
            self.x = self.x + 1
        if self.dire == 270:
            self.x = self.x - 1

def initScreen(n):
    out = [None] * n
    for i in range(n):
        out[i] = [0] * n
    return out
    
def printScreen(mat, ant, iter):
    s = ant.x, ant.y, ant.dire, iter
    print(s, end = " ")
    print("=" * (len(mat) - len(s) - 1 + 10))
    for y in range(len(mat)):
        for x in range(len(mat)):
            if mat[x][y] == 1:
                print("X", end = "")
            else:
                print(" ", end = "")
        print()
    

N = 60
M = initScreen(N)
ant = Ant(N >> 1, N >> 1, 0, M)

for i in range(4096):
    ant.move()
    printScreen(M, ant, i)
    time.sleep(0.04)




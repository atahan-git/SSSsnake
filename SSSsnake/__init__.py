from IPython.display import HTML
from IPython.display import display
from IPythonDisplayTurtle import Snake
from IPythonDisplayTurtle import ReadFile as ReadFileLib
import random
import math
import os.path

def ReadFile (filename):
    with open(os.path.join(os.path.dirname(__file__), 'levels' , filename), 'r') as myfile:
        data = myfile.read()
        return data

class SSSsnake(Snake):
    
    _unitSize = 50
    _rotationAmount = 90
    
    
    def __init__(self, homeX = 0, homeY = 0):
        self._turtleMainColor = "#00A651"
        self._turtleAccentColor = "#FFF600"
        self._speed = 5
        self._rotspeed = 5
        self._pendown = 0
        self._pencolor = "red"
        self._penwidth = 3
        self._rotation = 90
        self._gridmode = True
        self._gridsize = self._unitSize
        self._x = homeX
        self._y = homeY
        self._canvWidth = 410
        self._canvHeigth = 210
        self._actions = []
        self._appendCurrentState();
        
    ## Helper methods, these are the expected way to interract with the turtle
    # the SSS turtle can only move in units!
    def right(self):
        self.setheading(self._rotation + self._rotationAmount)
        
    def left(self):
        self.setheading(self._rotation - self._rotationAmount)
    
    def forward(self):
        newX = self._x + round(math.sin(math.radians(self._rotation)), 1)
        newY = self._y - round(math.cos(math.radians(self._rotation)), 1)
        self.goto(newX, newY)
        
    # These are the premade levels for our snake!
    def loadlevel(self, levelid):
        import random
        def houseAtXY(x,y):
            return [[x-1,y,3],[x+1,y,1],[x+2,y,4],[x+2,y+1,0],[x+2,y+2,0],[x+2,y+3,5],[x+1,y+3,1],[x,y+3,1],[x-1,y+3,2],[x-1,y+2,0],[x-1,y+1,0]]
        if levelid == 1:
            self.drawLevel(apple=[[3,3]], walls=[[0,2,1],[1,2,1],[2,2,4],[2,3,0]])
        elif levelid == 2:
            self.drawLevel(apple=[[5,1]], walls=[[4,0,3],[5,0,1],[6,0,1],[7,0,4],[7,1,0],[7,2,0],[7,3,5],[6,3,1],[5,3,1],[4,3,2],[4,1,0]], doors=[[4,2,0]])
        elif levelid == 3:
            walls = [];doors = [];walls.extend(houseAtXY(1,2));doors.append([1,2,1]);walls.extend(houseAtXY(5,3));doors.append([5,3,1]);walls.extend(houseAtXY(9,4));doors.append([9,4,1])
            self.drawLevel(xSize=16, ySize=8, gridSize=25, apple=[[15,7]], walls=walls, doors=doors)
        elif levelid == 4:
            walls = [];doors = [];walls.extend(houseAtXY(2,0));doors.append([2,0,1]);walls.extend(houseAtXY(7,1));doors.append([7,1,1]);walls.extend(houseAtXY(12,2));doors.append([12,2,1])
            self.drawLevel(xSize=16, ySize=8, gridSize=25, walls=walls, doors=doors)
        elif levelid == 5:
            d = random.randint(5, 12)
            self.drawLevel(xSize=16, ySize=3, gridSize=25, apple=[[15,7]], walls=[[d,0,0],[d,1,0],[d,2,0]])
        elif levelid == 6:
            d = random.randint(3, 6); c = random.randint(1, 3);lava = [];bridges = [];apple = []
            for i in range(4):
                if i != c:
                    lava.append([d,i])
                else:
                    bridges.append([d,i,0]);apple.append([d+1,i])
            self.drawLevel(xSize=8, ySize=4, gridSize=50, apple=apple, lava=lava, bridges=bridges)

        
        
    # This method checks if the snake will reach the apple, 
    # and send the corresponding miupload command so that our backend knows this student completed this task correctly
    def _checkifwinning(self):
        for act in self._actions:
            x = round((act[1] - 5 - self._gridsize/2)/self._gridsize)
            y = round((act[2] - 5 - self._gridsize/2)/self._gridsize)
            #print(x,y)
            if(not self.islocationclear(x,y)):
                #print("snek is ded")
                return 0
            if(self.islocationapple(x,y)):
                #print("snek won!!!")
                return 1
        #print("snek survived")
        return 0
    
    def display(self):
        super().display()
        # This will return 0 or 1 based on the result. 
        # You can use it for autograding purposes
        return self._checkifwinning() 

class SSSfirstsnake (SSSsnake):
    def left (self):
        raise Exception("I don't know what this command means!")
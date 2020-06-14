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
    
    _homeX = 30
    _homeY = 30
    
    def __init__(self):
        self._turtleMainColor = "green"
        self._turtleAccentColor = "yellow"
        self._backgroundColor = "white"
        self._speed = 5
        self._rotspeed = 5
        self._pendown = 0
        self._pencolor = "red"
        self._penwidth = 3
        self._rotation = 90
        self._x = self._homeX
        self._y = self._homeY
        self._actions = []
        self._appendCurrentState();
        
    ## Helper methods, these are the expected way to interract with the turtle
    # the SSS turtle can only move in units!
    def turnRight(self):
        self._rotateTo(self._rotation + self._rotationAmount)
        
    def turnLeft(self):
        self._rotateTo(self._rotation - self._rotationAmount)
    
    def move(self):
        newX = self._x + round(self._unitSize * math.sin(math.radians(self._rotation)), 1)
        newY = self._y - round(self._unitSize * math.cos(math.radians(self._rotation)), 1)
        self._moveTo(newX, newY)
        
    def display(self):
        super().display(410,210, False)
        #print((ReadFile(self._levelId) + "\n" + ReadFileLib('AtahansTurtle.js')))
        display(HTML('<script type="text/paperscript" canvas="canv%s">%s</script>'% \
                     (self._randHash, (ReadFile("level tools.js") + "\n" + ReadFile(self._levelId) + "\n" + ReadFileLib('AtahansTurtle.js')))))
    
    def loadLevel(self, levelId):
        self._levelId = "turtle level " + str(levelId) + ".js"

class SSSfirstsnake (SSSsnake):
    def turnLeft (self):
        raise Exception("I don't know what this command means!")
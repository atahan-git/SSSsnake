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
        newX = self._x + round(1 * math.sin(math.radians(self._rotation)), 1)
        newY = self._y - round(1 * math.cos(math.radians(self._rotation)), 1)
        self.goto(newX, newY)

class SSSfirstsnake (SSSsnake):
    def left (self):
        raise Exception("I don't know what this command means!")
# play.py

from constants import *
from game2d import *
from models import *
import math
import curses

cases=[[0,1,2],[3,4,5],[6,7,8], [0,3,6], [1,4,7],
        [2,5,8], [0,4,8], [2,4,6]]

class Play(object):
    """An instance controls a single game of TIC TAC TOE.
    
    INSTANCE ATTRIBUTES:
    _matrix     [list of Slots]
    _pics       [list of x/o objects]
    _turn       [turn of players: odd=player2, even=player1]
    _hint       [instance of GLabel, shows hints in the game]
    """
    
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getMatrix(self):
        return self._matrix 
    def getPics(self):
        return self._pics
    def getTurn(self):
        return self._turn
    def getWin(self):
        return self._whowon
    def getHint(self):
        return self._hint
    def getCase(self):
        return self._case
    
    # INITIALIZER
    def __init__(self):
        """Initializes a game of TIC TAC TOE"""
        self._pics=[]
        self._turn=0
        self._matrix=[]
        self.makeslots()
        self._hint=GLabel()
        self._whowon=None
        self._line=None
        self._case=None
        self._player1=Player(50, GAME_HEIGHT-50, "devil.png")
        self._player2=Player(GAME_WIDTH-50, GAME_HEIGHT-50, "angel.png")
        self._current=GEllipse(x=50, y=GAME_HEIGHT-50, 
            fillcolor=colormodel.CYAN, height=90, width=90)
        self._highlight=GEllipse()


    # UPDATE METHODS
    def Player1(self):
        return self._turn%2==0

    def make_move(self, s):
        """creates a temporary GImage corresponding to player 
        turn and appends it to the list of pics"""  
        if s.isnotClicked():  
            self._hint=GLabel()
            if self.Player1():
                temp=TicX(s.getXpos(), s.getYpos())
                self._current=GEllipse(x=GAME_WIDTH-50, y=GAME_HEIGHT-50, 
                        fillcolor=colormodel.MAGENTA, height=90, width=90)
                
            else:
                temp=TicY(s.getXpos(), s.getYpos())
                self._current=GEllipse(x=50, y=GAME_HEIGHT-50, 
                        fillcolor=colormodel.CYAN, height=90, width=90)
            self._pics.append(temp)
            self._turn+=1

        else:
            self._hint=GLabel(text="Try Again!", x=240, y=45, 
                font_name="ComicSansBold", font_size=18)

        
    # DRAW METHOD
    def draw(self, view):
        """"Draws the bricks and the paddle
        
        Parameter view: the view of the game
        Precondition: view is an instance of GView
        """
        for x in self.getMatrix():
            x.draw(view)
        for y in self.getPics():
            y.draw(view)
        self._highlight.draw(view)
        self._hint.draw(view)
        self._current.draw(view)
        self._player1.draw(view)
        self._player2.draw(view)


    # HELPER METHODS FOR HOVER RESPONSE
    def setHigh(self):
        if self.getWin()==0:
            self._current=GEllipse()
            self._highlight=GEllipse(x=GAME_WIDTH-50, y=GAME_HEIGHT-50, 
                        fillcolor=colormodel.YELLOW, height=120, width=120)
            
        elif self.getWin()==1:
            self._current=GEllipse()
            self._highlight=GEllipse(x=50, y=GAME_HEIGHT-50, 
                        fillcolor=colormodel.YELLOW, height=120, width=120)
        elif self.if_over()==True:
            self._current=GEllipse()
            
        

    def changeColor(self, p):

        for x in self.getMatrix():
            if x.hovers(p[0], p[1]):
                    x.setLineCol(colormodel.YELLOW)
            else: 
                    x.setLineCol(colormodel.RED)
                    
    def if_over(self):
        if len(self._pics)==9:
            self._hint=GLabel(text="Press R to Replay!", x=240, y=45, 
                font_name="ComicSansBold", font_size=18)
            return True

    # ADD ANY ADDITIONAL METHODS (FULLY SPECIFIED) HERE
    def makeslots(self):
        """creates the list of boxes"""
        p=list_of_x()
        o=list_of_y()
        for i in range(0, len(p)):
            for j in range(0, len(o)):
                x=(p[i], o[j])
                y=list(x)
                u=Slots(y[0], y[1])
                self._matrix.append(u)

    def wins(self):
        for x in cases:
            j=self._matrix[x[0]].whoClicked()==0
            k=self._matrix[x[1]].whoClicked()==0
            l=self._matrix[x[2]].whoClicked()==0

            f=self._matrix[x[0]].whoClicked()==1
            g=self._matrix[x[1]].whoClicked()==1
            h=self._matrix[x[2]].whoClicked()==1
            if j and k and l:
                self._case=x
                self._whowon=0
                self._hint=GLabel(text="Press R to Replay!", x=240, y=45, 
                font_name="ComicSansBold", font_size=18)
                return True

            elif f and g and h:
                self._case=x
                self._whowon=1
                self._hint=GLabel(text="Press R to Replay!", x=240, y=45, 
                font_name="ComicSansBold", font_size=18)
                return True

    def lineDraw(self, x, view):
        x1=self._matrix[x[0]].getXpos()
        y1=self._matrix[x[0]].getYpos()
        x2=self._matrix[x[2]].getXpos()
        y2=self._matrix[x[2]].getYpos()
        self._line=GPath(points=[x1, y1, x2,y2], linewidth=6, 
            linecolor=colormodel.MAGENTA)
        self._line.draw(view)


#HELPER FUNCTION

def list_of_x():
    start=(GAME_WIDTH-308)/2
    i=0
    lef_pos=[]
    while i<3:
        lef_pos.append(start+(slot_side+4)*i)
        i+=1
    return lef_pos

def list_of_y():
    start=60
    i=0
    top_pos=[]
    while i<3:
        top_pos.append(start+(slot_side+4)*i)
        i+=1
    return top_pos

    

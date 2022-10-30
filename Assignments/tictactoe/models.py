from constants import *
from game2d import *

class Slots(GRectangle):
    """instance of Grectangle.
    An object that displays the grid.
    """
    
    def getXpos(self):
        """Returns: the current x-coordinate of the slot"""
        return self.x
    
    def getYpos(self):
        """Returns: the Y-coordinate of the slot"""
        return self.y

    def isnotClicked(self):
        if self.isclicked:
            return False
        else:
            return True
    def isClicked(self):
        return self.isclicked

    def whoClicked(self):
        return self.who_clicked

    def use_slot(self, player):
        """Updates the _isclicked status, and assigns the appropriate player to who_clicked
        zero if player1; 1 if player2"""
        self.isclicked=True
        self.who_clicked=player
    
    def collides(self, touch):
        return self.contains(touch.x, touch.y)

    def hovers(self, x, y):
        return self.contains(x, y)

    def setLineCol(self, col):
        self.linecolor=col

    def setWidth(self, s):
        self.linewidth=s
        
    def __init__(self, x1, y1):
        super(Slots, self).__init__(left=x1, bottom=y1, height=slot_side, 
            width=slot_side, linewidth=lwidth, linecolor=colormodel.RED)
        self.isclicked=False
        self.who_clicked=None

class Button(GRectangle):
    """instance of Grectangle. A button"""
    def getXpos(self):
        """Returns: the current x-coordinate of the button"""
        return self.x
    
    def getYpos(self):
        """Returns: the Y-coordinate of the button"""
        return self.y

    def getText(self):
        return self._text

    def setColor(self, col):
        self.fillcolor=col
        self._text.fillcolor=col

    def hovers(self, x, y):
        return self.contains(x, y)

    def __init__(self, x1, y1, h1, w1, text1, view):
        super(Button, self).__init__(x=x1, y=y1, height=h1, width=w1, 
            linecolor=colormodel.BLACK, linewidth=1, fillcolor=colormodel.CYAN)
        self._text=GLabel(text=text1, font_name="ComicSansBold", font_size=18,
                            y=y1, x=x1, fillcolor=colormodel.CYAN)

    def collides(self, touch):
        return self.contains(touch.x, touch.y)

class TicX(GImage):
    def __init__(self, x1, y1):
        super(TicX, self).__init__(x=x1, y=y1, height=imgsize, width=imgsize)
        self.source="x.png"

class TicY(GImage):
    def __init__(self, x1, y1):
        super(TicY, self).__init__(x=x1, y=y1, height=imgsize, width=imgsize)
        self.source="o.png"

class Player(GImage):
    def __init__(self, x1, y1, s):
        super(Player, self).__init__(x=x1, y=y1, height=plysize, width=plysize)
        self.source=s


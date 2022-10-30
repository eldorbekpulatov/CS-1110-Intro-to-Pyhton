# play.py
# Eldor Bekpulatov (eb654) and Joe Fuentes (jrf268)
# November 28, 2016
"""Subcontroller module for Breakout

This module contains the subcontroller to manage a single game in the Breakout App. 
Instances of Play represent a single game.  If you want to restart a new game, you are 
expected to make a new instance of Play.

The subcontroller Play manages the paddle, ball, and bricks.  These are model objects.  
Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Piazza and we will answer."""
from constants import *
from game2d import *
from models import *
import math


# PRIMARY RULE: Play can only access attributes in models.py via getters/setters
# Play is NOT allowed to access anything in breakout.py (Subcontrollers are not
# permitted to access anything in their parent. To see why, take CS 3152)


################################################################
# Our Sound effects for Cheer and Boo were downloaded from
# "https://www.freesoundeffects.com/free-sounds/applause-10033/"
################################################################

class Play(object):
    """An instance controls a single game of breakout.
    
    This subcontroller has a reference to the ball, paddle, and bricks. It animates the 
    ball, removing any bricks as necessary.  When the game is won, it stops animating.  
    You should create a NEW instance of Play (in Breakout) if you want to make a new game.
    
    If you want to pause the game, tell this controller to draw, but do not update.  See 
    subcontrollers.py from Lecture 25 for an example.
    
    INSTANCE ATTRIBUTES:
        _paddle [Paddle]: the paddle to play with 
        _bricks [list of Brick]: the list of bricks still remaining 
        _ball   [Ball, or None if waiting for a serve]:  the ball to animate
        _tries  [int >= 0]: the number of tries left
        _score [int >=0]: number of bricks broken
        _bounceSound  [Sound] : sound to play when ball hits the paddle
        _winSound        [Sound] : sound to play when player wins
        _failSound         [Sound] : sound to play when player loses
        _wallSound       [Sound] : sound to play when ball hits the walls
        _brickSound      [Sound] : sound to play when ball hits the bricks
    
    As you can see, all of these attributes are hidden.  You may find that you want to
    access an attribute in class Breakout. It is okay if you do, but you MAY NOT ACCESS 
    THE ATTRIBUTES DIRECTLY. You must use a getter and/or setter for any attribute that 
    you need to access in Breakout.  Only add the getters and setters that you need for 
    Breakout.
    
    You may change any of the attributes above as you see fit. For example, you may want
    to add new objects on the screen (e.g power-ups).  If you make changes, please list
    the changes with the invariants.
    
    Our Sound effects for Cheer and Boo2 and applause6 were downloaded from
    "https://www.freesoundeffects.com/free-sounds/applause-10033/"
                  
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getBricks(self):
        """Returns: the list of instances of the class Bricks"""
        return self._bricks
    
    def getPaddle(self):
        """Returns: the instance of the class Paddle"""
        return self._paddle
    
    def getBall(self):
        """Returns: the instance of the class Ball"""
        return self._ball
    
    def getTries(self):
        """Returns: the number of tries left"""
        return self._tries
    
    def setTries(self, t):
        """Modifies the number of tries left"""
        self._tries=t
        
    def getScore(self):
        """Returns: the score"""
        return self._score
    
    # INITIALIZER (standard form) TO CREATE PADDLES AND BRICKS
    def __init__(self):
        """Initializer: make a game of breakout. Creates bricks, a ball, and a
        paddle. """
        self._bricks=[]
        self.buildBricks()
        self._paddle=Paddle(x=GAME_WIDTH/2.0, y=PADDLE_OFFSET,
                            height=PADDLE_HEIGHT,
                            width=PADDLE_WIDTH, fillcolor=colormodel.BLACK)
        self._ball=None
        self._tries=NUMBER_TURNS
        self._score=0
        self._bounceSound = Sound('bounce.wav')
        self._winSound=Sound('cheer.wav')
        self._failSound=Sound('boo2.wav')
        self._wallSound=Sound("saucer2.wav")
        self._brickSound=Sound("plate2.wav")
        
   
    # UPDATE METHODS TO MOVE PADDLE, SERVE AND MOVE THE BALL
    def updatePaddle(self, inp):
        """Moves the paddle left or right.
        
        Parameter inp: an input from the keyboard
        Precondition: inp is an instance of GInput
        """
        assert isinstance(inp, GInput)
        
        rang=[.5*PADDLE_WIDTH+(BRICK_SEP_H),
              GAME_WIDTH-(.5*PADDLE_WIDTH)-(BRICK_SEP_H)]
        cur=self.getPaddle().getXpos()
        if inp.is_key_down('left'):
            cur-= ANIMATION_STEP
        if inp.is_key_down('right'):
            cur += ANIMATION_STEP
        if cur<=max(rang) and cur>=min(rang):
            self.getPaddle().setXpos(cur)
        
    def moveBall(self):
        """Moves the ball by updating its x and y coordinates with vx and vy in class Ball.
        Also, it makes sure that the ball stays within the walls and makes a sound
        every time in contact with the wall"""
        
        self.getBall().moveYpos()
        self.getBall().moveXpos()
        self.getBall().withinWalls(self._wallSound)
        
    def serveBall(self):
        """Initializes an instance of Ball"""
        self._ball=Ball(GAME_WIDTH/2.0, GAME_HEIGHT/2.0,
                        BALL_DIAMETER, "beach-ball.png")
        
    # DRAW METHOD TO DRAW THE PADDLES, BALL, AND BRICKS
    def draw(self, view):
        """"Draws the bricks and the paddle
        
        Parameter view: the view of the game
        Precondition: view is an instance of GView
        """
        assert isinstance(view, GView)
        for x in self.getBricks():
            x.draw(view)
        self.getPaddle().draw(view)
        
    def drawBall(self, view):
        """Parameter view: the view of the game
        Precondition: view is an instance of GView
        """
        assert isinstance(view, GView)
        
        self.getBall().draw(view)
        
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION
    def delBrick(self):
        """Checks for collision in the list of bricks. If collides, then removes the brick and
        changes the velocities of the ball depending on the position of the ball with
        respect to the brick. If the ball is under or above the brick, then changes the vy. 
        Everywherelse, only changes the vx. """
        #got help with this one from Rohit, my AEW instructor
        for x in self.getBricks():
            if x.collides(self.getBall())==True:
                ###delete method
                self.getBricks().remove(x)
                self._score+=1
                ###bounce method
                vx=self.getBall().getVX()
                vy=self.getBall().getVY()
                #j: True if ball's center is less than y-coordinate of the bottom side of the brick
                j=x.getYpos()+(BRICK_HEIGHT/2.0)<self.getBall().getYpos()
                #k: True if ball's center is greater than y-coordinate of the top side of the brick
                k=x.getYpos()-(BRICK_HEIGHT/2.0)>self.getBall().getYpos()
                #l: True if the x coordinte of the center of the ball is within the width of the brick
                l=x.getXpos()-(BRICK_WIDTH/2.0)<self.getBall().getXpos()<x.getXpos()+(BRICK_WIDTH/2.0)
                if (j or k) and (l): #if from above or below the brick
                    self.getBall().setVY(-1*vy)
                else: #else, from the sides
                    self.getBall().setVX(-1*vx)
                #play sound
                self._brickSound.play()
                if len(self.getBricks())==0:
                    self._winSound.play()

    def updateTries(self):
        """Returns: True if the ball hits the bottom of the window.
        Also, passes a sound object to play when player loses a ball."""
        
        if self.getBall().wentUnder(self._failSound):
            return True
            
    def paddleBounce(self):
        """Bounces the ball off the paddle, if it collides with the paddle
        If the ball hits the corner of the paddle (defined by the left or right
        1/4th of the paddle) the x and y velocity of the ball will change signs.
        If the ball hits the middle of the paddle, only the y velocity changes.
        The _bouncesSound will play."""
        
        if self.getPaddle().collides(self.getBall()) and self.getBall().getVY()<0:
             ###bounce method
            vx=self.getBall().getVX()
            vy=self.getBall().getVY()
            if self.paddleControl():
                self.getBall().setVX(-1*vx)
                self.getBall().setVY(-1*vy)
            else:
                self.getBall().setVY(-1*vy)
            self._bounceSound.play()
    
    def getLeftOneFourth(self):
        """Returns Left 1/4th of the paddle as a Paddle"""
        
        return Paddle(width=PADDLE_WIDTH/4.0, height=PADDLE_HEIGHT,
                            x=self.getPaddle().getXpos()-(PADDLE_WIDTH*(3.0/4)),
                            y=self.getPaddle().getYpos())
       
    
    def getRightOneFourth(self):
        """Returns Right 1/4th of the paddle as Paddle"""
        
        return Paddle(width=PADDLE_WIDTH/4.0, height=PADDLE_HEIGHT,
                    x=self.getPaddle().getXpos()+(PADDLE_WIDTH*(3.0/4)),
                    y=self.getPaddle().getYpos())
        
        
    def paddleControl(self):
        """Returns: True if the ball hits left or the right 1/4th of the paddle"""
        
        left=self.getLeftOneFourth().collides(self.getBall())
        right=self.getRightOneFourth().collides(self.getBall())
        if left or right:
            return True
            
    # ADD ANY ADDITIONAL METHODS (FULLY SPECIFIED) HERE
    
    def buildBricks(self):
        """Creates the arrangement of bricks.
        
        Creates a list of Brick instances, each with different left-coordinate,
        top-coordinate and color. Uses the helper functions to generate a list of
        left-coordinates for the bricks in a row. Uses helper function to generate
        a list of top-coordinates for the brick rows. Then appends Brick instances
        into the attribute _bricks, each with unique left-top-color. """
        
        colorlist=[colormodel.RED,colormodel.RED,colormodel.ORANGE,
                   colormodel.ORANGE,colormodel.YELLOW, colormodel.YELLOW,
                   colormodel.GREEN,colormodel.GREEN,
                   colormodel.CYAN, colormodel.CYAN]
        
        p=list_of_xcoordinates()
        o=list_of_ycoordinates()
        for i in range(0, len(p)):
            for j in range(0, len(o)):
                x=(p[i], o[j], colorlist[j%10])
                y=list(x)
                self._bricks.append(Brick(left=y[0], top=y[1], width=BRICK_WIDTH,
                                          height=BRICK_HEIGHT, fillcolor=y[2]))

def list_of_xcoordinates():
    """Returns: a list with coordinates to be used by each brick's left attribute"""
    lstart=BRICK_SEP_H/2.0
    i=0
    lefpos=[]
    while i<BRICKS_IN_ROW:
        lefpos.append(lstart+(BRICK_WIDTH+BRICK_SEP_H)*i)
        i+=1
    return lefpos

def list_of_ycoordinates():
    """Returns: a list with coordinates to be used by each brick's top attribute"""
    tstart=GAME_HEIGHT-BRICK_Y_OFFSET
    ypos=[]    
    j=0
    while j<BRICK_ROWS:
        ypos.append(tstart-(BRICK_HEIGHT+BRICK_SEP_V)*j)
        j+=1
    return ypos
    
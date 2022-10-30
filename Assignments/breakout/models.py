# models.py
# Eldor Bekpulatov (eb654) and Joe Fuentes (jrf268)
# November 28, 2016
"""Models module for Breakout

This module contains the model classes for the Breakout game. That is anything that you
interact with on the screen is model: the paddle, the ball, and any of the bricks.

Technically, just because something is a model does not mean there has to be a special 
class for it.  Unless you need something special, both paddle and individual bricks could
just be instances of GRectangle.  However, we do need something special: collision 
detection.  That is why we have custom classes.

You are free to add new models to this module.  You may wish to do this when you add
new features to your game.  If you are unsure about whether to make a new class or 
not, please ask on Piazza."""
import random # To randomly generate the ball velocity
from constants import *
from game2d import *


# PRIMARY RULE: Models are not allowed to access anything except the module constants.py.
# If you need extra information from Play, then it should be a parameter in your method, 
# and Play should pass it as a argument when it calls the method.


class Paddle(GRectangle):
    """An instance is the game paddle.
    
    This class contains a method to detect collision with the ball, as well as move it
    left and right.  You may wish to add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getXpos(self):
        """Returns: the current x-coordinate of the Paddle"""
        return self.x
    
    def getYpos(self):
        """Returns: the Y-coordinate of the Paddle"""
        return self.y
    
    def setXpos(self, x1):
        """Modifies the x-position of the Paddle.
        
        Parameter x1: the position of the paddle
        Precondition: x1 is a number greater than 0, less than the GAME_WIDTH
        """
        assert type(x1) in [int, float]  and 0<=x1<=GAME_WIDTH
        self.x=x1
    
    # INITIALIZER TO CREATE A NEW PADDLE
    
    # METHODS TO MOVE THE PADDLE AND CHECK FOR COLLISIONS
    def collides(self,ball):
        """Returns: True if the ball collides with the Paddle.
        
        Parameter ball: The ball to check
        Precondition: ball is of class Ball"""
        assert isinstance(ball, Ball)
        
        xplus=ball.getXpos()+(BALL_DIAMETER/2)
        xminus=ball.getXpos()-(BALL_DIAMETER/2)
        yplus=ball.getYpos()+(BALL_DIAMETER/2)
        yminus=ball.getYpos()-(BALL_DIAMETER/2)
        tl=self.contains(xminus, yplus)
        tr=self.contains(xplus, yplus)
        bl=self.contains(xminus, yminus)
        br=self.contains(xplus, yminus)
        
        if (tl or tr or bl or br)==True:
            return True
        
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


class Brick(GRectangle):
    """An instance is the game Brick.
    
    This class contains a method to detect collision with the ball.  You may wish to 
    add more features to this class.
    
    The attributes of this class are those inherited from GRectangle.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
        y [int]: y position of the brick
        x [int]: x position of the brick
        width [int]: width of the brick
        height [int]: height of the brick
        color [Colormodel] : color of the brick
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getYpos(self):
        """Returns: the Y-coordinate of the Brick"""
        return self.y
    
    def getXpos(self):
        """Returns: the x-coordinate of the Brick"""
        return self.x
    # INITIALIZER TO CREATE A BRICK

    # METHOD TO CHECK FOR COLLISION
    def collides(self,ball):
        """Returns: True if the ball collides with this brick
        
        Parameter ball: The ball to check
        Precondition: ball is of class Ball"""
        assert isinstance(ball, Ball)
        
        xplus=ball.getXpos()+(BALL_DIAMETER/2)
        xminus=ball.getXpos()-(BALL_DIAMETER/2)
        yplus=ball.getYpos()+(BALL_DIAMETER/2)
        yminus=ball.getYpos()-(BALL_DIAMETER/2)
        tl=self.contains(xminus, yplus)
        tr=self.contains(xplus, yplus)
        bl=self.contains(xminus, yminus)
        br=self.contains(xplus, yminus)
        
        if (tl or tr or bl or br)==True:
            return True
        
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


class Ball(GImage):
    """Instance is a game ball.
    
    We extend GEllipse because a ball must have additional attributes for velocity.
    This class adds this attributes and manages them.
    
    INSTANCE ATTRIBUTES:
        _vx [int or float]: Velocity in x direction 
        _vy [int or float]: Velocity in y direction 
    
    The class Play will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with no
    setters for the velocities.
    
    How? The only time the ball can change velocities is if it hits an obstacle
    (paddle or brick) or if it hits a wall.  Why not just write methods for these
    instead of using setters?  This cuts down on the amount of code in Gameplay.
    
    NOTE: The ball does not have to be a GEllipse. It could be an instance
    of GImage (why?). This change is allowed, but you must modify the class
    header up above.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    def getXpos(self):
        """Returns: the x-coordinate of the Ball"""
        return self.x
    
    def getYpos(self):
        """Returns: the y-coordinate of the Ball"""
        return self.y
    
    def setVX(self, vx):
        """Modifies the x-velocity of the Ball"""
        self._vx=vx
        
    def setVY(self,vy):
        """Modifies the y-velocity of the Ball"""
        self._vy=vy
        
    def getVX(self):
        """Returns: the x-velocity of the Ball"""
        return self._vx
    
    def getVY(self):
        """Returns: the y-velocity of the Ball"""
        return self._vy
    
    # INITIALIZER TO SET RANDOM VELOCITY
    def __init__(self, x1, y1, dia, name):
        """Initializer: make a ball at position (x1, y1), with diameter dia,
        and name.
        
        The y velocity of the ball is BALL_YVELOCITY.
        The x velocity of the ball is a randomly chosen positive or negative
        number from 1.0 to 5.0.
        
        Parameter x1: The x coordinate of the original position of the ball
        Precondition: x1 is a number (float or int) >=0
        
        Parameter y1: The y coordinate of the original position of the ball
        Precondition: y1 is a number (float or int) >=0
        
        Parameter dia: The diameter of the ball
        Precondition: dia is a number (float or int) >=0
        
        Parameter name: The name of the ball
        Precondition: name is a valid string 
        """
        assert type(x1) in [int, float] and x1>=0
        assert type(y1) in [int, float] and y1>=0
        assert type(dia) in [int, float] and dia>=0
        assert type(name)==str
        #used online service to call the initializer of the parent class
        super(Ball, self).__init__(x=x1, y=y1, height=dia, width=dia, source=name)
        self._vy=-3.0
        self._vx = random.uniform(1.0,5.0) 
        self._vx = self._vx * random.choice([-1, 1])
        
    # METHODS TO MOVE AND/OR BOUNCE THE BALL
    def moveXpos(self):
        """Adds x-velocity to the X-coordinate of the Ball"""
        self.x+=self._vx
        
    def moveYpos(self):
        """Adds y-velocity to the Y-coordinate of the Ball"""
        self.y+=self._vy
    
    def withinWalls(self, sound):
        """Changes the velocity of the wall accordingly depending on which wall
        the ball hits. If the ball hits the top wall, the y velocity will turn
        negative. If the ball hits a side wall, the x velocity will be
        multiplied by -1.
        A sound will play if the ball hits any of the three walls.
        
        Parameter sound: the sound when the ball hits a wall
        Precondition: sound is an instance of Sound"""
        
        assert isinstance(sound, Sound)

        n=self.getYpos()+(BALL_DIAMETER/2.0)
        w=self.getXpos()-(BALL_DIAMETER/2.0)
        e=self.getXpos()+(BALL_DIAMETER/2.0)
        
        if n>=GAME_HEIGHT:
            cvy=self.getVY()
            self.setVY(cvy*-1)
            sound.play()
        if w<=0 or e>=GAME_WIDTH:
            cvx=self.getVX()
            self.setVX(cvx*-1)
            sound.play()
            
    def wentUnder(self, sound):
        """Returns: True if the ball hits the bottom of the screen
        
        Parameter sound: the sound when the ball hits the bottom of the screen
        Precondition: sound is an instance of Sound
        """
        assert isinstance(sound, Sound)
        s=self.getYpos()-(BALL_DIAMETER/2.0)
        if s<=0:
            sound.play()
            return True
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE

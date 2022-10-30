# breakout.py
# Eldor Bekpulatov (eb654) and Joe Fuentes (jrf268)
# November 28, 2016
"""Primary module for Breakout application

This module contains the main controller class for the Breakout application. There is no
need for any any need for additional classes in this module.  If you need more classes, 
99% of the time they belong in either the play module or the models module. If you 
are ensure about where a new class should go, 
post a question on Piazza."""
from constants import *
from game2d import *
from play import *


# PRIMARY RULE: Breakout can only access attributes in play.py via getters/setters
# Breakout is NOT allowed to access anything in models.py

class Breakout(GameApp):
    """Instance is the primary controller for the Breakout App
    
    This class extends GameApp and implements the various methods necessary for processing 
    the player inputs and starting/running a game.
    
        Method start begins the application.
        
        Method update either changes the state or updates the Play object
        
        Method draw displays the Play object and any other elements on screen
    
    Because of some of the weird ways that Kivy works, you SHOULD NOT create an
    initializer __init__ for this class.  Any initialization should be done in
    the start method instead.  This is only for this class.  All other classes
    behave normally.
    
    Most of the work handling the game is actually provided in the class Play.
    Play should have a minimum of two methods: updatePaddle(input) which moves
    the paddle, and updateBall() which moves the ball and processes all of the
    game physics. This class should simply call that method in update().
    
    The primary purpose of this class is managing the game state: when is the 
    game started, paused, completed, etc. It keeps track of that in an attribute
    called _state.
    
    INSTANCE ATTRIBUTES:
        view    [Immutable instance of GView; it is inherited from GameApp]:
                the game view, used in drawing (see examples from class)
        input   [Immutable instance of GInput; it is inherited from GameApp]:
                the user input, used to control the paddle and change state
        _state  [one of STATE_INACTIVE, STATE_COUNTDOWN, STATE_PAUSED, STATE_ACTIVE, STATE_NEWGAME]:
                the current state of the game represented a value from constants.py
        _game   [Play, or None if there is no game currently active]: 
                the controller for a single game, which manages the paddle, ball, and bricks
        _mssg   [GLabel, or None if there is no message to display]
                the currently active message
    
    STATE SPECIFIC INVARIANTS: 
        Attribute _game is only None if _state is STATE_INACTIVE.
    
    For a complete description of how the states work, see the specification for the
    method update().
    
    You may have more attributes if you wish (you might need an attribute to store
    any text messages you display on the screen). If you add new attributes, they
    need to be documented here.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    
        _last_keys [int >= 0, number of keys previous animation frame]:
                                number of keys held down last frame
        _paused [bool] : current state of the game, paused or not
        
        _frames [int >=0] : number that represents the current frame
        """
    
    # DO NOT MAKE A NEW INITIALIZER!
    
    # THREE MAIN GAMEAPP METHODS
    def start(self):
        """Initializes the application.
        
        This method is distinct from the built-in initializer __init__ (which you 
        should not override or change). This method is called once the game is running. 
        You should use it to initialize any game specific attributes.
        
        This method should make sure that all of the attributes satisfy the given 
        invariants. When done, it sets the _state to STATE_INACTIVE and create a message 
        (in attribute _mssg) saying that the user should press to play a game."""
        # IMPLEMENT ME
        self._last_keys = 0
        self._paused=False
        self._frames=0
        self._game=None
        self._state=STATE_INACTIVE
        self._mssg=GLabel(text="Press any key to play", font_size=36, font_name="ComicSans",
                          halign="center", valign="middle", x=GAME_WIDTH/2.0, y=GAME_HEIGHT/2.0)
        
        
    def update(self,dt):
        """Animates a single frame in the game.
        
        ALWAYS CHECKS FOR CURRENT STATE AND IF PAUSED!
        
        It is the method that does most of the work. It is NOT in charge of playing the
        game.  That is the purpose of the class Play.  The primary purpose of this
        game is to determine the current state, and -- if the game is active -- pass
        the input to the Play object _game to play the game.
        
        As part of the assignment, you are allowed to add your own states.  However, at
        a minimum you must support the following states: STATE_INACTIVE, STATE_NEWGAME,
        STATE_COUNTDOWN, STATE_PAUSED, and STATE_ACTIVE.  Each one of these does its own
        thing, and so should have its own helper.  We describe these below.
        
        STATE_INACTIVE: This is the state when the application first opens.  It is a 
        paused state, waiting for the player to start the game.  It displays a simple
        message on the screen.
        
        STATE_NEWGAME: This is the state creates a new game and shows it on the screen.  
        This state only lasts one animation frame before switching to STATE_COUNTDOWN.
        
        STATE_COUNTDOWN: This is a 3 second countdown that lasts until the ball is 
        served.  The player can move the paddle during the countdown, but there is no
        ball on the screen.  Paddle movement is handled by the Play object.  Hence the
        Play class should have a method called updatePaddle()
        
        STATE_ACTIVE: This is a session of normal gameplay.  The player can move the
        paddle and the ball moves on its own about the board.  Both of these
        should be handled by methods inside of class Play (NOT in this class).  Hence
        the Play class should have methods named updatePaddle() and updateBall().
        
        STATE_PAUSED: Like STATE_INACTIVE, this is a paused state. However, the game is
        still visible on the screen.
        
        The rules for determining the current state are as follows.
        
        STATE_INACTIVE: This is the state at the beginning, and is the state so long
        as the player never presses a key.  In addition, the application switches to 
        this state if the previous state was STATE_ACTIVE and the game is over 
        (e.g. all balls are lost or no more bricks are on the screen).
        
        STATE_NEWGAME: The application switches to this state if the state was 
        STATE_INACTIVE in the previous frame, and the player pressed a key.
        
        STATE_COUNTDOWN: The application switches to this state if the state was
        STATE_NEWGAME in the previous frame (so that state only lasts one frame).
        
        STATE_ACTIVE: The application switches to this state after it has spent 3
        seconds in the state STATE_COUNTDOWN.
        
        STATE_PAUSED: The application switches to this state if the state was 
        STATE_ACTIVE in the previous frame, the ball was lost, and there are still
        some tries remaining.
        
        You are allowed to add more states if you wish. Should you do so, you should 
        describe them here.
        
        STATE_GAMEOVER: The application switches to this state only if the previous
        frame was STATE_ACTIVE and the ball was lost and the number of tries left
        reached zero.
        
        STATE_COMPLETE: The application switches to this state only if the previous
        frame was STATE_ACTIVE and there were no more Bricks left to destroy.
        
        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        assert type(dt) in [int, float]
        
        # IMPLEMENT ME
        self._checkPaused()
        now=self._determineState()
        if self._state==STATE_INACTIVE:
            self._mssg=GLabel(text="Press any key to play", font_size=36,
                        font_name="ComicSans", halign="center", valign="middle",
                        x=GAME_WIDTH/2.0, y=GAME_HEIGHT/2.0)
            self._changeState(STATE_NEWGAME)
               
        elif now == STATE_NEWGAME:
            self._game=Play()
            self._mssg=GLabel()
            self._state=STATE_COUNTDOWN
            
        elif now==STATE_COUNTDOWN:
            self._countdownState()
                
        elif now==STATE_PAUSED:
            self._pausedState()
            
        elif now==STATE_GAMEOVER:
            self._gameoverState()
            
        elif now==STATE_COMPLETE:
            self._completeState()
        
        elif now ==STATE_ACTIVE:
            self._activeState()
        
            
    def draw(self):
        """Draws the game objects to the view.
        
        Every single thing you want to draw in this game is a GObject.  To draw a GObject 
        g, simply use the method g.draw(self.view).  It is that easy!
        
        Many of the GObjects (such as the paddle, ball, and bricks) are attributes in Play. 
        In order to draw them, you either need to add getters for these attributes or you 
        need to add a draw method to class Play.  We suggest the latter.  See the example 
        subcontroller.py from class."""
        # IMPLEMENT ME
        if self._state==STATE_INACTIVE:
            self._mssg.draw(self.view)
        if self._state==STATE_COUNTDOWN:
            self._game.draw(self.view)
            self._mssg.draw(self.view)
        if self._state==STATE_ACTIVE:
            self._mssg.draw(self.view)
            self._game.draw(self.view)
            self._game.drawBall(self.view)
        if self._state==STATE_PAUSED:
            self._mssg.draw(self.view)
        if self._state==STATE_COMPLETE:
            self._mssg.draw(self.view)
        if self._state==STATE_GAMEOVER:
            self._mssg.draw(self.view)
            
        
        
    # HELPER METHODS FOR THE STATES GO HERE
    def _determineState(self):
        """Returns: the current state of the game"""
        return self._state
    
    def _activeState(self):
        """ If the game is in play, displays the score and calls several
        functions to run the game. If the player is out of tries, the game
        is put in the paused state. If the player has eliminated all the
        bricks, the game is put in the complete state. If the game is paused,
        displays the pause menu."""
        
        if not self._paused:
            self._mssg=GLabel(text=`self._game.getScore()`, font_size=25,
            font_name="ComicSans", halign="center", valign="middle",
            x=20, y=GAME_HEIGHT-20)
            self._game.updatePaddle(self.input)
            self._game.moveBall()
            self._game.delBrick()
            self._game.paddleBounce()
            if self._game.updateTries()==True:
                c=self._game.getTries()-1
                self._game.setTries(c)
                if self._game.getTries()>0:
                    self._state=STATE_PAUSED
                else:
                    self._frames=0
                    self._state=STATE_GAMEOVER
            if len(self._game.getBricks())==0:
                self._state=STATE_COMPLETE
        else:
            self._mssg=GLabel(text="Paused...", font_size=30, font_name="ComicSans",
                              x= 75, y=40)
        
            
    def _countdownState(self):
        """If the game is not paused, displays the countdown. Once the
        countdown is finished, the game is started. If the game is paused,
        displays the pause menu."""
        
        if not self._paused:
            time=[3, 2, 1, "GO!"]
            self._game.updatePaddle(self.input)
            self._frames+=1
            p=int(self._frames/60)
            self._mssg=GLabel(text=`time[p]`, font_size=56, font_name="ComicSans",
                  halign="center", valign="middle", x=GAME_WIDTH/2.0, y=GAME_HEIGHT/2.0)
            if p>=3:
                self._mssg=GLabel()
                self._game.serveBall()
                self._state=STATE_ACTIVE
        else:
            self._mssg=GLabel(text="Paused...", font_size=30, font_name="ComicSans",
                              x= 75, y=40)
    
    def _pausedState(self):
        """Displays the amount of tries left. If the player is out of tries,
        puts the game in the game over state. Changes to the countdown state."""
        
        self._mssg=GLabel(text=`self._game.getTries()`+" tries left! \n Press to continue...",
            font_size=50, font_name="ComicSans", halign="center", valign="middle",
            x=GAME_WIDTH/2.0, y=GAME_HEIGHT/2.0)
        self._frames=0
        self._changeState(STATE_COUNTDOWN)
        
    def _gameoverState(self):
        """Displays the game over message and changes the state to
        the inactive state."""
        
        self._mssg=GLabel(text="GAME OVER! \n YOUR SCORE: "+ `self._game.getScore()`
            +"\n Press to play again!", font_size=50, font_name="ComicSans",
            halign="center", valign="middle", x=GAME_WIDTH/2.0, y=GAME_HEIGHT/2.0)
        self._changeState(STATE_INACTIVE)
    
    def _completeState(self):
        """Displays the well earned victory message. Changes the state to
        the inactive state."""
        
        self._mssg=GLabel(text="CONGRATS BRAAAH!!! \n You WON!", font_size=40,
                font_name="ComicSans", halign="center", valign="middle",
                x=GAME_WIDTH/2.0, y=GAME_HEIGHT/2.0)
        self._changeState(STATE_INACTIVE)
        self._frames=0
        
    def _checkPaused(self):
        """THIS FUNCTION WAS ADAPTED FROM THE DEMOS
        PRESENTED BY WALKER WHITE IN CLASS.
        
        Determines if the animation is paused, setting the attribute.
        
        The animation is paused when the user presses a SPECIFIC key (SPACEBAR).
        The rules for pressing a key are the same as state.py.  A key press is
        when a key is pressed for the FIRST TIME. We do not want the animation
        to pause and unpause while we hold down the key. The user must release
        the key and press it again to pause or unpause."""
        # Determine the current number of keys pressed
        curr_keys = self.input.is_key_down('spacebar')
        
        # Only change if we have just pressed the keys this animation frame
        change = curr_keys and self._last_keys== 0
        
        if change:
            self._paused = not self._paused
        
        # Update last_keys
        self._last_keys = curr_keys
        
        
    def _changeState(self, state):
        """THIS FUNCTION WAS ADAPTED FROM THE DEMOS
        PRESENTED BY WALKER WHITE IN CLASS.
        
        Determines the current state and assigns it to self.state
        
        This method checks for a key press, and if there is one, changes the state 
        to the next value.  A key press is when a key is pressed for the FIRST TIME.
        We do not want the state to continue to change as we hold down the key.  The
        user must release the key and press it again to change the state.
        
        Parameter state: the current state of the game
        Precondition: state is an int >= 0"""
        
        assert type(state)==int and int >= 0
        
        # Determine the current number of keys pressed
        curr_keys = self.input.key_count
        
        # Only change if we have just pressed the keys this animation frame
        change = curr_keys > 0 and self._last_keys == 0 
            
        if change:
            # Click happened.  Change the state
            self._state =state
            
        # Update last_keys
        self._last_keys= curr_keys
        

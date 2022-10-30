#tictactoe.py

from constants import *
from game2d import *
from play import *
from models import *




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

    INSTANCE ATTRIBUTES:

    input       [Instance of GInput inherited from GameApp]
    view        [Instance of GView inherited from  GameApp]
    _state      [one of the the game states: state_welcome, state_game, state_end]
    _game       [Instance of Play, or None in states end and welcome]
    _mssg       [Instance of Glabel from GameApp]
    _button1    [Instance of GRectangle]
    _last       [last click]
    _click      [instance of Sound object]
    """
    
    # DO NOT MAKE A NEW INITIALIZER!
    
    # THREE MAIN GAMEAPP METHODS
    def start(self):
        """Initializes the application."""
        self._state=state_welcome
        self._game=Play()
        self._mssg=GLabel(text="TIC TAC TOE", font_name="ComicSansBold", font_size=24,
                            y=410, x=GAME_WIDTH/2)
        self._button1=Button(GAME_WIDTH/2, 180, bttn_height, bttn_width, "2 Player Game", self.view)
        self._button2=Button(GAME_WIDTH/2, 300, bttn_height, bttn_width, "1 Player Game", self.view)
        self._last=None
        self._last_keys= 0
        self._click=Sound("click.wav")
        self._start=Sound("sound.wav")


    def update(self,dt):
        """Animates a single frame in the game.
        
        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        p=GMouse().p
        now=self._determineState()


        if now == state_welcome:
            self._mssg=GLabel(text="TIC TAC TOE", font_name="ComicSansBold", 
                font_size=24, y=410, x=GAME_WIDTH/2)
            self._game=Play()
            if self._button1.hovers(p[0], p[1]):
                self._button1.setColor(colormodel.RED)
            else: 
                self._button1.setColor(colormodel.CYAN)

            if self._button2.hovers(p[0], p[1]):
                self._button2.setColor(colormodel.RED)
            else: 
                self._button2.setColor(colormodel.CYAN)
            self._checkClick()
            self._quit()


        elif now == state_game:
            self._mssg=GLabel(text="TIC TAC TOE", font_name="ComicSansBold", 
                font_size=24, y=410, x=GAME_WIDTH/2)
            self._game.setHigh()
            game_on=self._game.if_over() or self._game.wins()
            self._game.changeColor(p)
            if not game_on:
                #self._game.changeColor(p)  
                self._pressGame()
            if game_on:
                if self._game.getWin()==0:
                    self._mssg=GLabel(text="Player 2 Won!", font_name="ComicSansBold", 
                        font_size=42, y=410, x=GAME_WIDTH/2)
                    
                elif self._game.getWin()==1:
                    self._mssg=GLabel(text="Player 1 Won!", font_name="ComicSansBold", 
                        font_size=42, y=410, x=GAME_WIDTH/2)
                    
                else:
                    self._mssg=GLabel(text="Tie!", font_name="ComicSansBold", 
                    font_size=42, y=410, x=GAME_WIDTH/2)
            self._replay()
            self._quit()


        elif now == state_comp:
            self._mssg=GLabel(text="TIC TAC TOE", font_name="ComicSansBold", 
                font_size=24, y=410, x=GAME_WIDTH/2)
            self._game.changeColor(p)
            self._pressGame()
            self._replay()
            self._quit()

            
    def draw(self):
        """Draws the game objects to the view."""
        if self._state ==state_welcome:
            self._mssg.draw(self.view)
            self._button1.draw(self.view)
            self._button1.getText().draw(self.view)
            self._button2.draw(self.view)
            self._button2.getText().draw(self.view)
            
        if self._state==state_game:
            self._game.draw(self.view)
            self._mssg.draw(self.view)
            if self._game.wins():
                self._game.lineDraw(self._game.getCase(), self.view)

        if self._state==state_comp:
            self._game.draw(self.view)
            self._mssg.draw(self.view)

        
    # HELPER METHODS FOR THE STATES GO HERE
    def _determineState(self):
        """Returns: the current state of the game"""
        return self._state


    def _checkClick(self):
        '''recognizes a click and starts a game based on user preference'''
        touch=self.input.touch
        if self._last==None and not touch is None:
            if self._button1.collides(touch):
                    self._start.play()
                    self._state=state_game
            if self._button2.collides(touch):
                    self._start.play()
                    self._state=state_comp
        self._last=touch


    def _pressGame(self):
        touch=self.input.touch
        if self._last==None and not touch is None:
            for x in self._game.getMatrix():
                if x.collides(touch):
                    self._click.play()
                    self._game.make_move(x)
                    x.use_slot(self._game.getTurn()%2)
        self._last=touch


    def _replay(self):
        curr_keys = self.input.is_key_down('r')
        # Only change if we have just pressed the keys this animation frame
        change = curr_keys and self._last_keys== 0
        if change:
            #changes the state to the main menu
            self._state = state_welcome 
            self._start.play()
        # Update last_keys
        self._last_keys = curr_keys


    def _quit(self):
        curr_keys = self.input.is_key_down('q')
        # Only change if we have just pressed the keys this animation frame
        change = curr_keys and self._last_keys== 0
        if change:
            #quits the game
            kivy.app.App.stop(self)
            sys.exit(0)  
        # Update last_keys
        self._last_keys = curr_keys
    
    
   
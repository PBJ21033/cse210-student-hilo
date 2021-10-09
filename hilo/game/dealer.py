from drawer import Drawer

class Dealer:
    '''The person who directs the game. Keeps track of score
    and controls the sequence of play.
    
    Attributes:
        keep_playing (bool): Whether the player continues to play
        score (int): The total number of points earned
        drawer (Drawer): Deals directly with cards
    '''

    def __init__(self):
        '''The class constructor.
        
        Args:
            self (Dealer): instance of Dealer
        '''
        self.keep_playing = True
        self.score = 0
        self.drawer = Drawer()

    def start_game(self):
        '''Starts game loop and controls sequence of play.
        
        Args:
            self (Dealer): instance of Dealer
        '''
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        
        repeat = True
        while repeat:
            user_choice = input('Higher or lower? [h/l] ')
            if user_choice.lower() == 'h':
                return True
            elif user_choice.lower() == 'l':
                return False

    def do_updates(self):
        pass

    def do_outputs(self):
        pass
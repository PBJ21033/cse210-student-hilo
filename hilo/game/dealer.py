from drawer import Drawer

class Dealer:
    '''The person who directs the game. Keeps track of score
    and controls the sequence of play.
    
    Attributes:
        keep_playing (bool): Whether the player continues to play
        score (int): The total number of points earned
        drawer (Drawer): Deals directly with cards'''

    def __init__(self):
        self.keep_playing = True
        self.score = 0
        self.drawer = Drawer()

    def start_game(self):
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        pass

    def do_updates(self):
        pass

    def do_outputs(self):
        pass
from drawer import Drawer

class Dealer:
    '''I will add documentation here later'''

    def __init__(self):
        self.keep_playing = True
        self.score = 0
        self.drawer = Drawer()

    def start_game(self):
        pass

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
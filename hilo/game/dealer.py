from drawer import Drawer

class Dealer:
    '''I will add documentation here later'''

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
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
        pass

    def do_updates(self):
        points = self.drawer.score_card
        self.score += points

    def do_outputs(self):
<<<<<<< Updated upstream
        '''Prints game information, including score and card values, during and after each round.
        '''
=======
>>>>>>> Stashed changes
        print(f'The card is: {None}')
        card_choice = self.get_inputs()
        second_card = self.drawer.draw_card()
        print(f'Next card was: {second_card}')
        print(f'Your score is: {None}')

        if self.drawer.can_draw():
            choice_play = input('Keep playing? [y/n] ')
            self.keep_playing = (choice_play == 'y')
        else:
            self.keep_playing = False
        pass
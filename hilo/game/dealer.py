from game.drawer import Drawer

class Dealer:
    '''The person who directs the game. Keeps track of score
        and controls the sequence of play.
    
        Attributes:
            keep_playing (bool): Whether the player continues to play
            score (int): The total number of points earned
            drawer (Drawer): Deals directly with cards

        I will add documentation here later
    '''

    def __init__(self):
        '''The class constructor.
        
            Args:
                self (Dealer): instance of Dealer
        '''
        self.keep_playing = True
        self.score = 300
        self.drawer = Drawer()

    def start_game(self):
        '''Starts game loop and controls sequence of play.
        
        Args:
            self (Dealer): instance of Dealer
        '''
        # self.drawer.draw_card()
        while self.keep_playing:
            # is_higher = self.get_inputs()
            # self.do_updates(is_higher)
            self.do_outputs()

    def get_inputs(self):
        repeat = True
        while repeat:
            user_choice = input('Higher or lower? [h/l] ')
            if user_choice.lower() == 'h':
                return True
            elif user_choice.lower() == 'l':
                return False

    def do_updates(self, is_higher):
        points = self.drawer.score_card(is_higher)
        self.score += points

    def do_outputs(self):
        '''Prints game information, including score and card values, during and after each round.
        '''
        new_card, old_card = self.drawer.draw_card()
        print(f'The card is: {old_card}')
        card_choice = self.get_inputs()
        self.do_updates(card_choice)
        print(f'Next card was: {new_card}')
        print(f'Your score is: {self.score}')

        if self.drawer.can_draw(self.score):
            choice_play = input('Keep playing? [y/n] ')
            self.keep_playing = (choice_play == 'y')
        else:
            self.keep_playing = False
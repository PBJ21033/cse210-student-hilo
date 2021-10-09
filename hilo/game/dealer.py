from drawer import Drawer

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
        points = self.drawer.score_card
        self.score += points

    def do_outputs(self):
        '''Prints game information, including score and card values, during and after each round.
        '''
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
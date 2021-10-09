import random

class Drawer(object):

    def __init__(self):
        """ Class constructor.

        Args:
        self(Drawer): Instance of the Drawer class

        Attributes:
        new_card(int): New card drawn thats value player is guessing
        old_card(int): Old card thats value was assigned by previous new_card
        turn_number(int): Incrementing turn number to check if old_card needs to be generated
        """
        self.new_card = 0
        self.old_card = 0
        self.turn_number = 0

    def draw_card(self):
        """ Randomly picks number between 1-13. Generates and returns value of 
        old_card(only generates once at begining of game) and new_card.

        Args:
        self(Drawer): Instance of the Drawer class
        """ 
        if self.turn_number == 0:
            self.old_card = random.randint(1,13)

        self.new_card = random.randint(1,13)
        return self.new_card, self.old_card

    def score_card(self, higher):
        """ Game logic that checks conditions to score and return points.
        Increments turn_number.

        Args:
        self(Drawer): Instance of the Drawer class
        higher(Bool): If the player guessed higher or lower
        """
        self.turn_number += 1

        if higher:
            if self.new_card > self.old_card:
                 return int(100)
            else:
                return int(-75) 

        if not higher:
            if self.new_card < self.old_card:
                return int(100)
            else:
                return int(-75)
            
    def can_draw(self, score):
        """ Game logic to return True if score is more than 0.

        Args:
        self(Drawer): Instance of the Drawer class
        score(int): current score
        """
        self.old_card = self.new_card
        if score > 0:
            return True
        else:
            return False

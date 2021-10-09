import random

class Drawer(object):

    def __init__(self):
        self.new_card = 0
        self.old_card = 0
        self.turn_number = 0

    def draw_card(self):
        if self.turn_number == 0:
            self.old_card = random.randint(1,13)

        self.new_card = random.randint(1,13)
        return self.new_card, self.old_card

    def score_card(self, higher):
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
        self.old_card = self.new_card
        if bool(score) or self.turn_number == 0:
            return True
        else:
            return False

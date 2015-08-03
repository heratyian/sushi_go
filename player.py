"""Sushi Go
    player.py
    
    Created: 2015
    Author: Ian Heraty
"""

class Player(object):
    pre_hand = None
    post_hand = None
    name = None
    points = None
    total_points = None

    def hit(self, card):
        self.pre_hand.append(card)
    
    def choose_card(self, card_name):
        self.post_hand.append(self.pre_hand.pop())

    def __str__(self):
        return "{}".format(self.name)

class User(Player):

    def __init__(self, name):
        self.pre_hand = []
        self.post_hand = []
        self.name = name
        self.points = 0
        self.total_points = 0



class Computer(Player):
    
    def __init__(self, name):
        self.pre_hand = []
        self.post_hand = []
        self.name = name
        self.points = 0
        self.total_points = 0





























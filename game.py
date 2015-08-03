"""Sushi Go
    game.py
    
    Created: 2015
    Author: Ian Heraty
"""

import sys
import os

from card import Deck, print_key, update_points, check_choice_validity, check_hand_for_card, index_of_choice
from player import User, Computer

"""Constants
"""
CARDS_PER_PLAYER = {2:10, 3:9, 4:8, 5:7}
TOTAL_ROUNDS = 3

class Game(object):
    round = None
    players = None # a list of all the players

class Sushi_Game(Game):
    
    def setup(self):
        """Setup game to prepare for round_loop()
        """
        self.round = 1
        self.players = []
        self.deck = Deck()
        self.add_players()
        self.deal_cards()

    def play(self):
        """Play sushi game
        """
        while True:
            self.show_hand()
            if self.players[0].pre_hand: # player has pre_hand cards
                self.show_info()
                self.choose_card()
                self.swap_hands()
            else: #round over
                for player in self.players: # calculate points
                    update_points(self, player, self.round, TOTAL_ROUNDS)
                # show point tabulation
                if self.round < TOTAL_ROUNDS: #not final round
                    self.round += 1
                    self.deal_cards() #play again
                else: #final round
                    break
    
    def choose_card(self):
        """Prompts user to choose a card from player.pre_hand
            adds chosen card to post_hand
        """
        choice = input("Which plate do you want to keep? ").upper()
        # if valid
        if check_choice_validity(self, choice):
            pass
        else:
            self.choose_card()
        # if in hand
        if check_hand_for_card(self, self.players[0].pre_hand, choice):
            pass
        else:
            self.choose_card()
        # find index of choice
        index = index_of_choice(self, choice, self.players[0].pre_hand)
        # add to post hand
        self.players[0].post_hand.append(self.players[0].pre_hand.pop(index))
        # update computer players
        self.computer.post_hand.append(self.computer.pre_hand.pop())
        
    def swap_hands(self):
        """ Swaps pre_hands for all players in players[]
        """
        #hold last players hand as temp value
        last_hand = self.players[len(self.players)-1].pre_hand
        for player in self.players:
            temp = player.pre_hand
            player.pre_hand = last_hand
            last_hand = temp
    
    def add_players(self):
        """Adds player objects to self.players[]
            TODO: prompt user for number of computer players
        """
        name = input("What's your name? ")
        self.player = User(name)
        self.players.append(self.player)
        self.computer = Computer("robot")
        self.players.append(self.computer)
    
    def deal_cards(self):
        # if players already have cards, remove them
        if self.players[0].pre_hand:
            for player in self.players:
                player.pre_hand = []

        for player in self.players:
            for _ in range(CARDS_PER_PLAYER[len(self.players)]):
                player.hit(self.deck.next_card())

    def show_hand(self):
        """Show hand
        """
        self.clear()
        print("Sushi Go")
        print("="*20)
        print("Conveyor Belt")
        hand = ', '.join(str(x) for x in self.player.pre_hand)
        print(hand)
        print("="*20)
        print("{}'s Plates".format(self.player.name))
        hand = ', '.join(str(x) for x in self.player.post_hand)
        print(hand)
        print("="*20)

    def show_info(self):
        """Show useful information on how to play the game
        """
        print_key(self)

    def display_score(self):
        """Show score after round of play
        """
        pass

    def clear(self):
        """Clear the screen
            """
        os.system('cls' if os.name == 'nt' else 'clear')

    # initializer
    def __init__(self):
        """Play a game of sushi game
        """
        self.setup()
        self.play()


Sushi_Game()


























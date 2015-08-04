"""Sushi Go
    game.py
    
    Created: 2015
    Author: Ian Heraty
"""

import sys
import os

from card import Deck, print_key, update_points, check_choice_validity, check_hand_for_card, index_of_choice, point_tabulation, WASABI_MULTIPLIER
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
                print_key(self) # show useful info
                self.choose_card()
                self.swap_hands()
            else: #round over
                update_points(self, self.players, self.round, TOTAL_ROUNDS)
                self.show_score() # show player score
                if self.round < TOTAL_ROUNDS: #not final round
                    self.round += 1
                    self.deal_cards() #play again
                else: #final round, game over
                    self.decide_winner()
                    break
    
    def choose_card(self):
        """Prompts user to choose a card from player.pre_hand
            adds chosen card to post_hand
            if player chooses nigiri, check for wasabi
        """
        choice = input("Which plate do you want to keep? ").upper()
        if check_choice_validity(self, choice) == False:
            self.choose_card()
        if check_hand_for_card(self, self.players[0].pre_hand, choice) == False:
            self.choose_card()
        index = index_of_choice(self, choice, self.players[0].pre_hand)
        # Nigiri and Wasabi
        if choice == 'N' and self.players[0].wasabi: # player has wasabi
            dip = input("Dip in wasabi? [Y/N] ").upper()
            if dip == 'Y':
                self.players[0].pre_hand[index].points *= WASABI_MULTIPLIER
                self.players[0].wasabi -= 1
        if choice == 'W':
            self.players[0].wasabi += 1
        # move card to post_hand
        self.players[0].post_hand.append(self.players[0].pre_hand.pop(index))
        # one robot
        #self.computer.post_hand.append(self.computer.pre_hand.pop())
        # multiple robots
        index = 1
        for player in self.players:
            if index > len(self.players)-1:
                break
            self.players[index].post_hand.append(self.players[index].pre_hand.pop())
            index += 1
        
    def swap_hands(self):
        """ Swaps pre_hands for all players in players[]
        """
        last_hand = self.players[len(self.players)-1].pre_hand
        for player in self.players:
            temp = player.pre_hand
            player.pre_hand = last_hand
            last_hand = temp
    
    def add_players(self):
        """Adds player objects to self.players[]
        """
        name = input("What's your name? ")
        self.player = User(name)
        self.players.append(self.player)
        # one robot
        #self.computer = Computer("name")
        #self.players.append(self.computer)
        
        # multiple robots
        num_opponents = int(input("How many robots would you like to play against? [1, 2, 3, or 4] "))
        while num_opponents:
            name = input("Robot name please... ")
            self.computer = Computer(name)
            self.players.append(self.computer)
            num_opponents -= 1
    
    
    def deal_cards(self):
        """Deal cards to each player to begin a round
        """
        # if players already have cards, remove them
        if self.players[0].post_hand:
            for player in self.players:
                #don't remove pudding!
                puddings = 0
                for card in player.post_hand:
                    if card.name == 'Pudding':
                        puddings += 1
                other_cards = True
                while (other_cards):
                    if len(player.post_hand) == puddings:
                        other_cards = False
                    for card in player.post_hand:
                        if card.name != 'Pudding':
                            player.post_hand.remove(card)
            
                player.pre_hand = []
                player.wasabi = 0
        # deal cards to pre_hand
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

    def show_score(self):
        """Show score after round of play
        """
        # show score for all players
        for player in self.players:
            print("{}:Round={} Total={}".format(player.name, player.points, player.total_points))
        input("Press Enter to continue...")
        # show point tabulation for user? point_tabulation(self)

    def decide_winner(self):
        """Iterate through players to determine final scoring order
            (eg 1st, 2nd, 3rd...)
        """
        self.clear()
        standings = []
        index = 0
        for player in self.players:
            standings.append((index, player.total_points))
            index += 1
        standings.sort(key=lambda tup: tup[1], reverse=True)
        index = 1
        for tup in standings:
            print("{}. {} with {} points".format(index, self.players[tup[0]].name, self.players[tup[0]].total_points))
            index += 1

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


























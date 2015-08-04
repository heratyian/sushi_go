"""Sushi Go
    card.py
    
    Created: 2015
    Author: Ian Heraty
"""

from random import shuffle

""" Constants
"""
CARD_TYPES = ["Tempura",
              "Sashimi",
              "Dumplings",
              "Maki Roll",
              "Wasabi",
              "Nigiri",
              "Pudding",
              "Chopsticks"]

CARD_SHORT = ["T",
              "S",
              "D",
              "M",
              "W",
              "N",
              "P",
              "CH"]

CARD_DESCRIPTIONS = ["a set of 2 tempura cards scores 5 points",
                     "a set of 3 sashimi cards scores 10 points",
                     "x1=1,x2=3,x3=6,x4=10,x5=15",
                     "the most scores 6 points, second most scores 3 points",
                     "next nigiri x3",
                     "Squid = 3 points, Salmon = 2 points, Egg = 1 point",
                     "after 3 rounds, most scores 6 points, least loses 6 points",
                     "swap for 2"]

#deck creation
TEMPURA_COUNT = 14
SASHIMI_COUNT = 14
DUMPLINGS_COUNT = 14
MAKI_ROLL_COUNT_ONE = 6
MAKI_ROLL_COUNT_TWO = 12
MAKI_ROLL_COUNT_THREE = 8
NIGIRI_SALMON_COUNT = 10
NIGIRI_SQUID_COUNT = 5
NIGIRI_EGG_COUNT = 5
PUDDING_COUNT = 10
WASABI_COUNT = 6
CHOPSTICKS_COUNT = 4

TOTAL_NIGIRI = NIGIRI_EGG_COUNT + NIGIRI_SALMON_COUNT + NIGIRI_SQUID_COUNT
TOTAL_MAKI = MAKI_ROLL_COUNT_ONE + MAKI_ROLL_COUNT_TWO + MAKI_ROLL_COUNT_THREE

#scoring
WASABI_MULTIPLIER = 3
MOST_MAKI_POINTS = 6
SECOND_MOST_MAKI_POINTS = 3
MOST_PUDDING_POINTS = 6
LEAST_PUDDING_POINTS = -6
DUMPLINGS_POINTS = {0:0, 1:1, 2:3, 3:6, 4:10, 5:15}
NIGIRI_POINTS = {'Egg':1, 'Salmon':2, 'Squid':3}
TEMPURA_POINTS = 5
SASHIMI_POINTS = 10

"""Deck() class and methods
"""

class Deck(object):
    """A list of card objects
    """

    def create_deck(self):
        """Creates and returns a deck of sushi cards
        """
        deck_of_cards = []
        self.add_tempura(deck_of_cards)
        self.add_sashimi(deck_of_cards)
        self.add_dumplings(deck_of_cards)
        self.add_maki_roll(deck_of_cards)
        self.add_wasabi(deck_of_cards)
        self.add_nigiri(deck_of_cards)
        self.add_pudding(deck_of_cards)
        self.add_chopsticks(deck_of_cards)
        return deck_of_cards
    
    def add_tempura(self, deck_of_cards):
        for _ in range(TEMPURA_COUNT):
            tempura = Tempura()
            deck_of_cards.append(tempura)

    def add_sashimi(self, deck_of_cards):
        for _ in range(SASHIMI_COUNT):
            sashimi = Sashimi()
            deck_of_cards.append(sashimi)

    def add_dumplings(self, deck_of_cards):
        for _ in range(DUMPLINGS_COUNT):
            dumplings = Dumplings()
            deck_of_cards.append(dumplings)

    def add_maki_roll(self, deck_of_cards):
        for index in range(TOTAL_MAKI):
            if index < MAKI_ROLL_COUNT_ONE:
                maki_roll = Maki_Roll(1)
            elif index < MAKI_ROLL_COUNT_ONE+MAKI_ROLL_COUNT_TWO:
                maki_roll = Maki_Roll(2)
            elif index < MAKI_ROLL_COUNT_ONE+MAKI_ROLL_COUNT_TWO+MAKI_ROLL_COUNT_THREE:
                maki_roll = Maki_Roll(3)
            deck_of_cards.append(maki_roll)

    def add_wasabi(self, deck_of_cards):
        for _ in range(WASABI_COUNT):
            wasabi = Wasabi()
            deck_of_cards.append(wasabi)

    def add_nigiri(self, deck_of_cards):
        for index in range(TOTAL_NIGIRI):
            if index < NIGIRI_EGG_COUNT:
                nigiri = Nigiri("Egg")
            elif index < NIGIRI_EGG_COUNT+NIGIRI_SALMON_COUNT:
                nigiri = Nigiri("Salmon")
            elif index < NIGIRI_EGG_COUNT+NIGIRI_SALMON_COUNT+NIGIRI_SQUID_COUNT:
                nigiri = Nigiri("Squid")
            deck_of_cards.append(nigiri)

    def add_pudding(self, deck_of_cards):
        for _ in range(PUDDING_COUNT):
            pudding = Pudding()
            deck_of_cards.append(pudding)
    
    def add_chopsticks(self, deck_of_cards):
        for _ in range(CHOPSTICKS_COUNT):
            chopsticks = Chopsticks()
            deck_of_cards.append(chopsticks)

    def next_card(self):
        """Deals next card in deck
        """
        try:
            return self.deck.pop(0)
        except IndexError:
            return None

    def __str__(self):
        """Returns a strings of short_hand for every card in deck
        """
        for card in self.deck:
            try:
                print(card)
            except IndexError:
                return None

    def __init__(self):
        self.deck = self.create_deck()
        shuffle(self.deck)

""" Card() class and subclasses
"""

class Card(object):
    """Each instance of Card class should have count, points, type, name, and short
    """
    
    name = None # full name
    short = None # shortened name
    type = None # sub type (eg Salmon)
    count = None # how many
    points = None # how many points
    description = None # description of card

class Tempura(Card):
    def __init__(self):
        self.name = "Tempura"
        self.short = "T"
        self.count = 1

    def __str__(self):
        return "{}".format(self.short)

class Sashimi(Card):
    def __init__(self):
        self.name = "Sashimi"
        self.short = "S"
        self.count = 1

    def __str__(self):
        return "{}".format(self.short)

class Dumplings(Card):
    def __init__(self):
        self.name = "Dumplings"
        self.short = "D"
        self.count = 1

    def __str__(self):
        return "{}".format(self.short)

class Maki_Roll(Card):
    def __init__(self, count):
        self.name = "Maki Roll"
        self.short = "M"
        self.count = count
    
    def __str__(self):
        return "{}({})".format(self.short, self.count)

class Wasabi(Card):
    def __init__(self):
        self.name = "Wasabi"
        self.short = "W"
        self.count = 1

    def __str__(self):
        return "{}".format(self.short)

class Nigiri(Card):
    def __init__(self, type):
        self.name = "Nigiri"
        self.short = "N"
        self.count = 1
        self.type = type
        if self.type == 'Egg':
            self.points = 1
        elif self.type == 'Salmon':
            self.points = 2
        elif self.type == 'Squid':
            self.points = 3

    def __str__(self):
        return "{}({})".format(self.short, self.type)

class Pudding(Card):
    def __init__(self):
        self.name = "Pudding"
        self.short = "P"
        self.count = 1
    
    def __str__(self):
        return "{}".format(self.short)

class Chopsticks(Card):
    def __init__(self):
        self.name = "Chopsticks"
        self.short = "CH"
        self.count = 1
    
    def __str__(self):
        return "{}".format(self.short)



""" Card Functions
"""

def update_points(self, players, round, total_rounds):
    """ Calculates points for a round from a hand
        updates player.points and player.total_points
        if round == 3, pudding is counted
    """
    
    for player in players:
        points = 0 # points in round
        player.count_dict = dict.fromkeys(CARD_TYPES, 0) # holds counts of each type
        
        # count how many of each type
        for master in CARD_TYPES:
            count = 0
            for player_card in player.post_hand:
                if player_card.name == master:
                    if player_card.name == 'Maki Roll':
                        player.count_dict[master] += player_card.count
                    elif player_card.name == 'Nigiri':
                        player.count_dict[master] += player_card.count
                        points += player_card.points
                    else:
                        player.count_dict[master] += 1

        # calc points using count
        for key in player.count_dict:
            if key == 'Tempura':
                temp_count = player.count_dict[key]
                while temp_count >= 2:
                    points += TEMPURA_POINTS
                    temp_count -= 2
            if key == 'Sashimi':
                temp_count = player.count_dict[key]
                while temp_count >= 3:
                    points += SASHIMI_POINTS
                    temp_count -= 3
            if key == 'Dumplings':
                points += DUMPLINGS_POINTS[player.count_dict[key]]

        player.points = points #round points
        player.total_points += player.points

    # compare players counts of maki rolls
    maki_list = []
    index = 0
    for player in players:
        maki_list.append((index, player.count_dict['Maki Roll']))
        index += 1
    maki_list.sort(key=lambda tup: tup[1], reverse=True)
    if maki_list[0][1] == maki_list[1][1]: #split pot
        players[maki_list[0][0]].points += MOST_MAKI_POINTS/2
        players[maki_list[1][0]].points += MOST_MAKI_POINTS/2
        players[maki_list[0][0]].total_points += MOST_MAKI_POINTS/2
        players[maki_list[1][0]].total_points += MOST_MAKI_POINTS/2
    else:
        players[maki_list[0][0]].points += MOST_MAKI_POINTS
        players[maki_list[1][0]].points += SECOND_MOST_MAKI_POINTS
        players[maki_list[0][0]].total_points += MOST_MAKI_POINTS
        players[maki_list[1][0]].total_points += SECOND_MOST_MAKI_POINTS

    # compare players counts of pudding
    if round == total_rounds:
        pudding_list = []
        index = 0
        for player in players:
            pudding_list.append((index, player.count_dict['Pudding']))
            index += 1
        maki_list.sort(key=lambda tup: tup[1], reverse=True)
        players[pudding_list[0][0]].points += MOST_PUDDING_POINTS
        players[pudding_list[len(pudding_list)-1][0]].points += LEAST_PUDDING_POINTS
        players[pudding_list[0][0]].total_points += MOST_PUDDING_POINTS
        players[pudding_list[len(pudding_list)-1][0]].total_points += LEAST_PUDDING_POINTS

def point_tabulation(self, player, round):
    """ Prints out total points by card type
        eg D x 3 = 6 points
    """
    pass

def check_choice_validity(self, choice):
    """ Checks validity of card choice
        loops through card_short
        returns True if valid
    """
    valid_card = False
    for card in CARD_SHORT:
        if choice == card:
            valid_card = True
            return valid_card
    return valid_card

def check_hand_for_card(self, hand, choice):
    """ Loops through hand to verify presence of choice
        returns True if valid
    """
    card_in_hand = False
    for card in hand:
        if card.short == choice:
            card_in_hand = True
            return card_in_hand
    return card_in_hand


def index_of_choice(self, choice, hand):
    """Returns index value of choice in hand
    """
    index = 0
    for card in hand:
        if card.short == choice:
            return index
        index += 1

def print_key(self):
    for index in range(len(CARD_TYPES)):
        print("{} = {}, {}".format(CARD_SHORT[index], CARD_TYPES[index], CARD_DESCRIPTIONS[index]))
















from Card import Card
from Hand import Hand
from typing import List
import random

"""The deck class initializes card objects and adds them all into a standard 52 card deck.
   This class also handles distributing cards to players and shuffling."""

class Deck():

    def hit(self, player: Hand):
        """Given a player's hand, add one card from the top of the deck and remove it from the deck."""
        player.hand.append(self.deck[len(self.deck) - 1])
        self.deck.pop(len(self.deck) - 1)

    def deal(self, players: List[Hand]):
        """Loop through all player hands and deal two cards to each"""
        for item in range(0, len(players)):
            current_player = players[item].hand
            current_player.append(self.deck[len(self.deck) - 1])
            self.deck.pop(len(self.deck) - 1)
        for item in range(0, len(players)):
            current_player = players[item].hand
            current_player.append(self.deck[len(self.deck) - 1])
            self.deck.pop(len(self.deck) - 1)

    def shuffle(self):
        """Shuffle the deck using a random seed which changes every game"""
        seed = random.seed()
        random.shuffle(self.deck)

    def create_deck(self):
        """This intializes the deck by creating 52 cards"""
        suits = ["diamonds", "hearts", "clubs", "spades"]
        colors = ["red", "black"]
        for i in range(1, 53):
            if i <= 13:
                self.deck.append(Card(f"{i}.png", i, colors[0], suits[0]))      #The images that represent the cards are numbered as "1.png", "2.png", etc.
            elif i <= 26 and i > 13:
                self.deck.append(Card(f"{i}.png", i - 13, colors[0], suits[1])) #Every 13 cards starts another suit.
            elif i <= 39 and i > 26:
                self.deck.append(Card(f"{i}.png", i - 26, colors[1], suits[2])) #Every 26 cards starts the next color.
            elif i <= 52 and i > 39:
                self.deck.append(Card(f"{i}.png", i - 39, colors[1], suits[3]))

    def __init__(self, deck: List[Card]):
        #A deck is essentially just a list of card objects.
        self.deck = deck

    def __str__(self):
        deck_values = ""
        for item in range(0, len(self.deck)):
            deck_values += f"{self.deck[item]}" + "\n"
        return deck_values + f"size: {len(self.deck)}"
        
from Card import Card
from Hand import Hand
from typing import List
import random

class Deck():

    def hit(self, player: Hand):
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
        seed = random.seed()
        random.shuffle(self.deck)

    def create_deck(self):
        suits = ["diamonds", "hearts", "clubs", "spades"]
        colors = ["red", "black"]
        for i in range(1, 53):
            if i <= 13:
                self.deck.append(Card(f"{i}.png", i, colors[0], suits[0]))
            elif i <= 26 and i > 13:
                self.deck.append(Card(f"{i}.png", i - 13, colors[0], suits[1]))
            elif i <= 39 and i > 26:
                self.deck.append(Card(f"{i}.png", i - 26, colors[1], suits[2]))
            elif i <= 52 and i > 39:
                self.deck.append(Card(f"{i}.png", i - 39, colors[1], suits[3]))

    def __init__(self, deck: List[Card]):
        self.deck = deck

    def __str__(self):
        deck_values = ""
        for item in range(0, len(self.deck)):
            deck_values += f"{self.deck[item]}" + "\n"
        return deck_values + f"size: {len(self.deck)}"
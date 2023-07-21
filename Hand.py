from Card import Card
from typing import List
import pygame
import os

"""The hand class represents the player's hand, and serves to function as the player in game."""

CARD_WIDTH, CARD_HEIGHT = 100, 150

class Hand():

    def draw(self, window: pygame.surface, reveal: bool):
        """draw takes in a window and a boolean reveal as parameters and draws the dealer and player hands.
           the dealer hand is drawn face down until the game is over and reveal is True. In such a case, all
           dealer's cards are revealed."""
        handlen = self.get_length()
        space_between = 6   #Space left between drawn cards
        posx = 590          #X and Y positions of the user's first card. The Y value is changed to 10 as seen below if the player is the dealer.
        posy = 560
        iter = 1
        if self.name != "Player":
            posy = 10
        if not reveal:
            for card in self.hand:
                if self.name != "Player":
                    image = pygame.image.load(os.path.join('Resources', 'blue.png'))
                    if iter == 1:
                        image = pygame.image.load(os.path.join('Resources', f'{card.id}'))
                else:
                    image = pygame.image.load(os.path.join('Resources', f'{card.id}'))
                
                image = pygame.transform.smoothscale(image, (CARD_WIDTH, CARD_HEIGHT))
                if iter == 1:
                    posx -= (handlen - 1) * ((CARD_WIDTH + space_between) / 2)
                window.blit(image, (posx, posy))
                posx += (CARD_WIDTH + space_between)                                            #As cards are added, the x position increases by the card's width and the space between cards
                iter += 1
        elif reveal:
            for card in self.hand:
                image = pygame.image.load(os.path.join('Resources', f'{card.id}'))
                image = pygame.transform.smoothscale(image, (CARD_WIDTH, CARD_HEIGHT))
                if iter == 1:
                    posx -= (handlen - 1) * ((CARD_WIDTH + space_between) / 2)
                window.blit(image, (posx, posy))
                posx += (CARD_WIDTH + space_between)
                iter += 1
            

    def get_total(self) -> int:
        """get_total determines the total points a hand has by looping through the hand and adding the card object's values to the sum.
           We use two separate for loops in this function because as cards are added into the hand, their values must be changed."""
           
        sum = 0

        #This for loop is used for all cards that are not aces and works as expected
        for i in self.hand:
            if i.value > 10:    #All face cards have a value of 10
                sum += 10
            elif i.value != 1 and i.value <= 10:
                sum += i.value

        #This for loop is used for aces and makes the card's value either a 1 or 11 depending on the total
        for i in self.hand:
            if i.value == 1:
                if sum + 11 <= 21:
                    sum += 11
                else:
                    sum += i.value
        return sum
    
    def get_length(self) -> int:
        """Returns the amount of cards within a player's hand"""
        return len(self.hand)

    def __init__(self, name: str, hand: List[Card]):
        self.name = name
        self.hand = hand

    def __str__(self):
        cards = ""
        for i in range(0, len(self.hand)):
            cards += f"{self.hand[i]}\n"
        return f"{self.name}'s hand is:\n" + cards + "Total: " + f"{self.get_total()}"
    
from Card import Card
from typing import List
import pygame
import os

CARD_WIDTH, CARD_HEIGHT = 100, 150

class Hand():

    def draw(self, window: pygame.surface, reveal: bool):
        handlen = self.get_length()
        space_between = 6
        posx = 590
        posy = 560
        iter = 1
        if self.name == "Dealer":
            posy = 10
        if not reveal:
            for card in self.hand:
                if self.name == "Dealer":
                    image = pygame.image.load(os.path.join('Resources', 'blue.png'))
                    if iter == 1:
                        image = pygame.image.load(os.path.join('Resources', f'{card.id}'))
                else:
                    image = pygame.image.load(os.path.join('Resources', f'{card.id}'))
                
                image = pygame.transform.smoothscale(image, (CARD_WIDTH, CARD_HEIGHT))
                if iter == 1:
                    posx -= (handlen - 1) * ((CARD_WIDTH + space_between) / 2)
                window.blit(image, (posx, posy))
                posx += (CARD_WIDTH + space_between)
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
        sum = 0
        for i in self.hand:
            if i.value > 10:
                sum += 10
            elif i.value != 1 and i.value <= 10:
                sum += i.value
        for i in self.hand:
            if i.value == 1:
                if sum + 11 <= 21:
                    sum += 11
                else:
                    sum += i.value
        return sum
    
    def get_length(self) -> int:
        return len(self.hand)

    def __init__(self, name: str, hand: List[Card]):
        self.name = name
        self.hand = hand

    def __str__(self):
        cards = ""
        for i in range(0, len(self.hand)):
            cards += f"{self.hand[i]}\n"
        return f"{self.name}'s hand is:\n" + cards + "Total: " + f"{self.get_total()}"
    
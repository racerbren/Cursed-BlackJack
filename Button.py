import pygame
import os

"""The button class is used to create standard buttons with no images and text centered in the button. This is mainly used for the action buttons"""

class Button():

    def draw(self):
        self.button = pygame.draw.rect(self.win, self.color, [self.x, self.y, self.width, self.height], 0, 5)      #Draw the button with a black outline if outline is set to true
        if self.outline:
            pygame.draw.rect(self.win, 'black', [self.x, self.y, self.width, self.height], 3, 5)
        text = self.font.render(self.text, True, self.text_color)
        self.win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2), self.y + round(self.height / 2) - round(text.get_height() / 2)))     #Draw the text on top of the button

    
    def click(self, pos):
        x1 = pos[0]     #Mouse x position
        y1 = pos[1]     #Mouse y position
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:    #If the mouse x and y positions are within the button positions then the button is being clicked
            return True
        else:
            return False


    def __init__(self, win, text: str, text_color: str, x: int, y: int, width: int, height: int, button_color: str, outline: bool):
        self.win = win
        self.text = text
        self.text_color = text_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = button_color
        self.outline = outline
        self.font = pygame.font.Font('freesansbold.ttf', 44)

    

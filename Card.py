"""The card class creates objects to represent cards. Each card is given an id to match with an image from resources,
   a value to determine the total in game, a color, and a suit."""

class Card():

    def __init__(self, id: str, value: int, color: str, suit: str):
        self.id = id
        self.value = value
        self.color = color
        self.suit = suit

    def __str__(self):
        return f"{self.value} {self.color} {self.suit} || ID: {self.id}"

 
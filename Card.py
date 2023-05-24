class Card():

    def __init__(self, id: str, value: int, color: str, suit: str):
        self.id = id
        self.value = value
        self.color = color
        self.suit = suit

    def __str__(self):
        return f"{self.value} {self.color} {self.suit} || ID: {self.id}"


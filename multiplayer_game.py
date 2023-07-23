from Deck import Deck
from Hand import Hand
from Card import Card

class Game:


    def get_turn(self):
        if not self.p1Went and self.p1Turn:
            return 0
        elif self.p1Went and not self.p2Went:
            self.p1Turn = False
            self.p1Turn = True
            return 1
        else:
            return -1


    def play(self, player, move):
        self.moves[player] = move
        if player == 0 and self.moves[player].upper() == "STAND":
            self.p1Went = True
            self.p1Turn = False
            self.p2Turn = True
        elif player == 1 and self.moves[player].upper() == "STAND":
            self.p2Turn = False
            self.p2Went = True
        elif self.moves[player].upper() == "HIT":
            self.deck.hit(self.players[player])
        elif self.moves[player].upper() == "REPLAY":
            self.votecount += 1


    def connected(self):
        return self.ready


    def bothWent(self):
        return self.p1Went and self.p2Went


    def __init__(self, id):
        self.id = id

        self.p1 = Hand("Player0", [])
        self.p2 = Hand("Player1", [])
        self.players = [self.p1, self.p2]

        self.deck = Deck([])
        self.deck.create_deck()
        self.deck.shuffle()
        self.deck.deal(self.players)

        self.votecount = 0

        self.p1Went = False
        self.p2Went = False
        self.p1Turn = True
        self.p2Turn = False
        self.ready = False
        self.scores = [0, 0]
        self.moves = [None, None]

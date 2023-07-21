from Deck import Deck
from Card import Card
from Hand import Hand
from Button import Button
from typing import List
from network import Network
from multiplayer_game import Game
import pygame
import os


################################################################################################

"""This enclosed section sets up the game"""

pygame.init()

WIDTH, HEIGHT = 1280, 720
X_MID, Y_MID = WIDTH / 2, HEIGHT / 2
CARD_WIDTH, CARD_HEIGHT = 100, 150
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cursed BlackJack")

CLOCK = pygame.time.Clock()
FPS = 60

FONT = pygame.font.Font('freesansbold.ttf', 44)                                         

FORCE_QUIT = False

BG_IMAGE = pygame.image.load(os.path.join('Resources', 'BG.png'))
BG = pygame.transform.smoothscale(BG_IMAGE, (WIDTH, HEIGHT))

DECK_IMAGE = pygame.image.load(os.path.join('Resources', 'blue.png'))
DECK = pygame.transform.smoothscale(DECK_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

################################################################################################


#Create hit, stand, and replay buttons
hit = Button(WINDOW, "Hit", "black", 1005, 560, 225, 72, "white", True)                             
stand = Button(WINDOW, "Stand", "black", 1005, 638, 225, 72, "white", True)
replay = Button(WINDOW, "Play Again?", "black", X_MID - 150, Y_MID + 83, 300, 100, "white", True)

action_buttons = [hit, stand, replay]     #List of buttons that are used during the game to hit, stand, or play again


def animate(lobby: List[Hand], reveal, active, end_text=""):
    """Draw the background, deck, action buttons, player's and dealer's cards to the screen."""
    WINDOW.blit(BG, (0, 0))
    WINDOW.blit(DECK, (((WIDTH / 2) - 50), ((HEIGHT / 2) - 75)))
    for player in lobby:
        player.draw(WINDOW, reveal)
    draw_buttons(lobby[0], active, end_text)
    pygame.display.update()
    
    
def draw_buttons(player, active, end_text):
    """This function draws all of the action buttons to the screen and draws the endgame text and box to the screen."""
    if active:                                                                              #Draw hit and stand buttons while the game is active
        hit.draw()
        stand.draw()
    else:                                                                                   #Draw end_text and play again buttons when the game is over
        pygame.draw.rect(WINDOW, 'white', [X_MID - 300, Y_MID - 50, 600, 100], 0, 5)
        pygame.draw.rect(WINDOW, 'black', [X_MID - 300, Y_MID - 50, 600, 100], 3, 5)
        end_text = FONT.render(f'{end_text}', True, 'black')
        x_offset = end_text.get_width() / 2
        y_offset = end_text.get_height() / 2
        WINDOW.blit(end_text, (X_MID - x_offset, Y_MID - y_offset))
        replay.draw()
    
    total_text = FONT.render(f'Total: {player.get_total()}', True, 'white')
    WINDOW.blit(total_text, (50, 616))
    
    
def endgame(player, dealer) -> str:
    """This function handles the end of game logic excluding when the user busts, which is handled in the main game loop.
        endgame does not draw anything to the screen. It only returns the text which should be drawn to the screen."""
    win = player.get_total() > dealer.get_total() and player.get_total() < 22 or player.get_total == 21
    draw = player.get_total() == dealer.get_total() and dealer.get_total != 21
    lose = (player.get_total() < dealer.get_total() and dealer.get_total() < 22) or dealer.get_total == 21
    dealer_bust = dealer.get_total() > 21
    if win:
        return "You Win!"
    elif draw:
        return "Draw!"
    elif lose:
        return "Dealer wins."
    elif dealer_bust:
        return "Dealer Bust. You Win!"
    

def game(lobby: List[Hand]):
    """The main game loop for singleplayer games"""
    run = True
    reveal = False
    active = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if action_buttons[0].click(event.pos):
                    main_deck.hit(player)       #If player clicks hit, then add a card from the deck to player's hand
                if action_buttons[1].click(event.pos):
                    run = False                 #If player clicks stand, then end turn
        if player.get_total() >= 21:
            run = False
        animate(lobby, reveal, active)
        
        
def main_menu() -> str:
    """This main menu does not use the button class as these buttons are not conventional as the action buttons. They have images and off centered text
        The main menu is meant to serve as a hub for users to choose between multiplayer and single player modes."""
    run = True
    while run:
        CLOCK.tick(FPS)
        
        WINDOW.fill('white')
        single_button = pygame.draw.rect(WINDOW, 'black', [X_MID - 420, Y_MID - 150, 300, 300], 10, 10)     #Create button for singleplayer
        multi_button = pygame.draw.rect(WINDOW, 'black', [X_MID + 120, Y_MID - 150, 300, 300], 10, 10)      #Create button for multiplayer
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if single_button.collidepoint(event.pos):   #Check for button clicks or single player or multiplayer and return the mode
                    return "single"
                if multi_button.collidepoint(event.pos):
                    return "multi"
        
        single_image = pygame.image.load(os.path.join('Resources', 'console.png'))              #Blit singleplayer image and text for button
        single = pygame.transform.smoothscale(single_image, (200, 200))
        single_text = FONT.render('Single Player', True, 'black')
        WINDOW.blit(single_text, (X_MID - 415, Y_MID + 150))
        
        multi_image = pygame.image.load(os.path.join('Resources', 'multiplayer.png'))           #Blit multiplayer image and text for button
        multi = pygame.transform.smoothscale(multi_image, (200, 200))
        multi_text = FONT.render('Multi-Player', True, 'black')
        WINDOW.blit(multi_text, (X_MID + 140, Y_MID + 150))
        
        title_text = FONT.render('Cursed BlackJack', True, 'black')                             #Blit title text
        WINDOW.blit(title_text, (X_MID - (title_text.get_width() / 2), Y_MID - 275))
        
        WINDOW.blit(single, (X_MID - 370, Y_MID - 100))                                         #Draw the multiplater and single player buttons
        WINDOW.blit(multi, (X_MID + 170, Y_MID - 100))
                                                                                                
        pygame.display.update()


def multi_endgame(game, player, other):
    win = game.players[player].get_total() > game.players[other].get_total() and game.players[player].get_total() < 22
    draw = game.players[player].get_total() == game.players[other].get_total() and game.players[other].get_total != 21
    lose = (game.players[player].get_total() < game.players[other].get_total() and game.players[other].get_total() < 22) or game.players[other].get_total == 21
    other_bust = game.players[other].get_total() > 21
    if win:
        return str(f"You Win!")
    elif draw:
        return "Draw!"
    elif lose:
        return str(f"Player {other} wins.")
    elif other_bust:
        return str(f"Player {other} Busted. You win!")


def redraw_window(win, game, player, reveal, active, end_text):
    game.players[player].name = "Player"
    for p in game.players:
        p.draw(WINDOW, reveal)
    if game.get_turn() == player:
            draw_buttons(game.players[player], active, end_text)
            if game.players[player].get_total() >= 21:
                n.send("stand")

    elif game.get_turn() != player:
        total_text = FONT.render(f'Total: {game.players[player].get_total()}', True, 'white')
        WINDOW.blit(total_text, (50, 616))
    
    pygame.display.update()


def multi_game(player):
    """"""
    run = True
    reveal = False
    active = True
    player = int(n.getPlayer())
    end_text = ""

    while run:
        CLOCK.tick(FPS)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run  = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if action_buttons[0].click(event.pos):
                    n.send(action_buttons[0].text)            #If player clicks hit, then add a card from the deck to player's hand
                if action_buttons[1].click(event.pos):
                    n.send(action_buttons[1].text)
        if not (game.connected()):
                CLOCK.tick(FPS)
                WINDOW.fill('white')
                text = FONT.render("Waiting for player...", True, "black")
                WINDOW.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
                pygame.display.update()
        else:
            WINDOW.blit(BG, (0, 0))
            WINDOW.blit(DECK, (((WIDTH / 2) - 50), ((HEIGHT / 2) - 75)))

            if game.bothWent():
                active = False
                reveal = True
                other = n.getOtherPlayer()

                if game.players[player].get_total() > 21:
                    end_text = str(f"You busted!")

                elif game.players[player].get_total() == 21:
                    end_text = str(f"You win!")
                
                else:
                    end_text = multi_endgame(game, player, other)
                
                draw_buttons(game.players[player], active, end_text)

            redraw_window(WINDOW, game, player, reveal, active, end_text)    
        
    

if __name__ == "__main__":
    
    mode = main_menu()

    if mode == "single":
        run1 = True
        while run1:
            #Set up the game by creating player, dealer, and lobby of players.
            player = Hand("Player", [])
            dealer = Hand("Dealer", [])
            players = [player, dealer]

            #Create the deck of cards and shuffle it. Then deal two cards one face up to both players.
            main_deck = Deck([])
            main_deck.create_deck()
            main_deck.shuffle()
            main_deck.deal(players)

            game(players)
        
            #Initialize end text and determine if the user busted.
            end_text = ""
            player_bust = player.get_total() > 21
            
            #If user did not bust then call endgame and find the winner. Otherwise print bust message.
            if not player_bust:                  
                while dealer.get_total() <= 16:
                    main_deck.hit(dealer)
                end_text = endgame(player, dealer)
            else:
                end_text = "You bust. You lose."
            
            run2 = True
            reveal = True
            active = False
            while run2:                                          #This while loop animates the end game screen with the winner status and play again button
                CLOCK.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:               #Quitting now needs to exit loop 1 and loop 2 to close the window
                        run1 = False
                        run2 = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if action_buttons[2].click(event.pos):  #Play again button only kills second loop
                            run2 = False
                animate(players, reveal, active, end_text)      #Play again button is animated when the game is not active and the end_text is animated

    elif mode == "multi":
        n = Network()
        player = int(n.getPlayer())
        print("You are player ", player)
        multi_game(player)
    
    pygame.quit()
    
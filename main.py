from Deck import Deck
from Card import Card
from Hand import Hand
from typing import List
import pygame
import os

pygame.init()

WIDTH, HEIGHT = 1280, 720
X_MID, Y_MID = WIDTH / 2, HEIGHT / 2
CARD_WIDTH, CARD_HEIGHT = 100, 150
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cursed BlackJack")
CLOCK = pygame.time.Clock()

FONT = pygame.font.Font('freesansbold.ttf', 44)

FORCE_QUIT = False

BG_IMAGE = pygame.image.load(os.path.join('Resources', 'BG.png'))
BG = pygame.transform.smoothscale(BG_IMAGE, (WIDTH, HEIGHT))

DECK_IMAGE = pygame.image.load(os.path.join('Resources', 'blue.png'))
DECK = pygame.transform.smoothscale(DECK_IMAGE, (CARD_WIDTH, CARD_HEIGHT))

action_buttons = []

FPS = 60


def animate(lobby: List[Hand], reveal, active, end_text=""):
    WINDOW.blit(BG, (0, 0))
    WINDOW.blit(DECK, (((WIDTH / 2) - 50), ((HEIGHT / 2) - 75)))
    for player in lobby:
        player.draw(WINDOW, reveal)
    draw_buttons(lobby[0], active, end_text)
    pygame.display.update()
    
    
def draw_buttons(player, active, end_text):
    if active:
        hit = pygame.draw.rect(WINDOW, 'white', [1005, 560, 225, 72], 0, 5)
        pygame.draw.rect(WINDOW, 'black', [1005, 560, 225, 72], 3, 5)
        hit_text = FONT.render('Hit', True, 'black')
        WINDOW.blit(hit_text, (1085, 577))
        action_buttons.append(hit)
        
        stand = pygame.draw.rect(WINDOW, 'white', [1005, 638, 225, 72], 0, 5)
        pygame.draw.rect(WINDOW, 'black', [1005, 638, 225, 72], 3, 5)
        stand_text = FONT.render('Stand', True, 'black')
        WINDOW.blit(stand_text, (1055, 655))
        action_buttons.append(stand)
    else:
        pygame.draw.rect(WINDOW, 'white', [X_MID - 250, Y_MID - 50, 500, 100], 0, 5)
        pygame.draw.rect(WINDOW, 'black', [X_MID - 250, Y_MID - 50, 500, 100], 3, 5)
        end_text = FONT.render(f'{end_text}', True, 'black')
        x_offset = end_text.get_width() / 2
        y_offset = end_text.get_height() / 2
        WINDOW.blit(end_text, (X_MID - x_offset, Y_MID - y_offset))
    
    total_text = FONT.render(f'Total: {player.get_total()}', True, 'white')
    WINDOW.blit(total_text, (50, 616))
    
    
def endgame(player, dealer) -> str:
    win = player.get_total() > dealer.get_total() and player.get_total() < 22
    draw = player.get_total() == dealer.get_total()
    lose = player.get_total() < dealer.get_total() and dealer.get_total() < 22
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
    run = True
    reveal = False
    active = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if action_buttons[0].collidepoint(event.pos):
                    main_deck.hit(player)
                if action_buttons[1].collidepoint(event.pos):
                    run = False
        if player.get_total() > 21:
            run = False
        if player.get_total() == 21:
            run = False
        animate(lobby, reveal, active)
        
        
def main_menu() -> str:
    run = True
    while run:
        CLOCK.tick(FPS)
        
        WINDOW.fill('white')
        single_button = pygame.draw.rect(WINDOW, 'black', [X_MID - 420, Y_MID - 150, 300, 300], 10, 10)
        multi_button = pygame.draw.rect(WINDOW, 'black', [X_MID + 120, Y_MID - 150, 300, 300], 10, 10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if single_button.collidepoint(event.pos):
                    return "single"
                if multi_button.collidepoint(event.pos):
                    return "multi"
        
        single_image = pygame.image.load(os.path.join('Resources', 'console.png'))
        single = pygame.transform.smoothscale(single_image, (200, 200))
        single_text = FONT.render('Single Player', True, 'black')
        WINDOW.blit(single_text, (X_MID - 415, Y_MID + 150))
        
        multi_image = pygame.image.load(os.path.join('Resources', 'multiplayer.png'))
        multi = pygame.transform.smoothscale(multi_image, (200, 200))
        multi_text = FONT.render('Multi-Player', True, 'black')
        WINDOW.blit(multi_text, (X_MID + 140, Y_MID + 150))
        
        title_text = FONT.render('Cursed BlackJack', True, 'black')
        WINDOW.blit(title_text, (X_MID - (title_text.get_width() / 2), Y_MID - 275))
        
        WINDOW.blit(single, (X_MID - 370, Y_MID - 100))
        WINDOW.blit(multi, (X_MID + 170, Y_MID - 100))
        
        pygame.display.update()


# def multi_menu() -> str:
#     run = True
#     while run:
#         CLOCK.tick(FPS)

#         WINDOW.fill('white')
#         create_button = pygame.draw.rect(WINDOW, 'black', [X_MID - 420, Y_MID - 150, 300, 300], 10, 10)
#         join_button = pygame.draw.rect(WINDOW, 'black', [X_MID + 120, Y_MID - 150, 300, 300], 10, 10)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run  = False
#             if event.type == pygame.MOUSEBUTTONUP:
#                 if create_button.collidepoint(event.pos):
#                     return "create"
#                 if join_button.collidepoint(event.pos):
#                     return "join"

#         create_image = pygame.image.load(os.path.join('Resources', 'create.png'))
#         create = pygame.transform.smoothscale(create_image, (200, 200))
#         create_text = FONT.render('Create Room', True, 'black')
#         WINDOW.blit(create_text, (X_MID - 410, Y_MID + 150))
        
#         join_image = pygame.image.load(os.path.join('Resources', 'join.png'))
#         join = pygame.transform.smoothscale(join_image, (200, 200))
#         join_text = FONT.render('Join Room', True, 'black')
#         WINDOW.blit(join_text, (X_MID + 150, Y_MID + 150))
        
#         title_text = FONT.render('Multi-Player Game', True, 'black')
#         WINDOW.blit(title_text, (X_MID - (title_text.get_width() / 2), Y_MID - 275))
        
#         WINDOW.blit(create, (X_MID - 370, Y_MID - 100))
#         WINDOW.blit(join, (X_MID + 170, Y_MID - 100))

#         pygame.display.update()
#     return choice


def multi_lobby():
    run = True
    while run:
        CLOCK.tick(FPS)

        WINDOW.fill('white')
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run  = False
            if event.type == pygame.MOUSEBUTTONUP:
                if start_button.collidepoint(event.pos):
                    run = False
        
        pygame.display.update()
    

if __name__ == "__main__":
    
    mode = main_menu()

    if mode == "single":
        player = Hand("Player1", [])
        dealer = Hand("Dealer", [])
        players = [player, dealer]

        main_deck = Deck([])
        main_deck.create_deck()
        main_deck.shuffle()
        main_deck.deal(players)

        game(players)
    
        end_text = ""
        player_bust = player.get_total() > 21
        
        if not player_bust:
            while dealer.get_total() <= 16:
                main_deck.hit(dealer)
            end_text = endgame(player, dealer)
        else:
            end_text = "You bust. You lose."
        
        run = True
        reveal = True
        active = False
        while run:
            CLOCK.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            animate(players, reveal, active, end_text)

    elif mode == "multi":
        multi_lobby()
    
    pygame.quit()
    
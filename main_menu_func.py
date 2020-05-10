import pygame
import os
from button import Button
from start_game_func import main
from map_menu_func import map_menu
from shop_menu_func import shop_menu

pygame.init()
pygame.font.init()  # Init the font

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# MAIN MENU
BG_MAIN_MENU = pygame.transform.scale(pygame.image.load(os.path.join("Images/Main_Menu", "BG.png")), (WIDTH, HEIGHT)).convert_alpha()
START_GAME_BTN = pygame.image.load(os.path.join("Images/Main_Menu", "Start_btn.png")).convert_alpha()
SHOP_GAME_BTN = pygame.image.load(os.path.join("Images/Main_Menu", "Shop_BTN.png")).convert_alpha()
MAP_GAME_BTN = pygame.image.load(os.path.join("Images/Main_Menu", "Map_BTN.png")).convert_alpha()
EXIT_GAME_BTN = pygame.image.load(os.path.join("Images/Main_Menu", "Exit_BTN.png")).convert_alpha()
INFO_GAME_BTN = pygame.image.load(os.path.join("Images/Main_Menu", "Info_BTN.png")).convert_alpha()
CAPTION_GAME_IMAGE = pygame.image.load(os.path.join("Images/Main_Menu", "header.png")).convert_alpha()


def main_menu(WIN, player):
    run = True

    def draw_main_menu():
        WIN.blit(BG_MAIN_MENU, (0, 0))
        WIN.blit(CAPTION_GAME_IMAGE, (WIDTH / 2 - CAPTION_GAME_IMAGE.get_width() / 2, 50))

        # Draw button

        start_button.draw(WIN)
        shop_button.draw(WIN)
        exit_button.draw(WIN)
        map_button.draw(WIN)

    # X , Y , WIDTH, HEIGHT, IMG
    start_button = Button(WIDTH / 2 - START_GAME_BTN.get_width() / 2, 225, 230, 80, START_GAME_BTN)
    shop_button = Button(WIDTH / 2 + SHOP_GAME_BTN.get_width() + 100, 230, 230, 80, SHOP_GAME_BTN)
    exit_button = Button(WIDTH / 2 - EXIT_GAME_BTN.get_width() / 2, 425, 230, 80, EXIT_GAME_BTN)
    map_button = Button(WIDTH / 2 - MAP_GAME_BTN.get_width() / 2, 325, 230, 80, MAP_GAME_BTN)

    pygame.display.update()

    while run:
        draw_main_menu()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.isOverButton(pos):
                    main(player)
                elif shop_button.isOverButton(pos):
                    shop_menu(player)
                elif map_button.isOverButton(pos):
                    map_menu(WIN)
                elif exit_button.isOverButton(pos):
                    with open("Status/Health.txt", "w+") as f:
                        f.write(str(player.max_health))
                        run = False
    pygame.quit()

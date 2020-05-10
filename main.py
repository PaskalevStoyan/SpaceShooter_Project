import pkg_resources.py2_warn
import pygame
from player import Player
from main_menu_func import main_menu

pygame.init()
pygame.font.init()  # Init the font

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

player = Player(0, HEIGHT - 125)
player.x = WIDTH // 2 - player.ship_img.get_width() // 2

main_menu(WIN, player)















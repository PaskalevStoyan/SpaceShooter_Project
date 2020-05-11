import pygame
import os
from button import Button

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# MAP MENU
MAP_MENU_BG = pygame.transform.scale(pygame.image.load(os.path.join("Images/BG", "bg.jpg")),
                                     (WIDTH, HEIGHT)).convert_alpha()
PLANET_A = pygame.image.load(os.path.join("Images/Planets", "18.png")).convert_alpha()
PLANET_B = pygame.image.load(os.path.join("Images/Planets", "9.png")).convert_alpha()

with open("Status/Level_a.txt", "r") as f:
    level_a = int(f.read())


def map_menu(window):
    run = True

    planet_a_button = Button(WIDTH // 2 - PLANET_A.get_width(), HEIGHT // 2 - PLANET_A.get_height() // 2, 64, 64,
                             PLANET_A)
    planet_b_button = Button(WIDTH // 2, HEIGHT // 2 - PLANET_A.get_height() // 2, 64, 64, PLANET_B)

    def draw_map_menu():
        window.blit(MAP_MENU_BG, (0, 0))
        font = pygame.font.SysFont('Arial', 30)
        planet_a_label = font.render("Planet A", 1, (255, 255, 255))
        planet_b_label = font.render("Planet B", 1, (255, 255, 255))

        window.blit(planet_a_label, (WIDTH // 2 - PLANET_A.get_width() // 2 - planet_a_label.get_width() // 2 - 30,
                                     HEIGHT // 2 - PLANET_A.get_height() // 2))
        window.blit(planet_b_label, (WIDTH // 2 + PLANET_A.get_width() // 2 - planet_a_label.get_width() // 2,
                                     HEIGHT // 2 - PLANET_A.get_height() // 2))
        planet_a_button.draw(window)
        planet_b_button.draw(window)

    while run:
        draw_map_menu()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if planet_a_button.isOverButton(pos):
                    with open("Status/planet_a.txt", "w") as f:
                        f.write("True")
                    with open("Status/planet_b.txt", "w") as f:
                        f.write("False")
                    run = False
                elif planet_b_button.isOverButton(pos):
                    if level_a == 20:
                        with open("Status/planet_a.txt", "w") as f:
                            f.write("False")
                        with open("Status/planet_b.txt", "w") as f:
                            f.write("True")
                        run = False


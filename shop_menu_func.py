import pygame
import os
from button import Button

pygame.init()
pygame.font.init()  # Init the font

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# SHOP STATS
SHOP_BG = pygame.transform.scale(pygame.image.load(os.path.join("Images/Shop", "Window.png")), (WIDTH, HEIGHT)).convert_alpha()
SHOP_ARMOR_IMAGE = pygame.image.load(os.path.join("Images/Shop", "Armor_Icon.png")).convert_alpha()
SHOP_HEALTH_IMAGE = pygame.image.load(os.path.join("Images/Shop", "HP_Icon.png")).convert_alpha()
SHOP_DAMAGE_IMAGE = pygame.image.load(os.path.join("Images/Shop", "Damage_Icon.png")).convert_alpha()
SHOP_SPEED_IMAGE = pygame.image.load(os.path.join("Images/Shop", "Speed_Icon.png")).convert_alpha()
SHOP_CAPTION_IMAGE = pygame.image.load(os.path.join("Images/Shop", "Header.png")).convert_alpha()
SHOP_CRYSTAL_PLAYER_IMAGE = pygame.image.load(os.path.join("Images/Shop", "Shop_Cristal_Icon_02.png")).convert_alpha()


SHOP_CRYSTAL_IMAGE = pygame.image.load(os.path.join("Images/Shop", "shop_cristal_icon_02.png")).convert_alpha()
BACK_TO_MENU_BTN = pygame.image.load(os.path.join("Images/Shop", "Menu_BTN.png")).convert_alpha()


def shop_menu(player):
    run = True

    with open("Status/Health_Crystals.txt", "r") as f:
        hp_crystals = int(f.read())

    with open("Status/Armor_Crystals.txt", "r") as f:
        armor_crystals = int(f.read())

    with open("Status/Speed_Crystals.txt", "r") as f:
        vel_crystals = int(f.read())

    with open("Status/Damage_Crystals.txt", "r") as f:
        damage_crystals = int(f.read())

    def draw_shop():

        # FONT
        font = pygame.font.SysFont('Arial', 30)
        # TEXT
        hp_crystal_price = font.render("X " + str(hp_crystals), 1, (255, 255, 255))
        velocity_crystal_price = font.render("X " + str(vel_crystals), 1, (255, 255, 255))
        damage_crystals_price = font.render("X " + str(damage_crystals), 1, (255, 255, 255))
        armor_crystal_price = font.render("X " + str(armor_crystals), 1, (255, 255, 255))

        player_money = font.render(f"{player.money}", 1, (255, 255, 255))
        buy_armor_label = font.render("Buy 10 armor", 1, (255, 255, 255))
        buy_hp_label = font.render("Buy 10 health", 1, (255, 255, 255))
        buy_damage_label = font.render("Buy 10 damage", 1, (255, 255, 255))
        buy_speed_label = font.render("Buy 0.5 atk speed", 1, (255, 255, 255))
        player_armor_label = font.render(f"{player.armor} / 100", 1, (255, 255, 255))
        player_health_label = font.render(f"{player.health} / 500", 1, (255, 255, 255))
        player_damage_label = font.render(f"{player.damage} / 500", 1, (255, 255, 255))
        player_attkSpeed_label = font.render(f"{player.attk_speed_counter} / 15", 1, (255, 255, 255))

        WIN.blit(SHOP_BG, (0, 0))
        WIN.blit(SHOP_CAPTION_IMAGE, (WIDTH / 2 - SHOP_CAPTION_IMAGE.get_width() / 2, 18))
        WIN.blit(SHOP_CRYSTAL_PLAYER_IMAGE, (50, 15))
        WIN.blit(player_money, (100, 28))
        # ARMOR
        WIN.blit(armor_crystal_price, (WIDTH // 2 - SHOP_ARMOR_IMAGE.get_width() / 2 + 240, 130))
        WIN.blit(SHOP_CRYSTAL_IMAGE, (WIDTH / 2 - SHOP_ARMOR_IMAGE.get_width() / 2 + 160, 110))
        WIN.blit(buy_armor_label, (150, 135))
        WIN.blit(player_armor_label, (WIDTH // 2 - SHOP_ARMOR_IMAGE.get_width() / 2 + 350, 130))
        # HEALTH
        WIN.blit(hp_crystal_price, (WIDTH / 2 - SHOP_ARMOR_IMAGE.get_width() / 2 + 240, 250))
        WIN.blit(SHOP_CRYSTAL_IMAGE, (WIDTH / 2 - SHOP_ARMOR_IMAGE.get_width() / 2 + 160, 230))
        WIN.blit(buy_hp_label, (150, 255))
        WIN.blit(player_health_label, (WIDTH // 2 - SHOP_ARMOR_IMAGE.get_width() // 2 + 350, 250))
        # DAMAGE
        WIN.blit(damage_crystals_price, (WIDTH / 2 - SHOP_ARMOR_IMAGE.get_width() / 2 + 240, 370))
        WIN.blit(SHOP_CRYSTAL_IMAGE, (WIDTH / 2 - SHOP_ARMOR_IMAGE.get_width() / 2 + 160, 350))
        WIN.blit(buy_damage_label, (150, 375))
        WIN.blit(player_damage_label, (WIDTH // 2 - SHOP_ARMOR_IMAGE.get_width() // 2 + 350, 370))
        # SPEED
        WIN.blit(velocity_crystal_price, (WIDTH / 2 - SHOP_ARMOR_IMAGE.get_width() / 2 + 240, 490))
        WIN.blit(SHOP_CRYSTAL_IMAGE, (WIDTH / 2 - SHOP_ARMOR_IMAGE.get_width() / 2 + 160, 470))
        WIN.blit(buy_speed_label, (150, 495))
        WIN.blit(player_attkSpeed_label, (WIDTH // 2 - SHOP_SPEED_IMAGE.get_width() // 2 + 350, 490))

        back_to_menu_btn.draw(WIN)

        armor_btn.draw(WIN)
        health_btn.draw(WIN)
        damage_btn.draw(WIN)
        speed_btn.draw(WIN)

    # BUTTONS
    back_to_menu_btn = Button(WIDTH - 130, HEIGHT - 130, 410, 230, BACK_TO_MENU_BTN)
    armor_btn = Button(WIDTH / 2 - SHOP_ARMOR_IMAGE.get_width() / 2, 100, 410, 230, SHOP_ARMOR_IMAGE)
    health_btn = Button(WIDTH / 2 - SHOP_HEALTH_IMAGE.get_width() / 2, 220, 410, 230, SHOP_HEALTH_IMAGE)
    damage_btn = Button(WIDTH / 2 - SHOP_DAMAGE_IMAGE.get_width() / 2, 340, 410, 230, SHOP_DAMAGE_IMAGE)
    speed_btn = Button(WIDTH / 2 - SHOP_SPEED_IMAGE.get_width() / 2, 460, 410, 230, SHOP_SPEED_IMAGE)

    while run:
        draw_shop()
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_to_menu_btn.isOverButton(pos):
                    run = False
                # BYING HEALTH
                if health_btn.isOverButton(pos):
                    if player.money >= hp_crystals:
                        if player.max_health < 500:
                            player.max_health += 10
                            player.health = player.max_health
                            player.money -= hp_crystals
                            hp_crystals += 300
                            with open("Status/Health.txt", "w+") as f:
                                f.write(str(player.max_health))
                            with open("Status/Health_Crystals.txt", "w+") as f:
                                f.write(str(hp_crystals))

                            with open("Status/Money.txt", "w+") as f:
                                f.write(str(player.money - hp_crystals))

                # BYING ARMOR
                elif armor_btn.isOverButton(pos):
                    if player.money >= armor_crystals:
                        if player.armor + 10 <= 100:
                            player.armor += 10
                            player.money -= armor_crystals
                            armor_crystals = int(armor_crystals) + 100
                            print("Armor: ", player.armor)
                            with open("Status/Armor.txt", "w+") as f:
                                f.write(str(player.armor))
                            with open("Status/Armor_Crystals.txt", "w+") as f:
                                f.write(str(armor_crystals))

                            with open("Status/Money.txt", "w+") as f:
                                f.write(str(player.money))

                # BYING ATCK SPEED
                elif speed_btn.isOverButton(pos):
                    if player.money >= vel_crystals:
                        if player.attk_speed_counter < 15:
                            player.COOLDOWN -= 1
                            player.attk_speed_counter += 1
                            player.money -= vel_crystals
                            vel_crystals += 400
                            with open("Status/Speed.txt", "w+") as f:
                                f.write(str(player.COOLDOWN))
                            with open("Status/Speed_Crystals.txt", "w+") as f:
                                f.write(str(vel_crystals))
                            with open("Status/Money.txt", "w+") as f:
                                f.write(str(player.money - vel_crystals))
                            with open("Status/Attk_Speed_Cnt.txt", "w+") as f:
                                f.write(str(player.attk_speed_counter))
                # BYING DAMAGE
                elif damage_btn.isOverButton(pos):
                    if player.money >= damage_crystals:
                        if player.damage + 10 <= 500:
                            player.damage += 10
                            player.money -= damage_crystals
                            damage_crystals += 200

                            with open("Status/Damage.txt", "w+") as f:
                                f.write(str(player.damage))
                            with open("Status/Damage_Crystals.txt", "w+") as f:
                                f.write(str(damage_crystals))
                            with open("Status/Money.txt", "w+") as f:
                                f.write(str(player.money - damage_crystals))

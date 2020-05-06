import pkg_resources.py2_warn
import pygame
import os
import random
from boss_1_a import Boss
from boss_2_a import Boss_2_a
from boss_1_b import Boss_1_b
from boss_2_b import Boss_2_b
from laser import collide
from player import Player
from enemy import Enemy
from button import Button

pygame.init()

pygame.font.init()  # Init the font

WIDTH, HEIGHT = 1000, 700

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# BACKGROUND
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Images/BG", "BG.jpg")), (WIDTH, HEIGHT))

# MAIN MENU
BG_MAIN_MENU = pygame.transform.scale(pygame.image.load(os.path.join("Images/Main_Menu", "BG.png")), (WIDTH, HEIGHT))
START_GAME_BTN = pygame.image.load(os.path.join("Images/Main_Menu", "Start_btn.png"))
SHOP_GAME_BTN = pygame.image.load(os.path.join("Images/Main_Menu", "Shop_BTN.png"))
MAP_GAME_BTN = pygame.image.load(os.path.join("Images/Main_Menu", "Map_BTN.png"))
EXIT_GAME_BTN = pygame.image.load(os.path.join("Images/Main_Menu", "Exit_BTN.png"))
INFO_GAME_BTN = pygame.image.load(os.path.join("Images/Main_Menu", "Info_BTN.png"))
CAPTION_GAME_IMAGE = pygame.image.load(os.path.join("Images/Main_Menu", "header.png"))

# SHOP VARIABLES
SHOP_BG = pygame.transform.scale(pygame.image.load(os.path.join("Images/Shop", "Window.png")), (WIDTH, HEIGHT))
SHOP_CAPTION_IMAGE = pygame.image.load(os.path.join("Images/Shop", "Header.png"))
# SHOP STATS
SHOP_ARMOR_IMAGE = pygame.image.load(os.path.join("Images/Shop", "Armor_Icon.png"))
SHOP_HEALTH_IMAGE = pygame.image.load(os.path.join("Images/Shop", "HP_Icon.png"))
SHOP_DAMAGE_IMAGE = pygame.image.load(os.path.join("Images/Shop", "Damage_Icon.png"))
SHOP_SPEED_IMAGE = pygame.image.load(os.path.join("Images/Shop", "Speed_Icon.png"))

SHOP_CRYSTAL_IMAGE = pygame.image.load(os.path.join("Images/Shop", "shop_cristal_icon_02.png"))
SHOP_CRYSTAL_PLAYER_IMAGE = pygame.image.load(os.path.join("Images/Shop", "Shop_Cristal_Icon_02.png"))
BACK_TO_MENU_BTN = pygame.image.load(os.path.join("Images/Shop", "Menu_BTN.png"))

# MAP MENU
MAP_MENU_BG = pygame.transform.scale(pygame.image.load(os.path.join("Images/BG", "bg.jpg")), (WIDTH, HEIGHT))
PLANET_A = pygame.image.load(os.path.join("Images/Planets", "18.png"))
PLANET_B = pygame.image.load(os.path.join("Images/Planets", "9.png"))
PLANET_C = pygame.image.load(os.path.join("Images/Planets", "3.png"))

player = Player(0, HEIGHT - 125)
player.x = WIDTH // 2 - player.ship_img.get_width() // 2

# MONEY
with open("Status/Money.txt", "r") as f:
    player.money = int(f.read())
# ARMOR
with open("Status/Armor.txt", "r") as f:
    player.armor = int(f.read())
# ATK SPEED
with open("Status/Speed.txt", "r") as f:
    player.COOLDOWN = int(f.read())
# DAMAGE
with open("Status/Damage.txt", "r") as f:
    player.damage = int(f.read())
# HEALTH
with open("Status/Health.txt", "r") as f:
    player.max_health = int(f.read())
    player.health = player.max_health
# ATTK SPEED COUNTER
with open("Status/Attk_Speed_Cnt.txt", "r") as f:
    player.attk_speed_counter = int(f.read())

planet_a = True
planet_b = False

with open("Status/Level_a.txt", "r") as f:
    level_a = int(f.read())


# Main Loop
def main():
    global planet_a
    global planet_b

    level = 0
    run = True
    FPS = 60
    lives = 5
    laser_vel = 5

    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 70)
    score_font = pygame.font.SysFont("comicsans", 50)
    cleared_planet_font = pygame.font.SysFont("comicsans", 50)
    player_status_font = pygame.font.SysFont("comicsans", 30)
    player_stat_font = pygame.font.SysFont("comicsans", 25)
    # ENEMY ATTR
    enemies = []
    wave_length = 5

    # BOSSES
    boses = []
    boses_2_a = []
    boses_1_b = []
    boses_2_b = []
    clock = pygame.time.Clock()
    lost = False
    lost_count = 0

    cleared_count = 0

    # REDRAW WINDOW
    def redraw_window():
        WIN.blit(BACKGROUND, (0, 0))

        # Draw text

        if not level == 21:
            level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
            WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        if level % 10 != 0:
            lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
            WIN.blit(lives_label, (10, 10))

        crystal_label = score_font.render(f" {player.money}", 1, (255, 255, 255))
        WIN.blit(SHOP_CRYSTAL_PLAYER_IMAGE, (10, HEIGHT - 60))
        WIN.blit(crystal_label, (60, HEIGHT - 50))

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 325))

        if level > 20:
            if planet_a:
                won_planet_label = cleared_planet_font.render("CONGRATIOLATIONS! You can Proceed to planet B!",
                                                              1, (255, 255, 255))
                WIN.blit(won_planet_label, (WIDTH / 2 - won_planet_label.get_width() / 2, 350))
                with open("Status/Level_a.txt", "w+") as f:
                    f.write(str(level - 1))

            elif planet_b:
                won_planet_label = cleared_planet_font.render("CONGRATIOLATIONS YOU WON THE GAME!", 1, (255, 255, 255))
                WIN.blit(won_planet_label, (WIDTH / 2 - won_planet_label.get_width() / 2, 350))

        # BLITTING PLAYER STATS
        player_stat_label = player_status_font.render(f"Player Stats:", 1, (255, 255, 255))
        player_health_label = player_stat_font.render(f"Health: {player.health}", 1, (255, 255, 255))
        player_damage_label = player_stat_font.render(f"Damage: {player.damage}", 1, (255, 255, 255))
        player_armor_label = player_stat_font.render(f"Armor: {player.armor}", 1, (255, 255, 255))
        player_attk_speed_label = player_stat_font.render(f"Attk Speed: {player.attk_speed_counter}", 1,
                                                          (255, 255, 255))

        WIN.blit(player_stat_label, (10, 50))
        WIN.blit(player_health_label, (10, 75))
        WIN.blit(player_damage_label, (10, 100))
        WIN.blit(player_armor_label, (10, 125))
        WIN.blit(player_attk_speed_label, (10, 150))

        # ----------------------------------------------------------
        # DRAWING ENEMIES / BOSES / PLAYER
        # NORMAL MOBS
        for enemy in enemies:
            if enemy.health > 0:
                enemy.draw(WIN)
            else:
                enemy.enemy_vel = 0
                enemy.index_ship_img += 1
                enemy.ship_img = enemy.ENEMY_MAP[enemy.choice_img][0][enemy.index_ship_img]
                pygame.time.delay(5)
                enemy.draw(WIN)

                if enemy.index_ship_img == len(enemy.ENEMY_MAP[enemy.choice_img][0]) - 1:
                    enemies.remove(enemy)
                    if planet_a:
                        player.money += 10
                    elif planet_b:
                        player.money += 30
            for laser in enemy.lasers:
                laser.change_enemy_laser(enemy, WIN)  # CHANGING THE IMAGE OF THE LASER

                # IF COLLISION SHOW EXPLOSION AROUND PLAYER
                if laser.collision(player):
                    if enemy.index_laser_img >= len(enemy.ENEMY_MAP[enemy.choice_img][1]) - 1:
                        enemy.index_laser_img = 0
                    enemy.change_collide_laser(WIN, player)
                    # IF INDEX LASER == LEN OF THE LASER LIST - 1 REMOVE LASER/PLAYER HEALTH -= ENEMY DAMAGE
                if enemy.index_laser_img == len(enemy.ENEMY_MAP[enemy.choice_img][1]) - 1:
                    enemy.lasers.remove(laser)
                    player.health -= enemy.damage

        # BOSS 1 PLANET A
        for boss in boses:
            if boss.health > 0:
                boss.draw(WIN)
                boss.healthshow(WIN)

                for laser in boss.lasers:
                    # CHANGE ENEMY LASER AFTER COLLISION
                    laser.change_laser_boss1(boss, WIN)

                    if laser.collision(player):
                        if boss.index_laser_img >= len(boss.ENEMY_LASER_MAP) - 1:
                            boss.index_laser_img = 4

                        player.health -= boss.damage
                        boss.change_laser_collision(WIN, player)
                        if boss.index_laser_img == len(boss.ENEMY_LASER_MAP) - 1:
                            boss.lasers.remove(laser)

            else:
                if boss.index_ship_img + 1 >= FPS:
                    boss.index_ship_img = 0
                boss.index_ship_img += 1
                boss.ship_img = boss.ENEMY_SHIP_MAP[boss.index_ship_img]
                pygame.time.delay(60)
                boss.draw(WIN)
                pygame.time.delay(60)
                if boss.index_ship_img == len(boss.ENEMY_SHIP_MAP) - 1:
                    boses.remove(boss)
                    player.money += 1000

        # BOSS 2 PLANET A
        for boss2 in boses_2_a:

            if boss2.health > 0:
                boss2.draw(WIN)
                boss2.healthshow(WIN)
                if len(boss2.rockets) > 0:
                    for rocket in boss2.rockets:
                        rocket.change_rocket_boss_2_a(boss2, WIN)

                        if boss2.index_rocket_ship != len(boss2.ROCKET[1]):
                            boss2.ship_img = boss2.ROCKET[1][boss2.index_rocket_ship]
                            boss2.index_rocket_ship += 1

                        if rocket.collision(player):
                            boss2.rockets.remove(rocket)
                            player.health -= player.max_health
                for laser in boss2.lasers:
                    laser.change_laser_boss_2_a(boss2, WIN)

                    if boss2.index_shooting != len(boss2.BOSS_SHOOT_IMAGE) - 1:
                        boss2.change_to_shooting_ship(WIN)

                    if laser.collision_boss_2(player):
                        if boss2.index_laser_img >= len(boss2.BOSS_ATTACK_1_EXP) - 1:
                            boss2.index_laser_img = 0
                        player.health -= boss2.damage
                        boss2.change_laser_collision(WIN, player)
                        if boss2.index_laser_img == len(boss2.BOSS_ATTACK_1_EXP) - 1:
                            boss2.lasers.remove(laser)
            else:
                if boss2.index_ship_img + 1 >= FPS:
                    boss2.index_ship_img = 0
                boss2.index_ship_img += 1
                boss2.ship_img = boss2.BOSS_SHIP[boss2.index_ship_img]

                boss2.draw(WIN)
                pygame.time.delay(90)
                if boss2.index_ship_img == len(boss2.BOSS_SHIP) - 1:
                    boses_2_a.remove(boss2)
                    player.money += 2000

        # BOSS 1 PLANET B
        for boss_1_b in boses_1_b:
            if boss_1_b.health > 0:
                boss_1_b.draw(WIN)
                boss_1_b.healthshow(WIN)

                for laser in boss_1_b.lasers:
                    laser.change_laser_boss_1_b(boss_1_b, WIN)

                    if laser.collision_boss_2(player):
                        boss_1_b.change_boss_laser_collision(player, WIN)
                        player.health -= boss_1_b.damage
                        if boss_1_b.index_laser_img == len(boss_1_b.BOSS_NORM_LASER) - 1:
                            boss_1_b.lasers.remove(laser)

                for rocket in boss_1_b.rockets:
                    rocket.change_rocket_boss_1_b(boss_1_b, WIN)
                    if rocket.collision(player):
                        boss_1_b.rockets.remove(rocket)
                        player.health -= player.max_health
            else:
                pygame.time.delay(60)
                boss_1_b.change_boss_image_exp(WIN)

                if boss_1_b.index_ship_img == len(boss_1_b.BOSS_IMAGES) - 1:
                    boses_1_b.remove(boss_1_b)
                    player.money += 5000

        # BOSS 2 PLANET B
        for boss2_b in boses_2_b:
            if boss2_b.health > 0:
                boss2_b.draw(WIN)
                boss2_b.healthshow(WIN)
                for laser in boss_2_b.lasers:
                    laser.change_laser_boss_2_b(boss_2_b, WIN)
                    if laser.collision(player):
                        boss2_b.lasers.remove(laser)
                        player.health -= boss2_b.damage

                for rocket in boss_2_b.rockets:
                    rocket.change_rocket_boss_2_b(boss_2_b, WIN)
                    if rocket.collision(player):
                        boss2_b.rockets.remove(rocket)
                        player.health -= player.max_health

                for robot in boss_2_b.robots:
                    robot.change_robot_image(boss2_b, WIN)
                    if robot.collision(player):
                        player.health -= 10
            else:
                pygame.time.delay(60)
                boss2_b.change_boss_image_exp(WIN)
                if boss2_b.index_ship_img == len(boss2_b.BOSS_IMAGES) - 1:
                    boses_2_b.remove(boss2_b)
                    player.money = 15000
        # PLAYER
        if player.health > 0:
            player.draw(WIN)
            player.ship_img = player.PLAYER_SHIP_MAP[0]
        else:
            for laser in player.lasers:
                player.lasers.remove(laser)

            print(player.counter)
            player.explosion(WIN)
        # ----------------------------------------------------------

        pygame.display.update()

    while run:

        clock.tick(FPS)
        redraw_window()
        # IF PLAYER IS DEAD STOP THE GAME OR LIVES == 0
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1
        if lost:
            if lost_count > FPS * 3:
                player.counter = 0
                run = False
                with open("Status/Money.txt", "w+") as f:
                    crystals = f.readline()
                    f.write(str(player.money) + crystals)

                    player.x = WIDTH // 2 - player.ship_img.get_width() // 2
                    player.y = HEIGHT - 125
                with open("Status/Health.txt", "r") as f:
                    player.health = int(f.read())
                if planet_a and level_a != 20:
                    with open("Status/Level_a.txt", "w+") as f:
                        f.write(str(level))

            else:
                continue
        # IF PLAYER EXCEEDS LEVEL 20 STOP THE GAME PROCEED TO NEXT PLANET
        if planet_a:
            if level > 20:
                cleared = True
                cleared_count += 1
                if cleared:
                    if cleared_count > FPS * 3:
                        planet_b = True
                        planet_a = False
                        run = False
                    else:
                        continue
        elif planet_b:
            if level > 20:
                cleared = True
                cleared_count += 1
                if cleared:
                    if cleared_count > FPS * 3:
                        run = False
                    else:
                        continue
        # IF THE LENGTH OF ALL THE MOBS [ENEMIES/BOSES] IS == 0 LEVEL += 1 BUT IF RUN IS FALSE CONTINUE

        if len(enemies) == 0 \
                and len(boses) == 0 and len(boses_2_a) == 0 \
                and len(boses_1_b) == 0 and len(boses_2_b) == 0:
            if not run:
                continue
            level += 1
        # CREATING PLANET A MOBS AND BOSES
        if planet_a:
            if level % 10 != 0:
                rand_choice = None
                if len(enemies) == 0:
                    if level <= 4:
                        wave_length += random.randrange(1, 2)
                    elif 4 < level < 9:
                        wave_length += random.randrange(1, 3)
                    elif 9 <= level < 20:
                        wave_length += random.randrange(1, 4)
                    for i in range(wave_length):
                        if level <= 4:
                            rand_choice = random.choice(["enemy_1", "enemy_2", "enemy_3"])

                        elif 4 < level <= 9:
                            rand_choice = random.choice(["enemy_1", "enemy_2", "enemy_3", "enemy_4"])

                        elif 9 < level < 21:
                            rand_choice = random.choice(["enemy_1", "enemy_2", "enemy_3", "enemy_4", "enemy_5"])
                        if level < 20:
                            enemy = Enemy(random.randrange(50, WIDTH - 200), random.randrange(-1000, -100),
                                          rand_choice)

                            enemy.choice_img = rand_choice
                            enemies.append(enemy)
                            # ENEMY ATTR
                            if rand_choice == "enemy_1":
                                enemy.max_health = 10
                                enemy.health = enemy.max_health
                                enemy.health_y = -15
                                enemy.health_x = 12
                                enemy.shoot_x = - 70
                                enemy.shoot_y = - 35
                                if player.armor < 30:
                                    enemy.damage = 20
                                elif player.armor >= 30:
                                    enemy.damage = 10
                                elif player.armor >= 70:
                                    enemy.damage = 5
                                elif player.armor == 100:
                                    enemy.damage = 2
                                enemy.enemy_vel = 3
                            elif rand_choice == "enemy_2":
                                enemy.max_health = 20
                                enemy.health = enemy.max_health
                                enemy.health_y = 10
                                enemy.health_x = 5
                                enemy.shoot_x = - 65
                                enemy.shoot_y = - 65
                                if player.armor < 30:
                                    enemy.damage = 30
                                elif player.armor >= 30:
                                    enemy.damage = 20
                                elif player.armor >= 70:
                                    enemy.damage = 10
                                elif player.armor == 100:
                                    enemy.damage = 5
                                enemy.enemy_vel = 3
                            elif rand_choice == "enemy_3":
                                enemy.max_health = 30
                                enemy.health = enemy.max_health
                                enemy.health_y = 10
                                enemy.health_x = 5
                                enemy.shoot_x = - 65
                                enemy.shoot_y = - 65
                                if player.armor < 30:
                                    enemy.damage = 35
                                elif player.armor >= 30:
                                    enemy.damage = 25
                                elif player.armor >= 70:
                                    enemy.damage = 15
                                elif player.armor == 100:
                                    enemy.damage = 5
                                enemy.enemy_vel = 2
                            elif rand_choice == "enemy_4":
                                enemy.health = 40
                                enemy.max_health = enemy.health
                                enemy.health_y = -10
                                enemy.health_x = -10
                                enemy.shoot_x = - 70
                                enemy.shoot_y = - 50
                                if player.armor < 30:
                                    enemy.damage = 40
                                elif player.armor >= 30:
                                    enemy.damage = 30
                                elif player.armor >= 70:
                                    enemy.damage = 20
                                elif player.armor == 100:
                                    enemy.damage = 8
                                enemy.enemy_vel = 2

                            elif rand_choice == "enemy_5":
                                enemy.health = 100
                                enemy.max_health = enemy.health
                                enemy.health_x = - 120
                                enemy.health_y = - 150
                                enemy.shoot_x = - 135
                                enemy.shoot_y = - 80
                                if player.armor < 30:
                                    enemy.damage = 50
                                elif player.armor >= 30:
                                    enemy.damage = 30
                                elif player.armor >= 70:
                                    enemy.damage = 25
                                elif player.armor == 100:
                                    enemy.damage = 10
                                enemy.enemy_vel = 2
            # BOSES ATTR
            elif level == 10:
                if len(boses) == 0:
                    boss = Boss(350, -300)
                    boss.health = 1000
                    boss.max_health = boss.health
                    boss.health_x = - 180
                    boss.health_y = 50
                    if player.armor < 30:
                        boss.damage = 10
                    elif player.armor >= 30:
                        boss.damage = 7
                    elif player.armor >= 70:
                        boss.damage = 5
                    elif player.armor == 100:
                        boss.damage = 3
                    boses.append(boss)
            elif level == 20:
                if len(boses_2_a) == 0 and len(enemies) == 0:
                    boss2 = Boss_2_a(250, -300)
                    boss2.health = 4000
                    boss2.max_health = boss2.health
                    boss2.health_x = - 140
                    boss2.health_y = - 20
                    if player.armor < 30:
                        boss2.damage = 40
                    elif player.armor >= 30:
                        boss2.damage = 25
                    elif player.armor >= 70:
                        boss2.damage = 10
                    elif player.armor == 100:
                        boss2.damage = 6
                    boses_2_a.append(boss2)
        # CREATING PLANET B MOBS AND BOSES
        elif planet_b:
            rand_choice = None
            if level % 10 != 0:
                if len(enemies) == 0:
                    if level <= 4:
                        wave_length += random.randrange(1, 2)
                    elif 4 < level < 9:
                        wave_length += random.randrange(1, 3)
                    elif 9 <= level < 20:
                        wave_length += random.randrange(1, 4)
                    for i in range(wave_length):
                        if level <= 4:
                            rand_choice = random.choice(
                                ['enemy_1_b', 'enemy_2_b', 'enemy_3_b'])

                        elif 4 < level <= 9:
                            rand_choice = random.choice(['enemy_1_b', 'enemy_2_b', 'enemy_3_b', 'enemy_4_b'])

                        elif 9 < level <= 14:
                            rand_choice = random.choice(['enemy_1_b', 'enemy_2_b', 'enemy_3_b',
                                                         'enemy_4_b', 'enemy_5_b'])
                        elif 15 < level < 30:
                            rand_choice = random.choice(['enemy_1_b', 'enemy_2_b', 'enemy_3_b',
                                                         'enemy_4_b', 'enemy_5_b', 'enemy_6_b'])

                        enemy = Enemy(random.randrange(50, WIDTH - 200), random.randrange(-1000, - 100),
                                      rand_choice)
                        enemy.choice_img = rand_choice
                        enemies.append(enemy)
                        # ENEMY ATTR
                        if rand_choice == "enemy_1_b":
                            enemy.max_health = 100
                            enemy.health = enemy.max_health
                            if player.armor < 30:
                                enemy.damage = 30
                            elif player.armor >= 30:
                                enemy.damage = 25
                            elif player.armor >= 70:
                                enemy.damage = 15
                            elif player.armor == 100:
                                enemy.damage = 10
                            enemy.enemy_vel = 2
                            enemy.shoot_x = - 40
                            enemy.shoot_y = - 40
                        elif rand_choice == "enemy_2_b":
                            enemy.max_health = 200
                            enemy.health = enemy.max_health
                            if player.armor < 30:
                                enemy.damage = 50
                            elif player.armor >= 30:
                                enemy.damage = 30
                            elif player.armor >= 70:
                                enemy.damage = 25
                            elif player.armor == 100:
                                enemy.damage = 10
                            enemy.enemy_vel = 3
                            enemy.shoot_x = - 40
                            enemy.shoot_y = - 40
                        elif rand_choice == "enemy_3_b":
                            enemy.max_health = 250
                            enemy.health = enemy.max_health
                            if player.armor < 30:
                                enemy.damage = 70
                            elif player.armor >= 30:
                                enemy.damage = 55
                            elif player.armor >= 70:
                                enemy.damage = 30
                            elif player.armor == 100:
                                enemy.damage = 15
                            enemy.enemy_vel = 2
                            enemy.shoot_x = - 40
                            enemy.shoot_y = - 40
                        elif rand_choice == "enemy_4_b":
                            enemy.max_health = 300
                            enemy.health = enemy.max_health
                            if player.armor < 30:
                                enemy.damage = 90
                            elif player.armor >= 30:
                                enemy.damage = 60
                            elif player.armor >= 70:
                                enemy.damage = 50
                            elif player.armor == 100:
                                enemy.damage = 30
                            enemy.enemy_vel = 2
                            enemy.shoot_x = - 40
                            enemy.shoot_y = - 40
                        elif rand_choice == "enemy_5_b":
                            enemy.max_health = 300
                            enemy.health = enemy.max_health
                            if player.armor < 30:
                                enemy.damage = 120
                            elif player.armor >= 30:
                                enemy.damage = 90
                            elif player.armor >= 70:
                                enemy.damage = 50
                            elif player.armor == 100:
                                enemy.damage = 25
                            enemy.enemy_vel = 2
                            enemy.shoot_x = - 80
                            enemy.shoot_y = - 65
                        elif rand_choice == "enemy_6_b":
                            enemy.max_health = 400
                            enemy.health = enemy.max_health
                            if player.armor < 30:
                                enemy.damage = 150
                            elif player.armor >= 30:
                                enemy.damage = 125
                            elif player.armor >= 70:
                                enemy.damage = 100
                            elif player.armor == 100:
                                enemy.damage = 75
                            enemy.enemy_vel = 1
                            enemy.shoot_x = - 80
                            enemy.shoot_y = - 70
            # BOSES ATTR
            elif level == 10:
                if len(boses_1_b) == 0:
                    boss_1_b = Boss_1_b(0, -300)
                    boss_1_b.x = WIDTH // 2 - boss_1_b.ship_img.get_width() // 2
                    boss_1_b.health = 5000
                    boss_1_b.max_health = boss_1_b.health
                    if player.armor < 30:
                        boss_1_b.damage = 25
                    elif player.armor >= 30:
                        boss_1_b.damage = 20
                    elif player.armor >= 70:
                        boss_1_b.damage = 15
                    elif player.armor == 100:
                        boss_1_b.damage = 10
                    boses_1_b.append(boss_1_b)

            elif level == 20:
                if len(boses_2_b) == 0:
                    boss_2_b = Boss_2_b(0, - 300)
                    boss_2_b.x = WIDTH // 2 - boss_2_b.ship_img.get_width() // 2
                    boss_2_b.health = 10000
                    boss_2_b.max_health = boss_2_b.health
                    if player.armor < 30:
                        boss_2_b.damage = 250
                    elif player.armor >= 30:
                        boss_2_b.damage = 200
                    elif player.armor >= 70:
                        boss_2_b.damage = 170
                    elif player.armor == 100:
                        boss_2_b.damage = 150
                    boses_2_b.append(boss_2_b)

        # IF X BUTTON IS CLICKED QUIT THE GAME
        # DOESNT SAVE THE MONEY GATHERED WHILE PLAYING THIS SESSION!!!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        #   W   |
        # A   D | - MOVEMENT KEYS. IF A OR D IS PRESSED PLAYER SHIP IMAGE IS CHANGED
        #   S   |
        if keys[pygame.K_a] and player.x - player.player_vel > 0:
            player.x -= player.player_vel
            player.ship_img = player.PLAYER_SHIP_MAP[2]
        if keys[pygame.K_d] and player.x + player.player_vel + player.get_width() < WIDTH:
            player.x += player.player_vel
            player.ship_img = player.PLAYER_SHIP_MAP[1]
        if keys[pygame.K_w] and player.y - player.player_vel > 0:
            player.y -= player.player_vel
        if keys[pygame.K_s] and player.y + player.player_vel + player.get_height() + 20 < HEIGHT:
            player.y += player.player_vel

        if keys[pygame.K_SPACE]:
            player.shoot()
        # -----------------------------------------------
        # MAKING ENEMIES / PLAYER / BOSES SHOOT
        if planet_a:
            if not level % 10 == 0:
                for enemy in enemies[:]:
                    enemy.move()
                    enemy.move_lasers(laser_vel)
                    if level < 10:
                        if random.randrange(0, FPS * 2) == 8:
                            if enemy.y >= 0:
                                enemy.index_laser_img = 0
                                enemy.laser_img = enemy.ENEMY_MAP[enemy.choice_img][1][enemy.index_laser_img]
                                enemy.shoot()

                    elif level >= 10:
                        if random.randrange(0, FPS) == 8:
                            if enemy.y >= 0:
                                enemy.index_laser_img = 0
                                enemy.laser_img = enemy.ENEMY_MAP[enemy.choice_img][1][enemy.index_laser_img]
                                enemy.shoot()
                    elif level >= 15:
                        if random.randrange(0, FPS / 2) == 8:
                            if enemy.y >= 0:
                                enemy.index_laser_img = 0
                                enemy.laser_img = enemy.ENEMY_MAP[enemy.choice_img][1][enemy.index_laser_img]
                                enemy.shoot()
                    if collide(enemy, player):
                        player.health -= player.health
                    elif enemy.y + enemy.get_height() > HEIGHT:
                        lives -= 1
                        enemies.remove(enemy)

                player.move_lasers(-laser_vel, enemies)

            elif level == 10:
                for boss in boses[:]:
                    boss.move(3)
                    boss.move_boss_lasers(laser_vel)
                    if random.randrange(0, 45) == 8:
                        if boss.y >= 0:
                            boss.index_laser_img = 0
                            boss.laser_img = boss.ENEMY_LASER_MAP[boss.index_laser_img]
                            boss.shoot()

                    if collide(boss, player):
                        player.health -= player.health

                player.move_lasers(-laser_vel, boses)
            elif level == 20:
                for boss2 in boses_2_a[:]:
                    boss2.move(3)
                    boss2.move_boss_lasers(laser_vel)
                    boss2.move_boss_rockets(laser_vel)

                    if random.randrange(0, 45) == 8:
                        if boss2.y >= 0:
                            boss2.laser_img = boss2.BOSS_ATTACK_1[0]
                            boss2.index_shooting = 0
                            boss2.shoot1()
                            boss2.shoot2()

                    if random.randrange(0, FPS * 2) == 8:
                        if boss2.y >= 0:
                            boss2.index_rocket_ship = 0
                            boss2.rocket_img = boss2.ROCKET[0][0]
                            boss2.rocket_attack()

                    if collide(boss2, player):
                        player.health -= player.health
                player.move_lasers(-laser_vel, boses_2_a)
        elif planet_b:
            if not level % 10 == 0:
                for enemy in enemies[:]:
                    enemy.move()
                    enemy.move_lasers(laser_vel)
                    if level <= 4:
                        if random.randrange(0, FPS * 2) == 8:
                            if enemy.y >= 0:
                                enemy.index_laser_img = 0
                                enemy.laser_img = enemy.ENEMY_MAP[enemy.choice_img][1][enemy.index_laser_img]
                                enemy.shoot()

                    elif 4 < level <= 9:
                        if random.randrange(0, FPS) == 8:
                            if enemy.y >= 0:
                                enemy.index_laser_img = 0
                                enemy.laser_img = enemy.ENEMY_MAP[enemy.choice_img][1][enemy.index_laser_img]
                                enemy.shoot()
                    elif 9 < level <= 13:
                        if random.randrange(0, FPS / 2) == 8:
                            if enemy.y >= 0:
                                enemy.index_laser_img = 0
                                enemy.laser_img = enemy.ENEMY_MAP[enemy.choice_img][1][enemy.index_laser_img]
                                enemy.shoot()
                    elif 21 <= level < 20:
                        if random.randrange(0, FPS / 3) == 8:
                            if enemy.y >= 0:
                                enemy.index_laser_img = 0
                                enemy.laser_img = enemy.ENEMY_MAP[enemy.choice_img][1][enemy.index_laser_img]
                                enemy.shoot()

                    if collide(enemy, player):
                        player.health -= player.health
                    elif enemy.y + enemy.get_height() > HEIGHT:
                        lives -= 1
                        enemies.remove(enemy)

                player.move_lasers(-laser_vel, enemies)

            elif level == 10:
                for boss_1_b in boses_1_b[:]:
                    boss_1_b.move(3)
                    boss_1_b.move_boss_laser(laser_vel)
                    boss_1_b.move_boss_rocket(laser_vel)
                    if random.randrange(0, 40) == 8:
                        if boss_1_b.y >= 0:
                            boss_1_b.shoot_lasers()

                    if random.randrange(0, FPS * 2) == 8:
                        if boss_1_b.y >= 0:
                            boss_1_b.shoot_rockets()

                player.move_lasers(-laser_vel, boses_1_b)

            elif level == 20:
                for boss_2_b in boses_2_b[:]:
                    boss_2_b.move(3)
                    boss_2_b.move_boss_lasers(laser_vel)
                    boss_2_b.move_boss_rockets(laser_vel)
                    boss_2_b.move_boss_robots(10)
                    if random.randrange(0, 45) == 8:
                        if boss_2_b.y >= -10:
                            boss_2_b.shoot_lasers()
                    if random.randrange(0, FPS * 4) == 8:
                        if boss_2_b.y >= - 10:
                            boss_2_b.shoot_rockets()
                    if random.randrange(0, FPS) == 8:
                        if boss_2_b.y >= - 10:
                            boss_2_b.create_robots()

                player.move_lasers(-laser_vel, boses_2_b)
        # -----------------------------------------------


def map_menu():
    run = True
    global planet_a
    global planet_b

    def draw_map_menu():
        WIN.blit(MAP_MENU_BG, (0, 0))

        planet_a_button.draw(WIN)
        planet_b_button.draw(WIN)

    planet_a_button = Button(WIDTH // 2 - PLANET_A.get_width(), HEIGHT // 2 - PLANET_A.get_height() // 2, 64, 64,
                             PLANET_A)
    planet_b_button = Button(WIDTH // 2, HEIGHT // 2 - PLANET_A.get_height() // 2, 64, 64, PLANET_B)

    while run:
        draw_map_menu()
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if planet_a_button.isOverButton(pos):
                    planet_a = True
                    run = False
                elif planet_b_button.isOverButton(pos):
                    if level_a == 20:
                        planet_b = True
                        planet_a = False
                        planet_c = False
                        run = False

    main_menu()


def shop_menu():
    run = True
    hp_crystals = 100
    with open("Status/Health_Crystals.txt", "r") as f:
        hp_crystals = int(f.read())
    armor_crystals = 300
    with open("Status/Armor_Crystals.txt", "r") as f:
        armor_crystals = int(f.read())
    vel_crystals = 300
    with open("Status/Speed_Crystals.txt", "r") as f:
        vel_crystals = int(f.read())
    damage_crystals = 200
    with open("Status/Damage_Crystals.txt", "r") as f:
        damage_crystals = int(f.read())

    def draw_shop():

        # FONT
        font = pygame.font.SysFont('comicsans', 40)
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
                    main_menu()
                # BYING HEALTH
                if health_btn.isOverButton(pos):
                    if player.money >= 200:
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
                    if player.money >= armor_crystals and player.armor <= 100:
                        player.armor += 10
                        player.money -= 200
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
                    if player.money >= damage_crystals and player.damage <= 500:
                        player.damage += 10
                        player.money -= damage_crystals
                        damage_crystals += 200

                        with open("Status/Damage.txt", "w+") as f:
                            f.write(str(player.damage))
                        with open("Status/Damage_Crystals.txt", "w+") as f:
                            f.write(str(damage_crystals))
                        with open("Status/Money.txt", "w+") as f:
                            f.write(str(player.money - damage_crystals))


def main_menu():
    run = True

    def draw_main_menu():
        WIN.blit(BG_MAIN_MENU, (0, 0))
        WIN.blit(CAPTION_GAME_IMAGE, (WIDTH / 2 - CAPTION_GAME_IMAGE.get_width() / 2, 50))

        # Draw button

        start_button.draw(WIN)
        shop_button.draw(WIN)
        exit_button.draw(WIN)
        map_button.draw(WIN)
        info_button.draw(WIN)

    # X , Y , WIDTH, HEIGHT, IMG
    start_button = Button(WIDTH / 2 - START_GAME_BTN.get_width() / 2, 225, 230, 80, START_GAME_BTN)
    shop_button = Button(WIDTH / 2 + SHOP_GAME_BTN.get_width() + 100, 230, 230, 80, SHOP_GAME_BTN)
    exit_button = Button(WIDTH / 2 - EXIT_GAME_BTN.get_width() / 2, 425, 230, 80, EXIT_GAME_BTN)
    map_button = Button(WIDTH / 2 - MAP_GAME_BTN.get_width() / 2, 325, 230, 80, MAP_GAME_BTN)
    info_button = Button(WIDTH / 2 + INFO_GAME_BTN.get_width() + 100, 410, 230, 80, INFO_GAME_BTN)

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
                    main()
                elif shop_button.isOverButton(pos):
                    shop_menu()
                elif map_button.isOverButton(pos):
                    map_menu()
                elif exit_button.isOverButton(pos):
                    with open("Status/Health.txt", "w+") as f:
                        f.write(str(player.max_health))
                    quit()

    pygame.quit()


main_menu()

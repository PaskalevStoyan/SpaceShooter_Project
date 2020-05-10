import pygame
import os
import boss_2_b
from create_Enemies_Boses import *
from shooting_funcs import *

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Images/BG", "BG.jpg")),
                                    (WIDTH, HEIGHT)).convert_alpha()
SHOP_CRYSTAL_PLAYER_IMAGE = pygame.image.load(os.path.join("Images/Shop", "Shop_Cristal_Icon_02.png")).convert_alpha()

planet_a = True
planet_b = False
with open("Status/Level_a.txt", "r") as f:
    level_a = int(f.read())


# Main Loop
def main(player):
    global planet_a
    global planet_b

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
    # MONEY
    with open("Status/Money.txt", "r") as f:
        player.money = int(f.read())

    level = 0
    run = True
    FPS = 60
    lives = 5
    laser_vel = 5

    main_font = pygame.font.SysFont("Arial", 40)
    lost_font = pygame.font.SysFont("Arial", 60)
    score_font = pygame.font.SysFont("Arial", 40)
    cleared_planet_font = pygame.font.SysFont("Arial", 40)
    player_status_font = pygame.font.SysFont("Arial", 25)
    player_stat_font = pygame.font.SysFont("Arial", 20)
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
    def redraw_WIN():
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

        WIN.blit(player_stat_label, (10, 70))
        WIN.blit(player_health_label, (10, 115))
        WIN.blit(player_damage_label, (10, 140))
        WIN.blit(player_armor_label, (10, 165))
        WIN.blit(player_attk_speed_label, (10, 190))

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

            if player.counter != len(player.PLAYER_EXP) - 1:
                player.explosion(WIN)
        # ----------------------------------------------------------

        pygame.display.update()

    while run:

        clock.tick(FPS)
        redraw_WIN()
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
                create_Planet_A_Enemies(player, enemies, level, wave_length)

            # BOSES ATTR
            elif level == 10:
                create_Planet_A_Boss_1(player, boses)

            elif level == 20:
                create_Planet_A_Boss_2(player, boses_2_a)

        elif planet_b:
            if level % 10 != 0:
                create_Planet_B_Enemies(player, level, enemies, wave_length)

            elif level == 10:
                create_Planet_B_Boss_1(boses_1_b, player)

            elif level == 20:
                create_Planet_B_Boss_2(boses_2_b, player)

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
                make_enemies_shoot(level, enemies, player, laser_vel, FPS, lives, HEIGHT)

            elif level == 10:
                make_boss_1_a_shoot(boses, laser_vel, player)

            elif level == 20:
                make_boss_2_a_shoot(boses_2_a, laser_vel, FPS, player)

        elif planet_b:
            if not level % 10 == 0:
                make_enemies_b_shoot(level, enemies, player, laser_vel, FPS, lives, HEIGHT)

            elif level == 10:
                make_boss_1_b_shoot(boses_1_b, laser_vel, FPS, player)

            elif level == 20:
                make_boss_2_b_shoot(boses_2_b, laser_vel, FPS, player)

        # -----------------------------------------------




import random
from enemy import Enemy
from boss_1_a import Boss
from boss_2_a import Boss_2_a
from boss_1_b import Boss_1_b
from boss_2_b import Boss_2_b

WIDTH, HEIGHT = 1000, 700


# Create Enemies/Boses for Planet A.
def create_Planet_A_Enemies(player, enemies, level, wave_length):
    """
    Create Enemies of Planet A
    :param player: player
    :param enemies: enemies
    :param level: Int
    :param wave_length: Int
    :return: None
    """
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


def create_Planet_A_Boss_1(player, boses):
    """
    Creates Boss 1 of Planet A
    :param player: player
    :param boses: boses
    :return:
    """
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


def create_Planet_A_Boss_2(player, boses_2_a):
    """
    Creates Boss 2 of Plabet A
    :param player: player
    :param boses_2_a: boses_2_a
    :return:
    """
    if len(boses_2_a) == 0:
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


# Create Enemies/Boses for Planet B

def create_Planet_B_Enemies(player, level, enemies, wave_length):
    """
    Creates Enemies of Planet B
    :param player: player
    :param level: Int
    :param enemies: enemies
    :param wave_length: Int
    :return: None
    """
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
                rand_choice = random.choice(
                    ['enemy_1_b', 'enemy_2_b', 'enemy_3_b'])

            elif 4 < level <= 9:
                rand_choice = random.choice(['enemy_1_b', 'enemy_2_b', 'enemy_3_b', 'enemy_4_b'])

            elif 9 < level <= 14:
                rand_choice = random.choice(['enemy_1_b', 'enemy_2_b', 'enemy_3_b',
                                             'enemy_4_b', 'enemy_5_b'])
            elif 15 < level < 20:
                rand_choice = random.choice(['enemy_1_b', 'enemy_2_b', 'enemy_3_b',
                                             'enemy_4_b', 'enemy_5_b', 'enemy_6_b'])
            if level < 20:
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


def create_Planet_B_Boss_1(boses_1_b, player):
    """
    Creates Boss 1 of Planet B
    :param boses_1_b: boses_1_b
    :param player: player
    :return: None
    """
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


def create_Planet_B_Boss_2(boses_2_b, player):
    """
    Creates Boss 2 of Planet B
    :param boses_2_b: boses_2_b
    :param player: player
    :return: None
    """
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

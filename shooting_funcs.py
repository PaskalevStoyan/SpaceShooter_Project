import random
from laser import collide

# Planet A


def make_enemies_shoot(level, enemies, player, laser_vel, FPS, lives, HEIGHT):
    """
    Making Enemies of Planet A Shoot
    :param level: Int
    :param enemies: enemies
    :param player: player
    :param laser_vel: Int
    :param FPS: Int
    :param lives: Int
    :param HEIGHT: Int
    :return: None
    """
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

    player.move_lasers(-laser_vel, enemies)


def make_boss_1_a_shoot(boses, laser_vel, player):
    """
     Making Boss 1 of Planet A Shoot
     :param boses: boses
     :param laser_vel: Int
     :param player: player
     :return: None
     """
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


def make_boss_2_a_shoot(boses_2_a, laser_vel, FPS, player):
    """
    Making Boss 2 of Planet A Shoot
    :param boses_2_a: boses_2_a
    :param laser_vel: Int
    :param FPS: Int
    :param player: player
    :return: None
    """
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


# PLANET B
def make_enemies_b_shoot(level, enemies, player, laser_vel, FPS, lives, HEIGHT):
    """
    Making Enemies of Planet B Shoot
    :param level: Int
    :param enemies: enemies
    :param player: player
    :param laser_vel: Int
    :param FPS: Int
    :param lives: Int
    :param HEIGHT: Int
    :return: None
    """
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


def make_boss_1_b_shoot(boses_1_b, laser_vel, FPS, player):
    """
      Making the Boss 1 of Planet B Shoot
      :param boses_1_b: boses_1_b
      :param laser_vel: Int
      :param FPS: Int
      :param player: player
      :return: None
      """
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


def make_boss_2_b_shoot(boses_2_b, laser_vel, FPS, player):
    """
    Making the Boss 2 of Planet B Shoot
    :param boses_2_b: boses_2_b
    :param laser_vel: Int
    :param FPS: Int
    :param player: player
    :return: None
    """
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

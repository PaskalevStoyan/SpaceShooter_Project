import pygame
import os
from laser import Laser
from rocket import Rocket
from ship import Ship

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# MAIN BOSS IMAGE
MAIN_BOSS_IMAGE = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01", "Boss_Full.png")).convert_alpha()
# BOSS DEATH/EXPLOSION
BOSS_EXPLOSION_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Death_000.png")).convert_alpha()
BOSS_EXPLOSION_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Death_001.png")).convert_alpha()
BOSS_EXPLOSION_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Death_002.png")).convert_alpha()
BOSS_EXPLOSION_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Death_003.png")).convert_alpha()
BOSS_EXPLOSION_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Death_004.png")).convert_alpha()
BOSS_EXPLOSION_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Death_005.png")).convert_alpha()
BOSS_EXPLOSION_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Death_006.png")).convert_alpha()
BOSS_EXPLOSION_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Death_007.png")).convert_alpha()
BOSS_EXPLOSION_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Death_008.png")).convert_alpha()
BOSS_EXPLOSION_10 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Explosion_001.png")).convert_alpha()
BOSS_EXPLOSION_11 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Explosion_002.png")).convert_alpha()
BOSS_EXPLOSION_12 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Explosion_003.png")).convert_alpha()
BOSS_EXPLOSION_13 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Explosion_004.png")).convert_alpha()
BOSS_EXPLOSION_14 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Explosion_005.png")).convert_alpha()
BOSS_EXPLOSION_15 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Explosion_006.png")).convert_alpha()
BOSS_EXPLOSION_16 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Explosion_007.png")).convert_alpha()
BOSS_EXPLOSION_17 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Exp", "Explosion_008.png")).convert_alpha()

# ROCKET ATTACK / BOSS IMAGES / PLAYER EXPLOSION
ROCKET_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "Missile_000.png")).convert_alpha()
ROCKET_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "Missile_001.png")).convert_alpha()
ROCKET_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "Missile_002.png")).convert_alpha()
ROCKET_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "Missile_003.png")).convert_alpha()
ROCKET_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "Missile_004.png")).convert_alpha()
ROCKET_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "Missile_005.png")).convert_alpha()
ROCKET_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "Missile_006.png")).convert_alpha()
ROCKET_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "Missile_007.png")).convert_alpha()
ROCKET_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "Missile_008.png")).convert_alpha()
ROCKET_10 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "Missile_009.png")).convert_alpha()
BOSS_R_ATTACK_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "R_Attack_1.png")).convert_alpha()
BOSS_R_ATTACK_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "R_Attack_2.png")).convert_alpha()
BOSS_R_ATTACK_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "R_Attack_3.png")).convert_alpha()
BOSS_R_ATTACK_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "R_Attack_4.png")).convert_alpha()
BOSS_R_ATTACK_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "R_Attack_5.png")).convert_alpha()
BOSS_R_ATTACK_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "R_Attack_6.png")).convert_alpha()
BOSS_R_ATTACK_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "R_Attack_7.png")).convert_alpha()
BOSS_R_ATTACK_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "R_Attack_8.png")).convert_alpha()
BOSS_R_ATTACK_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "R_Attack_9.png")).convert_alpha()
BOSS_R_ATTACK_10 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Rocket_Attack", "R_Attack_10.png")).convert_alpha()

# NORMAL ATTACK
BOSS_ATTACK_IMG_1_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Shot_001.png")).convert_alpha()
BOSS_ATTACK_IMG_1_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Shot_002.png")).convert_alpha()
BOSS_ATTACK_IMG_1_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Shot_003.png")).convert_alpha()
BOSS_ATTACK_IMG_1_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Shot_004.png")).convert_alpha()
BOSS_ATTACK_IMG_1_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Shot_005.png")).convert_alpha()
BOSS_ATTACK_IMG_1_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Shot_006.png")).convert_alpha()
BOSS_ATTACK_IMG_1_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Shot_007.png")).convert_alpha()
BOSS_ATTACK_IMG_1_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Shot_008.png")).convert_alpha()
BOSS_SHOOT_IMG_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Attack_1.png")).convert_alpha()
BOSS_SHOOT_IMG_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Attack_2.png")).convert_alpha()
BOSS_SHOOT_IMG_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Attack_3.png")).convert_alpha()
BOSS_SHOOT_IMG_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Attack_4.png")).convert_alpha()
BOSS_SHOOT_IMG_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Attack_5.png")).convert_alpha()
BOSS_SHOOT_IMG_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Attack_6.png")).convert_alpha()
BOSS_SHOOT_IMG_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Attack_7.png")).convert_alpha()
BOSS_SHOOT_IMG_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Attack_8.png")).convert_alpha()
BOSS_SHOOT_IMG_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Attack_9.png")).convert_alpha()
BOSS_SHOOT_IMG_10 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss_01/Norm_Attack", "Attack_10.png")).convert_alpha()


class Boss_2_a(Ship):
    MOVE = False
    # NORMAL ATTACK
    BOSS_ATTACK_1 = [BOSS_ATTACK_IMG_1_1, BOSS_ATTACK_IMG_1_2, BOSS_ATTACK_IMG_1_3, BOSS_ATTACK_IMG_1_4]

    BOSS_ATTACK_1_EXP = [BOSS_ATTACK_IMG_1_5, BOSS_ATTACK_IMG_1_6, BOSS_ATTACK_IMG_1_7, BOSS_ATTACK_IMG_1_8]

    BOSS_SHOOT_IMAGE = [BOSS_SHOOT_IMG_1, BOSS_SHOOT_IMG_2, BOSS_SHOOT_IMG_3, BOSS_SHOOT_IMG_4, BOSS_SHOOT_IMG_5,
                        BOSS_SHOOT_IMG_6, BOSS_SHOOT_IMG_7, BOSS_SHOOT_IMG_8, BOSS_SHOOT_IMG_9, BOSS_SHOOT_IMG_10]
    # ROCKET ATTACK
    ROCKET = ([ROCKET_1, ROCKET_2, ROCKET_3, ROCKET_4, ROCKET_5, ROCKET_6, ROCKET_7, ROCKET_8, ROCKET_9, ROCKET_10],
              [BOSS_R_ATTACK_1, BOSS_R_ATTACK_2, BOSS_R_ATTACK_3, BOSS_R_ATTACK_4, BOSS_R_ATTACK_5,
               BOSS_R_ATTACK_6, BOSS_R_ATTACK_7, BOSS_R_ATTACK_8, BOSS_R_ATTACK_9, BOSS_R_ATTACK_10])

    # BOSS SHIP IMG/EXPLOSION
    BOSS_SHIP = [MAIN_BOSS_IMAGE, BOSS_EXPLOSION_1, BOSS_EXPLOSION_2, BOSS_EXPLOSION_3, BOSS_EXPLOSION_4,
                 BOSS_EXPLOSION_5, BOSS_EXPLOSION_6, BOSS_EXPLOSION_7, BOSS_EXPLOSION_8, BOSS_EXPLOSION_9,
                 BOSS_EXPLOSION_10, BOSS_EXPLOSION_11, BOSS_EXPLOSION_12, BOSS_EXPLOSION_13, BOSS_EXPLOSION_14,
                 BOSS_EXPLOSION_15, BOSS_EXPLOSION_16, BOSS_EXPLOSION_17]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 0
        self.index_ship_img = 0
        self.index_laser_img = 0
        self.index_shooting = 0
        self.ship_img = self.BOSS_SHIP[0]  # IMG FOR THE BOSS SHIP
        self.laser_img = self.BOSS_ATTACK_1[0]  # IMG FOR THE NORMAL ATTACK
        self.rocket_img = self.ROCKET[0][0]  # IMG FOR THE ROCKET ATTACK
        self.rockets = []
        self.index_rocket_ship = 0
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.health_x = 0
        self.health_y = 0
        self.laser_x = 0
        self.laser_y = 0

    def get_health(self):
        return self.health

    def draw(self, window):
        for rocket in self.rockets:
            rocket.draw_rocket(window)
        for laser in self.lasers:
            laser.draw(window)

        super().draw(window)

    def move_boss_lasers(self, vel):
        """
        Moves the lasers of the boss (Y-axis)
        :param vel: Int
        :return: None
        """
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)

    def move_boss_rockets(self, vel):
        """
        Moves the rockets of the boss (Y-axis)
        :param vel: Int
        :return: None
        """
        for rocket in self.rockets:
            rocket.move(vel)
            if rocket.off_screen(HEIGHT):
                self.rockets.remove(rocket)

    def shoot1(self):
        """
        Creates a laser
        :return: None
        """
        laser = Laser(self.x + self.BOSS_SHIP[0].get_width() // 2 - 40,
                      self.y + self.BOSS_SHIP[0].get_height() - 50,
                      self.laser_img)
        self.lasers.append(laser)

    def shoot2(self):
        """
        Creates a laser
        :return: None
        """
        laser = Laser(self.x + self.BOSS_ATTACK_1[0].get_width() // 2 - 70,
                      self.y + self.BOSS_SHIP[0].get_height() - 50,
                      self.laser_img)
        self.lasers.append(laser)

    def rocket_attack(self):
        """
        Creates the rocket
        :return: None
        """

        rocket = Rocket(self.x + self.BOSS_SHIP[0].get_width() // 2 - self.rocket_img.get_width() // 2,
                        self.y + self.BOSS_SHIP[0].get_height() // 2 + self.rocket_img.get_height() // 2,
                        self.rocket_img)

        self.rockets.append(rocket)

    def change_to_shooting_ship(self, window):
        """
        Changes the Ship Image when shooting normal laser
        :param window: WIN
        :return: None
        """
        self.index_shooting += 1

        try:
            self.ship_img = self.BOSS_SHOOT_IMAGE[self.index_shooting//2]

        except Exception as e:
            print("IN FILE {BOSS_2_A} [EXCEPTION]: ", e)
        window.blit(self.ship_img, (self.x, self.y))

    def change_laser_collision(self, window, obj):
        """
        Changes the laser images to exploding laser images over the player
        :param window: WIN
        :param obj: Player
        :return: None
        """
        self.index_laser_img += 1
        try:
            self.laser_img = self.BOSS_ATTACK_1_EXP[self.index_laser_img]
        except Exception as e:
            print("IN FILE {ENEMY} [EXCEPTION]: ", e)

        window.blit(self.laser_img, (obj.x - 65, obj.y - 70))

    def healthshow(self, window):
        health_font = pygame.font.SysFont("comicsans", 40)
        health_label = health_font.render(f"Boss Health: {self.get_health()}", 1, (255, 255, 255))
        window.blit(health_label, (10, 10))

    def move(self, vel):
        """
        Moves the boss left / right
        :param vel: Int
        :return: None
        """
        if self.y < 50:
            self.y += vel

        if self.health > 0:
            if self.y >= - 25:
                if self.MOVE:
                    if self.x + 2 <= 0:
                        self.MOVE = False
                    elif self.x + 2 > 0:
                        self.x -= 2
                elif not self.MOVE:
                    if self.x + 2 + self.get_width() >= WIDTH:
                        self.MOVE = True
                    elif self.x + 2 + self.get_width() < WIDTH:
                        self.x += 2
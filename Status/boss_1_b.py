import pygame
import os
from ship import Ship
from laser import Laser
from rocket import Rocket
import random

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# BOSS IMAGE/DEATH/EXPLOSION
BOSS_IMAGE = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b", "Boss_Full.png")).convert_alpha()
BOSS_EXP_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Death_000.png")).convert_alpha()
BOSS_EXP_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Death_001.png")).convert_alpha()
BOSS_EXP_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Death_002.png")).convert_alpha()
BOSS_EXP_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Death_003.png")).convert_alpha()
BOSS_EXP_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Death_004.png")).convert_alpha()
BOSS_EXP_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Death_005.png")).convert_alpha()
BOSS_EXP_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Death_006.png")).convert_alpha()
BOSS_EXP_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Death_007.png")).convert_alpha()
BOSS_EXP_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Death_008.png")).convert_alpha()
BOSS_EXP_10 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Death_009.png")).convert_alpha()
BOSS_EXP_11 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_1.png")).convert_alpha()
BOSS_EXP_12 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_2.png")).convert_alpha()
BOSS_EXP_13 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_3.png")).convert_alpha()
BOSS_EXP_14 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_4.png")).convert_alpha()
BOSS_EXP_15 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_5.png")).convert_alpha()
BOSS_EXP_16 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_6.png")).convert_alpha()
BOSS_EXP_17 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_7.png")).convert_alpha()
BOSS_EXP_18 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_8.png")).convert_alpha()
BOSS_EXP_19 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_9.png")).convert_alpha()
BOSS_EXP_20 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_10.png")).convert_alpha()
BOSS_EXP_21 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_11.png")).convert_alpha()
BOSS_EXP_22 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_12.png")).convert_alpha()
BOSS_EXP_23 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_13.png")).convert_alpha()
BOSS_EXP_24 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_14.png")).convert_alpha()
BOSS_EXP_25 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Exp", "Explosion1_15.png")).convert_alpha()

# BOSS LASER
BOSS_LASER_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_1.png")).convert_alpha()
BOSS_LASER_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_2.png")).convert_alpha()
BOSS_LASER_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_3.png")).convert_alpha()
BOSS_LASER_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_4.png")).convert_alpha()
BOSS_LASER_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_5.png")).convert_alpha()
BOSS_LASER_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_6.png")).convert_alpha()
BOSS_LASER_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_7.png")).convert_alpha()
BOSS_LASER_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_8.png")).convert_alpha()
BOSS_LASER_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_9.png")).convert_alpha()
BOSS_LASER_10 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_10.png")).convert_alpha()
BOSS_LASER_11 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_11.png")).convert_alpha()
BOSS_LASER_12 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_12.png")).convert_alpha()
BOSS_LASER_13 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_13.png")).convert_alpha()
BOSS_LASER_14 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_14.png")).convert_alpha()
BOSS_LASER_15 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_15.png")).convert_alpha()
BOSS_LASER_16 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_16.png")).convert_alpha()
BOSS_LASER_17 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_17.png")).convert_alpha()
BOSS_LASER_18 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_18.png")).convert_alpha()
BOSS_LASER_19 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_19.png")).convert_alpha()
BOSS_LASER_20 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_20.png")).convert_alpha()
BOSS_LASER_21 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_21.png")).convert_alpha()
BOSS_LASER_22 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Boss_Laser_1", "shot_22.png")).convert_alpha()

# BOSS ROCKET
BOSS_ROCKET_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Rocket", "Missile_000.png")).convert_alpha()
BOSS_ROCKET_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Rocket", "Missile_001.png")).convert_alpha()
BOSS_ROCKET_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Rocket", "Missile_002.png")).convert_alpha()
BOSS_ROCKET_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Rocket", "Missile_003.png")).convert_alpha()
BOSS_ROCKET_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Rocket", "Missile_004.png")).convert_alpha()
BOSS_ROCKET_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Rocket", "Missile_005.png")).convert_alpha()
BOSS_ROCKET_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Rocket", "Missile_006.png")).convert_alpha()
BOSS_ROCKET_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Rocket", "Missile_007.png")).convert_alpha()
BOSS_ROCKET_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Rocket", "Missile_008.png")).convert_alpha()
BOSS_ROCKET_10 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss1_b/Rocket", "Missile_009.png")).convert_alpha()


class Boss_1_b(Ship):
    MOVE = True
    BOSS_IMAGES = [BOSS_IMAGE, BOSS_EXP_1, BOSS_EXP_2, BOSS_EXP_3, BOSS_EXP_4, BOSS_EXP_5, BOSS_EXP_6, BOSS_EXP_7,
                   BOSS_EXP_8, BOSS_EXP_9, BOSS_EXP_10, BOSS_EXP_11, BOSS_EXP_12, BOSS_EXP_13, BOSS_EXP_14, BOSS_EXP_15,
                   BOSS_EXP_16, BOSS_EXP_17, BOSS_EXP_18, BOSS_EXP_19, BOSS_EXP_20, BOSS_EXP_21, BOSS_EXP_22,
                   BOSS_EXP_23, BOSS_EXP_24, BOSS_EXP_25]

    BOSS_NORM_LASER = [BOSS_LASER_1, BOSS_LASER_2, BOSS_LASER_3, BOSS_LASER_4, BOSS_LASER_5, BOSS_LASER_6, BOSS_LASER_7,
                       BOSS_LASER_8, BOSS_LASER_9, BOSS_LASER_10, BOSS_LASER_11, BOSS_LASER_12, BOSS_LASER_13,
                       BOSS_LASER_14, BOSS_LASER_15, BOSS_LASER_16, BOSS_LASER_17, BOSS_LASER_18, BOSS_LASER_19,
                       BOSS_LASER_20, BOSS_LASER_21, BOSS_LASER_22]

    BOSS_ROCKET = [BOSS_ROCKET_1, BOSS_ROCKET_2, BOSS_ROCKET_3, BOSS_ROCKET_4, BOSS_ROCKET_5,
                   BOSS_ROCKET_6, BOSS_ROCKET_7, BOSS_ROCKET_8, BOSS_ROCKET_9, BOSS_ROCKET_10]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.health = 0
        self.ship_img = self.BOSS_IMAGES[0]
        self.laser_img = self.BOSS_NORM_LASER[0]
        self.rocket_img = self.BOSS_ROCKET[0]
        self.rockets = []
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.index_ship_img = 0
        self.index_laser_img = 10
        self.health_x = 0
        self.health_y = 0

    def get_health(self):
        return self.health

    def draw(self, window):
        super().draw(window)

        for rocket in self.rockets:
            rocket.draw_rocket(window)
        for laser in self.lasers:
            laser.draw(window)

    def move_boss_rocket(self, vel):
        for rocket in self.rockets:
            rocket.move(vel)
            if rocket.off_screen(HEIGHT):
                self.rockets.remove(rocket)

    def shoot_rockets(self):
        rocket = Rocket(random.randrange(50, WIDTH - 200), - 75, self.rocket_img)
        rocket1 = Rocket(random.randrange(50, WIDTH - 200), - 75, self.rocket_img)

        self.rockets.append(rocket)
        self.rockets.append(rocket1)

    def move_boss_laser(self, vel):
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)

    def shoot_lasers(self):
        laser = Laser(self.x + self.ship_img.get_width() // 2 - self.laser_img.get_width() // 2 - 45,
                      self.y + self.ship_img.get_height(),
                      self.laser_img)

        self.lasers.append(laser)

        laser = Laser(self.x + self.ship_img.get_width() // 2 - self.laser_img.get_width() // 2 + 45,
                      self.y + self.ship_img.get_height(),
                      self.laser_img)

        self.lasers.append(laser)

    def change_boss_image_exp(self, window):
        """
        CHANGE BOSS IMAGE WHEN HEALTH < 0
        :param window: WIN
        :return: None
        """
        if self.index_ship_img >= len(self.BOSS_IMAGES) - 1:
            self.index_ship_img = 0

        self.index_ship_img += 1
        try:
            self.ship_img = self.BOSS_IMAGES[self.index_ship_img]
        except Exception as e:
            print("IN FILE {BOSS} [EXCEPTION]: ", e)
        window.blit(self.ship_img, (self.x, self.y))

    def change_boss_laser_collision(self, obj, window):
        """
        CHANGE BOSS LASER IMAGE WHEN COLLISION IS TRUE
        :param obj: Player
        :param window: WIN
        :return: None
        """
        if self.index_laser_img >= len(self.BOSS_NORM_LASER) - 1:
            self.index_laser_img = 10

        self.index_laser_img += 1
        try:
            self.laser_img = self.BOSS_NORM_LASER[self.index_laser_img]
        except Exception as e:
            print("IN FILE {BOSS_1_B} [EXCEPTION]: ", e)

        window.blit(self.laser_img,
                    (obj.x - self.laser_img.get_width() // 2 + obj.ship_img.get_width() // 2,
                     obj.y - obj.ship_img.get_height()))

    def healthshow(self, window):
        """
        SHOWS BOSS HEALTH
        :param window: WIN
        :return: None
        """
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

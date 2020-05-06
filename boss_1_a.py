import pygame
import os
from laser import Laser
from ship import Ship

WIDTH, HEIGHT = 1000, 700
# BOSS SHIPS / BOSS EXPLOSION
ENEMY_BOSS_SHIP_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Boss", "enemy_boss_ship.png"))
ENEMY_BOSS_SHIP_EXPLOSION_5 = pygame.image.load(
    os.path.join("Images/Enemy/Planet_A/Ship_Explosion/Ship6_Explosion", "Ship5_Explosion_008.png"))
ENEMY_BOSS_SHIP_EXPLOSION_6 = pygame.image.load(
    os.path.join("Images/Enemy/Planet_A/Ship_Explosion/Ship6_Explosion", "Ship5_Explosion_011.png"))
ENEMY_BOSS_SHIP_EXPLOSION_7 = pygame.image.load(
    os.path.join("Images/Enemy/Planet_A/Ship_Explosion/Ship6_Explosion", "Ship5_Explosion_013.png"))
ENEMY_BOSS_SHIP_EXPLOSION_8 = pygame.image.load(
    os.path.join("Images/Enemy/Planet_A/Ship_Explosion/Ship6_Explosion", "Ship5_Explosion_014.png"))
ENEMY_BOSS_SHIP_EXPLOSION_9 = pygame.image.load(
    os.path.join("Images/Enemy/Planet_A/Ship_Explosion/Ship6_Explosion", "Ship5_Explosion_017.png"))
ENEMY_BOSS_SHIP_EXPLOSION_10 = pygame.image.load(
    os.path.join("Images/Enemy/Planet_A/Ship_Explosion/Ship6_Explosion", "Ship5_Explosion_019.png"))

# BOSS LASERS
BOSS_LASER_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_1.png"))
BOSS_LASER_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_2.png"))
BOSS_LASER_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_3.png"))
BOSS_LASER_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_4.png"))
BOSS_LASER_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_asset.png"))
BOSS_LASER_EXPLOSION_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_exp1.png"))
BOSS_LASER_EXPLOSION_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_exp2.png"))
BOSS_LASER_EXPLOSION_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_exp3.png"))
BOSS_LASER_EXPLOSION_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_exp4.png"))
BOSS_LASER_EXPLOSION_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_exp5.png"))
BOSS_LASER_EXPLOSION_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_exp6.png"))
BOSS_LASER_EXPLOSION_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_exp7.png"))
BOSS_LASER_EXPLOSION_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_exp8.png"))
BOSS_LASER_EXPLOSION_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_exp9.png"))
BOSS_LASER_EXPLOSION_10 = pygame.image.load(os.path.join("Images/Enemy/Planet_A/Enemy_lasers/Shot6", "shot6_exp10.png"))


class Boss(Ship):
    MOVE = True
    ENEMY_SHIP_MAP = [ENEMY_BOSS_SHIP_1, ENEMY_BOSS_SHIP_EXPLOSION_5,
                      ENEMY_BOSS_SHIP_EXPLOSION_6, ENEMY_BOSS_SHIP_EXPLOSION_7, ENEMY_BOSS_SHIP_EXPLOSION_8,
                      ENEMY_BOSS_SHIP_EXPLOSION_9, ENEMY_BOSS_SHIP_EXPLOSION_10]

    ENEMY_LASER_MAP = [BOSS_LASER_1, BOSS_LASER_2, BOSS_LASER_3, BOSS_LASER_4, BOSS_LASER_5,
                       BOSS_LASER_EXPLOSION_1, BOSS_LASER_EXPLOSION_2, BOSS_LASER_EXPLOSION_3, BOSS_LASER_EXPLOSION_4,
                       BOSS_LASER_EXPLOSION_5, BOSS_LASER_EXPLOSION_6, BOSS_LASER_EXPLOSION_7, BOSS_LASER_EXPLOSION_8,
                       BOSS_LASER_EXPLOSION_9, BOSS_LASER_EXPLOSION_10]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 0
        self.ship_img = self.ENEMY_SHIP_MAP[0]
        self.laser_img = self.ENEMY_LASER_MAP[0]
        self.index_ship_img = 0
        self.index_laser_img = 4
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.health_x = 0
        self.health_y = 0

    def get_health(self):
        return self.health

    def draw(self, win):
        super().draw(win)

    def move_boss_lasers(self, vel):
        """
        MOVES BOSS LASER
        :param vel: Int
        :return: None
        """
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)

    def change_laser_collision(self, window, obj):
        """
        CHANGE BOSS LASER IMAGE WHEN COLLISION IS TRUE
        :param window: WIN
        :param obj: Player
        :return: None
        """
        self.index_laser_img += 1
        try:
            self.laser_img = self.ENEMY_LASER_MAP[self.index_laser_img]
        except Exception as e:
            print("IN FILE {ENEMY} [EXCEPTION]: ", e)

        window.blit(self.laser_img, (obj.x - 65, obj.y - 70))

    def shoot(self):
        laser = Laser(int(self.x + self.ship_img.get_width() / 2 - 130), self.y + self.ship_img.get_height() - 80,
                      self.laser_img)
        self.lasers.append(laser)

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
        MOVES THE BOSS LEFT/RIGHT
        :param vel: Int
        :return: None
        """
        if self.y < 0:
            self.y += vel

        if self.health > 0:
            if self.y >= 0:
                if self.MOVE:
                    if self.x + 2 <= 0:
                        self.MOVE = False
                    if self.x + 2 > 0:
                        self.x -= 2
                elif not self.MOVE:
                    if self.x + 2 + self.get_width() >= WIDTH:
                        self.MOVE = True
                    if self.x + 2 + self.get_width() < WIDTH:
                        self.x += 2

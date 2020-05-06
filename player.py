import pygame
import os
from ship import Ship
from laser import Laser

WIDTH, HEIGHT = 900, 700

# Ship image
PLAYER_SHIP = pygame.image.load(os.path.join("Images/Player", "Player_ship.png"))
PLAYER_EXP_1 = pygame.image.load(os.path.join("Images/Player", "Explosion_001.png"))
PLAYER_EXP_2 = pygame.image.load(os.path.join("Images/Player", "Explosion_002.png"))
PLAYER_EXP_3 = pygame.image.load(os.path.join("Images/Player", "Explosion_003.png"))
PLAYER_EXP_4 = pygame.image.load(os.path.join("Images/Player", "Explosion_004.png"))
PLAYER_EXP_5 = pygame.image.load(os.path.join("Images/Player", "Explosion_005.png"))
PLAYER_EXP_6 = pygame.image.load(os.path.join("Images/Player", "Explosion_006.png"))
PLAYER_EXP_7 = pygame.image.load(os.path.join("Images/Player", "Explosion_007.png"))
PLAYER_EXP_8 = pygame.image.load(os.path.join("Images/Player", "Explosion_008.png"))
PLAYER_RIGHT_TURN = pygame.image.load(os.path.join("Images/Player", "Player_right_turn.png"))
PLAYER_LEFT_TURN = pygame.image.load(os.path.join("Images/Player", "Player_left_turn.png"))
PLAYER_LASER = pygame.image.load(os.path.join("Images/Player", "Player_1_Laser.png"))


class Player(Ship):
    PLAYER_SHIP_MAP = [PLAYER_SHIP, PLAYER_RIGHT_TURN, PLAYER_LEFT_TURN]
    PLAYER_EXP = [PLAYER_EXP_1, PLAYER_EXP_2, PLAYER_EXP_3, PLAYER_EXP_4, PLAYER_EXP_5,
                  PLAYER_EXP_6, PLAYER_EXP_7, PLAYER_EXP_8]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.ship_img = self.PLAYER_SHIP_MAP[0]
        self.laser_img = PLAYER_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = 100
        self.health = self.max_health
        self.attk_speed_counter = 1
        self.money = 0
        self.player_vel = 8
        self.counter = 0

    def draw(self, window):
        for laser in self.lasers:
            laser.draw(window)
        super().draw(window)
        self.healthbar(window)

    def explosion(self, window):

        if self.counter != len(self.PLAYER_EXP) - 1:

            self.counter += 1
            self.ship_img = self.PLAYER_EXP[self.counter]
            window.blit(self.ship_img, (self.x, self.y))

    def move_lasers(self, vel, objs):
        """
        MOVES THE LASER OF THE PLAYER
        :param vel: Int
        :param objs: ENEMIES / BOSES
        :return: None
        """
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        obj.health -= self.damage
                        try:
                            self.lasers.remove(laser)
                        except Exception as e:
                            print("IN FILE {PLAYER} [EXCEPTION] ", e)

    def shoot(self):
        if self.cooldown_counter == 0:
            laser = Laser(self.x - 3, self.y - self.ship_img.get_height() - 45, self.laser_img)
            self.lasers.append(laser)
            self.cooldown_counter = 2

    def healthbar(self, window):
        if self.health > 0:
            pygame.draw.rect(window, (0, 255, 0),
                             (self.x, self.y + self.ship_img.get_height() + 10,
                              self.ship_img.get_width() * (self.health / self.max_health), 10))

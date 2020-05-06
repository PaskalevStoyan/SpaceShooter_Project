import random
import pygame
import os
from ship import Ship
from laser import Laser
from robot import Robot
from rocket import Rocket

WIDTH, HEIGHT = 1000, 700

# BOSS IMAGE/DEATH/EXPLOSION
BOSS_IMAGE = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b", "Boss_Full.png"))
BOSS_EXP_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Death_000.png"))
BOSS_EXP_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Death_001.png"))
BOSS_EXP_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Death_002.png"))
BOSS_EXP_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Death_003.png"))
BOSS_EXP_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Death_004.png"))
BOSS_EXP_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Death_005.png"))
BOSS_EXP_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Death_006.png"))
BOSS_EXP_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Death_007.png"))
BOSS_EXP_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Death_008.png"))
BOSS_EXP_10 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Death_009.png"))
BOSS_EXP_11 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_1.png"))
BOSS_EXP_12 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_2.png"))
BOSS_EXP_13 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_3.png"))
BOSS_EXP_14 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_4.png"))
BOSS_EXP_15 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_5.png"))
BOSS_EXP_16 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_6.png"))
BOSS_EXP_17 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_7.png"))
BOSS_EXP_18 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_8.png"))
BOSS_EXP_19 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_9.png"))
BOSS_EXP_20 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_10.png"))
BOSS_EXP_21 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_11.png"))
BOSS_EXP_22 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_12.png"))
BOSS_EXP_23 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_13.png"))
BOSS_EXP_24 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_14.png"))
BOSS_EXP_25 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Exp", "Explosion1_15.png"))

# BOSS LASER
BOSS_LASER_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Laser", "Shot_1.png"))
BOSS_LASER_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Laser", "Shot_2.png"))
BOSS_LASER_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Laser", "Shot_3.png"))
BOSS_LASER_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Laser", "Shot_4.png"))
BOSS_LASER_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Laser", "Shot_5.png"))
BOSS_LASER_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Laser", "Shot_6.png"))
BOSS_LASER_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Laser", "Shot_7.png"))
BOSS_LASER_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Laser", "Shot_8.png"))
BOSS_LASER_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Laser", "Shot_9.png"))

# BOSS ROCKETS
BOSS_ROCKET_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Rocket", "Missile_000.png"))
BOSS_ROCKET_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Rocket", "Missile_001.png"))
BOSS_ROCKET_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Rocket", "Missile_002.png"))
BOSS_ROCKET_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Rocket", "Missile_003.png"))
BOSS_ROCKET_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Rocket", "Missile_004.png"))
BOSS_ROCKET_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Rocket", "Missile_005.png"))
BOSS_ROCKET_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Rocket", "Missile_006.png"))
BOSS_ROCKET_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Rocket", "Missile_007.png"))
BOSS_ROCKET_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Rocket", "Missile_008.png"))
BOSS_ROCKET_10 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Rocket", "Missile_009.png"))

# ROBOT FOR BOSS 2 PLANET B
BOSS_MINI_ROBOT_1 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Robot", "Robot_1.png"))
BOSS_MINI_ROBOT_2 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Robot", "Robot_2.png"))
BOSS_MINI_ROBOT_3 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Robot", "Robot_3.png"))
BOSS_MINI_ROBOT_4 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Robot", "Robot_4.png"))
BOSS_MINI_ROBOT_5 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Robot", "Robot_5.png"))
BOSS_MINI_ROBOT_6 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Robot", "Robot_6.png"))
BOSS_MINI_ROBOT_7 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Robot", "Robot_7.png"))
BOSS_MINI_ROBOT_8 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Robot", "Robot_8.png"))
BOSS_MINI_ROBOT_9 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Robot", "Robot_9.png"))
BOSS_MINI_ROBOT_10 = pygame.image.load(os.path.join("Images/Enemy/Planet_B/Boss2_b/Robot", "Robot_10.png"))


class Boss_2_b(Ship):
    MOVE = True
    BOSS_IMAGES = [BOSS_IMAGE, BOSS_EXP_1, BOSS_EXP_2, BOSS_EXP_3, BOSS_EXP_4, BOSS_EXP_5, BOSS_EXP_6, BOSS_EXP_7,
                   BOSS_EXP_8, BOSS_EXP_9, BOSS_EXP_10, BOSS_EXP_11, BOSS_EXP_12, BOSS_EXP_13, BOSS_EXP_14, BOSS_EXP_15,
                   BOSS_EXP_16, BOSS_EXP_17, BOSS_EXP_18, BOSS_EXP_19, BOSS_EXP_20, BOSS_EXP_21, BOSS_EXP_22,
                   BOSS_EXP_23, BOSS_EXP_24, BOSS_EXP_25]

    BOSS_LASER = [BOSS_LASER_1, BOSS_LASER_2, BOSS_LASER_3, BOSS_LASER_4, BOSS_LASER_5,
                  BOSS_LASER_6, BOSS_LASER_7, BOSS_LASER_8, BOSS_LASER_9]

    BOSS_ROCKET = [BOSS_ROCKET_1, BOSS_ROCKET_2, BOSS_ROCKET_3, BOSS_ROCKET_4, BOSS_ROCKET_5,
                   BOSS_ROCKET_6, BOSS_ROCKET_7, BOSS_ROCKET_8, BOSS_ROCKET_9, BOSS_ROCKET_10]

    ROBOT = [BOSS_MINI_ROBOT_1, BOSS_MINI_ROBOT_2, BOSS_MINI_ROBOT_3, BOSS_MINI_ROBOT_4, BOSS_MINI_ROBOT_5,
             BOSS_MINI_ROBOT_6, BOSS_MINI_ROBOT_7, BOSS_MINI_ROBOT_8, BOSS_MINI_ROBOT_9, BOSS_MINI_ROBOT_10]

    def __init__(self, x, y):

        super().__init__(x, y)
        self.x = x
        self.y = y
        self.ship_img = self.BOSS_IMAGES[0]
        self.laser_img = self.BOSS_LASER[0]
        self.rocket_img = self.BOSS_ROCKET[0]
        self.robot_image = self.ROBOT[0]
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.rockets = []
        self.robots = []
        self.index_ship_img = 0
        self.index_laser_img = 0
        self.health_x = 0
        self.health_y = 0

    def get_health(self):
        return self.health

    def draw(self, window):
        super().draw(window)

        for laser in self.lasers:
            laser.draw(window)
        for rocket in self.rockets:
            rocket.draw_rocket(window)
        for robot in self.robots:
            robot.draw(window)

    def shoot_lasers(self):
        laser1 = Laser(self.x + self.ship_img.get_width() // 2 - self.laser_img.get_width() // 2 - 30,
                       self.y + self.ship_img.get_height() - self.laser_img.get_width() // 2 - 15,
                       self.laser_img)

        laser2 = Laser(self.x + self.ship_img.get_width() // 2 - self.laser_img.get_width() // 2 + 60,
                       self.y + self.ship_img.get_height() - self.laser_img.get_width() // 2 - 15,
                       self.laser_img)

        self.lasers.append(laser1)
        self.lasers.append(laser2)

    def move_boss_lasers(self, vel):
        """
        MOVE BOSS LASER
        :param vel: Int
        :return: None
        """
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)

    def shoot_rockets(self):
        rocket1 = Rocket(random.randrange(50, WIDTH - 200), - 75, self.rocket_img)
        rocket2 = Rocket(random.randrange(50, WIDTH - 200), - 75, self.rocket_img)
        self.rockets.append(rocket1)
        self.rockets.append(rocket2)

    def move_boss_rockets(self, vel):
        """
        MOVE BOSS ROCKETS
        :param vel: Int
        :return: None
        """
        for rocket in self.rockets:
            rocket.move(vel)
            if rocket.off_screen(HEIGHT):
                self.rockets.remove(rocket)

    def create_robots(self):
        robot = Robot(random.randrange(50, WIDTH - 200), - 50, self.robot_image)

        self.robots.append(robot)

    def move_boss_robots(self, vel):
        """
        MOVE BOSS ROBOTS
        :param vel: Int
        :return: None
        """
        for robot in self.robots:
            robot.move(vel)
            if robot.off_screen(HEIGHT):
                self.robots.remove(robot)

    def change_boss_image_exp(self, window):
        """
        CHANGE BOSS IMAGE WHEN HEALTH < 0
        :param window: WIN
        :return: None
        """
        if self.index_ship_img >= len(self.BOSS_IMAGES) - 1:
            self.index_ship_img = 0
        self.index_ship_img += 1
        self.ship_img = self.BOSS_IMAGES[self.index_ship_img]
        window.blit(self.ship_img, (self.x, self.y))

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
        if self.y < - 10:
            self.y += vel

        if self.health > 0:
            if self.y >= - 10:
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

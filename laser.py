import pygame


def collide(obj1, obj2):
    """
    Checks if there is an overlap of the masks between the two Objects
    :param obj1: Player
    :param obj2: Either Enemy/Boss
    :return: Boolean
    """
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


def collide_boss2_a(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y - obj2.ship_img.get_height()

    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


class Laser(object):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.laser_index = 0
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def change_enemy_laser(self, obj, window):
        """
        Changes the laser image of the enemy before collision
        :param obj: enemy
        :param window: WIN
        :return: none
        """
        self.laser_index += 1
        if self.laser_index >= len(obj.ENEMY_MAP[obj.choice_img][1]):
            self.laser_index = 0

        self.img = obj.ENEMY_MAP[obj.choice_img][1][self.laser_index]
        window.blit(self.img, (self.x, self.y))

    def change_laser_boss1(self, obj, window):
        """
        Changes the laser images of the first boss of planet A before collision
        :param obj: boss
        :param window: WIN
        :return: None
        """

        self.laser_index += 1
        if self.laser_index >= len(obj.ENEMY_LASER_MAP):
            self.laser_index = 0

        self.img = obj.ENEMY_LASER_MAP[self.laser_index]
        window.blit(self.img, (self.x, self.y))

    def change_laser_boss_2_a(self, obj, window):
        """
        Changes the normal attack image of the second boss of planet A before collision
        :param obj: Boss 2
        :param window: WIN
        :return: None
        """
        if self.laser_index != len(obj.BOSS_ATTACK_1) - 1:
            if self.laser_index >= len(obj.BOSS_ATTACK_1) - 1:
                self.laser_index = 0
            self.laser_index += 1
            self.img = obj.BOSS_ATTACK_1[self.laser_index]
            window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def change_laser_boss_1_b(self, obj, window):
        """
        Changes the normal attack image of the first boss of planet B before collision
        :param obj: Boss 1
        :param window: WIN
        :return: None
        """
        if self.laser_index >= len(obj.BOSS_NORM_LASER) - 1:
            self.laser_index = 0
        self.laser_index += 1
        self.img = obj.BOSS_NORM_LASER[self.laser_index]
        window.blit(self.img, (self.x, self.y))

    def change_laser_boss_2_b(self, obj, window):
        """
        Changes the normal attack image of the second boss of Planet B before collision
        :param obj: Boss 2
        :param window: WIN
        :return: None
        """
        if self.laser_index >= len(obj.BOSS_LASER) - 1:
            self.laser_index = 0
        self.laser_index += 1
        self.img = obj.BOSS_LASER[self.laser_index]
        window.blit(self.img, (self.x, self.y))

    def off_screen(self, height):
        """
        Checks if the laser images are off screen
        :param height: HEIGHT of the screen
        :return: Boolean
        """
        return not (height >= self.y >= -90)

    def collision(self, obj):
        """
        Checks if there is a collision between 2 objects
        :param obj: either enemy/player/boses
        :return: Boolean
        """
        return collide(self, obj)

    def collision_boss_2(self, obj):
        """
        Checking if laser of boss_2_a is coliding with the player
        :param obj: Player
        :return: Boolean
        """
        return collide_boss2_a(self, obj)

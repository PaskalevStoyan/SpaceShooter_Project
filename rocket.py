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


class Rocket(object):

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.rocket_index = 0

        self.mask = pygame.mask.from_surface(self.img)

    def draw_rocket(self, window):
        window.blit(self.img, (self.x, self.y))

    def change_rocket_boss_2_a(self, obj, window):
        """
        Changes the rocket attack image of the second boss of planet A before collision
        :param obj: Boss 2
        :param window: WIN
        :return: None
        """
        if self.rocket_index >= len(obj.ROCKET[0]) - 1:
            self.rocket_index = 0

        self.rocket_index += 1
        self.img = obj.ROCKET[0][self.rocket_index]
        window.blit(self.img, (self.x, self.y))

    def change_rocket_boss_1_b(self, obj, window):
        """
        CHANGES THE ROCKET OF BOSS 1 OF PLANET B
        :param obj: BOSS 1 OF PLANET B
        :param window: WIN
        :return: None
        """

        if self.rocket_index >= len(obj.BOSS_ROCKET) - 1:
            self.rocket_index = 0

        self.rocket_index += 1
        self.img = obj.BOSS_ROCKET[self.rocket_index]
        window.blit(self.img, (self.x, self.y))

    def change_rocket_boss_2_b(self, obj, window):
        """
        CHANGES THE ROCKETS OF BOSS 2 OF PLANET B
        :param obj: BOSS 2 PLANET B
        :param window: WIN
        :return: None
        """
        if self.rocket_index >= len(obj.BOSS_ROCKET) - 1:
            self.rocket_index = 0
        self.rocket_index += 1
        self.img = obj.BOSS_ROCKET[self.rocket_index]
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

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
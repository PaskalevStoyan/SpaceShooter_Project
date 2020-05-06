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


class Robot(object):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.robot_index = 0
        self.robot_health = 500

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def change_robot_image(self, obj, window):
        if self.robot_index >= len(obj.ROBOT) - 1:
            self.robot_index = 0
        self.robot_index += 1
        self.img = obj.ROBOT[self.robot_index]
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

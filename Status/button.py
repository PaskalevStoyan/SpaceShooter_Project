import pygame


class Button(object):
    def __init__(self, x, y, width, height, img):
        self.x = x
        self.y = y

        self.width = width
        self.height = height
        self.img = img

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()

    def isOverButton(self, pos):
        """
        CHECKS IF MOUSE IS OVER THE BUTTON BOUNDS
        :param pos: (self.x, self.y)
        :return: Boolean
        """
        if self.x < pos[0] < self.x + self.img.get_width():
            if self.y < pos[1] < self.y + self.img.get_height():
                return True

        return False

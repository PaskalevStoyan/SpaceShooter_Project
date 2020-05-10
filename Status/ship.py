# Abstract Class

WIDTH, HEIGHT = 1000, 700


class Ship(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.max_health = 0
        self.armor = 0
        self.damage = 0
        self.ship_img = None
        self.laser_img = None
        self.lasers = []

        self.cooldown_counter = 0  # Cooldown for lasers
        self.COOLDOWN = 30

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def cooldown(self):
        """
        MAKES A COOLDOWN OF THE SHOOTING OF THE PLAYER
        :return:
        """
        if self.cooldown_counter >= self.COOLDOWN:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

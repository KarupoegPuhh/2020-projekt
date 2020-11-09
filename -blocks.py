import pygame

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.laius = 32
        self.kõrgus = 32

    def render(self, bg):
        pygame.draw.rect(bg, (0,0,0),(self.x, self.y, self.laius, self.kõrgus))
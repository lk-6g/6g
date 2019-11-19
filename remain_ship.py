import pygame
from pygame.sprite import Sprite

class RemainShip(Sprite):
    def __init__(self, screen):
        super().__init__()

        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (30, 24))
        self.rect = self.image.get_rect()
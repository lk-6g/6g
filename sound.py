import pygame

class Sound():
    def __init__(self, pygame):
        self.pygame = pygame
        self.pygame.init()
        self.pygame.mixer.init()
        
    def bullet_fire_sound(self):
        pygame.mixer_music.load('media/bullet_fire.mp3')
        pygame.mixer_music.set_volume(1)
        pygame.mixer_music.play()
        
    def bullet_alien_sound(self):
        pygame.mixer_music.load('media/bullet_alien.mp3')
        pygame.mixer_music.set_volume(1)
        pygame.mixer_music.play()
        
    def explode_sound(self):
        pygame.mixer_music.load('media/explode.mp3')
        pygame.mixer_music.set_volume(1)
        pygame.mixer_music.play()

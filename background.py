import pygame

class Background():
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen    
        
        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.rect.right = self.screen_rect.right - 20
        self.rect.centery = self.screen_rect.centery + 20
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

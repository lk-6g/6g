import pygame.font
from pygame.sprite import Group
from remain_ship import RemainShip

class Scoreboard():
    def __init__(self,ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        self.text_color = (255, 215, 0)
        self.font = pygame.font.SysFont(None, 30)
        
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_remain_ships()
        
    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = 'Sco: ' + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str ='Max: ' +  "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 400
        self.high_score_rect.top = 20
        
    def prep_level(self):
        self.level_str = 'Level: ' + str(self.stats.level)
        self.level_image = self.font.render(self.level_str, True, self.text_color, self.ai_settings.bg_color)
        
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.centerx = self.screen_rect.centerx - 200
        self.level_image_rect.top = 20
        
    def prep_remain_ships(self):
        self.remain_ships = Group()
        for ship_number in range(self.stats.ships_left):
            remain_ship = RemainShip(self.screen)
            remain_ship.rect.x = 10 + ship_number * remain_ship.rect.width
            remain_ship.rect.y = 10
            self.remain_ships.add(remain_ship)
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.remain_ships.draw(self.screen)
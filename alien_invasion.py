import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from background import Background
from sound import Sound

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width))
    pygame.display.set_caption('Alien Invasion')
    
    sound = Sound(pygame)
    bg = Background(ai_settings, screen)
    play_button = Button(ai_settings, screen, 'PLAY')
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    sb = Scoreboard(ai_settings, screen, stats)
    
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    while True:
        gf.check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb, sound)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb, sound)
            gf.update_aliens(ai_settings, screen, ship, aliens, bullets, stats, sb, sound)
            
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb, bg)
    
run_game()
class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 1200
        self.bg_color = (6, 31, 62)
        
        self.ship_limit = 2
        
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (218, 122, 214)
        self.bullet_allowed = 8
        
        self.fleet_drop_speed = 10
        
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 2
        
        self.fleet_direction = 1
        
        self.alien_points = 50
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.score_scale * self.alien_points)
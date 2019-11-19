class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        
        self.read_max_score()
        
        self.high_score = int(self.read_max_score())
        
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        
    def read_max_score(self):
        filename = 'max_score_history.txt'
        
        with open(filename) as file_object:
            contents = file_object.read()
            if contents.strip() != "":
                return contents
            else:
                return 0
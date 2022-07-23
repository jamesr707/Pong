import random


class Settings:
    """a class to store all setting from Pong"""
    def __init__(self):

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (32, 32, 32)

        # paddle setting
        self.paddle_color = (255, 255, 255)
        self.paddle_width = 30
        self.paddle_height = 140
        self.paddle_speed = 1.0

        # ball settings
        self.ball_width = 30
        self.ball_height = 30
        self.ball_color = (0, 255, 255)
        self.ball_x_coordinate = self.screen_width/2 - self.ball_width/2
        self.ball_y_coordinate = self.screen_height/2 - self.ball_height/2
        self.ball_speed = 0.5
        # 1 represents right -1 represents left
        self.ball_horizontal_direction = random.choice((1, -1))
        self.ball_vertical_direction = random.choice((1, -1))

        # scoreboard position
        self.scoreboard_coor = 10

        # start game
        self.game_start = False



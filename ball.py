import pygame
import random
from time import sleep


class Ball:
    """create ball"""

    def __init__(self, pd_game):
        super().__init__()
        self.screen = pd_game.screen
        self.settings = pd_game.settings
        self.screen_rect = self.screen.get_rect()
        # create ball
        self.ball = self.center_ball = pygame.Rect(self.settings.ball_x_coordinate, self.settings.ball_y_coordinate,
                                                   self.settings.ball_width, self.settings.ball_height)
        # store x and y coordinates as decimal
        self.ball_x = float(self.ball.x)
        self.ball_y = float(self.ball.y)
        self.center_ball_x = float(self.center_ball.x)
        self.center_ball_y = float(self.center_ball.y)

    def update(self):
        self.ball_x += self.settings.ball_speed * self.settings.ball_horizontal_direction
        self.ball_y += self.settings.ball_speed * self.settings.ball_vertical_direction
        self.reset_ball()
        self.ball.x = self.ball_x
        self.ball.y = self.ball_y

    def draw_ball(self):
        pygame.draw.ellipse(self.screen, self.settings.ball_color, self.ball)

    def reset_ball(self):
        if self.ball.left <= 0 or self.ball.right >= self.settings.screen_width:
            sleep(1)
            self.ball_x = self.center_ball_x
            self.ball_y = self.center_ball_y
            self.settings.ball_horizontal_direction *= -1
            self.settings.ball_vertical_direction *= random.choice((1, -1))




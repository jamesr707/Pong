import pygame


class Paddles:

    def __init__(self, pd_game):
        super().__init__()

        self.screen = pd_game.screen
        self.settings = pd_game.settings
        self.screen_rect = pd_game.screen.get_rect()

        self.paddle_2_width = self.settings.screen_height/2 - self.settings.paddle_height/2
        self.first_paddle = pygame.Rect(0, self.settings.screen_height/2 - self.settings.paddle_height/2,
                                   self.settings.paddle_width, self.settings.paddle_height)

        self.second_paddle = pygame.Rect(self.settings.screen_width - self.settings.paddle_width, self.paddle_2_width,
                                         self.settings.paddle_width, self.settings.paddle_height)

        # store a decimal for the paddles vertical positions
        self.f_y = float(self.first_paddle.y)
        self.s_y = float(self.second_paddle.y)
        self.reset_paddles()

        # movement flags
        self.f_moving_up = False
        self.f_moving_down = False
        self.s_moving_up = False
        self.s_moving_down = False

    def update(self):
        if self.f_moving_up and self.first_paddle.top > 0:
            self.f_y -= self.settings.paddle_speed
        if self.s_moving_up and self.second_paddle.top > 0:
            self.s_y -= self.settings.paddle_speed
        if self.f_moving_down and self.first_paddle.bottom < self.screen_rect.bottom:
            self.f_y += self.settings.paddle_speed
        if self.s_moving_down and self.second_paddle.bottom < self.screen_rect.bottom:
            self.s_y += self.settings.paddle_speed
        # update the rect positions of my paddles
        self.first_paddle.y = self.f_y
        self.second_paddle.y = self.s_y

    def draw_paddles(self):
        pygame.draw.rect(self.screen, self.settings.paddle_color, self.first_paddle)
        pygame.draw.rect(self.screen, self.settings.paddle_color, self.second_paddle)

    def reset_paddles(self):
        self.first_paddle.midleft = self.screen_rect.midleft
        self.second_paddle.midright = self.screen_rect.midright
        self.f_y = float(self.first_paddle.y)
        self.s_y = float(self.second_paddle.y)










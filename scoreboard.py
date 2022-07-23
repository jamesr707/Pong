import pygame.font


class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, pd_game):
        self.screen = pd_game.screen
        self.settings = pd_game.settings
        self.screen_rect = pd_game.screen.get_rect()
        self.font = pygame.font.SysFont(None, 60)

        self.l_paddle_score = 0
        self.r_paddle_score = 0

        self.winning_score = 1
        self.prep_score()

    def prep_score(self):
        """turn the score into a rendered image"""
        l_score_str = f'{self.l_paddle_score}'
        r_score_str = f'{self.r_paddle_score}'

        self.l_score_image = self.font.render(l_score_str, True, self.settings.paddle_color, self.settings.bg_color)
        self.r_score_image = self.font.render(r_score_str, True, self.settings.paddle_color, self.settings.bg_color)

        # position scores on top left and right corners of the screen
        self.l_score_rect = self.l_score_image.get_rect()
        self.r_score_rect = self.r_score_image.get_rect()

        self.l_score_rect.x = self.settings.scoreboard_coor
        self.l_score_rect.y = self.settings.scoreboard_coor

        self.r_score_rect.x = self.settings.screen_width - self.l_score_rect.width - self.settings.scoreboard_coor
        self.r_score_rect.y = self.settings.scoreboard_coor

    def show_score(self):
        self.screen.blit(self.l_score_image, self.l_score_rect)
        self.screen.blit(self.r_score_image, self.r_score_rect)


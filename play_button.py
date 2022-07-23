import pygame


class PlayButton:
    """a class to manage play button"""

    def __init__(self, pd_game):

        super().__init__()
        self.settings = pd_game.settings
        self.screen = pd_game.screen
        self.screen_rect = pd_game.screen.get_rect()

        # load the play button
        self.image = pygame.image.load('images/play button.bmp')
        self.image_rect = self.image.get_rect()

        self.image_rect.center = self.screen_rect.center

    def draw_button(self):
        self.screen.blit(self.image, self.image_rect)

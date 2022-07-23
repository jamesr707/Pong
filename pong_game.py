import sys
import pygame
from settings import Settings
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
from play_button import PlayButton


class Pong:
    def __init__(self):
        """Initializing game and creating game resources"""

        pygame.init()  # initiates all pygame modules
        self.settings = Settings()
        # make screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Pong Game")
        self.pd = Paddles(self)
        self.ball = Ball(self)
        self.sb = Scoreboard(self)
        self.play = PlayButton(self)
        self.paused = False

    def run_game(self):
        """start the main loop of the game"""
        while True:
            self._check_events()
            if self.paused:
                continue
            else:
                if self.settings.game_start:
                    self.pd.update()
                    self.ball.update()
                    self._update_ball()
                    self._update_score()
            # creates screen
            self._update_screen_mode()

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play.image_rect.collidepoint(mouse_pos)
        if button_clicked and not self.settings.game_start:
            self.settings.game_start = True
            # hide mouse cursor
            pygame.mouse.set_visible(False)


    def _check_events(self):
        """watch for keyboard and mouse inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # lets you exit out of the window
            elif event.type == pygame.KEYDOWN:  # check to see if the key has been pressed
                self._check_keyboard_down_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyboard_up_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keyboard_down_event(self, event):
        """create key inputs to control game"""
        if event.key == pygame.K_w:
            self.pd.f_moving_up = True
        elif event.key == pygame.K_UP:
            self.pd.s_moving_up = True
        elif event.key == pygame.K_DOWN:
            self.pd.s_moving_down = True
        elif event.key == pygame.K_s:
            self.pd.f_moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            self.paused = not self.paused

    def _check_keyboard_up_event(self, event):
        """create return booleans to false when up key"""
        if event.key == pygame.K_w:
            self.pd.f_moving_up = False
        elif event.key == pygame.K_UP:
            self.pd.s_moving_up = False
        elif event.key == pygame.K_DOWN:
            self.pd.s_moving_down = False
        elif event.key == pygame.K_s:
            self.pd.f_moving_down = False

    def _update_ball(self):
        """change directions of the ball"""
        if self.ball.ball.bottom > self.settings.screen_height or self.ball.ball.top < 0:
            self.settings.ball_vertical_direction *= -1
        if self.ball.ball.colliderect(self.pd.first_paddle) or self.ball.ball.colliderect(self.pd.second_paddle):
            self.settings.ball_horizontal_direction *= -1

    def _update_score(self):
        """update score when player scores point"""
        if self.sb.l_paddle_score < self.sb.winning_score and self.sb.r_paddle_score < self.sb.winning_score:
            if self.ball.ball.left <= 0:
                self.sb.r_paddle_score += 1
                self.pd.reset_paddles()

            if self.ball.ball.right >= self.settings.screen_width:
                self.sb.l_paddle_score += 1
                self.pd.reset_paddles()
            self.sb.prep_score()
        else:
            self.settings.game_start = False
            pygame.mouse.set_visible(True)
            self.sb.r_paddle_score = 0
            self.sb.l_paddle_score = 0

    def _update_screen_mode(self):
        """redraw the screen during each pass through the loop"""

        self.screen.fill(self.settings.bg_color)
        # draw score
        self.sb.show_score()
        # draw middle line
        pygame.draw.aaline(self.screen, self.settings.paddle_color,
                           (self.settings.screen_width/2, 0), (self.settings.screen_width/2, self.settings.screen_height))
        self.ball.draw_ball()
        # draw play button to screen
        if not self.settings.game_start:
            self.play.draw_button()
        self.pd.draw_paddles()
        # make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    pg = Pong()
    pg.run_game()




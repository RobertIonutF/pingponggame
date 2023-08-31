import pygame
from ball import Ball
from paddle import Paddle
from score import Score

import pygame
from ball import Ball
from paddle import Paddle
from score import Score

class Game:
    """
    A class representing the Ping Pong game.

    Attributes:
    - WIDTH (int): the width of the game screen
    - HEIGHT (int): the height of the game screen
    - BG_COLOR (tuple): the background color of the game screen
    - screen (pygame.Surface): the game screen
    - clock (pygame.time.Clock): the game clock
    - ball (Ball): the ball object in the game
    - left_paddle (Paddle): the left paddle object in the game
    - right_paddle (Paddle): the right paddle object in the game
    - font (pygame.font.Font): the font used for the score display
    - left_score (Score): the left player's score object
    - right_score (Score): the right player's score object

    Methods:
    - ai_move(): moves the right paddle based on the ball's position
    - run(): runs the game loop
    """

    def __init__(self):
        """
        Initializes the game.
        """
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.BG_COLOR = (0, 0, 0)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Ping Pong')
        self.clock = pygame.time.Clock()

        # Game objects
        self.ball = Ball(self.WIDTH // 2, self.HEIGHT // 2, 15, (255, 255, 255))
        self.left_paddle = Paddle(50, self.HEIGHT // 2 - 50, 10, 100, (255, 255, 255), 5)
        self.right_paddle = Paddle(self.WIDTH - 60, self.HEIGHT // 2 - 50, 10, 100, (255, 255, 255), 5)

        self.font = pygame.font.Font(None, 36)
        self.left_score = Score(self.font, self.WIDTH // 4, 10)
        self.right_score = Score(self.font, 3 * self.WIDTH // 4, 10)

    def ai_move(self):
        """
        Moves the right paddle based on the ball's position.
        """
        if self.ball.speed[0] > 0:
            if self.right_paddle.y + self.right_paddle.height/2 < self.ball.y:
                self.right_paddle.move('down', self.HEIGHT)
            else:
                self.right_paddle.move('up', self.HEIGHT)

    def run(self):
        """
        Runs the game loop.
        """
        running = True
        while running:
            self.screen.fill(self.BG_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.left_paddle.move('up', self.HEIGHT)
            if keys[pygame.K_s]:
                self.left_paddle.move('down', self.HEIGHT)

            self.ai_move()

            self.ball.move()
            if self.ball.y - self.ball.radius <= 0 or self.ball.y + self.ball.radius >= self.HEIGHT:
                self.ball.bounce('y')
            if self.ball.rect.colliderect(self.left_paddle.rect) or self.ball.rect.colliderect(self.right_paddle.rect):
                self.ball.bounce('x')

            if self.ball.x - self.ball.radius <= 0:
                self.right_score.increment()
                self.ball = Ball(self.WIDTH // 2, self.HEIGHT // 2, 15, (255, 255, 255))
            elif self.ball.x + self.ball.radius >= self.WIDTH:
                self.left_score.increment()
                self.ball = Ball(self.WIDTH // 2, self.HEIGHT // 2, 15, (255, 255, 255))

            self.ball.draw(self.screen)
            self.left_paddle.draw(self.screen)
            self.right_paddle.draw(self.screen)
            self.left_score.draw(self.screen)
            self.right_score.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
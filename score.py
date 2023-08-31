import pygame

class Score:
    """
    A class representing the score in a game of ping pong.

    Attributes:
    font (pygame.font.Font): The font used to render the score.
    x (int): The x-coordinate of the score's position on the screen.
    y (int): The y-coordinate of the score's position on the screen.
    score (int): The current score.
    """

    def __init__(self, font, x, y):
        self.score = 0
        self.font = font
        self.x = x
        self.y = y

    def increment(self):
        """
        Increment the score by 1.
        """
        self.score += 1

    def draw(self, screen):
        """
        Draw the score on the screen.

        Args:
        screen (pygame.Surface): The surface to draw the score on.
        """
        score_text = self.font.render(str(self.score), True, (255, 255, 255))
        screen.blit(score_text, (self.x, self.y))
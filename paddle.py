import pygame

import pygame

class Paddle:
    """
    A class to represent a paddle in a game of Ping Pong.

    Attributes
    ----------
    x : int
        The x-coordinate of the top-left corner of the paddle.
    y : int
        The y-coordinate of the top-left corner of the paddle.
    width : int
        The width of the paddle.
    height : int
        The height of the paddle.
    color : tuple
        The RGB color code of the paddle.
    speed : int
        The speed at which the paddle moves.

    Methods
    -------
    move(direction: str, max_height: int) -> None:
        Moves the paddle up or down based on the given direction.
    draw(screen: pygame.Surface) -> None:
        Draws the paddle on the given screen.
    """
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction, max_height):
        """
        Moves the paddle up or down based on the given direction.

        Parameters
        ----------
        direction : str
            The direction in which to move the paddle. Can be 'up' or 'down'.
        max_height : int
            The maximum height of the screen.

        Returns
        -------
        None
        """
        if direction == 'up' and self.y > 0:
            self.y -= self.speed
        elif direction == 'down' and self.y + self.height < max_height:
            self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        """
        Draws the paddle on the given screen.

        Parameters
        ----------
        screen : pygame.Surface
            The screen on which to draw the paddle.

        Returns
        -------
        None
        """
        pygame.draw.rect(screen, self.color, self.rect)
import pygame

import pygame

class Ball:
    """
    A class to represent a ball in a game of ping pong.

    Attributes
    ----------
    x : int
        The x-coordinate of the center of the ball.
    y : int
        The y-coordinate of the center of the ball.
    radius : int
        The radius of the ball.
    color : tuple
        The RGB color of the ball.
    speed : tuple, optional
        The speed of the ball in pixels per frame in the x and y directions, respectively. Default is (4, 4).

    Methods
    -------
    move():
        Move the ball according to its speed.
    draw(screen):
        Draw the ball on the given screen.
    bounce(axis):
        Reverse the direction of the ball's speed in the given axis ('x' or 'y').
    """
    def __init__(self, x, y, radius, color, speed=(4,4)):
        """
        Constructs all the necessary attributes for the ball object.

        Parameters
        ----------
            x : int
                The x-coordinate of the center of the ball.
            y : int
                The y-coordinate of the center of the ball.
            radius : int
                The radius of the ball.
            color : tuple
                The RGB color of the ball.
            speed : tuple, optional
                The speed of the ball in pixels per frame in the x and y directions, respectively. Default is (4, 4).
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)

    def move(self):
        """
        Move the ball according to its speed.
        """
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect.topleft = (self.x - self.radius, self.y - self.radius)

    def draw(self, screen):
        """
        Draw the ball on the given screen.

        Parameters
        ----------
        screen : pygame.Surface
            The surface on which to draw the ball.
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def bounce(self, axis):
        """
        Reverse the direction of the ball's speed in the given axis ('x' or 'y').

        Parameters
        ----------
        axis : str
            The axis in which to reverse the ball's speed ('x' or 'y').
        """
        if axis == 'x':
            self.speed = (-self.speed[0], self.speed[1])
        elif axis == 'y':
            self.speed = (self.speed[0], -self.speed[1])
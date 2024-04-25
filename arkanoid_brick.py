from turtle import Turtle
from typing import Union


class Brick(Turtle):
    """
    Represents a brick in the game.
    """

    BRICK_COLORS: list[str] = ["red", "orange", "yellow", "green", "blue"]
    BRICK_WIDTH: int = 50
    BRICK_HEIGHT: int = 20
    BRICK_GAP: int = 5  # Gap between bricks in the same row
    BRICK_ROWS: int = 5
    BRICK_COLS: int = 10

    def __init__(self, x: int, y: int, color: str) -> None:
        """
        Initializes the Brick object.

        Args:
            x (int): The x-coordinate of the brick.
            y (int): The y-coordinate of the brick.
            color (str): The color of the brick.

        Returns:
            None
        """
        super().__init__(shape="square")
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=1, stretch_len=2)  # Increases vertical size of the brick

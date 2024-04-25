from turtle import Screen, Turtle
from typing import List, Tuple

STARTING_POSITIONS: List[Tuple[int, int]] = [(0, -280), (-20, -280)]  # Start positions
MOVE_DISTANCE: int = 20
LEFT_BOUNDARY: int = -280  # Left border
RIGHT_BOUNDARY: int = 280  # Right border
PAD_WIDTH: int = 60  # Width of the pad


class Pad:
    """
    Represents a paddle in the game.
    """

    def __init__(self, screen: Screen, ball: Turtle) -> None:
        """
        Initializes the Pad object.

        Args:
            screen (Screen): The turtle screen.
            ball (Turtle): The ball object.

        Returns:
            None
        """
        self.pads: List[Turtle] = []
        self.screen: Screen = screen
        self.ball: Turtle = ball
        self.create_pad()
        self.head: Turtle = self.pads[1]

    def create_pad(self) -> None:
        """
        Creates the paddle objects.

        Returns:
            None
        """
        for pos in STARTING_POSITIONS:
            pad: Turtle = Turtle(shape="square")
            pad.color("white")
            pad.penup()
            pad.goto(pos)
            pad.shapesize(stretch_wid=0.5, stretch_len=PAD_WIDTH / 20)  # changes vertical size of the pad
            self.pads.append(pad)

    def move_left(self) -> None:
        """
        Moves the paddle to the left.

        Returns:
            None
        """
        if self.pads[0].xcor() - MOVE_DISTANCE > LEFT_BOUNDARY:
            for i in range(len(self.pads)):
                self.pads[i].goto(self.pads[i].xcor() - MOVE_DISTANCE, self.pads[i].ycor())
            self.screen.listen()

    def move_right(self) -> None:
        """
        Moves the paddle to the right.

        Returns:
            None
        """
        if self.pads[-1].xcor() + MOVE_DISTANCE < RIGHT_BOUNDARY:
            for i in range(len(self.pads)):
                self.pads[i].goto(self.pads[i].xcor() + MOVE_DISTANCE, self.pads[i].ycor())
            self.screen.listen()

from turtle import Turtle

BALL_RADIUS = Turtle().shapesize()[0] * 10 / 2  # Radius of the ball
BALL_COLOR = "white"
BALL_SPEED = 2  # Speed of the ball


class Ball(Turtle):
    """A class representing the ball in the game."""

    def __init__(self):
        """Initialize the Ball object."""
        super().__init__(shape="circle")
        self.color(BALL_COLOR)
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.dx: float = BALL_SPEED  # Speed along the X-axis
        self.dy: float = BALL_SPEED  # Speed along the Y-axis

    def move(self, pad: "Pad") -> None:
        """
        Move the ball.

        Args:
            pad (Pad): The pad object representing the game paddle.

        Returns:
            None
        """
        self.setx(self.xcor() + self.dx / 2)
        self.sety(self.ycor() + self.dy / 2)

        # Ball boundaries
        ball_top = self.ycor() + BALL_RADIUS
        ball_bottom = self.ycor() - BALL_RADIUS
        ball_left = self.xcor() - BALL_RADIUS
        ball_right = self.xcor() + BALL_RADIUS

        # Check collision with the top wall
        if ball_top > 290:
            self.dy *= -1

        # Check collision with the right wall
        if ball_right > 290:
            self.dx *= -1

        # Check collision with the left wall
        if ball_left < -290:
            self.dx *= -1

        # Check collision with the paddle
        if (ball_bottom < pad.pads[0].ycor() + 10) and (
                ball_right > pad.pads[0].xcor() - 50 and ball_left < pad.pads[0].xcor() + 50):
            self.dy *= -1

    def bounce_y(self) -> None:
        """Change the vertical direction of the ball."""
        self.dy *= -1

    def bounce_x(self) -> None:
        """Change the horizontal direction of the ball."""
        self.dx *= -1

    def reset_position(self) -> None:
        """Reset the position of the ball."""
        self.goto(0, 0)
        self.dx = abs(self.dx) * BALL_SPEED  # Set the X-axis speed while maintaining direction
        self.dy = abs(self.dy) * BALL_SPEED  # Set the Y-axis speed while maintaining direction

    def increase_speed(self) -> None:
        """Increase the speed of the ball."""
        global BALL_SPEED
        BALL_SPEED += 3
        # Update the dx and dy values of the ball object
        self.dx = self.dx / abs(self.dx) * BALL_SPEED  # Maintain the direction of movement along the X-axis
        self.dy = self.dy / abs(self.dy) * BALL_SPEED  # Maintain the direction of movement along the Y-axis

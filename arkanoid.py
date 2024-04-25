import threading
from turtle import Screen, ontimer
from arkanoid_pad import Pad
from arkanoid_brick import Brick
from arkanoid_ball import Ball
from arkanoid_info import Info
import time

SPEED_TIME = 10  # Time in milliseconds to increase speed
score: int = 0
level: int = 1

screen: Screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My breakout")
screen.tracer(0)

ball: Ball = Ball()
pad: Pad = Pad(screen, ball)
info: Info = Info()
if info is not None:
    info.update_info()
bricks: list[Brick] = []

start_y: int = 200
for row in range(Brick.BRICK_ROWS):
    color: str = Brick.BRICK_COLORS[row]
    y: int = start_y - row * (Brick.BRICK_HEIGHT + Brick.BRICK_GAP)
    for col in range(Brick.BRICK_COLS):
        x: int = -250 + col * (Brick.BRICK_WIDTH + Brick.BRICK_GAP)
        bricks.append(Brick(x, y, color))

screen.onkeypress(pad.move_left, "a")
screen.onkeypress(pad.move_right, "d")


def update() -> None:
    """
    Update function for the game loop.

    Returns:
        None
    """
    check_brick_collision()
    check_game_over()
    screen.update()
    ontimer(update, SPEED_TIME)


def ball_movement(ball: Ball, pad: Pad) -> None:
    """
    Function to move the ball.

    Args:
        ball (Ball): The ball object.
        pad (Pad): The pad object.

    Returns:
        None
    """
    while True:
        if ball is not None:
            ball.move(pad)
        time.sleep(0.01)


ball_thread: threading.Thread = threading.Thread(target=ball_movement, args=(ball, pad))
ball_thread.daemon = True
ball_thread.start()


def check_brick_collision() -> None:
    """
    Check collision with bricks.

    Returns:
        None
    """
    global score
    for brick in bricks:
        if ball.distance(brick) < 20:
            ball.bounce_y()
            bricks.remove(brick)
            brick.hideturtle()
            score += 1
            if info is not None:
                info.update_score(score)
            break


def check_game_over() -> None:
    """
    Check if the game is over.

    Returns:
        None
    """
    if ball is not None and info is not None:
        if ball.ycor() < -290:
            ball.reset_position()
            ball.dy = 0
            ball.dx = 0
            info.game_over()


def increase_speed_periodically() -> None:
    """
    Increase ball speed periodically.

    Returns:
        None
    """
    global level
    while True:
        time.sleep(15)
        ball.increase_speed()
        level += 1
        if info is not None:
            info.update_level(level)


speed_increase_thread: threading.Thread = threading.Thread(target=increase_speed_periodically)
speed_increase_thread.daemon = True
speed_increase_thread.start()

update()
screen.listen()


def on_close() -> None:
    """
    Event handler for window close.

    Returns:
        None
    """
    screen.bye()
    exit()


screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_close)

screen.mainloop()

from turtle import Turtle


class Info(Turtle):
    """
    Represents the information display in the game.
    """

    def __init__(self) -> None:
        """
        Initializes the Info object.

        Returns:
            None
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 50)
        self.score: int = 0
        self.level: int = 1

    def update_info(self) -> None:
        """
        Updates the displayed information with the current score and level.

        Returns:
            None
        """
        self.clear()
        self.write(f"Score: {self.score} Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def game_over(self) -> None:
        """
        Displays the game over message.

        Returns:
            None
        """
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))

    def update_level(self, level: int) -> None:
        """
        Updates the level and displays the updated information.

        Args:
            level (int): The new level.

        Returns:
            None
        """
        self.level = level
        self.update_info()

    def update_score(self, score: int) -> None:
        """
        Updates the score and displays the updated information.

        Args:
            score (int): The new score.

        Returns:
            None
        """
        self.score = score
        self.update_info()

class Score:
    """A class that describes a single game score."""

    def __init__(self, name: str, difficulty: str, time: int):
        """The class constructor that creates a new score.

        Args:
            name (str): The player's name.
            difficulty (str): The difficulty level of the game.
            time (int): The time spent solving the game as seconds.
        """

        self.name = name
        self.difficulty = difficulty
        self.time = time

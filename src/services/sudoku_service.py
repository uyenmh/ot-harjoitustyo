import time
from tkinter import Entry
from sudoku import Sudoku
from entities.score import Score
from repositories.score_repository import score_repository


class SudokuService:
    """A class that is responsible for the application logic.

    The class handles the creation of a Sudoku game and manages the time spent on the game,
    as well as saving and displaying of game scores.
    """

    def __init__(self, difficulty: str = "Easy"):
        """The class constructor. Initializes the Sudoku game based on difficulty level.

        Args:
            difficulty (str, optional): Defines the difficulty level of the Sudoku game.
                Defaults to "Easy".
        """

        self.difficulty = self._define_difficulty(difficulty)
        self.puzzle = Sudoku(3, seed=None).difficulty(self.difficulty)
        self.solution = self.puzzle.solve()
        self.start_time = time.time()
        self.pause_time_start = None
        self.total_paused_time = 0
        self._score_repository = score_repository

    def _define_difficulty(self, difficulty: str):
        """Changes the difficulty from a string to a numeric value between 0-1.

        Args:
            difficulty (str): A string that describes the chosen difficulty level
                for the Sudoku game.

        Returns:
            float: The chosen difficulty level converted into a numeric value.
        """

        if difficulty == "Easy":
            self.difficulty = 0.3
            return self.difficulty
        if difficulty == "Medium":
            self.difficulty = 0.45
            return self.difficulty
        self.difficulty = 0.6
        return self.difficulty

    def get_puzzle_board(self):
        """Returns the generated Sudoku board.

        Returns:
            list[list[Optional[int]]]: The generated Sudoku board.
        """

        return self.puzzle.board

    def get_solution_board(self):
        """Returns the solution to the generated Sudoku board.

        Returns:
            list[list[int]]: The solution to the generated Sudoku board.
        """

        return self.solution.board

    # AI generated code starts here
    def is_solution_correct(self, board: list[list[Entry]]) -> bool:
        """Checks if the given board matches with the solution to the generated Sudoku.

        Args:
            board (list[list[Entry]]): The game board that the user has filled out
                while trying to solve the Sudoku.

        Returns:
            bool: True if the user's solution is correct, False otherwise.
        """

        for row in range(9):
            for col in range(9):
                if board[row][col].get() != str(self.solution.board[row][col]):
                    return False
        return True
    # AI generated code ends here

    def get_elapsed_time_for_current_game(self):
        """Calculates the elapsed time for the current game.

        Returns:
            tuple: A tuple of elapsed hours, minutes, seconds and the total elapsed
                time in seconds.
        """

        current_time = time.time()
        elapsed_time = int(current_time - self.start_time - self.total_paused_time)
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)

        return hours, minutes, seconds, elapsed_time

    def pause_game(self):
        """Saves the time when the current game was last paused."""

        self.pause_time_start = time.time()

    def continue_game(self):
        """Saves the time when the paused game was continued and calculates the total paused time"""

        pause_time_end = time.time()
        self.total_paused_time += pause_time_end - self.pause_time_start

    def _get_elapsed_time_as_string(self, score: Score) -> str:
        """Converts the given score's elapsed time into a string.

        Args:
            score (Score): The object that contains the elapsed time in seconds.

        Returns:
            str: The elapsed time as a string.
        """

        elapsed_time = int(score.time)
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)

        time_as_str = ""
        if hours > 0:
            time_as_str = f"{hours}h {minutes}m {seconds}s"
        elif hours == 0 and minutes > 0:
            time_as_str = f"{minutes}m {seconds}s"
        else:
            time_as_str = f"{seconds}s"

        return time_as_str

    def save_score(self, name: str, difficulty: str, elapsed_time: int):
        """Saves the score of the current game.

        Args:
            name (str): The player's name.
            difficulty (str): The difficulty level of the played game.
            elapsed_time (int): The time spent solving the game as seconds.
        """

        self._score_repository.save(Score(name, difficulty, elapsed_time))

    def show_leaderboard(self):
        """Organizes the top ten scores of each difficulty into their respective lists.

        Returns:
            tuple: A tuple of three lists with each score formatted into a string.
        """

        scores = self._score_repository.show_top_ten()

        scores_at_hard = []
        scores_at_medium = []
        scores_at_easy = []

        index_hard = 1
        index_medium = 1
        index_easy = 1

        for score in scores:
            time_as_str = self._get_elapsed_time_as_string(score)

            if score.difficulty == "Hard":
                scores_at_hard.append(f"{index_hard}. {score.name} {time_as_str}")

                index_hard += 1
            elif score.difficulty == "Medium":
                scores_at_medium.append(f"{index_medium}. {score.name} {time_as_str}")

                index_medium += 1
            elif score.difficulty == "Easy":
                scores_at_easy.append(f"{index_easy}. {score.name} {time_as_str}")

                index_easy += 1

        return scores_at_hard, scores_at_medium, scores_at_easy

import time
from sudoku import Sudoku
from entities.score import Score
from repositories.score_repository import score_repository


class SudokuGame:
    def __init__(self, difficulty="Easy"):
        self.difficulty = self._define_difficulty(difficulty)
        self.puzzle = Sudoku(3, seed=None).difficulty(self.difficulty)
        self.solution = self.puzzle.solve()
        self.start_time = time.time()
        self.pause_time_start = None
        self.total_paused_time = 0
        self._score_repository = score_repository

    def _define_difficulty(self, difficulty):
        if difficulty == "Easy":
            self.difficulty = 0.3
            return self.difficulty
        if difficulty == "Medium":
            self.difficulty = 0.45
            return self.difficulty
        self.difficulty = 0.6
        return self.difficulty

    def get_puzzle_board(self):
        return self.puzzle.board

    def get_solution_board(self):
        return self.solution.board

    # AI generated code starts here
    def is_solution_correct(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col].get() != str(self.solution.board[row][col]):
                    return False
        return True
    # AI generated code ends here

    def get_elapsed_time_for_current_game(self):
        current_time = time.time()
        elapsed_time = int(current_time - self.start_time - self.total_paused_time)
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)

        return hours, minutes, seconds, elapsed_time

    def pause_game(self):
        self.pause_time_start = time.time()

    def continue_game(self):
        pause_time_end = time.time()
        self.total_paused_time += pause_time_end - self.pause_time_start

    def get_elapsed_time_as_string(self, score):
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

    def save_score(self, name, difficulty, elapsed_time):
        score = self._score_repository.save(Score(name, difficulty, elapsed_time))

        return score

    def show_leaderboard(self):
        scores = self._score_repository.show_top_ten()

        scores_at_hard = []
        scores_at_medium = []
        scores_at_easy = []

        index_hard = 1
        index_medium = 1
        index_easy = 1

        for score in scores:
            time_as_str = self.get_elapsed_time_as_string(score)

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

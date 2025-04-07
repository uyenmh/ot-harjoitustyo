import time
from sudoku import Sudoku


class SudokuGame:
    def __init__(self, difficulty="Easy"):
        self.difficulty = self._define_difficulty(difficulty)
        self.puzzle = Sudoku(3, seed=None).difficulty(self.difficulty)
        self.solution = self.puzzle.solve()
        self.start_time = time.time()
        self.end_time = None

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

    def get_elapsed_time(self):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
        return hours, minutes, seconds

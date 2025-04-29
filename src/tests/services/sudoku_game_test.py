import unittest
import time
import tkinter as tk
from sudoku import Sudoku
from services.sudoku_game import SudokuService


class TestSudokuService(unittest.TestCase):
    def setUp(self):
        self.game = SudokuService()

    def test_difficulty_not_changed(self):
        self.assertEqual(self.game.difficulty, 0.3)

    def test_change_difficulty_to_medium(self):
        self.game._define_difficulty("Medium")

        self.assertEqual(self.game.difficulty, 0.45)

    def test_change_difficulty_to_hard(self):
        self.game._define_difficulty("Hard")

        self.assertEqual(self.game.difficulty, 0.6)

    def test_get_puzzle_board_is_list(self):
        puzzle_board = self.game.get_puzzle_board()

        self.assertIsInstance(puzzle_board, list)

    def test_get_puzzle_board_is_correct_size_list(self):
        puzzle_board = self.game.get_puzzle_board()

        self.assertEqual(len(puzzle_board), 9)
        for row in range(9):
            self.assertEqual(len(puzzle_board[row]), 9)

    def test_get_solution_board_is_list(self):
        solution_board = self.game.get_solution_board()

        self.assertIsInstance(solution_board, list)

    def test_get_solution_board_is_correct_size_list(self):
        solution_board = self.game.get_solution_board()

        self.assertEqual(len(solution_board), 9)

        for row in range(9):
            self.assertEqual(len(solution_board[row]), 9)

    def test_get_solution_board_no_cells_are_none(self):
        solution_board = self.game.get_solution_board()

        for row in range(9):
            for col in range(9):
                self.assertIsNotNone(solution_board[row][col])

    def test_solution_is_incorrect(self):
        root = tk.Tk()
        puzzle = self.game.get_puzzle_board()
        board = [[tk.Entry(root) for _ in range(9)] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                preset_value = puzzle[row][col]
                if not preset_value:
                    board[row][col].insert(0, str(0))
                board[row][col].insert(0, str(preset_value))

        result = self.game.is_solution_correct(board)
        self.assertEqual(result, False)

    def test_solution_is_correct(self):
        root = tk.Tk()
        solution = self.game.get_solution_board()
        board = [[tk.Entry(root) for _ in range(9)] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                correct_value = solution[row][col]
                board[row][col].insert(0, str(correct_value))

        result = self.game.is_solution_correct(board)
        self.assertEqual(result, True)

    def test_getting_elapsed_time(self):
        time.sleep(5)
        elapsed_time = self.game.get_elapsed_time_for_current_game()

        self.assertEqual(elapsed_time, (0,0,5,5))
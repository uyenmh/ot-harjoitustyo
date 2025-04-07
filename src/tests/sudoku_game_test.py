import unittest
import tkinter as tk
from sudoku import Sudoku
from entities.sudoku_game import SudokuGame


class TestSudokuGame(unittest.TestCase):
    def setUp(self):
        self.game = SudokuGame()

    def test_define_difficulty(self):
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

    def test_is_solution_correct(self):
        pass

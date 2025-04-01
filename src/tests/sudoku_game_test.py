import unittest
import tkinter as tk
from sudoku import Sudoku
from entities.sudoku_game import SudokuGame  

class TestSudokuGame(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = SudokuGame(self.root)

    def test_choose_difficulty(self):
        self.app.difficulty.set("Hard")

        self.assertEqual(self.app.difficulty.get(), "Hard")

    def test_start_game_at_easy(self):
        self.app.start_game()

        self.assertEqual(self.app.difficulty.get(), "Easy")
        self.assertIsNotNone(self.app.game_root)
        self.assertEqual(self.app.game_root.title(), "Sudoku")
        self.assertIsInstance(self.app.puzzle, Sudoku)
        self.assertIsInstance(self.app.solution, Sudoku)

    def test_start_game_at_medium(self):
        self.app.difficulty.set("Medium")

        self.app.start_game()

        self.assertEqual(self.app.difficulty.get(), "Medium")
        self.assertIsNotNone(self.app.game_root)
        self.assertEqual(self.app.game_root.title(), "Sudoku")
        self.assertIsInstance(self.app.puzzle, Sudoku)
        self.assertIsInstance(self.app.solution, Sudoku)

    def test_start_game_at_hard(self):
        self.app.difficulty.set("Hard")

        self.app.start_game()

        self.assertEqual(self.app.difficulty.get(), "Hard")
        self.assertIsNotNone(self.app.game_root)
        self.assertEqual(self.app.game_root.title(), "Sudoku")
        self.assertIsInstance(self.app.puzzle, Sudoku)
        self.assertIsInstance(self.app.solution, Sudoku)

    def test_exit_game(self):
        pass
    
    def test_end_game(self):
        pass

    def test_check_correct_solution(self):
        pass

    def test_check_incorrect_solution(self):
        pass
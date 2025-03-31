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

    def test_start_game(self):
        pass

    def test_exit_game(self):
        pass

    def test_create_sudoku(self):
        pass
    
    def test_end_game(self):
        pass

    def test_check_solution(self):
        pass
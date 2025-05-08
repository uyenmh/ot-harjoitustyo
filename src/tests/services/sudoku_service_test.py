import unittest
import time
import tkinter as tk
from entities.score import Score
from services.sudoku_service import SudokuService


class FakeScoreRepository:
    def __init__(self, scores=None):
        self.scores = scores or []

    def save(self, score):
        self.scores.append(score)

        return score

    def show_top_ten(self):
        top_ten = []
        difficulties = ["Hard", "Medium", "Easy"]

        for difficulty in difficulties:
            scores_at_current_difficulty = []
            for score in self.scores:
                if score.difficulty == difficulty:
                    scores_at_current_difficulty.append(score)
            scores_at_current_difficulty.sort(key=lambda score: score.time)

            top_ten.extend(scores_at_current_difficulty[:10])

        return top_ten


class TestSudokuService(unittest.TestCase):
    def setUp(self):
        self.fake_score_repository = FakeScoreRepository()
        self.game = SudokuService("Easy", self.fake_score_repository)

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

    def test_getting_elapsed_time_for_current_game_no_pause(self):
        time.sleep(2)
        elapsed_time = self.game.get_elapsed_time_for_current_game()

        self.assertEqual(elapsed_time, (0,0,2,2))

    def test_getting_elapsed_time_for_current_game_with_pause(self):
        time.sleep(2)

        self.game.pause_game()
        time.sleep(1)
        self.game.continue_game()
        elapsed_time = self.game.get_elapsed_time_for_current_game()

        self.assertEqual(elapsed_time, (0,0,2,2))

    def test_pausing_game_gives_current_time(self):
        current_time = time.time()
        self.game.pause_game()

        self.assertEqual(int(self.game.pause_time_start), int(current_time))

    def test_continuing_once_paused_game_gives_total_paused_time(self):
        self.game.pause_game()
        time.sleep(1)
        self.game.continue_game()

        self.assertEqual(int(self.game.total_paused_time), 1)

    def test_continuing_twice_paused_game_gives_total_paused_time(self):
        self.game.pause_game()
        time.sleep(1)
        self.game.continue_game()

        self.game.pause_game()
        time.sleep(1)
        self.game.continue_game()

        self.assertEqual(int(self.game.total_paused_time), 2)

    def test_getting_elapsed_time_as_string_with_only_seconds(self):
        score = Score("anna", "Easy", 50)

        time_as_str = self.game._get_elapsed_time_as_string(score)

        self.assertEqual(time_as_str, "50s")

    def test_getting_elapsed_time_as_string_with_seconds_and_minutes(self):
        score = Score("anna", "Easy", 100)

        time_as_str = self.game._get_elapsed_time_as_string(score)

        self.assertEqual(time_as_str, "1m 40s")

    def test_getting_elapsed_time_as_string_with_seconds_minutes_and_hours(self):
        score = Score("anna", "Easy", 3605)

        time_as_str = self.game._get_elapsed_time_as_string(score)

        self.assertEqual(time_as_str, "1h 0m 5s")

    def test_save_score_saves_one_score_in_repository(self):
        self.game.save_score("anna", "Easy", 40)

        self.assertEqual(len(self.fake_score_repository.scores), 1)

        self.assertEqual(self.fake_score_repository.scores[0].name, "anna")
        self.assertEqual(self.fake_score_repository.scores[0].difficulty, "Easy")
        self.assertEqual(self.fake_score_repository.scores[0].time, 40)

    def test_save_score_saves_two_scores_in_repository(self):
        self.game.save_score("anna", "Easy", 40)
        self.game.save_score("eddie", "Hard", 500)

        self.assertEqual(len(self.fake_score_repository.scores), 2)

        self.assertEqual(self.fake_score_repository.scores[0].name, "anna")
        self.assertEqual(self.fake_score_repository.scores[0].difficulty, "Easy")
        self.assertEqual(self.fake_score_repository.scores[0].time, 40)

        self.assertEqual(self.fake_score_repository.scores[1].name, "eddie")
        self.assertEqual(self.fake_score_repository.scores[1].difficulty, "Hard")
        self.assertEqual(self.fake_score_repository.scores[1].time, 500)

    def test_show_leaderboard_with_less_than_ten_scores_each_difficulty(self):
        self.game.save_score("anna", "Easy", 40)
        self.game.save_score("jessie", "Medium", 300)
        self.game.save_score("eddie", "Hard", 500)

        leaderboard = self.game.show_leaderboard()

        self.assertEqual(len(leaderboard[0]), 1)
        self.assertEqual(len(leaderboard[1]), 1)
        self.assertEqual(len(leaderboard[2]), 1)

        self.assertEqual(leaderboard[0][0], "1. eddie 8m 20s")
        self.assertEqual(leaderboard[1][0], "1. jessie 5m 0s")
        self.assertEqual(leaderboard[2][0], "1. anna 40s")

    def test_show_leaderboard_with_more_than_ten_scores_at_easy(self):
        self.game.save_score("anna", "Easy", 40)
        self.game.save_score("anna", "Easy", 45)
        self.game.save_score("anna", "Easy", 50)
        self.game.save_score("betty", "Easy", 50)
        self.game.save_score("betty", "Easy", 55)

        self.game.save_score("anna", "Easy", 100)
        self.game.save_score("anna", "Easy", 100)
        self.game.save_score("anna", "Easy", 120)
        self.game.save_score("betty", "Easy", 140)
        self.game.save_score("anna", "Easy", 180)

        self.game.save_score("anna", "Easy", 240)

        self.game.save_score("jessie", "Medium", 300)
        self.game.save_score("eddie", "Hard", 500)

        leaderboard = self.game.show_leaderboard()

        self.assertEqual(len(leaderboard[0]), 1)
        self.assertEqual(len(leaderboard[1]), 1)
        self.assertEqual(len(leaderboard[2]), 10)

        self.assertEqual(leaderboard[0][0], "1. eddie 8m 20s")
        self.assertEqual(leaderboard[1][0], "1. jessie 5m 0s")

        self.assertEqual(leaderboard[2][0], "1. anna 40s")
        self.assertEqual(leaderboard[2][1], "2. anna 45s")
        self.assertEqual(leaderboard[2][2], "3. anna 50s")
        self.assertEqual(leaderboard[2][3], "4. betty 50s")
        self.assertEqual(leaderboard[2][4], "5. betty 55s")

        self.assertEqual(leaderboard[2][5], "6. anna 1m 40s")
        self.assertEqual(leaderboard[2][6], "7. anna 1m 40s")
        self.assertEqual(leaderboard[2][7], "8. anna 2m 0s")
        self.assertEqual(leaderboard[2][8], "9. betty 2m 20s")
        self.assertEqual(leaderboard[2][9], "10. anna 3m 0s")

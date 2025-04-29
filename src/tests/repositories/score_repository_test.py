import unittest
import sqlite3
from entities.score import Score
from repositories.score_repository import ScoreRepository

class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")

        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE scores (
                name TEXT,
                difficulty TEXT,
                time INTEGER
            )
        """)

        self.score_repository = ScoreRepository(self.connection)
    
    def tearDown(self):
        if self.connection:
            self.connection.close()

    def test_save(self):
        score = Score("anna", "Easy", 240)
        self.score_repository.save(score)

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT * FROM scores
        """)

        row = cursor.fetchone()        

        self.assertEqual(row[0], "anna")
        self.assertEqual(row[1], "Easy")
        self.assertEqual(row[2], 240)

    def test_show_top_ten(self):
        score1 = Score("anna", "Easy", 240)
        score2 = Score("becky", "Medium", 400)
        score3 = Score("michelle", "Hard", 700)

        self.score_repository.save(score1)
        self.score_repository.save(score2)
        self.score_repository.save(score3)

        top_ten_scores = self.score_repository.show_top_ten()

        self.assertEqual(
            (top_ten_scores[0].name, top_ten_scores[0].difficulty, top_ten_scores[0].time),
            (score3.name, score3.difficulty, score3.time)
        )
        self.assertEqual(
            (top_ten_scores[1].name, top_ten_scores[1].difficulty, top_ten_scores[1].time),
            (score2.name, score2.difficulty, score2.time)
        )
        self.assertEqual(
            (top_ten_scores[2].name, top_ten_scores[2].difficulty, top_ten_scores[2].time),
            (score1.name, score1.difficulty, score1.time))


import unittest
from entities.score import Score


class TestScore(unittest.TestCase):
    def test_score(self):
        score = Score("unknown", "Easy", 100)

        self.assertEqual((score.name, score.difficulty, score.time), ("unknown", "Easy", 100))

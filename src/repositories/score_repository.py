from entities.score import Score
from db_connection import get_db_connection

class ScoreRepository:
    def __init__(self, connection):
        self._connection = connection

    def save(self, score):
        cursor = self._connection.cursor()

        cursor.execute("""
            INSERT INTO scores (name, difficulty, time) values (?, ?, ?)
        """, (score.name, score.difficulty, score.time))

        self._connection.commit()

        return score

    def show_top_ten(self):
        cursor = self._connection.cursor()

        cursor.execute("""
            SELECT * FROM (
                SELECT name, difficulty, time, row_number() OVER
                    (PARTITION BY difficulty ORDER BY time ASC) 
                    AS row_number
                FROM scores
                )
            WHERE row_number <= 10
            ORDER BY 
                CASE difficulty
                    WHEN 'Hard' THEN 1
                    WHEN 'Medium' THEN 2
                    WHEN 'Easy' THEN 3
                END, 
                time ASC
        """)

        scores = cursor.fetchall()

        return [Score(name, difficulty, time) for name, difficulty, time, _ in scores]


score_repository = ScoreRepository(get_db_connection())

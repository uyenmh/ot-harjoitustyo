from entities.score import Score
from db_connection import get_db_connection

class ScoreRepository:
    """A class responsible for the database operations related to the game scores."""

    def __init__(self, connection):
        """The class constructor.

        Args:
            connection (sqlite3.Connection): The database connection object.
        """

        self._connection = connection

    def save(self, score: Score):
        """Saves the score to the database.

        Args:
            score (Score): An object that contains a name, difficulty and time.

        Returns:
            Score: The saved score as a Score object.
        """

        cursor = self._connection.cursor()

        cursor.execute("""
            INSERT INTO scores (name, difficulty, time) values (?, ?, ?)
        """, (score.name, score.difficulty, score.time))

        self._connection.commit()

        return score

    def show_top_ten(self):
        """Retrieves the top ten scores for each difficulty level.

        Returns:
            list[Score]: A list of Score objects, sorted first by difficulty and then time.
        """

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

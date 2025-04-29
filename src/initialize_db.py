from db_connection import get_db_connection


def drop_tables(connection):
    """Deletes database tables.

    Args:
        connection (sqlite3.Connection): The database connection object.
    """

    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS scores
    """)

    connection.commit()


def create_tables(connection):
    """Creates database tables.

    Args:
        connection (sqlite3.Connection): The database connection object.
    """

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE scores (
            name TEXT,
            difficulty TEXT,
            time INTEGER)
    """)

    connection.commit()


def initialize_database():
    """_Initializes the database tables."""

    connection = get_db_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()

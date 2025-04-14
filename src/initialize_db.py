from db_connection import get_db_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS scores
    """)

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE scores (
            name TEXT,
            difficulty TEXT,
            time INTEGER)
    """)

    connection.commit()


def initialize_database():
    connection = get_db_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()

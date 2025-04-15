import unittest
import sqlite3
from initialize_db import drop_tables, create_tables


class TestInitializeDatabase(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")

    def tearDown(self):
        if self.connection:
            self.connection.close()

    def test_create_tables(self):
        create_tables(self.connection)

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT name FROM sqlite_master WHERE type="table" AND name="scores"
        """)

        self.assertIsNotNone(cursor.fetchone())

    def test_drop_tables(self):
        create_tables(self.connection)

        drop_tables(self.connection)

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT name FROM sqlite_master WHERE type="table" AND name="scores"
        """)

        self.assertIsNone(cursor.fetchone())        


    def test_initialize_database(self):
        pass
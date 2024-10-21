import sqlite3
from datetime import datetime


class ReplyDatabase:
    def __init__(self, db_name="replies.db"):
        """
        Initializes the database connection and creates the Replies table if it doesn't exist.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        """
        Creates the Replies table with columns ID, Submission, Reply, and Reply_Date.
        """
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS Replies (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Submission TEXT NOT NULL,
                    Reply TEXT NOT NULL,
                    Reply_Date TEXT NOT NULL
                );
            """
            )

    def insert_reply(self, submission, reply):
        """
        Inserts a new reply into the Replies table.
        Args:
            submission (str): The submission content.
            reply (str): The reply content.
        """
        reply_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO Replies (Submission, Reply, Reply_Date)
                VALUES (?, ?, ?)
            """,
                (submission, reply, reply_date),
            )

    def check_reply_exists(self, submission):
        """
        Checks if a reply has already been made to the given submission.
        Args:
            submission (str): The submission content.

        Returns:
            bool: True if a reply exists for the submission, False otherwise.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT 1 FROM Replies WHERE Submission = ?
        """,
            (submission,),
        )
        return cursor.fetchone() is not None

    def close(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()

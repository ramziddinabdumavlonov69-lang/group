import sqlite3
from datetime import datetime

class Memory:
    def __init__(self):
        self.conn = sqlite3.connect("database.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT,
            value TEXT,
            created_at TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            created_at TEXT
        )
        """)

        self.conn.commit()

    def save_data(self, key, value):
        self.cursor.execute(
            "INSERT INTO data (key, value, created_at) VALUES (?, ?, ?)",
            (key, value, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        self.conn.commit()

    def search_data(self, keyword):
        self.cursor.execute(
            "SELECT key, value, created_at FROM data WHERE key LIKE ? OR value LIKE ?",
            ('%' + keyword + '%', '%' + keyword + '%')
        )
        return self.cursor.fetchall()

    def save_file(self, filename):
        self.cursor.execute(
            "INSERT INTO files (filename, created_at) VALUES (?, ?)",
            (filename, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        self.conn.commit()

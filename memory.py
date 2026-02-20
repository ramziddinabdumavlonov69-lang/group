import sqlite3

class Memory:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            content TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
        """)

        self.conn.commit()

    def add_memory(self, mtype, content):
        self.cursor.execute(
            "INSERT INTO memories (type, content) VALUES (?, ?)",
            (mtype, content)
        )
        self.conn.commit()

    def search_memory(self, keyword):
        self.cursor.execute(
            "SELECT content FROM memories WHERE content LIKE ?",
            ('%' + keyword + '%',)
        )
        return self.cursor.fetchall()

    def add_log(self, question, answer):
        self.cursor.execute(
            "INSERT INTO logs (question, answer) VALUES (?, ?)",
            (question, answer)
        )
        self.conn.commit()

    def get_all_memories(self):
        self.cursor.execute("SELECT id, type, content FROM memories")
        return self.cursor.fetchall()

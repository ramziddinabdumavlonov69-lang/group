import sqlite3

class Memory:
    def init(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT
        )
        """)
        self.conn.commit()

    def add_memory(self, text):
        self.cursor.execute("INSERT INTO memories (content) VALUES (?)", (text,))
        self.conn.commit()

    def get_all_memories(self):
        self.cursor.execute("SELECT * FROM memories")
        return self.cursor.fetchall()

    def search_memory(self, keyword):
        self.cursor.execute("SELECT * FROM memories WHERE content LIKE ?", ('%' + keyword + '%',))
        return self.cursor.fetchall()

    def delete_memory(self, memory_id):
        self.cursor.execute("DELETE FROM memories WHERE id=?", (memory_id,))
        self.conn.commit()

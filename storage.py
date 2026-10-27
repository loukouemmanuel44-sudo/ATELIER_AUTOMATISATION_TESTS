import sqlite3

def init_db():
    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status_code INTEGER,
            success INTEGER
        )
    """)

    conn.commit()
    conn.close()

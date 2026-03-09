import sqlite3

def init_db():
    conn = sqlite3.connect("youtube.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS watch_later (
        title TEXT
    )
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS playlists (
        playlist_name TEXT,
        video_title TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_watch_later(title):
    conn = sqlite3.connect("youtube.db")
    c = conn.cursor()
    c.execute("INSERT INTO watch_later VALUES (?)", (title,))
    conn.commit()
    conn.close()

def get_watch_later():
    conn = sqlite3.connect("youtube.db")
    c = conn.cursor()
    c.execute("SELECT * FROM watch_later")
    data = c.fetchall()
    conn.close()
    return data

import sqlite3

def get_connection():
    # Pour le MVP on utilise SQLite (plus simple que Postgres)
    conn = sqlite3.connect("sales.db")
    return conn

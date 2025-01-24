from models import initialize_db
import sqlite3

def add_user(name, age):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    initialize_db()
    add_user("Alice", 25)
    add_user("Bob", 30)
    print("Users in the database:")
    for user in get_users():
        print(user)
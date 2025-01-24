from database import create_connection, create_table

DATABASE = "test.db"

def initialize_db():
    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    );
    """

    conn = create_connection(DATABASE)
    if conn is not None:
        create_table(conn, sql_create_users_table)
        conn.close()
    else:
        print("Error: Cannot create the database connection.")
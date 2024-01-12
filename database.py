import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect('calendar_app.db')
        return conn
    except Exception as e:
        print(e)
    return None

def create_table():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS notes (
                              id INTEGER PRIMARY KEY,
                              date TEXT NOT NULL,
                              note TEXT NOT NULL
                              )""")
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()

def add_note(date, note):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO notes (date, note) VALUES (?, ?)", (date, note))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()

def get_notes(date):
    conn = create_connection()
    notes = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, note FROM notes WHERE date = ?", (date,))
            notes = cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            conn.close()
    return notes

# ... [rest of your database.py code]

# ... [rest of your database.py code]

def delete_note(date):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notes WHERE date = ?", (date,))
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()


# Initialize database and create tables
create_table()

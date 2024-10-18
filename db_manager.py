import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
def connect_db():
    conn = sqlite3.connect('movies.db')
    return conn

# Initialize the database with the necessary table
def initialize_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            language TEXT,
            watched BOOLEAN,
            rating INTEGER,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a new movie to the database
def add_movie(title, language=None, watched=False, rating=None, notes=None):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO movies (title, language, watched, rating, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, language, watched, rating, notes))
    conn.commit()
    conn.close()
    return "Successfully saved"

# Function to search movies by title
def search_movies_by_title(title_part, search_notes=False):
    conn = connect_db()
    cursor = conn.cursor()
    if search_notes:
        cursor.execute('''
            SELECT * FROM movies WHERE title LIKE ? OR notes LIKE ?
        ''', (f'%{title_part}%', f'%{title_part}%'))
    else:
        cursor.execute('''
            SELECT * FROM movies WHERE title LIKE ?
        ''', (f'%{title_part}%',))
    results = cursor.fetchall()
    conn.close()
    return results

# Function to edit a movie record
def edit_movie(movie_id, title=None, language=None, watched=None, rating=None, notes=None):
    conn = connect_db()
    cursor = conn.cursor()
    update_fields = {}
    if title is not None:
        update_fields['title'] = title
    if language is not None:
        update_fields['language'] = language
    if watched is not None:
        update_fields['watched'] = watched
    if rating is not None:
        update_fields['rating'] = rating
    if notes is not None:
        update_fields['notes'] = notes
    
    if update_fields:
        set_clause = ', '.join([f"{field} = ?" for field in update_fields])
        cursor.execute(f'''
            UPDATE movies SET {set_clause} WHERE id = ?
        ''', tuple(update_fields.values()) + (movie_id,))
        conn.commit()
    conn.close()
    return "Record updated successfully"

# Function to delete a movie record
def delete_movie(movie_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM movies WHERE id = ?
    ''', (movie_id,))
    conn.commit()
    conn.close()
    return "Record deleted successfully"
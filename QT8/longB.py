import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    c = conn.cursor()

    c.execute("SELECT id FROM genres WHERE title='боевик'")
    genre_id = c.fetchone()[0]

    c.execute("DELETE FROM films WHERE genre=? AND duration >= 90", (genre_id,))

    conn.commit()
    conn.close()



get_result("films.db")
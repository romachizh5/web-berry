import sqlite3


def create_db():
    db_lp = sqlite3.connect('login_password.db')
    cursor_db = db_lp.cursor()
    sql_create = '''CREATE TABLE passwords(
                id INT PRIMARY KEY,
                login TEXT NOT NULL,
                password TEXT NOT NULL);
                '''

    cursor_db.execute(sql_create)
    db_lp.commit()

    # cursor_db.close()
    # db_lp.close()


def change_login_password(login, password):
    id = 0
    db_lp = sqlite3.connect('login_password.db')
    cursor_db = db_lp.cursor()
    cursor_db.execute("""UPDATE passwords SET login = ? WHERE id = ?""", (login, id))
    cursor_db.execute("""UPDATE passwords SET password = ? WHERE id = ?""", (password, id))
    db_lp.commit()
    cursor_db.execute("""SELECT * FROM passwords""")
    print(cursor_db.fetchall())

    # cursor_db.close()
    # db_lp.close()


# create_db()
import sqlite3

db = sqlite3.connect('users_questionaire.db')
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            sex TEXT NOT NULL,
            abowt TEXT NOT NULL,
            photo TEXT NOT NULL
)
""")
db.commit()

def add_user_questionaire(user_id: int,user_data: dict):
    cur.execute("""
    INSERT INTO users(id, name, age, sex, abowt, photo) VALUES (?, ?, ?, ?, ?, ?)
    """,
    (user_id, user_data["name"], user_data["age"], user_data["sex"], user_data["about"], user_data["photo"],))

    db.commit()
    
    return print('данные добавлены в базу')


def get_user_data(user_id: int,):
    cur.execute("""SELECT * FROM users WHERE id = ?""", (user_id,))
    user_data = cur.fetchall()[0]
    print(user_data)
    result = {"name": user_data[1], "age": user_data[2], "sex": user_data[3], "about": user_data[4], "photo": user_data[5]}
    return  result


def get_all_users():
    cur.execute("""
        SELECT * FROM users
    """)
    return cur.fetchall()

print(get_all_users())
import sqlite3

db = sqlite3.connect('users_questionaire.db')
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            abowt TEXT NOT NULL,
            photo TEXT NOT NULL
)
""")
db.commit()

def add_user_questionaire(user_id: int,user_data: dict):
    cur.execute("""
    REPLACE INTO users(id, name, age, gender, abowt, photo) VALUES (?, ?, ?, ?, ?, ?)
    """,
    (user_id, user_data["name"], user_data["age"], user_data["gender"], user_data["about"], user_data["photo"],))

    db.commit()
    
    return print('данные добавлены в базу')


def get_user_data(user_id: int,):
    cur.execute("""SELECT * FROM users WHERE id = ?""", (user_id,))
    user_data = cur.fetchall()[0]
    print(user_data)
    result = {"имя": user_data[1], "возраст": user_data[2], "пол": user_data[3], "о себе": user_data[4], "photo": user_data[5]}
    return  result


def get_all_users():
    cur.execute("""
        SELECT * FROM users
    """)
    return cur.fetchall()

print(get_all_users())

def get_users_id_list():
    cur.execute("SELECT id FROM users")
    users_id = cur.fetchall()
    users_id = [users_id[i][0] for i in range(0,len(users_id)) ]
    return users_id

print(str(get_users_id_list()) + "<------------------------------------")
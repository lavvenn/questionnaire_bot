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
    (user_id, user_data["name"], user_data["age"], user_data["gender"], user_data["about"], user_data["photo"]))

    db.commit()
    
    return None


def get_user_data(user_id: int,) -> dict:
    cur.execute("""SELECT * FROM users WHERE id = ?""", (user_id,))
    user_data = cur.fetchall()[0]
    return  {"имя": user_data[1], "возраст": user_data[2], "пол": user_data[3], "о себе": user_data[4], "photo": user_data[5]}

def get_user_username(user_id: int):
    cur.execute("SELECT telegram_name FROM users WHERE id = ?", (user_id))


def get_all_users():
    cur.execute("""
        SELECT * FROM users
    """)
    return cur.fetchall()

print(get_all_users())

def get_users_id_list(without: int = 0):
    cur.execute("SELECT id FROM users")
    users_id = cur.fetchall()
    users_id = [users_id[i][0] for i in range(0,len(users_id)) ]
    if without == 0:
        return users_id
    else:
        users_id.remove(without)
        return users_id

print(f'в боте зарегистрированно : {len(get_users_id_list())} анкет')

print(str(get_users_id_list()) + "<------------------------------------")


def database_recovery(list):
    for i in list: 
        cur.execute("""REPLACE INTO users(id, name, age, gender, abowt, photo) VALUES (?, ?, ?, ?, ?, ?)
        """,(i[0], i[1], i[2], i[3], i[4], i[5]))
    db.commit()
    
    return "урааааааааа"



if __name__ == "__main__":

    data_baze = []

    database_recovery(data_baze)
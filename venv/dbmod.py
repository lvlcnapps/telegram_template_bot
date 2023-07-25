import sqlite3
from sqlite3 import Error


def restore_table():
    connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")
    print("1")
    create_users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT NOT NULL, mark INTEGER, description TEXT NOT NULL)"
    execute_query(connection, create_users_table)


def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return conn


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def add_line(id_n, name, mark, desc):
    connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")
    create_users = f'INSERT INTO users (id, name, mark, description) VALUES ({id_n}, "{name}", {mark}, "{desc}")'
    execute_query(connection, create_users)
    return


def update_line(id_n, name, mark):
    connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")
    create_users = f'UPDATE users SET mark={mark} WHERE id = {id_n} and name = "{name}"'
    execute_query(connection, create_users)
    return


def show_all():
    connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")
    print("1")
    select_users = "SELECT * from users"
    users = execute_read_query(connection, select_users)
    ans = ""
    i = 0
    for user in users:
        ans += f'{i}) {user[1]} - {user[3]} [{user[2]}]\n'
        i += 1
    return ans


def show_marked():
    connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")
    print("1")
    select_users = "SELECT * from users where mark = 1"
    users = execute_read_query(connection, select_users)
    ans = ""
    i = 0
    for user in users:
        ans += f'{i}) {user[1]} - {user[3]} [{user[2]}]\n'
        i += 1
    return ans


def delete_all():
    connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")
    print("1")
    del_all = "drop table users"
    execute_query(connection, del_all)
    return

def clear_all(id_n):
    connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")
    print("1")
    cl_all = f'DELETE FROM users WHERE id = {id_n}'
    execute_query(connection, cl_all)
    return

def clear_marked(id_n):
    connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")
    print("1")
    cl_mrkd = f'DELETE FROM users WHERE id = {id_n} and mark = 1'
    execute_query(connection, cl_mrkd)
    return

def clear_task(id_n, name):
    connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")
    print("1")
    cl_all = f'DELETE FROM users WHERE id = {id_n} and name = "{name}"'
    execute_query(connection, cl_all)
    return

# connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")

# execute_query(connection, create_users_table)
# execute_query(connection, create_posts_table)
# execute_query(connection, create_comments_table)
# execute_query(connection, create_likes_table)

# execute_query(connection, create_users)
# execute_query(connection, create_posts)
# execute_query(connection, create_comments)
# execute_query(connection, create_likes)

# select_users = "SELECT * from users"
# users = execute_read_query(connection, select_users)

# for user in users:
# print(user)

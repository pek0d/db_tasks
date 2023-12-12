import psycopg2


# Установка соединения с базой данных
def connect():
    conn = psycopg2.connect(
        dbname="netology_db",
        user="postgres",
        password="",
    )
    return conn


# Создание структуры базы данных
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS clients (
            id SERIAL PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            phone TEXT[]
        )
        """
    )
    conn.commit()
    conn.close()


# Добавление нового клиента
def add_client(first_name, last_name, email):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO clients (first_name, last_name, email) VALUES (%s, %s, %s)
        """,
        (first_name, last_name, email),
    )
    conn.commit()
    conn.close()


# Добавление телефона для существующего клиента
def add_phone(client_id, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE clients SET phone = array_append(phone, %s) WHERE id = %s
        """,
        (phone, client_id),
    )
    conn.commit()
    conn.close()


# Изменение данных о клиенте
def update_client(client_id, first_name, last_name, email, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE clients SET first_name = %s, last_name = %s, email = %s, phone = %s WHERE id = %s
        """,
        (first_name, last_name, email, phone, client_id),
    )
    conn.commit()
    conn.close()


# Удаление телефона для существующего клиента
def delete_phone(client_id, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """
        UPDATE clients SET phone = array_remove(phone, %s) WHERE id = %s
        """,
        (phone, client_id),
    )
    conn.commit()
    conn.close()


# Удаление существующего клиента
def delete_client(client_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """
        DELETE FROM clients WHERE id = %s
        """,
        (client_id,),
    )
    conn.commit()
    conn.close()


# Поиск клиента по данным
def find_client(data):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM clients WHERE first_name = %s OR last_name = %s OR email = %s OR %s = ANY(phone)
        """,
        (data, data, data, data),
    )
    result = cur.fetchall()
    conn.close()
    return result


# Получение информации о клиентах
def get_client_info():
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT id, first_name, last_name, email FROM clients
        """
    )
    result = cur.fetchall()
    conn.close()
    return result


# create_table()
# add_client("Xьюго", "Лоскин", "hugo@boss.com")
# add_client("Бен", "Кеноби", "jd@stars.com")
# add_phone(2, "+723456732323")
# update_client(2, "Леон", "Тучков", "ivan@mail.com", ["+723456801"])
# delete_phone(2, "+723456801")
# delete_client(2)
print(get_client_info())  # get_client_id()
# print(find_client("ivan@mail.com"))

from psycopg2 import Error
from ps_connection import create_connection
from faker import Faker
from random import choice


def perform_sql(conn, sql, params):
    cur = conn.cursor()
    try:
        cur.execute(sql, params)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


def create_user(conn, status):
    sql = """
    INSERT INTO users(fullname, email) VALUES(%s,%s);
    """
    perform_sql(conn, sql, status)


def create_status(conn, status):
    sql = """
    INSERT INTO status(name) VALUES(%s);
    """
    perform_sql(conn, sql, status)


def create_task(conn, task):
    sql = """
    INSERT INTO tasks(title,description,status_id,user_id) VALUES(%s,%s,%s,%s);
    """
    perform_sql(conn, sql, task)


def fill_in_db_with_random_data():
    fake = Faker()
    with create_connection() as conn:
        # Додаємо статуси
        statuses = ["new", "in progress", "completed"]
        for status in statuses:
            create_status(conn, (status,))

        # Додаємо 5 випадкових користувачів
        for _ in range(5):
            fullname = fake.name()
            email = fake.unique.email()
            create_user(conn, (fullname, email))

        # Отримуємо id статусів та користувачів для зв'язків
        cur = conn.cursor()
        cur.execute("SELECT id FROM status;")
        status_ids = [row[0] for row in cur.fetchall()]

        cur.execute("SELECT id FROM users;")
        user_ids = [row[0] for row in cur.fetchall()]
        cur.close()

        # Додаємо 10 випадкових задач
        for _ in range(10):
            title = fake.sentence(nb_words=5)
            description = fake.text(max_nb_chars=100)
            status_id = choice(status_ids)
            user_id = choice(user_ids)
            create_task(conn, (title, description, status_id, user_id))


if __name__ == "__main__":
    fill_in_db_with_random_data()

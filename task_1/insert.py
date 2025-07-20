from psycopg2 import Error
from ps_connection import create_connection

def insert_task_for_user(conn, task):
    sql = """
    INSERT INTO tasks(title, description, status_id, user_id)
    VALUES (%s, %s, %s, %s);
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, task)
        conn.commit()
        print("Task inserted successfully.")
    except Error as e:
        print(e)
    finally:
        cur.close()

def perform_insert_queries():
    with create_connection() as conn:
        # Наприклад, додаємо завдання користувачу з user_id=1, статусом status_id=2
        task = (
            "Вивчити PostgreSQL",
            "Пройти GoIT заняття по PostgreSQL та виконати завдання.",
            2,  # статус, наприклад 'in progress'
            1   # user_id
        )
        insert_task_for_user(conn, task)

if __name__ == "__main__":
    perform_insert_queries()

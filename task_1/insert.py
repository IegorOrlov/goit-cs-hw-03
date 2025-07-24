from psycopg2 import Error
from ps_connection import create_connection


def insert_task_for_user(conn, title, description, status_id, user_id):
    sql = """
    INSERT INTO tasks(title, description, status_id, user_id)
    VALUES (%s, %s, %s, %s);
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, (title, description, status_id, user_id))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


def perform_insert_queries():
    with create_connection() as conn:
        insert_task_for_user(
            conn,
            "Learn SQL Joins",
            "Practice writing advanced SQL join queries.",
            1,  # status_id, e.g., 'new'
            1,  # user_id
        )


if __name__ == "__main__":
    perform_insert_queries()

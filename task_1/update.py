from psycopg2 import Error
from ps_connection import create_connection


def update_task_status(conn, status_id, task_id):
    sql = """
    UPDATE tasks
    SET status_id = %s
    WHERE id = %s;
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, (status_id, task_id))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


def update_user_name(conn, user_id, new_name):
    sql = """
    UPDATE users
    SET fullname = %s
    WHERE id = %s;
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, (new_name, user_id))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()


def perform_update_queries():
    with create_connection() as conn:
        update_task_status(conn, 2, 1)  # Set task id=1 status to 'in progress'
        update_user_name(conn, 1, "New User Name")


if __name__ == "__main__":
    perform_update_queries()

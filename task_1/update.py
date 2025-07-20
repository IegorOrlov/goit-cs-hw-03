from psycopg2 import Error
from ps_connection import create_connection

def update_task(conn, parameters):
    sql = """
    UPDATE tasks
    SET title = %s, description = %s
    WHERE id = %s;
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, parameters)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

def update_task_status(conn, parameters):
    sql = """
    UPDATE tasks
    SET status_id = %s
    WHERE id = %s;
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, parameters)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

def perform_update_queries():
    with create_connection() as conn:
        update_task(conn, ("Updated Title", "Updated Description", 1))
        update_task_status(conn, (2, 1))  # статус_id = 2, task_id = 1

if __name__ == "__main__":
    perform_update_queries()
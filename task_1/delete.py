from psycopg2 import Error
from ps_connection import create_connection

def delete_task(conn, task_id):
    sql = "DELETE FROM tasks WHERE id = %s;"
    cur = conn.cursor()
    try:
        cur.execute(sql, (task_id,))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

def perform_delete_queries():
    with create_connection() as conn:
        delete_task(conn, 2)

if __name__ == "__main__":
     perform_delete_queries()
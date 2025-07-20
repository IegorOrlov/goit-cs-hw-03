from psycopg2 import Error
from ps_connection import create_connection

def select_all_users(conn):
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_all_tasks(conn):
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks;")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def select_tasks_by_status(conn, status_name):
    rows = None
    cur = conn.cursor()
    try:
        cur.execute("""
            SELECT t.* FROM tasks t
            JOIN status s ON t.status_id = s.id
            WHERE s.name = %s;
        """, (status_name,))
        rows = cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()
    return rows

def perform_select_queries():
    with create_connection() as conn:
        print("Users:")
        print(select_all_users(conn))
        print("\nAll Tasks:")
        print(select_all_tasks(conn))
        print("\nTasks with status 'new':")
        print(select_tasks_by_status(conn, 'new'))

if __name__ == "__main__":
    perform_select_queries()


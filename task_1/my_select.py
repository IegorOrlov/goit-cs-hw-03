from psycopg2 import Error
from ps_connection import create_connection
from pprint import pprint


def get_tasks_by_user(conn, user_id):
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM tasks WHERE user_id = %s;", (user_id,))
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()


def get_tasks_by_status(conn, status_name):
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT * FROM tasks
            WHERE status_id = (
                SELECT id FROM status WHERE name = %s
            );
        """,
            (status_name,),
        )
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()


def get_users_without_tasks(conn):
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT * FROM users
            WHERE id NOT IN (
                SELECT DISTINCT user_id FROM tasks WHERE user_id IS NOT NULL
            );
        """
        )
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()


def get_uncompleted_tasks(conn):
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT * FROM tasks
            WHERE status_id != (
                SELECT id FROM status WHERE name = 'completed'
            );
        """
        )
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()


def find_users_by_email_pattern(conn, pattern):
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT * FROM users
            WHERE email LIKE %s;
        """,
            (pattern,),
        )
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()


def get_task_count_by_status(conn):
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT s.name, COUNT(t.id) 
            FROM status s
            LEFT JOIN tasks t ON s.id = t.status_id
            GROUP BY s.name;
        """
        )
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()


def get_tasks_by_user_email_domain(conn, domain_pattern):
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT t.* FROM tasks t
            JOIN users u ON t.user_id = u.id
            WHERE u.email LIKE %s;
        """,
            (domain_pattern,),
        )
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()


def get_tasks_without_description(conn):
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT * FROM tasks WHERE description IS NULL OR description = '';
        """
        )
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()


def get_users_and_their_inprogress_tasks(conn):
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT u.fullname, t.title, t.description FROM users u
            INNER JOIN tasks t ON u.id = t.user_id
            INNER JOIN status s ON t.status_id = s.id
            WHERE s.name = 'in progress';
        """
        )
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()


def get_users_with_task_count(conn):
    cur = conn.cursor()
    try:
        cur.execute(
            """
            SELECT u.fullname, COUNT(t.id) FROM users u
            LEFT JOIN tasks t ON u.id = t.user_id
            GROUP BY u.fullname;
        """
        )
        return cur.fetchall()
    except Error as e:
        print(e)
    finally:
        cur.close()


def perform_select_queries():
    with create_connection() as conn:
        print("Tasks by user_id=1:")
        pprint(get_tasks_by_user(conn, 1))
        print("\nTasks with status 'new':")
        pprint(get_tasks_by_status(conn, "new"))
        print("\nUsers without tasks:")
        pprint(get_users_without_tasks(conn))
        print("\nUncompleted tasks:")
        pprint(get_uncompleted_tasks(conn))
        print("\nUsers with email LIKE '%@example.com':")
        pprint(find_users_by_email_pattern(conn, "%@example.com"))
        print("\nTask count by status:")
        pprint(get_task_count_by_status(conn))
        print("\nTasks assigned to users with '%@example.com' emails:")
        pprint(get_tasks_by_user_email_domain(conn, "%@example.com"))
        print("\nTasks without description:")
        pprint(get_tasks_without_description(conn))
        print("\nUsers and their 'in progress' tasks:")
        pprint(get_users_and_their_inprogress_tasks(conn))
        print("\nUsers with task count:")
        pprint(get_users_with_task_count(conn))


if __name__ == "__main__":
    perform_select_queries()

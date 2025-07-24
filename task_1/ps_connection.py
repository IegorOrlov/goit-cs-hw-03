import psycopg2
from contextlib import contextmanager
from config import DATABASE_CONFIG


@contextmanager
def create_connection(db_config=DATABASE_CONFIG):
    """Create a database connection to a PostgreSQL database"""
    conn = psycopg2.connect(**db_config)
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Transaction rolled back due to: {e}")
        raise
    finally:
        conn.close()


# Використання:
if __name__ == "__main__":
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            print(cur.fetchone())

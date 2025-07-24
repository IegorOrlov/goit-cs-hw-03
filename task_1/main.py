from create_table import create_tables
from seed import fill_in_db_with_random_data
from my_select import perform_select_queries
from insert import perform_insert_queries
from update import perform_update_queries
from delete import perform_delete_queries

if __name__ == "__main__":
    create_tables()
    fill_in_db_with_random_data()
    perform_select_queries()
    perform_insert_queries()
    perform_update_queries()
    perform_delete_queries()

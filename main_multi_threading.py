import threading
import time
from time import sleep
from databasestructure import *

def database_operation(database, operation, table_name, data=None, key=None):
    """
    This function do not include select_by_column_value and join
    """
    if operation == 'insert':
        database.insert(table_name, data)
    elif operation == 'delete':
        database.delete(table_name, key)
    elif operation == 'select':
        headers, result = database.select(table_name, key)
        print(f"Selected: {result}")
    elif operation == 'select_all':
        headers, result = database.select_all(table_name)
        print(f"Selected All: {result}")
    elif operation == 'update':
        database.update(table_name, key, data)
    else:
        print("Unknown operation")

if __name__ == '__main__':
    db = CustomDatabase()
    db.create_table('test_table', ['id', 'name'])

    # List of operations to realize
    operations = [
    ('insert', 'test_table', [None, 'Alice']),
    ('insert', 'test_table', [None, 'Bob']),
    ('insert', 'test_table', [None, 'Charlie']),
    ('select_all', 'test_table'),
    ('delete', 'test_table', None, 1),
    ('select_all', 'test_table')
    ]

    # Create a start process by threads
    """
    Thinking to add a LOCK mechanism to be sure of coherence of data. Right now,
    i'm creating threads based on the type of the operation and adding the necessary
    arguments depending the case 
    """
    threads = []
    start_time = time.time()
    for op in operations:
        if op[0] == 'insert' or op[0] == 'update':
            t = threading.Thread(target=database_operation, args=(db, op[0], op[1], op[2]))
        elif op[0] == 'delete' or op[0] == 'select':
            t = threading.Thread(target=database_operation, args=(db, op[0], op[1], None, op[3]))
        else:
            t = threading.Thread(target=database_operation, args=(db, op[0], op[1]))
        threads.append(t)
        t.start()

    # Wait until all threads ends
    for t in threads:
        t.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total execution time: {total_time} seconds\n")
    print("All operations completed.")
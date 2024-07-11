import pickle
import time
from databasestructure import *


if __name__ == '__main__':
    # Example usage
    # Create a new database
    try:
        db = CustomDatabase()
        start_time = time.time()
        # Create a table with the 'id' as the key_index start=0
        db.create_table('users', ['id', 'name', 'age'], key_index=0)
        print("table created")

        # Insert data
        db.insert('users', [None, 'Alice', 30])
        db.insert('users', [None, 'Bob', 25])

        # Select data
        print("Select user with id 0:", db.select('users', 0))
        print("Select user with id 1:", db.select('users', 1))

        # Update data
        db.update('users', 0, [0, 'Alice', 31])
        print("After update user with id 0:", db.select('users', 0))

        # Delete data
        db.delete('users', 1)
        print("After delete user with id 1:", db.select_all('users'))

        # Add a new column
        db.add_column('users', 'email')
        print("After adding column 'email':", db.select('users', 0))

        # Save the database in binary format
        db.save('./avl_database.pkl')

        # Load the database from binary format
        loaded_db = CustomDatabase.load('./avl_database.pkl')
        print("Loaded database user with id 0:", loaded_db.select('users', 0))

        # Transaction example
        try:
            db.insert('users', [None, 'Charlie', 28])
            print("Before rollback user with latest id:", db.select_all('users'))
            db.rollback('users')
            print("After rollback user with latest:", db.select_all('users'))
        except Exception as rollback_error:
            print("rollback error: ",str(rollback_error))

        try:
            db.insert('users', [None, 'Charlie', 28])
            db.commit('users')
            print("After commit user with latest id:", db.select_all('users'))
        except Exception as commit_error:
            print("commit error: ",str(commit_error))
    
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Total execution time: {total_time} seconds\n")
    except Exception as error:
        print(str(error))
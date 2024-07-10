import pickle
from databasestructure import *


if __name__ == '__main__':
    # Example usage
    # Create a new database
    try:
        db = CustomDatabase()

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
        print("After delete user with id 1:", db.select('users', 1))

        # Add a new column
        db.add_column('users', 'email')
        print("After adding column 'email':", db.select('users', 0))

        # Save the database in binary format
        db.save('./avl_database.pkl')

        # Load the database from binary format
        loaded_db = CustomDatabase.load('./avl_database.pkl')
        print("Loaded database user with id 0:", loaded_db.select('users', 0))

        # Transaction example
        db.insert('users', [None, 'Charlie', 28])
        print("Before rollback user with id 2:", db.select('users', 2))
        db.rollback('users')
        print("After rollback user with id 2:", db.select('users', 2))

        db.insert('users', [None, 'Charlie', 28])
        db.commit('users')
        print("After commit user with id 2:", db.select('users', 2))
    
    except Exception as error:
        print(str(error))
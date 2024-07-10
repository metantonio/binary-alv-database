import pickle
from databasestructure import *


if __name__ == 'main':
    # Example usage
    # Create a new database
    db = CustomDatabase()

    # Create a table with the 'id' as the key
    db.create_table('users', key_index=0)

    # Insert data
    db.insert('users', [1, 'Alice', 30])
    db.insert('users', [2, 'Bob', 25])

    # Select data
    print("Select user with id 1:", db.select('users', 1))
    print("Select user with id 2:", db.select('users', 2))

    # Update data
    db.update('users', 1, [1, 'Alice', 31])
    print("After update user with id 1:", db.select('users', 1))

    # Delete data
    db.delete('users', 2)
    print("After delete user with id 2:", db.select('users', 2))

    # Save the database in binary format
    db.save('custom_avl_database.pkl')

    # Load the database from binary format
    loaded_db = CustomDatabase.load('custom_avl_database.pkl')
    print("Loaded database user with id 1:", loaded_db.select('users', 1))

    # Transaction example
    db.insert('users', [3, 'Charlie', 28])
    print("Before rollback user with id 3:", db.select('users', 3))
    db.rollback('users')
    print("After rollback user with id 3:", db.select('users', 3))

    db.insert('users', [3, 'Charlie', 28])
    db.commit('users')
    print("After commit user with id 3:", db.select('users', 3))
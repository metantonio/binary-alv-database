import pickle
from databasestructure import *

if __name__ == '__main__': 

    # Load the database from binary format
    loaded_db = CustomDatabase.load('./avl_database.pkl')
    row_header, user_row = loaded_db.select('users', 0)
    print("\nPrint user with id 0:\n", row_header, '\n', user_row)

    # Insert new data
    loaded_db.insert('users', [None, 'Antonio', 35])
    loaded_db.commit('users')
    print("\nInserted new user in users")

    # Select by value
    header, user = loaded_db.select_by_column_value("users", "age", '>', 25)
    print("\nSelect user row:\n", header,'\n', user)

    # Select all data
    headers, table = loaded_db.select_all('users')
    print("\nSelect all users table:\n", headers, '\n', table)

    # AFTER COMMITS ARE MADE, WRITE TO THE DATABASE
    loaded_db.save('./avl_database.pkl')
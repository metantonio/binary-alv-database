import pickle
from databasestructure import *

if __name__ == '__main__': 

    # Load the database from binary format
    loaded_db = CustomDatabase.load('./avl_database.pkl')
    print("\nLoaded database user with id 0:", loaded_db.select('users', 0))

    # Insert new data
    #loaded_db.insert('users', [None, 'Antonio', 35])
    #loaded_db.commit('users')
    #print("Inserted new user in users")

    # Select all data
    print("\nSelect all users table:", loaded_db.select_all('users'))

    # AFTER COMMITS ARE MADE, WRITE TO THE DATABASE
    loaded_db.save('./avl_database.pkl')
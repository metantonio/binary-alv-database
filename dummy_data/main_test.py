import pickle
import time
from ..databasestructure import *


if __name__ == '__main__':
    try:
        db = CustomDatabase()
        start_time = time.time()
        # Create a table with the 'id' as the key_index start=0
        db.create_table('users', ['id', 'name', 'age'], key_index=0)
        print("table created")

        db.load_from_csv("users", "./dummy_users.csv")

    except Exception as error:
        print(str(error))
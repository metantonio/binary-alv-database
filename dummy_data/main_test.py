import pickle
import time
from ..databasestructure import *


if __name__ == '__main__':
    try:
        db = CustomDatabase()
        
        # Create a tables 
        start_time = time.time()
        db.create_table('users', ['id', 'name', 'age'], key_index=0)
        db.create_table('orders', ['order_id', 'user_id', 'product'], key_index=0)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Tables creation, Total execution time: {total_time} seconds\n")

        # Load data from CSV files
        start_time = time.time()
        db.load_from_csv("users", "./dummy_users.csv")
        db.commit('users')
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Loaded 10,000 users rows to memory, Total execution time: {total_time} seconds\n")

        start_time = time.time()
        db.load_from_csv("orders", "./dummy_orders.csv")
        db.commit('orders')
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Loaded 20,000 orders rows to memory, Total execution time: {total_time} seconds\n")

        # I/O Write binary database to disk
        start_time = time.time()
        db.save('./dummy_database.pkl')
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Loaded 20,000 orders rows to memory, Total execution time: {total_time} seconds\n")

    except Exception as error:
        print(str(error))
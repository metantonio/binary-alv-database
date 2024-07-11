import pickle
from databasestructure import *


if __name__ == '__main__':

    try:
    
        db_test = CustomDatabase()
        # Create tables
        db_test.create_table('users', ['id', 'name', 'age'], key_index=0)
        db_test.create_table('orders', ['order_id', 'user_id', 'product'], key_index=1)

        # Insert data into tables
        db_test.insert('users', [None, 'Charlie', 28])
        db_test.insert('users', [None, 'Alice', 30])
        db_test.insert('orders', [101, 0, 'Laptop'])
        db_test.insert('orders', [102, 1, 'Smartphone'])

        # Commit transactions
        db_test.commit('users')
        db_test.commit('orders')

        # Perform the join
        headers, joined_data = db_test.join('users', 'orders', key_index1=0, key_index2=1)

        # Display the joined data
        #print("Joined Data:\n", joined_data)
        print("Joined Data:\n")
        print(headers)
        for data in joined_data:
            print(data)

        # Save the database in binary format
        db_test.save('./test_database.pkl')

    except Exception as err:
        print("Error: ", str(err))
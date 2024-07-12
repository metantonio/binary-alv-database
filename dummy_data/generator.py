import csv
import random

# Users dummy data variables
path_csv = "./dummy_data/"
file_name='dummy_users.csv'
file_path = path_csv + file_name
num_users = 10000
min_age = 18
max_age = 60

# Orders dummy data variable
path_csv2 = "./dummy_data/"
file_name2='dummy_orders.csv'
file_path2 = path_csv2 + file_name2
products = ["apple", "laptop", "smartphone", "watch", "tv", "pear"]

# Open csv file for users
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Headers row
    writer.writerow(['id', 'name', 'age'])
    
    # Generate and write data
    for user_id in range(1, num_users + 1):
        name = "Name " + str(user_id)
        age = int(random.randint(min_age, max_age))  # Generar a random age
        writer.writerow([int(user_id), name, age])

print("File 1 generated")

# Open csv file for orders
with open(file_path2, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Headers row
    writer.writerow(['order_id', 'user_id', 'product'])
    
    # Generate and write data
    for order_id in range(1, num_users*2 + 1):
        product = random.choice(products)
        user_id = int(random.randint(1, num_users))  # Generate a random user_id
        writer.writerow([int(order_id), user_id, product])

print("File 2 generated")
import csv
import random

path_csv = "./dummy_data/"
file_name='dummy_users.csv'
file_path = path_csv + file_name
num_users = 10000
min_age = 18
max_age = 60

# Abrir el archivo CSV para escribir
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Escribir la fila de encabezado
    writer.writerow(['id', 'name', 'age'])
    
    # Generar y escribir los datos de los usuarios
    for user_id in range(1, num_users + 1):
        name = "Name " + str(user_id)
        age = random.randint(min_age, max_age)  # Generar una edad aleatoria entre 18 y 90
        writer.writerow([user_id, name, age])

print("File generated")
# Binary database using AVL tree data structure (Balanced-Binary Tree)

An implementation of the AVL tree to store data. I'm also include basic transaction handling with commit and rollback methods using in-memory snapshots and saving it to a .pkl (binary file)

# How to Use

## Create a database object

```python
db = CustomDatabase()
```

## Create a table

Example about how to create a table named users, with columns `id`, `name` and `age`:

```python
db.create_table('users', ['id', 'name', 'age'], key_index=0)
```

Note: ``key_index`` is wich column index has the `id` column, in this case `id` is on the first column, that's why **key_index=0**.

## Insert data to table

```python
db.insert('users', [None, 'Alice', 30])
db.commit('users')
```

Note: That for `id` field that is the index, you use None to use the automatic autoincrement

## Select (search) Data

### Select data based on the index

This will look on the `id` column.

```python
# Select the user with id=0
user = db.select('users', 0)
print(user)
```

### Select data based on a value of a column

```python
# Select the user with age > 25
user = db.select_by_column_value("users", "age", '>', 25)
print(user)
```

Valid operators:

- `>`
- `>=`
- `<`
- `<=`
- `==`
- `!=`

### Select data whole table

```python
# Select table
table = db.select_all('users')
print(table)
```

## Update Data

### Update a row

```python
# You need the index of the row to be updated
user = db.update('users', 0, [0, 'Alice', 31])
print(user)
```

### Update a Table

```python
# Add the column email to users table
db.add_column('users', 'email')
print(db.select_all('users'))
```

## Delete Data

```python
# You need the index of the row to be deleted
db.delete('users', 1)
```

## Joining Operation

Let's say that we have these tables: 

- Table `users`:

id | name | age
:--- | :---: | :---:
| 0  | Charlie|  28 |
| 1  | Alice  |  30 |

- Table `orders`:

| order_id | user_id |  product  
:--- | :---: | :---:
|   101    |    0    |  Laptop   |
|   102    |    1    | Smartphone|


If we want to join tables, we must do it based on the `key_index` value.

 - ``key_index1 = 0``: This means that the join key for the first table (``users``) is in the first column (``id``).
 - ``key_index2 = 1``: This means that the join key for the second table (``orders``) is in the second column (``user_id``).


So, to join table `users` and table `orders` by `user_id` column:

```python
# Perform the join
headers, joined_data = db.join('users', 'orders', key_index1=0, key_index2=1)

# Print the joined data
print("Joined Data:\n")
print(headers)
for data in joined_data:
    print(data)
```

Note: Check `test_joining.py` file

## Transactions

### Rollback

```python
db.insert('users', [None, 'Charlie', 28])
print("Before rollback user with latest id:", db.select_all('users'))
db.rollback('users')
print("After rollback user with latest:", db.select_all('users'))
```

### Commit

```python
db.insert('users', [None, 'Charlie', 28])
db.commit('users')
print("After commit user with latest id:", db.select_all('users'))
```

## Save data to a .pkl file

```python
# Save the database in binary format
db.save('./avl_database.pkl')
```

## Load data from a .pkl file

```python
# Load the database in binary format
db = CustomDatabase.load('./avl_database.pkl')
```

## Load data from a .csv file

You must have a .csv with the same structure that the table you want to upload. Let's say table `users`, you will need a .csv file with a structure like the example:

id | name | age
:--- | :---: | :---:
1 | John | 25
2 | Jane | 30
3 | Bob | 22

```python
db.load_from_csv("users", "./data.csv")
```
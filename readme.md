# Binary database using AVL tree data structure (Balanced-Binary Tree)

An implementation of the AVL tree to store data. I'm also include basic transaction handling with commit and rollback methods using in-memory snapshots and saving it to a .pkl (binary file)

## How to Use

### Create a database object

```python
db = CustomDatabase()
```

### Create a table

Example about how to create a table named users, with columns `id`, `name` and `age`:

```python
db.create_table('users', ['id', 'name', 'age'], key_index=0)
```

Note: Index will start on 0 and autoincrement is automatic by default

### Insert data to table

```python
db.insert('users', [None, 'Alice', 30])
db.commit('users')
```

Note: That for `id` field that is the index, you use None to use the automatic autoincrement

### Select (seach) Data

#### Select data based on the index

```python
# Select the user with id=0
user=db.select('users', 0)
print(user)
```
#### Select data whole table

```python
# Select table
table=db.select_all('users')
print(table)
```

### Update Data

#### Update a row

```python
# You need the index of the row to be updated
user = db.update('users', 0, [0, 'Alice', 31])
print(user)
```

#### Update a Table

```python
# Add the column email to users table
db.add_column('users', 'email')
print(db.select_all('users'))
```

### Delete Data

```python
# You need the index of the row to be deleted
db.delete('users', 1)
```

### Transactions

#### Rollback

```python
db.insert('users', [None, 'Charlie', 28])
print("Before rollback user with id 2:", db.select('users', 2))
db.rollback('users')
print("After rollback user with id 2:", db.select('users', 2))
```

#### Commit

```python
db.insert('users', [None, 'Charlie', 28])
db.commit('users')
print("After commit user with id 2:", db.select('users', 2))
```

### Save data to a .pkl file

```python
# Save the database in binary format
db.save('./avl_database.pkl')
```

### Load data from a .pkl file

```python
# Save the database in binary format
db = CustomDatabase.load('./avl_database.pkl')
```
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


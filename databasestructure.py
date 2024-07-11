import pickle
import csv

class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def insert(self, root, key, value):
        if not root:
            return AVLNode(key, value)
        elif key < root.key:
            root.left = self.insert(root.left, key, value)
        else:
            root.right = self.insert(root.right, key, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.value = temp.value
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    
    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root)
            res = res + self.inorder_traversal(root.right)
        return res


class TransactionalAVLTree:
    def __init__(self):
        self.tree = AVLTree()
        self.root = None
        self.transactions = []

    def insert(self, key, value):
        self.root = self.tree.insert(self.root, key, value)
        self.transactions.append(('insert', key, value))

    def delete(self, key):
        self.root = self.tree.delete(self.root, key)
        self.transactions.append(('delete', key))

    def search(self, key):
        return self.tree.search(self.root, key)
    
    def select_all(self):
        return self.tree.inorder_traversal(self.root)

    def commit(self):
        self.transactions = []

    def rollback(self):
        while self.transactions:
            action = self.transactions.pop()
            if action[0] == 'insert':
                self.root = self.tree.delete(self.root, action[1])
            elif action[0] == 'delete':
                self.root = self.tree.insert(self.root, action[1], action[2])


class CustomDatabase:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, columns, key_index=0):
        print("creating table...", table_name)
        if table_name in self.tables:
            raise ValueError("Table already exists.")
        self.tables[table_name] = {
            "tree": TransactionalAVLTree(),
            "columns": columns,
            "key_index": key_index,
            "auto_increment": 0
        }

    def insert(self, table_name, data):
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")
        table = self.tables[table_name]
        if table["key_index"] is not None and data[table["key_index"]] is None:
            data[table["key_index"]] = table["auto_increment"]
            table["auto_increment"] += 1
        key = data[table["key_index"]]
        table["tree"].insert(key, data)

    def select(self, table_name, key):
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")
        node = self.tables[table_name]["tree"].search(key)
        return node.value if node else None
    
    def select_all(self, table_name):
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")
        nodes = self.tables[table_name]["tree"].select_all()
        #print("nodes:",nodes) # should print memory address
        for node in nodes:
            if not hasattr(node, 'value'):
                raise AttributeError(f"Node {node} does not have a 'value' attribute")
        return [node.value for node in nodes]

    def update(self, table_name, key, data):
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")
        self.tables[table_name]["tree"].delete(key)
        self.tables[table_name]["tree"].insert(key, data)

    def delete(self, table_name, key):
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")
        self.tables[table_name]["tree"].delete(key)

    def commit(self, table_name):
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")
        self.tables[table_name]["tree"].commit()

    def rollback(self, table_name):
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")
        self.tables[table_name]["tree"].rollback()

    def save(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(file_name):
        with open(file_name, 'rb') as file:
            return pickle.load(file)

    def add_column(self, table_name, column_name):
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")
        table = self.tables[table_name]
        if column_name in table["columns"]:
            raise ValueError("Column already exists.")
        table["columns"].append(column_name)
        for node in self._inorder_traversal(table["tree"].root):
            node.value.append(None)

    def _inorder_traversal(self, root):
        if root is None:
            return []
        return self._inorder_traversal(root.left) + [root] + self._inorder_traversal(root.right)

    def load_from_csv(self, table_name, file_name):
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")
        
        table = self.tables[table_name]
        
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Leer encabezados
            for row in reader:
                if table["key_index"] is not None and row[table["key_index"]] == '':
                    row[table["key_index"]] = None
                self.insert(table_name, row)
    
    def select_by_column_value(self, table_name, column_name, operator, value):
        if table_name not in self.tables:
            raise ValueError("Table does not exist.")
        
        table = self.tables[table_name]
        
        if column_name not in table["columns"]:
            raise ValueError(f"Column '{column_name}' does not exist in table '{table_name}'.")
        
        column_index = table["columns"].index(column_name)
        
        result = []
        for node in self._inorder_traversal(table["tree"].root):
            column_value = node.value[column_index]
            if self._compare(column_value, operator, value):
                result.append(node.value)
        
        return result

    def _compare(self, column_value, operator, value):
        if operator == '==':
            return column_value == value
        elif operator == '!=':
            return column_value != value
        elif operator == '<':
            return column_value < value
        elif operator == '<=':
            return column_value <= value
        elif operator == '>':
            return column_value > value
        elif operator == '>=':
            return column_value >= value
        else:
            raise ValueError(f"Invalid operator '{operator}'. Valid operators are ==, !=, <, <=, >, >=.")


    def join(self, table1_name, table2_name, key_index1=0, key_index2=0):
        if table1_name not in self.tables or table2_name not in self.tables:
            raise ValueError("One or both tables do not exist.")

        table1 = self.tables[table1_name]
        table2 = self.tables[table2_name]

        table1_data = self.select_all(table1_name)
        table2_data = self.select_all(table2_name)

        joined_data = []

        table2_dict = {row[key_index2]: row for row in table2_data}

        headers = table1["columns"] + table2["columns"]

        for row1 in table1_data:
            key = row1[key_index1]
            if key in table2_dict:
                row2 = table2_dict[key]
                joined_data.append(row1 + row2)

        return headers, joined_data
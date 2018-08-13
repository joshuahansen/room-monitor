from sqlite_connection import SqliteConnection


db = SqliteConnection()

# db.delete_table_content()

data = db.get_data()
for row in data:
    print(row)

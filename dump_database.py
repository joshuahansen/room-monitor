from sqlite_connection import SqliteConnection


db = SqliteConnection()

# db.delete_table_content()
#db.drop_bluetooth()
#db.create_bluetooth_table()

data = db.get_data()
for row in data:
    print(row)

blue = db.get_bluetooth()
for row in blue:
    print(row)

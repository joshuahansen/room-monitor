from sqlite_connection import SqliteConnection


db = SqliteConnection()

data = db.get_data()

for row in data:
    print(row)

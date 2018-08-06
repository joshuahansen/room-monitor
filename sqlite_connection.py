import sqlite3
from datetime import datetime


class SqliteConnection:

    def __init__(self):
        self.conn = sqlite3.connect('sense_hat_readings.db')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute('''CREATE TABLE sense_readings
                (timestamp text, temperature real, humidity real)''')

    def save_data(self, time, temp, humi):
        self.cur.execute(''' INSERT INTO sense_readings
                VALUES(?, ?, ?)''', (time, temp, humi))

    def get_data(self):
        return self.cur.execute('SELECT * FROM sense_readings')


db = SqliteConnection()
try:
    db.create_table()
except sqlite3.OperationalError:
    print('Table already created')

db.save_data(datetime.now(), 27.1, 34)

data = db.get_data()

for row in data:
    print(row)

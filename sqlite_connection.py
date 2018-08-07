import sqlite3
import logging


# Database class for handling all interactions with the SQLite database
class SqliteConnection:

    # Constructor gets connection and creates a cursor,
    # Create a logger for error reporting
    def __init__(self):
        self.logger = logging.getLogger('sqlite_logger')
        self.logger.setLevel(logging.ERROR)

        # Create file handler and set formatter for logging
        fh = logging.FileHandler('/home/pi/room-monitor/sqlite_error.log')
        fh.setLevel(logging.ERROR)
        formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s'
        )
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)
        try:
            self.conn = sqlite3.connect('/home/pi/room-monitor/sense_hat_readings.db')
            self.cur = self.conn.cursor()
        except sqlite3.Error as err:
            self.logger.error(err)

    # Initially used to create the table for the sense hat readings
    def create_table(self):
        try:
            self.cur.execute('''CREATE TABLE sense_readings
                   (timestamp text, temperature real, humidity real)''')
            self.conn.commit()
        except sqlite3.Error as err:
            self.logger.error(err)

    # Save the data into the database
    def save_data(self, time, temp, humi):
        try:
            self.cur.execute(''' INSERT INTO sense_readings
                    VALUES(?, ?, ?)''', (time, temp, humi))
            self.conn.commit()
        except sqlite3.Error as err:
            self.logger.error(err)

    # Retrieve all the data from the database
    def get_data(self):
        try:
            return self.cur.execute('SELECT * FROM sense_readings')
        except sqlite3.Error as err:
            self.logger.error(err)

    # Delete all the data from the database. Remove for final release
    def delete_table_content(self):
        try:
            self.cur.execute('DELETE FROM sense_readings')
            self.conn.commit()
        except sqlite3.Error as err:
            self.logger.error(err)

    # close the connection with the database
    def close(self):
        try:
            self.conn.close()
        except sqlite3.Error as err:
            self.logger.error(err)

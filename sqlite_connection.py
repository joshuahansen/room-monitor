"""
Author: Joshua Hansen
Student Number: s3589185
Email: s3589185@student.rmit.edu.au

Programming Interrnet of Things COSC2674
Semester 2, 2018
Assignment 1

This module is used for connecting to the sqlite database on the raspberry pi.
It haddles all sql queries to keep the database seperate from the
main application.
"""
import sqlite3
import logging
from os import path


class SqliteConnection:
    """Database class for handling all interactions with the SQLite database"""

    def __init__(self):
        """
        Constructor gets connection and creates a cursor.
        Create a logger for error reporting
        """
        self.logger = logging.getLogger('sqlite_logger')
        self.logger.setLevel(logging.ERROR)

        # get Root path
        root = path.dirname(path.realpath(__file__))

        # Create file handler and set formatter for logging
        file_handle = logging.FileHandler(path.join(root, "sqlite_error.log"))
        file_handle.setLevel(logging.ERROR)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        file_handle.setFormatter(formatter)

        self.logger.addHandler(file_handle)
        try:
            self.conn = sqlite3.connect(
                path.join(root, "sense_hat_readings.db")
            )
            self.cur = self.conn.cursor()
        except sqlite3.Error as err:
            self.logger.error(err)

    def create_table(self):
        """Initially used to create the table for the sense hat readings"""
        try:
            self.cur.execute('''CREATE TABLE sense_readings
                   (timestamp text, temperature real, humidity real)''')
            self.conn.commit()
        except sqlite3.Error as err:
            self.logger.error(err)

    def create_bluetooth_table(self):
        """Used to create a table for storing bluetooth devices"""
        try:
            self.cur.execute('''CREATE TABLE bluetooth_device
                (name text, device text)''')
            self.conn.commit()
        except sqlite3.Error as err:
            self.logger.error(err)

    def save_data(self, time, temp, humi):
        """Save the data into the database"""
        try:
            self.cur.execute(''' INSERT INTO sense_readings
                    VALUES(?, ?, ?)''', (time, temp, humi))
            self.conn.commit()
        except sqlite3.Error as err:
            self.logger.error(err)

    def get_data(self):
        """Retrieve all the data from the database"""
        try:
            return self.cur.execute('SELECT * FROM sense_readings')
        except sqlite3.Error as err:
            self.logger.error(err)

    def get_last_entry(self):
        """Retrieve last entry from the database"""
        try:
            return self.cur.execute('SELECT * FROM sense_readings ORDER BY timestamp DESC LIMIT 1')
        except sqlite3.Error as err:
            self.logger.error(err)

    def get_last_24_hours(self):
        """Retrieve all the data from the database"""
        try:
            return self.cur.execute(
                '''SELECT * FROM sense_readings
                WHERE timestamp >
                DATETIME('now', '-1 day')'''
            )
        except sqlite3.Error as err:
            self.logger.error(err)

    def add_bluetooth(self, name, device):
        """Save the bluetooth into the database"""
        try:
            self.cur.execute(''' INSERT INTO bluetooth_device
                    VALUES(?, ?)''', (name, device))
            self.conn.commit()
        except sqlite3.Error as err:
            self.logger.error(err)

    def get_bluetooth(self):
        """Retrieve all the data from the database"""
        try:
            return self.cur.execute('SELECT * FROM bluetooth_device')
        except sqlite3.Error as err:
            self.logger.error(err)


    def delete_table_content(self):
        """Delete all the data from the database. Remove for final release"""
        try:
            self.cur.execute('DELETE FROM sense_readings')
            self.conn.commit()
        except sqlite3.Error as err:
            self.logger.error(err)

    def drop_bluetooth(self):
        """Remove bluetooth table"""
        try:
            self.cur.execute('DROP TABLE bluetooth_device')
            self.conn.commit()
        except sqlite3.Error as err:
            self.logger.error(err)

    def close(self):
        """Close the connection with the database"""
        try:
            self.conn.close()
        except sqlite3.Error as err:
            self.logger.error(err)

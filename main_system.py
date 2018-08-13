"""
Author: Joshua Hansen
Student Number: s3589185
Email: s3589185@student.rmit.edu.au

Programming Interrnet of Things COSC2674
Semester 2, 2018
Assignment 1

This is the main system for runnign the room monitoring system
This module combines the functionality of all other modules for
the assignment.
"""
from datetime import datetime
from pushbullet import Pushbullet
from sensor_monitor import SensorMonitor
from sqlite_connection import SqliteConnection


def main():
    """Main function for runnign the room monitor system"""
    push_bullet = Pushbullet()
    monitor = SensorMonitor()
    database = SqliteConnection()

    # Threshold to notify users once temperature has fallen bellow it
    temp_threshold = 20

    hum = monitor.get_hum()
    temp = monitor.get_temp()
    time = datetime.now()

    monitor.write("SENSING TEMPERATURE")

    database.save_data(time, temp, hum)

    if temp < temp_threshold:
        push_bullet.send_note(
            "Cold",
            "The room is under 20 degrees you should bring a jacket"
        )

    database.close()

if __name__ == "__main__":
    main()

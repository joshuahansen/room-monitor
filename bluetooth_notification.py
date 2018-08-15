#!/usr/bin/env python3
"""
Author: Joshua Hansen
Student Number: s3589185
Email: s3589185@student.rmit.edu.au

Programming Interrnet of Things COSC2674
Semester 2, 2018
Assignment 1

This module was written for the raspberry pi sense hat bluetooth.
It is intended to be run with python 3 and is used as part
of Assignement 1 for the course.
"""
import bluetooth
from sqlite_connection import SqliteConnection
from sensor_monitor import SensorMonitor


def find_devices():
    """
    Method for finding nearby devices
    Once it finds a saved device it greats them on the LED screen
    """

    database = SqliteConnection()
    sense = SensorMonitor()
    saved_devices = dict()

    sense.bluetooth_logo()

    data = database.get_bluetooth()
    for row in data:
        saved_devices[row[1]] = row[0]

    nearby_devices = bluetooth.discover_devices()
    temp = sense.get_temp()
    sense.clear_led()
    found_match = False

    for device in nearby_devices:
        device_name = bluetooth.lookup_name(device)
        if device_name in saved_devices.keys():
            sense.write(
                "Welcome {0}! The Temperature is {1}"
                .format(saved_devices[device_name], temp)
            )
            found_match = True

    if not found_match:
        sense.error_logo()

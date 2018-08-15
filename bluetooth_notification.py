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
from sense_hat import SenseHat


def find_devices():
    """Method for finding nearby devices"""
    sense = SenseHat()
    sense.show_message("Scanning")
    nearby_devices = bluetooth.discover_devices()
    for device in nearby_devices:
        print("Name: {0} \nDevice: {1}".format(bluetooth.lookup_name(device), device))

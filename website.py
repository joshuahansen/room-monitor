#!/usr/bin/env python3
"""
Author: Joshua Hansen
Student Number: s3589185
Email: s3589185@student.rmit.edu.au

Programming Interrnet of Things COSC2674
Semester 2, 2018
Assignment 1

This script is used for visual display of the logged
data via a website using the flask framework and
javascript Charts.js library
"""

import threading
from flask import Flask, request, render_template
from sqlite_connection import SqliteConnection
import bluetooth_notification as bluetooth


def create_app():
    """Create a falsk application to serve the website"""

    app = Flask(__name__)


    @app.route('/', methods=['GET', 'POST'])
    def home():
        """Function used to display home page"""
        database = SqliteConnection()
        if request:
            if request.method == 'GET' and request.args:
                thread = threading.Thread(target=bluetooth.find_devices, daemon=True)
                thread.start()

            if request.method == 'POST':
                form = request.form
                name = form['name']
                device = form['device_name']
                print(name)
                print(device)
                database.add_bluetooth(name, device)

        print("BEFORE")
        data = database.get_last_24_hours()
        print(data)
        print("AFTER")
        recordings = list()
        try:
            print("TRY")
            for row in data:
                recordings.append(row)
                print(row)

            print("BEFORE ERROR CHECK")
            if not recordings:
                print("VALUEERROR")
                raise ValueError

            return render_template('home.html', data=recordings)
        except (TypeError, ValueError):
            print("EXCEPT")
            return render_template('nodata.html')
        finally:
            database.close()

    return app


if __name__ == '__main__':
    FLASK_APP = create_app()
    FLASK_APP.run(host='0.0.0.0', debug=True)

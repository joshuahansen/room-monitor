#!/usr/bin/env python
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

import flask
from sqlite_connection import SqliteConnection


def create_app():
    """Create a falsk application to serve the website"""

    app = flask.Flask(__name__)


    @app.route('/')
    def home():
        """Function used to display home page"""
        database = SqliteConnection()
        data = database.get_data()
        recordings = list()
        try:
            for row in data:
                recordings.append(row)

            if not recordings:
                raise ValueError
            elif len(recordings) > 24:
                recordings = recordings[-24:]

            return flask.render_template('home.html', data=recordings)
        except (TypeError, ValueError):
            return flask.render_template('nodata.html')
        finally:
            database.close()

    return app


if __name__ == '__main__':
    FLASK_APP = create_app()
    FLASK_APP.run(host='0.0.0.0', debug=True)

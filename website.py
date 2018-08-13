#!/usr/bin/env python

import flask
from sqlite_connection import SqliteConnection


app = flask.Flask(__name__)


@app.route('/')
def home():
    db = SqliteConnection()
    data = db.get_data()
    recordings = list()
    try:
        for row in data:
            recordings.append(row)
   
        if len(recordings) < 1:
            raise ValueError

        return flask.render_template('home.html', data=recordings)
    except (TypeError, ValueError):
        return flask.render_template('nodata.html')
    finally:
        db.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

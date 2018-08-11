import flask
from sqlite_connection import SqliteConnection
import json


app = flask.Flask(__name__)



@app.route('/')
def home():
    db = SqliteConnection()
    data = db.get_data()
    recordings = list()
    try:
        for row in data:
            recordings.append(row)
    except:
        print("Error getting data from database")
    db.close()
    return flask.render_template('home.html', data = recordings)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)

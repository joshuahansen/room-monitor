import flask
import sqlite_connection


app = flask.Flask(__name__)
db = sqlite_connection.SqliteConnection()

@app.route('/')
def home():
    data = db.get_data()
    return flask.render_template('home.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

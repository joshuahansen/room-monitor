from pushbullet import Pushbullet
from sensor_monitor import SensorMonitor
from sqlite_connection import SqliteConnection
from datetime import datetime


pb = Pushbullet()
sm = SensorMonitor()
db = SqliteConnection()

hum = sm.get_hum()
temp = sm.get_temp()
time = datetime.now()

db.save_data(time, temp, hum)

if temp < 20:
    pb.send_note(
        "Cold",
        "The room is under 20 degrees you should bring a jacket"
    )
    
db.close()

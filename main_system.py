from sense_hat import SenseHat
from pushbullet import Pushbullet


sense = SenseHat()
pb = Pushbullet()

temp = sense.get_temperature()

if temp < 20:
    pb.send_note(
        "Cold",
        "The room is under 20 degrees you should bring a jacket"
    )

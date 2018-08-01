from sense_hat import SenseHat
from send_message import SendMessage


sense = SenseHat()
sm = SendMessage()

temp = sense.get_temperature()

print(sm.get_devices())

# if temp > 25:
#	sm.send("Temperature", "The Temperature is {}, please remember to drink water".format(round(temp, 1)))

# ROOM MONITOR README #

This is a simple room monitor that measures the humidity of a room over the course of a week nad recoded it to a database.
A cron job is set up to run at a specific time interval to pull data from the sense-hat.
This data is then represented as a web interface.
The sensor needs to be calibrated to account for the raspberry pi CPU temperature which warms the temperature approximatly 10 degrees.


## PUSHBULLET ##

Using pushbullet the raspberry pi notifies user that the room temperature has dropped bellow a specified temperature (20 degreees) and reminds them to bring a jumper.
This is integreated using the pushbullet API


## BLUETOOTH ##

When the pi detects close Bluetooth devices a greeting with the current room temperature is sent to the user.

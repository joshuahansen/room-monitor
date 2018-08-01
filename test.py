import cpu_temperature as cpuTemp
import time
from sense_hat import SenseHat
'''
while True:
    print(cpuTemp.getCPUTemperature())
    time.sleep(1)
'''

sense = SenseHat()

print(sense.get_temperature())


while(True):
    print(sense.get_humidity())
    time.sleep(1)

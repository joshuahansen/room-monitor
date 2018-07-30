import cpu_temperature as cpuTemp
import time

while True:
    print(cpuTemp.getCPUTemperature())
    time.sleep(1)

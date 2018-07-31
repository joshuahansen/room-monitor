import os


def getCPUTemperature():
    temp = os.popen('vcgencmd messure_temp').readline()
    return (temp.replace("temp=", ""))

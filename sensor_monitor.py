from sense_hat import SenseHat
import os


class SensorMonitor:

    def __init__(self):
        self.sense = SenseHat()

    # Get the humidity from sense hat to given decimal place
    def get_hum(self, dec_place=2):
        hum = self.sense.get_humidity()
        return round(hum, dec_place)

    # Takes the average humidity over a sample size or a default range
    def avg_hum(self, sample_size=5, dec_place=2):
        hum = list()
        for x in range(sample_size):
            hum.append(self.sense.get_humidity())
        return round((sum(hum)/len(hum)), dec_place)

    # Get the temperature from the sense hat to given decimal place
    def get_temp(self, dec_place=2):
        temp = self.sense.get_temperature()
        temp = round(temp, dec_place)
        cpu_temp = self.get_cpu_temperature()

        return temp - ((cpu_temp - temp)/1.5)

    # Returns the average temperature over a given sample size
    # or a default range
    def avg_temp(self, sample_size=5, dec_place=2):
        temp = list()
        for x in range(sample_size):
            temp.append(self.sense.get_temperature())
        temp = round((sum(temp)/len(temp)), dec_place)
        cpu_temp = self.get_cpu_temperature()

        return temp - ((cpu_temp - temp)/1.5)

    def write(self, message):
        self.sense.show_message(message)

    def get_cpu_temperature(self):
        res = os.popen("vcgencmd measure_temp").readline()
        t = float(res.replace("temp=", "").replace("'C\n", ""))
        return(t)

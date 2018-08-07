from sense_hat import SenseHat


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
        return round(temp, dec_place)

    # Returns the average temperature over a given sample size
    # or a default range
    def avg_temp(self, sample_size=5, dec_place=2):
        temp = list()
        for x in range(sample_size):
            temp.append(self.sense.get_temperature())
        return round((sum(temp)/len(temp)), dec_place)

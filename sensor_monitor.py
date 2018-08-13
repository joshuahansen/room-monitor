"""
Author: Joshua Hansen
Student Number: s3589185
Email: s3589185@student.rmit.edu.au

Programming Interrnet of Things COSC2674
Semester 2, 2018
Assignment 1

This module was written for the raspberry pi sense hat.
It is intended to be run with python 3 and is used as part
of Assignement 1 for the course
"""
import os
from sense_hat import SenseHat


class SensorMonitor:
    """
    SensorMonitor Class
    This Class deals with all the different readings from the sense
    hat. This keeps all sense hat functionallity in the one class.
    As more measurements are needed a new method can be defined
    """

    def __init__(self):
        """Contructor creates a sense hat instance"""
        self.sense = SenseHat()

    def get_hum(self, dec_place=2):
        """Get the humidity from sense hat to given decimal place"""
        hum = self.sense.get_humidity()
        return round(hum, dec_place)

    def avg_hum(self, sample_size=5, dec_place=2):
        """Takes the average humidity over a sample size or a default range"""
        hum = list()
        for _ in range(sample_size):
            hum.append(self.sense.get_humidity())
        return round((sum(hum)/len(hum)), dec_place)

    def get_temp(self, dec_place=2):
        """Get the temperature from the sense hat to given decimal place"""
        temp = self.sense.get_temperature()
        temp = round(temp, dec_place)

        return self.calibrate_temp(temp, dec_place)

    def avg_temp(self, sample_size=5, dec_place=2):
        """Returns the average temperature over a given sample size or a default range"""
        temp = list()
        for _ in range(sample_size):
            temp.append(self.sense.get_temperature())
        temp = round((sum(temp)/len(temp)), dec_place)

        return self.calibrate_temp(temp, dec_place)

    def write(self, message):
        """Writes a message on the sense hat LED panel"""
        self.sense.show_message(message)

    @staticmethod
    def get_cpu_temperature():
        """Gets the temperature of the cpu and formats as a float"""
        res = os.popen("vcgencmd measure_temp").readline()
        cpu_temp = float(res.replace("temp=", "").replace("'C\n", ""))
        return cpu_temp

    def calibrate_temp(self, sense_temp, dec_place):
        """Calibrates the messured temperature with the cpu temperature"""
        cpu_temp = self.get_cpu_temperature()
        return round(sense_temp - ((cpu_temp - sense_temp)/1.5), dec_place)

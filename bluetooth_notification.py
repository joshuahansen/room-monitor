from bluetooth import *


def findDevices():
    nearby_devices = bluetooth.discover_devices()
    for device in nearby_devices:
        print("Name: {0} \nDevice: {1}".format(bluetooth.lookup_name(device), device))

findDevices()

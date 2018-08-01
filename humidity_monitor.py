from sense_hat import SenseHat


# Get the humidity from sense hat to given decimal place
def get_humidity(dec_place=2):
    sense = SenseHat()
    humidity = sense.get_humidity()
    return round(humidity, dec_place)


# takes the average humidity over 5 readings
def avg_humidity(sample_size=5, dec_place=2):
    sense = SenseHat()
    humidity = list()
    for x in range(sample_size):
        humidity.append(sense.get_humidity())
    return round((sum(humidity)/len(humidity)), dec_place)


# testing function call for humidity
print("Humidity")
print(get_humidity(3))
print(get_humidity(5))
print(get_humidity(1))
print(get_humidity())

# testing average humidity function
print("Average Humidity")
print(avg_humidity())
print(avg_humidity(10))
print(avg_humidity(2, 3))

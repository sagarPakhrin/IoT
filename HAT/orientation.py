from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
r = (255,0,0)
g = (0,255,0)
b = (0,0,255)

while True:
    sleep(2)
    raw = sense.get_gyroscope_raw()
    #print("p:{x}, r:{y}, y:{z}".format(**raw))
    print(i for i in raw)

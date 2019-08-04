from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

g = (0,255,0)
b = (0,0,255)

def pick_random_color():
    r_r = randint(0,255)
    r_g= randint(0,255)
    r_b= randint(0,255)
    return (r_r,r_g,r_b)


while True:
    creeper_pixels = [
            g,g,g,g,g,g,g,g,
            g,g,g,g,g,g,g,g,
            g,b,b,g,g,b,b,g,
            g,b,b,g,g,b,b,g,
            g,g,g,b,b,g,g,g,
            g,g,b,b,b,b,g,g,
            g,g,b,b,b,b,g,g,
            g,g,b,g,g,b,g,g,
            ]
    g = pick_random_color()
    b = pick_random_color()
    sense.set_pixels(creeper_pixels)
    sleep(1)

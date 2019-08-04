from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
def pick_random_color():
    r_r = randint(0,255)
    r_g= randint(0,255)
    r_b= randint(0,255)
    return (r_r,r_g,r_b)

while True:
    sense.show_letter("I",text_colour= pick_random_color())
    sleep(1)
    sense.show_letter("O",text_colour= pick_random_color())
    sleep(1)
    sense.show_letter("T",text_colour= pick_random_color())
    sleep(1)

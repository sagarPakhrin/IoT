from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

X = [255, 0, 0]  # Red
O = [0, 0, 0]  # White

charct = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]


def printBall(r,c):
    ball_position = r*8+c
    for key,value in enumerate(charct): charct[key] = O
    charct[ball_position] = X
    sense.set_pixels(charct)

try:
    r = 0
    c = 0
    while True:
        printBall(r,c)
        event = sense.stick.wait_for_event()
        sleep(0.1)
        event = sense.stick.wait_for_event()
        if event.direction == "right":
            if not c >= 7:
                c+=1
        if event.direction == "left":
            if not c >= 7:
                c-=1
        sleep(1)

except KeyboardInterrupt:
    print("Closed")

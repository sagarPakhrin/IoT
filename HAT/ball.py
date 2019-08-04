from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
r = (255,0,0)
g = (0,255,0)
b = (0,0,255)

sense.set_imu_config(False,True,False)


raw = sense.get_gyroscope()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**raw))

new_raw = {}

for item in raw.keys():
    new_raw[item] = round(raw[item],1)

X = [255, 0, 0]  # Red
O = [0, 0, 0]  # White

question_mark = [
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
    for key,value in enumerate(question_mark):
        question_mark[key] = O

    question_mark[ball_position] = X
    sense.set_pixels(question_mark)

try:
    x = 2
    y = 4
    direction = 1
    while True:
        raw = sense.get_gyroscope()
        print("p: {pitch}, r: {roll}, y: {yaw}".format(**raw))

        x = x+direction
        if x>6:
            direction = -direction
        if x < 2:
            direction = -direction

        sleep(4.09)
        printBall(x,y)

except KeyboardInterrupt:
    sense.clear(O)

from time import sleep

from picamera import PiCamera

camera = PiCamera(resolution=(1280,720), framerate=30)

#set ISO to desired value
camera.iso=100

sleep(2)


camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'

g=camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

camera.capture_sequence(['image%02d.jpg'% i for i in range(10)])

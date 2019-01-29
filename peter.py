import picamera
from PIL import Image
from time import sleep
from gpiozero import Button


camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 24
button = Button(2)
camera.start_preview()

def overlay():

   global o

   img = Image.open('CFoa1.gif')
   Image.framerate = 4
   pad = Image.new('RGB', (
       ((img.size[0] + 31) // 32) * 32,
       ((img.size[1] + 15) // 16) * 16,
       ))
   pad.paste(img, (0, 0))

   o = camera.add_overlay(pad.tobytes(), size=img.size)
   o.alpha = 128
   o.layer = 3

def removeoverlay():
   camera.remove_overlay(o)

button.when_pressed = overlay()

button.when_released = removeoverlay()

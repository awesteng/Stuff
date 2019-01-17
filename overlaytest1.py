import picamera
from PIL import Image
from time import sleep
from gpiozero import Button


camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 24
button = Button(2)
camera.start_preview()

def default():
    camera.start_preview()
    time.sleep(10)

def overlay():

  img = Image.open('CFoa1.gif')
  Image.framerate = 4
# Create an image padded to the required size with
# mode 'RGB'
  pad = Image.new('RGB', (
      ((img.size[0] + 31) // 32) * 32,
      ((img.size[1] + 15) // 16) * 16,
      ))
# Paste the original image into the padded one
  pad.paste(img, (0, 0))

# Add the overlay with the padded image as the source,
# but the original image's dimensions
  o = camera.add_overlay(pad.tobytes(), size=img.size)
# By default, the overlay is in layer 0, beneath the
# preview (which defaults to layer 2). Here we make
# the new overlay semi-transparent, then move it above
# the preview
  o.alpha = 128
  o.layer = 3

  main()


while True:
    button.when_pressed = overlay()
    button.when_released = default()

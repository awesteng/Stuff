from picamera import PiCamera

camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.start_recording('my_video.h264')
camera.wait_recording(30)
camera.stop_recording()

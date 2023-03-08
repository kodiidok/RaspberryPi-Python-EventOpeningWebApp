import webbrowser
import os
from gpiozero import Button, LED
from time import sleep

new = 2

led1 = LED(25)
led2 = LED(27)
led3 = LED(22)
led4 = LED(23)

touch_sensor = Button(18)

led1.off()
led2.off()
led3.off()
led4.off()

counter = 0

def on_touch():
  global counter
  counter += 1
  f = open('test.txt', 'w')
  if counter == 1:
    led1.on()
  elif counter == 2:
    led2.on()
  elif counter == 3:
    led2.on()
  elif counter == 4:
    led2.on()
  elif counter == 5:
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    os.system('chromium-browser --start-fullscreen myfolder/index.html')
    
    
while True:
  touch_sensor.when_pressed = on_touch
  print(counter)
  if(counter == 5):
    break

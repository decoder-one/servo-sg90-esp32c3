#
# example ESP32 servo
#
import time
import machine
from servo_2 import Servo

servo_pin = machine.Pin(2)
my_servo = Servo(servo_pin)
delay = 0.01
min = 15
max = 165

while True:
    for i in range(min,max):
      my_servo.write_angle(i)
      time.sleep(delay)
    for i in range(max, min, -1):
      my_servo.write_angle(i)
      time.sleep(delay)

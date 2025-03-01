from servo import Servo
import time

motor=Servo(pin=2) # datenpin
motor.move(0) # servo 0°
time.sleep(0.3)
motor.move(90) # servo 90°
time.sleep(0.3)
motor.move(180) # servo 180°
time.sleep(0.3)
motor.move(90) # servo 90°
time.sleep(0.3)
motor.move(0) # servo 0°
time.sleep(0.3)

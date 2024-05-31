from servo import Servo
from serial_reader import read

# Create Servo objects
# Servo connected to GPIO pin 8 and assigned to axis 0
servo_1 = Servo(8, 0)
# Servo connected to GPIO pin 10 and assigned to axis 1
servo_2 = Servo(10, 1)

# Read Objects
# Start reading PWM values from the serial device and controlling servo_1
read(servo_1)
# Start reading PWM values from the serial device and controlling servo_2
read(servo_2)
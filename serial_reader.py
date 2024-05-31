import time
from serial import Serial

def read(servo):
    """
    Reads the PWM value from a serial device and sets the duty cycle of the servo.

    This function continuously reads from a serial device connected to '/dev/ttyACM0' at a baud rate of 19200.
    The read values are expected to be in the format of a string of numbers separated by '|'.
    The function uses the servo's axis number to index into the split string and get the corresponding value.
    This value is then converted to a float, scaled, and used to set the duty cycle of the servo.

    Parameters
    ----------
    servo : Servo
        The servo whose duty cycle is to be set.

    Raises
    ------
    SerialException
        If there is any error in communicating with the serial device.
    ValueError
        If the read value cannot be converted to a float.
    """
    try:
        # Open the serial port once outside the loop
        ser = Serial('/dev/ttyACM0', 19200, timeout=1)
        
        while True:
            time.sleep(0.01)
            
            # Read from the serial port
            line = ser.readline().decode("utf-8").strip().split("|")[servo.axis]
            pwm_value = (float(line) * 5) + 7.5
            print(pwm_value)
            try:
                # Convert to duty cycle between 2.5% and 12.5%
                servo.pwm.ChangeDutyCycle(pwm_value)
            except ValueError:
                print(f"Invalid servo value: {line}")
    except Serial.SerialException as e:
        print(f"Failed to communicate with the serial device: {e}")
    finally:
        # Stop the servo and clean up GPIO resources
        print(str(servo.axis) + " stopped")
        servo.stop()
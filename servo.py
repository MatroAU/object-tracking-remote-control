import RPi.GPIO as GPIO

class Servo:
    """
    A class used to represent a Servo motor.

    Attributes
    ----------
    pin : int
        The GPIO pin number where the servo is connected.
    axis : int
        The axis number of the servo.
    pwm_frequency : int
        The frequency of the PWM signal.
    initial_duty_cycle : float
        The initial duty cycle of the PWM signal.
    pwm_value : None
        The PWM value of the servo. This is set to None initially.
    pwm : GPIO.PWM
        The PWM object from the RPi.GPIO library.

    Methods
    -------
    set_duty_cycle(duty_cycle)
        Sets the duty cycle of the servo.
    stop()
        Stops the servo and cleans up GPIO resources.
    """

    def __init__(self, pin, axis, pwm_frequency=50, initial_duty_cycle=2.5):
        """
        Constructs all the necessary attributes for the Servo object.

        Parameters
        ----------
        pin : int
            The GPIO pin number where the servo is connected.
        axis : int
            The axis number of the servo.
        pwm_frequency : int, optional
            The frequency of the PWM signal (default is 50).
        initial_duty_cycle : float, optional
            The initial duty cycle of the PWM signal (default is 2.5).
        """

        self.pin = pin
        self.axis = axis
        self.pwm_frequency = pwm_frequency
        self.initial_duty_cycle = initial_duty_cycle
        self.pwm_value = None

        try:
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.pin, GPIO.OUT)
            self.pwm = GPIO.PWM(self.pin, self.pwm_frequency)
            self.pwm.start(0)
            self.set_duty_cycle(initial_duty_cycle)
        except Exception as e:
            print(f"Failed to initialize servo on pin {self.pin}: {str(e)}")

    def set_duty_cycle(self, duty_cycle):
        """
        Sets the duty cycle of the servo.

        Parameters
        ----------
        duty_cycle : float
            The duty cycle to set.
        """

        self.pwm.ChangeDutyCycle(duty_cycle)

    def stop(self):
        """
        Stops the servo and cleans up GPIO resources.
        """

        self.pwm.stop()
        GPIO.cleanup()
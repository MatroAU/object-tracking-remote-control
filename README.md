# Raspberry Pi Servo Control

This project provides code to control servos connected to a Raspberry Pi using PWM values read from a serial device.

## Project Structure

The project is divided into two main directories:

- `Rasp Pi`: Contains the main Python scripts for the Raspberry Pi.
- `Rasp Pi Pico`: Contains the MicroPython scripts for the Raspberry Pi Pico.

### Rasp Pi

- `main.py`: The main script that creates Servo objects and starts reading PWM values from the serial device.
- `servo.py`: Defines the Servo class.
- `serial_reader.py`: Contains the function to read PWM values from a serial device.

### Rasp Pi Pico

- `MPU6050.py`: MicroPython driver for the MPU6050 6-axis accelerometer and gyroscope.
- `ooled.py`: Script to control an SSD1306 OLED display.
- `read_mpu.py`: Script to read data from the MPU6050.
- `scanner.py`: I2C scanner script.
- `ssd1306.py`: MicroPython SSD1306 OLED driver.

## Usage

To use this project, run the `main.py` script on your Raspberry Pi:

```sh
python3 main.py

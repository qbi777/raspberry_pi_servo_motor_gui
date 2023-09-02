# raspberry_pi_servo_motor_gui

Raspberry Pi Servo Motor Control with GUI This Python script demonstrates how to control a servo motor using a Raspberry Pi with a graphical user interface (GUI) built using the tkinter library. The script allows you to move the servo motor to specific angles (0 to 180 degrees) by clicking buttons in the GUI.
![raspberry_pi_servo_motor](https://github.com/qbi777/raspberry_pi_servo_motor_gui/assets/123941775/9319ced5-d027-48b7-9ca5-5192877ab199)

Prerequisites
Before running this code, make sure you have the following components and software set up:
![vnc_servo](https://github.com/qbi777/raspberry_pi_servo_motor_gui/assets/123941775/df8223dc-aae8-4dbd-8a50-3ca8a71016b5)

Raspberry Pi (any model with GPIO pins)
RPi.GPIO library (Python library for GPIO control)
Python 3
tkinter library (for GUI creation)
GPIO Configuration
Pin 11 is configured as an output and is used as the servo PWM pin.
The PWM frequency is set to 50Hz, which is a common frequency for servo motors.
The move_servo function is used to control the servo motor by specifying the desired angle.

The GUI window will open, allowing you to control the servo motor with the following buttons:

"0 to 180": Moves the servo to 180 degrees.
"180 to 0": Moves the servo back to 0 degrees.

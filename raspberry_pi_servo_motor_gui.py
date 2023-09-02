import RPi.GPIO as GPIO
import time
import tkinter as tk

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set pin 23 as an output, and define it as the servo PWM pin
GPIO.setup(23, GPIO.OUT)
servo = GPIO.PWM(23, 50)  # Pin 23 for servo, pulse 50Hz
servo.start(0)  # Start servo at 0 degrees

# Function to move the servo to a specified angle
def move_servo(angle):
    duty_cycle = 2 + (angle / 18)
    servo.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)

# Create the GUI window
root = tk.Tk()
root.title("Servo Control")

# Function to move the servo to 0 degrees
def move_to_0():
    move_servo(0)

# Function to move the servo to 180 degrees
def move_to_180():
    move_servo(180)

# Create buttons in the GUI
button_0to180 = tk.Button(root, text="0 to 180", command=move_to_180)
button_0to180.pack()

button_180to0 = tk.Button(root, text="180 to 0", command=move_to_0)
button_180to0.pack()

# Start the GUI main loop
root.mainloop()

# Cleanup GPIO on exit
servo.stop()
GPIO.cleanup()

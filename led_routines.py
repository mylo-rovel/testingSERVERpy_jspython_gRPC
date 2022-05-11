import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

# PIN 8 => AMARILLO
# PIN 10 => AZUL
# PIN 12 => VERDE

def rutina_secuencia1():
    pinUsar = 8
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(pinUsar, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
    for x in range(5):
        GPIO.output(pinUsar, GPIO.HIGH) # Turn on
        sleep(1) # Sleep for 1 second
        GPIO.output(pinUsar, GPIO.LOW) # Turn off
        sleep(1) # Sleep for 1 second

def rutina_secuencia2():
    pinUsar = 10
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(pinUsar, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
    for x in range(5):
        GPIO.output(pinUsar, GPIO.HIGH) # Turn on
        sleep(1) # Sleep for 1 second
        GPIO.output(pinUsar, GPIO.LOW) # Turn off
        sleep(1) # Sleep for 1 second

def rutina_secuencia3():
    pinUsar = 12
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(pinUsar, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
    for x in range(5):
        GPIO.output(pinUsar, GPIO.HIGH) # Turn on
        sleep(1) # Sleep for 1 second
        GPIO.output(pinUsar, GPIO.LOW) # Turn off
        sleep(1) # Sleep for 1 second
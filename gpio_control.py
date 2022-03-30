import RPi.GPIO as GPIO
import time

buzzer = 17
access_denied_led = 27
access_granted_led = 22
locked_led = 23
unlocked_led = 24
lock_gpio = 25


def close():
    GPIO.output(buzzer, GPIO.HIGH)
    GPIO.output(access_granted_led, GPIO.LOW)
    GPIO.output(access_denied_led, GPIO.HIGH)
    GPIO.output(lock_gpio, GPIO.LOW)

    time.sleep(0.5)

    GPIO.output(buzzer, GPIO.LOW)

    time.sleep(5)

    GPIO.output(access_denied_led, GPIO.LOW)


def open():
    GPIO.output(buzzer, GPIO.HIGH)
    GPIO.output(access_granted_led, GPIO.HIGH)
    GPIO.output(access_denied_led, GPIO.LOW)
    GPIO.output(lock_gpio, GPIO.HIGH)

    time.sleep(0.5)

    GPIO.output(buzzer, GPIO.LOW)

    time.sleep(5)

    GPIO.output(access_granted_led, GPIO.LOW)
    GPIO.output(lock_gpio, GPIO.LOW)


def unlock():
    GPIO.output(locked_led, GPIO.LOW)
    GPIO.output(unlocked_led, GPIO.HIGH)


def lock():
    GPIO.output(locked_led, GPIO.HIGH)
    GPIO.output(unlocked_led, GPIO.LOW)
    GPIO.output(access_granted_led, GPIO.LOW)
    GPIO.output(access_denied_led, GPIO.LOW)
    GPIO.output(buzzer, GPIO.LOW)
    GPIO.output(lock_gpio, GPIO.LOW)


def config_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer, GPIO.OUT)
    GPIO.setup(access_denied_led, GPIO.OUT)
    GPIO.setup(access_granted_led, GPIO.OUT)
    GPIO.setup(locked_led, GPIO.OUT)
    GPIO.setup(unlocked_led, GPIO.OUT)
    GPIO.setup(lock_gpio, GPIO.OUT)

    GPIO.output(buzzer, GPIO.LOW)
    GPIO.output(access_denied_led, GPIO.LOW)
    GPIO.output(access_granted_led, GPIO.LOW)
    GPIO.output(locked_led, GPIO.LOW)
    GPIO.output(unlocked_led, GPIO.HIGH)
    GPIO.output(lock_gpio, GPIO.LOW)
    
    
def end_gpio():
 	GPIO.cleanup()

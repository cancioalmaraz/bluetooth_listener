#!/usr/bin/env python
import serial
import json
import RPi.GPIO as GPIO


class BluetoothListener:
    def __init__(self, port='/dev/rfcomm0'):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.bluetooth_serial = serial.Serial(port, 9600)
        self.pwm_pin_dict = dict()

    def waitCommand(self):
        print('Waiting for command...')
        json_command = self.bluetooth_serial.readline().decode('utf-8')
        command = json.loads(json_command)
        return (command['action'], command['pin'], command['value'])

    def executeCommand(self, action, pin, value):
        print('Action: ', action)
        print('Pin: ', pin)
        print('Value: ', value)
        if (action == 'turn'):
            self.setPin(pin, value)
        elif (action == 'pwm'):
            self.setPwmPin(pin, value)
        else:
            print('Command not allowed')

    def setPin(self, pin, value):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, value)

    def setPwmPin(self, pin, value):
        if (not pin in self.pwm_pin_dict):
            GPIO.setup(pin, GPIO.OUT)
            pwm = GPIO.PWM(pin, 1000)
            self.pwm_pin_dict[pin] = pwm
        else:
            pwm = self.pwm_pin_dict[pin]
        pwm.start(0)
        pwm.ChangeDutyCycle(value)

    def run(self):
        while True:
            (action, pin, value) = self.waitCommand()
            self.executeCommand(action, pin, value)
            print()
            print()


if __name__ == '__main__':
    bluetoothListener = BluetoothListener()
    bluetoothListener.run()

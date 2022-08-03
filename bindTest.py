# In order to overcome current limits on a Raspberry Pi Pico, a physical switch can be used:
    # Apply 3.3V from an external power source so that when the switch is pressed, it powers on 
    # the reciever and simultaneously is read by a GPIO pin.
    # When GPIO pin reads high, bind pulses are sent.

# Spektrum Binding Protocol:
    # Must send a specified number of falling pulses within 200ms of powering on
    # 3 Internal DSM2 22ms
    # 4 External DSM2 22ms
    # 5 Internal DSM2 11ms
    # 6 External DSM2 11ms 
    # 7 Internal DSMx 22ms
    # 8 External DSMx 22ms
    # 9 Internal DSMx 11ms (UNIVERSAL INTERNAL)
    # 10 External DSMx 11ms 

from machine import Pin
import time

class bindDSM: 
    def __init__(self, signalPin, vccPin, numBindPulses=9, pulseWidth_us=120):
        self.signalPin = Pin(signalPin, Pin.OUT)    #Signal pin
        self.vccPin = Pin(vccPin, Pin.OUT)          #Power to reciever
        self.numBindPulses = numBindPulses          #Number of falling pulses determines protocol
        self.pulseWidth_us = pulseWidth_us          #Must allow for all pulses to be delivered within 200ms of powering receiver

    def sendBindPulses(self):                       #Deliver falling pulses
        for i in range(self.numBindPulses):
            self.signalPin.value(0)
            time.sleep_us(self.pulseWidth_us)
            self.signalPin.value(1)
            time.sleep_us(self.pulseWidth_us)
            print(i+1)


switchSignal = Pin(15,Pin.IN,Pin.PULL_DOWN)         #Switch input with pull down resistor
rc = bindDSM(signalPin=10, vccPin=0)                #Create bind object

rc.vccPin.value(1)                                  #Power Reciever Pin to prepare for physical switch input
rc.signalPin.value(1)                               #Power Signal Pin to prepare for falling pulse
time.sleep(2)                                       #Delay to ensure pins powered on

while(1):
    if (switchSignal.value()):
        print('High')
        time.sleep_ms(100)                          #Delay to ensure reciever fully powered on before pulses delivered

        rc.sendBindPulses()                         #Send the pulses

        print('Pulses Sent')
        time.sleep(15)                              #Put transmitter into bind mode during this 15 second period
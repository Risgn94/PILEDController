#import RPi.GPIO as GPIO
import time
from multiprocessing import Process
import datetime
import os

class LED():
    def __init__(self, pattern):
        self._speed = 0
        self._pauseSpeed = 0
        self.__morse = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }
        self.pattern = self.__convertString(pattern)

        GPIO.setmode(GPIO.BCM)
        LED_PIN = 21
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.HIGH)
        GPIO.output(LED_PIN, GPIO.LOW)

    def __convertString(self, textString):
        morseString = []
        for letters in textString:
            if(letters == " "):
                morseString.append('&&')
            else:
                morseString.append(self.__morse[letters.upper()])
                morseString.append('&')
        return morseString


    def setPattern(self, pattern):
        self.process.terminate()
        self.pattern = self.__convertString(pattern)
        self.startLights()

    #Start LEDS
    def startLights(self):
        self.process = Process(target=self.runLights)
        self.process.start()

    def runLights(self):
        pureChars = "".join(self.pattern)
        while True:
            for chars in pureChars:
                time.sleep(0.5)
                if(chars == '.'):
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.25)
                    GPIO.output(LED_PIN, GPIO.LOW)
                elif(chars == '-'):
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(LED_PIN, GPIO.LOW)
                elif(chars == '&&'):
                    time.sleep(2)
                elif(chars == '&'):
                    time.sleep(1)

    #Stop LEDS
    def stopLigths(self):
        self.process.terminate()
'''
@Author Brian McGinnis
Error handler is given a ledProcess
When an error occurs in another class it will call the error errorHandler
Either the handler will flahs red and try and wait for the problem to be
fixed or it will start flashing red for an un-recoverable error and attempt
to reboot
After the error code has been show it it will flash green to show it is going to
show the next color

The Error number will flash RED in binary

Error Numbers are as follows
1:Config was not properly read
2:STT was not started
3:TTS was not started
4:Conversation was not Started
5:Visual Rec was not Started
6:Bioloid was not started

15:To many errors have occured
'''
import time
from subprocess import call

class errorHandler:
    errorLimit = 5
    errorCount = 0
    def __init__(self, ledProcess):
        self.led = ledProcess

    def erros():
        led.red()
        errorCount += 1
        if errorCount > errorLimit:
            fatalError(15)

    def fatalError(error):
        code = bin(error)
        code = list(str(code))
        for i in range(0,4):
            led.green()
            time.sleep(1)
            for n in code:
                if n == '1':
                    led.red()
                elif n == '0':
                    led.customColor(0,0,0)
                time.sleep(.5)
        call("sudo showdown -r now", shell=True)

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

    '''
        This function gets a error and increments the error count. when it gets an
        error it turns the LED red and increments the error count. d
        in the event there have been a large number of errors a fatal error will
        be triggered.
    '''
    def error(self):
        led.red()
        errorCount += 1
        if errorCount > errorLimit:
            fatalError(15)
    '''
        this function handles the events when a un recoverable error occurs
        and the Bioloid needs to reboot itsself in order to continue. A Number
        is passed to the function and this number is coneverted to binary. then
        its binary representation is changed to a char list that is iterated over..
        4 times and displayed using the RED status LED On the Bioloidself. after
        it has iterated the system will restart. 
    '''
    def fatalError(self, error):
        code = bin(error)
        code = list(str(code))
        for i in range(0,4):
            self.led.green()
            time.sleep(1)
            for n in code:
                if n == '1':
                    self.led.red()
                elif n == '0':
                    self.led.customColor(0,0,0)
                time.sleep(.5)
        call("sudo showdown -r now", shell=True)

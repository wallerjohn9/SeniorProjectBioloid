'''
@Author Brian McGinnis
Error handler is given a ledProcess
When an error occurs in another class it will call the error errorHandler
Either the handler will flahs red and try and wait for the problem to be
fixed or it will start flashing red for an un-recoverable error and attempt
to reboot

The Error number will flash RED in binary

Error Numbers are as follows
1:Config was not properly read
2:STT was not started
3:TTS was not started
4:Conversation was not Started
5:Visual Rec was not Started
6:Bioloid was not started
'''
import time

class errorHandler:

    def __init__(self, ledProcess):
        self.led = ledProcess

    def erros():
        led.red()

    def fatalError(error):
        code = bin(error)
        code = list(str(code))
        for(i = 0; i < 4; i++):
            led.green()
            time.sleep(1)
            for n in code:
                if n == '1':
                    led.red()
                else if n=='0':
                    led.off()
                time.sleep(.5)

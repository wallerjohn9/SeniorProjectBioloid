#!/usr/bin/env python

"""

                  888
                  888
                  888
88888b.   .d88b.  88888b.   .d88b.  888  888
888 "88b d88""88b 888 "88b d88""88b `Y8bd8P'
888  888 888  888 888  888 888  888   X88K
888  888 Y88..88P 888 d88P Y88..88P .d8""8b.     http://nobox.io
888  888  "Y88P"  88888P"   "Y88P"  888  888     http://github.com/noboxio


TJBot

Author: Brian McGinnis
Date: 6/23/17
"""

import conversation
import ledProcess
import led
import textToSpeech
import streaming
import time
import RPi.GPIO as GPIO
import time
import movements
import bioloid as bio
#import visualRecognition as vis
import errorHandler
from subprocess import call
import configparser
import signal


def sig_handler(signum, frame):
    print("segFault")
    call("sudo ./home/pi/SeniorProjectBioloid/start.sh", shell = True)
    #call("sudo shutdown -r now", shell=True)

def main():

    #Attempts at handling segementation faults and pipe faults
    signal.signal(signal.SIGPIPE, sig_handler)
    signal.signal(signal.SIGSEGV, sig_handler)

    #Creation of the LED object and Process
    #led_obj = led.Led()
    #ledP = ledProcess.LedProcess(led_obj)

    #Creation of the error handler and it passed the LED process so it can reference it
    #errorHandle = errorHandler.errorHandler(ledP)
    config = configparser.ConfigParser()

    #This pulls in all of the credentials from the config files
    #If one of these fails to pull in a fatal error is called
    try:
        config.read('/home/pi/SeniorProjectBioloid/config.cfg')
        sttUser = config.get('Bioloid Credentials','sttUser')
        sttPw = config.get('Bioloid Credentials','sttPassword')
        ttsUser = config.get('Bioloid Credentials','ttsUser')
        ttsPw = config.get('Bioloid Credentials','ttsPassword')
        convoUser = config.get('Bioloid Credentials','convoUser')
        convoPw = config.get('Bioloid Credentials','convoPassword')
        convoWorkSpace = config.get('Bioloid Credentials','convoWorkSpace')
        # configuration for timeout options
        timeoutWarning = float(config.get('Bioloid Information','timeoutWarning'))
        timeoutShutdown = float(config.get('Bioloid Information','timeoutShutdown'))
        soundsLike = config.get('Bioloid Information', 'soundsLike')
    except:
        errorHandle.fatalError(1)
    homophones = soundsLike.split(",")

    #Start Creating the Watson servicesself.
    #If one of them fails then it gives an erro
    #the credentials can be changed in the config file
    try:
        stt = streaming.StreamingSTT(
            sttUser,
            sttPw)
    except:
        print("error 2")
        #errorHandle.fatalError(2)

    try:
        print("Attempted to login to TTS")
        tts = textToSpeech.TextToSpeech(
            ttsUser,
            ttsPw)
    except:
        #errorHandle.fatalError(3)
        print("error 3")
    try:
        convo = conversation.Assistant(
            convoUser,
            convoPw,
            convoWorkSpace)
    except:
        errorHandle.fatalError(4)

    #Starts up the Visual recogniton abilites.
#    try:
#        vr = vis.VisualRecognition()
#    except:
#        errorHandle.fatalError(5)
    #Creates the bioloid so we cna control the motors
    try:
        bioloid = bio.Bioloid()
    except:
        print("error6")
#        errorHandle.fatalError(6)

    #bioloid.doLookUp()

    #say = vr.viewObjects()
    #tts.speak(say, False)
    #say = vr.viewFaces()
    #tts.speak(say, False)

    #bioloid.doIdle(False)
    #Gets the name of the robot from the Config File
    name = config.get('Bioloid Information','name')

    #This allows to see if the robot has been inactive
    lastActiveTime = time.time()

    activeTimeCheck = True # This boolean differentiates between inactivity for 60 or 120 seconds.

#    bioloid.doBow()
    #Kind of a hello works to know TTS is working.
    tts.speak('Hello my name is ' + name + ' I am a big robot!')
   # bioloid.doPushUp(2)
    i=0
    while i!=1:

        if all( [time.time() - lastActiveTime > timeoutWarning, activeTimeCheck == True] ):
            bioloid.doSit()
            tts.speak("I have been inactive for 1 minute. After another minute, I will shut down")
            activeTimeCheck = False

        if all( [time.time() - lastActiveTime > timeoutShutdown, activeTimeCheck == False] ):
            bioloid.doSit()
            tts.speak("Shutting down now.")
            call("sudo shutdown -h now", shell=True)


        """
        if(lastActiveTime - time.time() > 60): #if it is inactive for 1 min then it powers down.
            #Go home
            tts.speak("I have been inactive for 1 minute. After another minute, I will shut down")
        """
        #bioloid.doListen()
        i=1
        try:
            phrase = stt.get_phrase()
            print(phrase)
            try:
                response = convo.sendMessage(phrase)
            except:
                print("The Response was blank")
        except:
            errorHandle.fatalError(1)
        if (name in phrase) or (checkForName(homophones, phrase)):

            lastActiveTime = time.time() #if its name is heard then we can assume it is active
            activeTimeCheck = True
            #try:
            #    response = convo.sendMessage(phrase)
            #except:
            #    print("The Response was blank")
            #if '~' in response:
            #    response = processCommand(response, bioloid)
            #else:
            #    bioloid.doIdle(False)


            tts.speak(response)



def processCommand(response, bioloid):
    if '~UNKNOWN' in response:
        bioloid.doScratchHead(False)
    if '~INSULT' in response:
        bioloid.doBeatChest(False)
    if '~PUSH' in response:
        bioloid.doPushUp(2)
    if '~AGGRESSIVE' in response:
        bioloid.doBeatChest(False)
    if '~APOLOGETIC' in response:
        bioloid.doBow(False)
    if '~TIME' in response:
        os.enviorn['TZ'] = 'US/Central'
        time.tzset()
        t = time.now()
        t = time.strftime("%H:%M")
        response = "The Time is currently" + t
    if '~VR' in response:
        response = vr.viewObjects()
    return response
    '''
    if '~RED' in response:
        ledP.red()
        response = response.replace('~RED', '', 1)
    if '~ORANGE' in response:
        ledP.orange()
        response = response.replace('~ORANGE', '', 1)
    if '~YELLOW' in response:
        ledP.yellow()
        response = response.replace('~YELLOW', '', 1)
    if '~GREEN' in response:
        ledP.green()
        response = response.replace('~GREEN', '', 1)
    if '~BLUE' in response:
        print('Its Blue')
        ledP.blue()
        response = response.replace('~BLUE', '', 1)
    if '~PURPLE' in response:
        ledP.purple()
        response = response.replace('~PURPLE', '', 1)
    if '~PINK' in response:
        ledP.pink()
        response = response.replace('~PINK', '', 1)
    if '~WHITE' in response:
        ledP.white()
        response = response.replace('~WHITE', '', 1)
    if '~RAINBOW' in response:
        ledP.rainbow()
        response = response.replace('~RAINBOW', '', 1)
    if '~RAINBOWCYCLE' in response:
        ledP.rainbowCycle()
        response = response.replace('~RAINBOWCYCLE', '', 1)
    if '~MUSICPLAY' in response:
        musicP.play()
        response = response.replace('~MUSICPLAY', '', 1)
    if '~MUSICSTOP' in response:
        musicP.stop()
        response = response.replace('~MUSICSTOP', '', 1)
    if '~LEDOFF' in response:
        ledP.off()
        response = response.replace('~LEDOFF', '', 1)
    if '~ARMSTOP' in response:
        servoP.stop()
        response = response.replace('~ARMSTOP', '', 1)
    if '~ARMUP' in response:
        servoP.armUp()
        response = response.replace('~ARMUP', '', 1)
    if '~ARMDOWN' in response:
        servoP.armDown()
        response = response.replace('~ARMDOWN', '', 1)
    if '~DANCE' in response:
        servoP.wave(10)
        ledP.rainbowCycle(1, 50)
        response = response.replace('~DANCE', '', 1)
    if '~ARMANGLE' in response:
        response = response.replace('~ARMANGLE', '', 1)
        param = int(response.split("~", 1)[0])
        response = response.split("~", 1)[1]
        servoP.angle(param)
    if '~ARMWAVECOUNT' in response:
        response = response.replace('~ARMWAVECOUNTARMANGLE', '', 1)
        param = int(response.split("~", 1)[0])
        response = response.split("~", 1)[1]
        servoP.wave(param)
    if '~ARMWAVE' in response:
        servoP.wave(2)
        response = response.replace('~ARMWAVE', '', 1)
    if response == '':
        response = 'akward silence'
    '''

def checkForName(words, phrase):
    #words = words.toLower()
    phrase= phrase.lower()
    for w in words:
        w=w.lower()
        if w in phrase:
            return True
    return False



if __name__ == "__main__":
    main()

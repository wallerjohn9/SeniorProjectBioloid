'''
Created on Jan 21, 2018

@author: Cody Black and Brian McGinnis

This Class is resposnible for the creation and handling the robot Object
created using pypot

It also contains the movements functions that can be called to enable movements for
the bioloid
Each of these functions are prefaced with do and then followed by the name of
the action
Some of these movements allow a boolen value to be passed to them. This allows
the movement to operate in a new thread and other processes to exist at the same
time. Be careful of this as if two movements try and operate at the same time
There will be errors that crash the program. 
'''
import time
import movements
import pypot.robot
import primitives
import botSetup

class Bioloid:
    def __init__(self):
        print('Configuring bioloid...')
        self.bioloid = pypot.robot.from_config(botSetup.bot_config)
        self.bioloid.start_sync()
        self.rightStep = True

        #tells us which "Square he is in. OR maybe we do some step count where we count how
        #many steps he has taken in certain directions to get an idea of where he is. He should
        #return home most when he needs to stop.
        """self.location=[[0,0,0,0,0
                        0,0,0,0,0
                        0,0,1,0,0
                        0,0,0,0,0,
                        0,0,0,0,0]]
        """
        #have this be some product of turns Tells us which direction he is looking at
        self.orientation = 0

        #print('Configuration complete...\n')
        #print('Bioloid:\n')

        # Primitives code block
        self.idlePosition = primitives.StartPosPrimitive(self.bioloid)
        self.redeem = primitives.Redeemer(self.bioloid)
        self.dance = primitives.DancePrimitive1(self.bioloid)
        self.bow = primitives.Bow(self.bioloid)
        self.pushUpStart = primitives.pushUpStart(self.bioloid)
        self.pushUpMiddle = primitives.pushUpMiddle(self.bioloid)
        self.pushUpEnd = primitives.pushUpEnd(self.bioloid)
        self.getUpFront = primitives.getUpFront(self.bioloid)
        self.handStand1 = primitives.handStand1(self.bioloid)
        self.handStand2 = primitives.handStand2(self.bioloid)
        self.handStand3 = primitives.handStand3(self.bioloid)
        self.prepareWalk = primitives.prepareWalk(self.bioloid)
        self.frontWalkStartL = primitives.frontWalkStartL(self.bioloid)
        self.frontWalkStartR1 = primitives.frontWalkStartR1(self.bioloid)
        self.frontWalkMiddleL1 = primitives.frontWalkMiddleL1(self.bioloid)
        self.frontWalkMiddleR1 = primitives.frontWalkMiddleR1(self.bioloid)
        self.frontWalkEndL1 = primitives.frontWalkEndL1(self.bioloid)
        self.frontWalkEndR1 = primitives.frontWalkEndR1(self.bioloid)
        self.sit = primitives.sit(self.bioloid)
        self.lookUp = primitives.lookUp(self.bioloid)
        self.listen = primitives.listen(self.bioloid)
        self.scratchHead = primitives.scratchHead(self.bioloid)
        self.beatChest = primitives.beatChest(self.bioloid)



        idlePosition.start()
        idlePosition.wait_to_stop()
        self.bioloid.compliant = True
        self.bioloid.compliant = False #this tells the motors to get stiff
        self.idlePosition.start()
        self.idlePosition.wait_to_stop()

    def doIdle(self, wait=True):
        self.bioloid.start_sync()
        self.idlePosition.start()
        if wait:
            self.idlePosition.wait_to_stop()
    def doBow(self, wait=True):
        self.bioloid.start_sync()
        self.bow.start()
        if wait:
            self.bow.wait_to_stop()

    def doPushUp(self, count = 1):
        self.bioloid.start_sync()
        self.pushUpStart.start()
        self.pushUpStart.wait_to_stop()
        while(count > 0):
            self.bioloid.start_sync()
            self.pushUpMiddle.start()
            self.pushUpMiddle.wait_to_stop()
            count = count - 1
        self.bioloid.start_sync()
        self.pushUpEnd.start()
        self.pushUpEnd.wait_to_stop()

    def doWalkFront(self, steps = 1):
        self.bioloid.start_sync()
        if(self.rightStep):
            self.frontWalkStartR1.start()
            self.frontWalkStartR1.wait_to_stop()
            self.rightStep = False
        else:
            self.frontWalkStartL.start()
            self.frontWalkStartL.wait_to_stop()
            self.rightStep = True
        while(steps > 0):
            if(self.rightStep):
                self.frontWalkMiddleR1.start()
                self.frontWalkMiddleR1.wait_to_stop()
                self.rightStep = False
            else:
                self.frontWalkMiddleL1.start()
                self.frontWalkMiddleL1.wait_to_stop()
                self.rightStep = True
            steps = steps - 1
        if(self.rightStep):
            self.frontWalkEndR1.start()
            self.frontWalkEndR1.wait_to_stop()
            self.rightStep = False
        else:
            self.frontWalkEndL1.start()
            self.frontWalkEndL1.wait_to_stop()
            self.rightStep = True

    def doSit(self):
        self.sit.start()
        self.sit.wait_to_stop()

    def doLookUp(self):
        self.lookUp.start()
        self.lookUp.wait_to_stop()

    def doListen(self, wait=True):
        self.bioloid.start_sync()
        self.listen.start()
        if wait:
            self.listen.wait_to_stop()

    def doScratchHead(self, wait=True):
        self.bioloid.start_sync()
        self.scratchHead.start()
        if wait:
            self.scratchHead.wait_to_stop()

    def doBeatChest(self, wait=True):
        self.bioloid.start_sync()
        self.beatChest.start()
        if wait:
            self.beatChest.wait_to_stop()


    def close(self):
        self.bioloid.close()

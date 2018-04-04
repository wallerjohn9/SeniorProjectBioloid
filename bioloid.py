'''
Created on Jan 21, 2018

@author: codyblack
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



        #idlePosition.start()
        #idlePosition.wait_to_stop()
        self.bioloid.compliant = True
        self.bioloid.compliant = False #this tells the motors to get stiff
        self.idlePosition.start()
        self.idlePosition.wait_to_stop()

    def doBow(self):
        self.bow.start()
        self.bow.wait_to_stop()

    def doPushUp(self, count = 1):
        self.pushUpStart.start()
        self.pushUpStart.wait_to_stop()
        while(count > 0):
            self.pushUpMiddle.start()
            self.pushUpMiddle.wait_to_stop()
            count = count - 1
        self.pushUpEnd.start()
        self.pushUpEnd.wait_to_stop()

    def doWalkFront(self, steps = 1):
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
        if(self.rightStep):
            self.frontWalkEndR1.start()
            self.frontWalkEndR1.wait_to_stop()
            self.rightStep = False
        else:
            self.frontWalkEndL1.start()
            self.frontWalkEndL1.wait_to_stop()
            self.rightStep = True



    def close(self):
        self.bioloid.close()

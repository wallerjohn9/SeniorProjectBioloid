import time
import pypot.primitive
import movements
import numpy

class StartPosPrimitive(pypot.primitive.Primitive):
    def __init__(self, robot):
        self.robot = robot
        pypot.primitive.Primitive.__init__(self, robot)

    def run(self):
        print("1")
        self.robot.goto_position(movements.startPosDict, 1, 'dummy', True)
        #self.robot.goto_position(movements.startPosDictA, 1, 'dummy', False)
        print("2")

class Redeemer(pypot.primitive.Primitive):
    def __init__(self, robot):
        self.robot = robot
        pypot.primitive.Primitive.__init__(self, robot)

    def run(self):
        print("1")
        self.robot.goto_position(movements.redeemer, 1, 'dummy', False)
        print("2")

class DancePrimitive(pypot.primitive.Primitive):
    def __init__(self, robot):
        self.robot = robot
        pypot.primitive.Primitive.__init__(self, robot)

    def run(self):
        #while self.elapsed_time < 15:
        print("Dancing")
        print(self.elapsed_time)
        print(self.robot)
        print("1")
        """for m in self.robot.arms:
            m.compliant = False
            m.goal_position = 90
            time.sleep(.02)
        """
        for m in self.robot.arms:
            m.compliant = False
        self.robot.goto_position({'left_hand': -90, 'right_hand': 90}, 1, 'dummy', True)
        print("2")
        self.robot.goto_position({'left_hand': 0, 'right_hand': 0}, 1, 'dummy', True)
        print("3")
        #time.sleep(3)
        print("4")

class DancePrimitive1(pypot.primitive.Primitive):

    def __init__(self, robot, amp=100, freq=0.5):
        self.robot = robot
        self.amp = amp
        self.freq = freq
        pypot.primitive.Primitive.__init__(self, robot)

    def run(self):
        amp = self.amp
        freq = self.freq
        # self.elapsed_time gives you the time (in s) since the primitive has been running
        while self.elapsed_time < 15:
            print(self.elapsed_time)
            x = amp * numpy.sin(2 * numpy.pi * freq * self.elapsed_time)
            self.robot.right_hand.goal_position = -x
            self.robot.right_shoulder.goal_position = -x
            self.robot.left_hand.goal_position = x
            self.robot.left_shoulder.goal_position = x
            time.sleep(.1)

class Bow(pypot.primitive.Primitive):
    def __init__(self, robot):
        self.robot = robot
        pypot.primitive.Primitive.__init__(self, robot)

    def run(self):

        self.robot.goto_position(movements.bow0, movements.bowTimes['0'], 'dummy', True)
        self.robot.goto_position(movements.bow1, movements.bowTimes['1'], 'dummy', True)
        self.robot.goto_position(movements.bow2, movements.bowTimes['2'], 'dummy', True)
        self.robot.goto_position(movements.bow3, movements.bowTimes['3'], 'dummy', True)
        self.robot.goto_position(movements.bow4, movements.bowTimes['4'], 'dummy', True)
        self.robot.goto_position(movements.bow5, movements.bowTimes['5'], 'dummy', True)
        self.robot.goto_position(movements.bow6, movements.bowTimes['6'], 'dummy', True)


##################################
###########Bravo#########
###################################

class Bravo(pypot.primitive.Primitive):
	def __init__(self, robot):
            self.robot = robot
            pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.Bravo0, movements.BravoTimes['0'], 'dummy', True)
		self.robot.goto_position(movements.Bravo1, movements.BravoTimes['1'], 'dummy', True)
		self.robot.goto_position(movements.Bravo2, movements.BravoTimes['2'], 'dummy', True)
		self.robot.goto_position(movements.Bravo3, movements.BravoTimes['3'], 'dummy', True)
		self.robot.goto_position(movements.Bravo4, movements.BravoTimes['4'], 'dummy', True)


##################################
###########pushUpStart#########
###################################

class pushUpStart(pypot.primitive.Primitive):
	def __init__(self, robot):
        self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.pushUpStart0, movements.pushUpStartTimes['0'], 'dummy', True)
		self.robot.goto_position(movements.pushUpStart1, movements.pushUpStartTimes['1'], 'dummy', True)
		self.robot.goto_position(movements.pushUpStart2, movements.pushUpStartTimes['2'], 'dummy', True)
		self.robot.goto_position(movements.pushUpStart3, movements.pushUpStartTimes['3'], 'dummy', True)
		self.robot.goto_position(movements.pushUpStart4, movements.pushUpStartTimes['4'], 'dummy', True)
		self.robot.goto_position(movements.pushUpStart5, movements.pushUpStartTimes['5'], 'dummy', True)

##################################
###########pushUpMiddle#########
###################################

class pushUpMiddle(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.pushUpMiddle0, movements.pushUpMiddleTimes['0'], 'dummy', True)
		self.robot.goto_position(movements.pushUpMiddle1, movements.pushUpMiddleTimes['1'], 'dummy', True)

##################################
###########pushUpEnd#########
###################################

class pushUpEnd(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.pushUpEnd0, movements.pushUpEndTimes['0'], 'dummy', True)
		self.robot.goto_position(movements.pushUpEnd1, movements.pushUpEndTimes['1'], 'dummy', True)
		self.robot.goto_position(movements.pushUpEnd2, movements.pushUpEndTimes['2'], 'dummy', True)
		self.robot.goto_position(movements.pushUpEnd3, movements.pushUpEndTimes['3'], 'dummy', True)
		self.robot.goto_position(movements.pushUpEnd4, movements.pushUpEndTimes['4'], 'dummy', True)
		self.robot.goto_position(movements.pushUpEnd5, movements.pushUpEndTimes['5'], 'dummy', True)
		self.robot.goto_position(movements.pushUpEnd6, movements.pushUpEndTimes['6'], 'dummy', True)

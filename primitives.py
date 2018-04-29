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


##################################
###########getUpFront#########
###################################

class getUpFront(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.getUpFront0, movements.getUpFrontTimes['0'], 'dummy', True)
		self.robot.goto_position(movements.getUpFront1, movements.getUpFrontTimes['1'], 'dummy', True)
		self.robot.goto_position(movements.getUpFront2, movements.getUpFrontTimes['2'], 'dummy', True)
		self.robot.goto_position(movements.getUpFront3, movements.getUpFrontTimes['3'], 'dummy', True)
		self.robot.goto_position(movements.getUpFront4, movements.getUpFrontTimes['4'], 'dummy', True)


##################################
###########handStand1#########
###################################

class handStand1(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.handStand10, movements.handStand1Times['0'], 'dummy', True)
		self.robot.goto_position(movements.handStand11, movements.handStand1Times['1'], 'dummy', True)
		self.robot.goto_position(movements.handStand12, movements.handStand1Times['2'], 'dummy', True)
		self.robot.goto_position(movements.handStand13, movements.handStand1Times['3'], 'dummy', True)
		self.robot.goto_position(movements.handStand14, movements.handStand1Times['4'], 'dummy', True)
		self.robot.goto_position(movements.handStand15, movements.handStand1Times['5'], 'dummy', True)

##################################
###########handStand2#########
###################################

class handStand2(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.handStand20, movements.handStand2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.handStand21, movements.handStand2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.handStand22, movements.handStand2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.handStand23, movements.handStand2Times['3'], 'dummy', True)

##################################
###########handStand3#########
###################################

class handStand3(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.handStand30, movements.handStand3Times['0'], 'dummy', True)
		self.robot.goto_position(movements.handStand31, movements.handStand3Times['1'], 'dummy', True)
		self.robot.goto_position(movements.handStand32, movements.handStand3Times['2'], 'dummy', True)
		self.robot.goto_position(movements.handStand33, movements.handStand3Times['3'], 'dummy', True)
		self.robot.goto_position(movements.handStand34, movements.handStand3Times['4'], 'dummy', True)


##################################
###########getUpBack#########
###################################

class getUpBack(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.getUpBack0, movements.getUpBackTimes['0'], 'dummy', True)
		self.robot.goto_position(movements.getUpBack1, movements.getUpBackTimes['1'], 'dummy', True)
		self.robot.goto_position(movements.getUpBack2, movements.getUpBackTimes['2'], 'dummy', True)
		self.robot.goto_position(movements.getUpBack3, movements.getUpBackTimes['3'], 'dummy', True)
		self.robot.goto_position(movements.getUpBack4, movements.getUpBackTimes['4'], 'dummy', True)

##################################
###########prepareWalk#########
###################################

class prepareWalk(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.prepareWalk0, movements.prepareWalkTimes['0'], 'dummy', True)

##################################
###########frontWalkStartL#########
###################################

class frontWalkStartL(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.frontWalkStartL0, movements.frontWalkStartLTimes['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL1, movements.frontWalkStartLTimes['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL2, movements.frontWalkStartLTimes['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL3, movements.frontWalkStartLTimes['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL4, movements.frontWalkStartLTimes['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL5, movements.frontWalkStartLTimes['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL6, movements.frontWalkStartLTimes['6'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL20, movements.frontWalkStartL2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL21, movements.frontWalkStartL2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL22, movements.frontWalkStartL2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL23, movements.frontWalkStartL2Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL24, movements.frontWalkStartL2Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL25, movements.frontWalkStartL2Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL26, movements.frontWalkStartL2Times['6'], 'dummy', True)

##################################
###########frontWalkStartL2#########
###################################

class frontWalkStartL2(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.frontWalkStartL20, movements.frontWalkStartL2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL21, movements.frontWalkStartL2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL22, movements.frontWalkStartL2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL23, movements.frontWalkStartL2Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL24, movements.frontWalkStartL2Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL25, movements.frontWalkStartL2Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartL26, movements.frontWalkStartL2Times['6'], 'dummy', True)

##################################
###########frontWalkStartR1#########
###################################

class frontWalkStartR1(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.frontWalkStartR10, movements.frontWalkStartR1Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR11, movements.frontWalkStartR1Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR12, movements.frontWalkStartR1Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR13, movements.frontWalkStartR1Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR14, movements.frontWalkStartR1Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR15, movements.frontWalkStartR1Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR16, movements.frontWalkStartR1Times['6'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR20, movements.frontWalkStartR2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR21, movements.frontWalkStartR2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR22, movements.frontWalkStartR2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR23, movements.frontWalkStartR2Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR24, movements.frontWalkStartR2Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR25, movements.frontWalkStartR2Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR26, movements.frontWalkStartR2Times['6'], 'dummy', True)

##################################
###########frontWalkStartR2#########
###################################

class frontWalkStartR2(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.frontWalkStartR20, movements.frontWalkStartR2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR21, movements.frontWalkStartR2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR22, movements.frontWalkStartR2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR23, movements.frontWalkStartR2Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR24, movements.frontWalkStartR2Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR25, movements.frontWalkStartR2Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkStartR26, movements.frontWalkStartR2Times['6'], 'dummy', True)

##################################
###########frontWalkMiddleL1#########
###################################

class frontWalkMiddleL1(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.frontWalkMiddleL10, movements.frontWalkMiddleL1Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL11, movements.frontWalkMiddleL1Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL12, movements.frontWalkMiddleL1Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL13, movements.frontWalkMiddleL1Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL14, movements.frontWalkMiddleL1Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL15, movements.frontWalkMiddleL1Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL16, movements.frontWalkMiddleL1Times['6'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL20, movements.frontWalkMiddleL2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL21, movements.frontWalkMiddleL2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL22, movements.frontWalkMiddleL2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL23, movements.frontWalkMiddleL2Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL24, movements.frontWalkMiddleL2Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL25, movements.frontWalkMiddleL2Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL26, movements.frontWalkMiddleL2Times['6'], 'dummy', True)


##################################
###########frontWalkMiddleL2#########
###################################

class frontWalkMiddleL2(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.frontWalkMiddleL20, movements.frontWalkMiddleL2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL21, movements.frontWalkMiddleL2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL22, movements.frontWalkMiddleL2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL23, movements.frontWalkMiddleL2Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL24, movements.frontWalkMiddleL2Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL25, movements.frontWalkMiddleL2Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleL26, movements.frontWalkMiddleL2Times['6'], 'dummy', True)

##################################
###########frontWalkMiddleR1#########
###################################

class frontWalkMiddleR1(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.frontWalkMiddleR10, movements.frontWalkMiddleR1Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR11, movements.frontWalkMiddleR1Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR12, movements.frontWalkMiddleR1Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR13, movements.frontWalkMiddleR1Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR14, movements.frontWalkMiddleR1Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR15, movements.frontWalkMiddleR1Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR16, movements.frontWalkMiddleR1Times['6'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR20, movements.frontWalkMiddleR2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR21, movements.frontWalkMiddleR2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR22, movements.frontWalkMiddleR2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR23, movements.frontWalkMiddleR2Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR24, movements.frontWalkMiddleR2Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR25, movements.frontWalkMiddleR2Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR26, movements.frontWalkMiddleR2Times['6'], 'dummy', True)


##################################
###########frontWalkMiddleR2#########
###################################

class frontWalkMiddleR2(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.frontWalkMiddleR20, movements.frontWalkMiddleR2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR21, movements.frontWalkMiddleR2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR22, movements.frontWalkMiddleR2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR23, movements.frontWalkMiddleR2Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR24, movements.frontWalkMiddleR2Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR25, movements.frontWalkMiddleR2Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkMiddleR26, movements.frontWalkMiddleR2Times['6'], 'dummy', True)

##################################
###########frontWalkEndL1#########
###################################

class frontWalkEndL1(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.frontWalkEndL10, movements.frontWalkEndL1Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL11, movements.frontWalkEndL1Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL12, movements.frontWalkEndL1Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL13, movements.frontWalkEndL1Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL14, movements.frontWalkEndL1Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL15, movements.frontWalkEndL1Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL16, movements.frontWalkEndL1Times['6'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL20, movements.frontWalkEndL2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL21, movements.frontWalkEndL2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL22, movements.frontWalkEndL2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL23, movements.frontWalkEndL2Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL24, movements.frontWalkEndL2Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL25, movements.frontWalkEndL2Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL26, movements.frontWalkEndL2Times['6'], 'dummy', True)

##################################
###########frontWalkEndL2#########
###################################

class frontWalkEndL2(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.frontWalkEndL20, movements.frontWalkEndL2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL21, movements.frontWalkEndL2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL22, movements.frontWalkEndL2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL23, movements.frontWalkEndL2Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL24, movements.frontWalkEndL2Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL25, movements.frontWalkEndL2Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndL26, movements.frontWalkEndL2Times['6'], 'dummy', True)

##################################
###########frontWalkEndR1#########
###################################

class frontWalkEndR1(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.frontWalkEndR10, movements.frontWalkEndR1Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR11, movements.frontWalkEndR1Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR12, movements.frontWalkEndR1Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR13, movements.frontWalkEndR1Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR14, movements.frontWalkEndR1Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR15, movements.frontWalkEndR1Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR16, movements.frontWalkEndR1Times['6'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR20, movements.frontWalkEndR2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR21, movements.frontWalkEndR2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR22, movements.frontWalkEndR2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR23, movements.frontWalkEndR2Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR24, movements.frontWalkEndR2Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR25, movements.frontWalkEndR2Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR26, movements.frontWalkEndR2Times['6'], 'dummy', True)

##################################
###########frontWalkEndR2#########
###################################

class frontWalkEndR2(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.frontWalkEndR20, movements.frontWalkEndR2Times['0'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR21, movements.frontWalkEndR2Times['1'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR22, movements.frontWalkEndR2Times['2'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR23, movements.frontWalkEndR2Times['3'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR24, movements.frontWalkEndR2Times['4'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR25, movements.frontWalkEndR2Times['5'], 'dummy', True)
		self.robot.goto_position(movements.frontWalkEndR26, movements.frontWalkEndR2Times['6'], 'dummy', True)


##################################
###########sit#########
###################################

class sit(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.sit0, movements.sitTimes['0'], 'dummy', True)

##################################
###########lookUp#########
###################################

class lookUp(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.lookUp0, movements.lookUpTimes['0'], 'dummy', True)

##################################
###########listen#########
###################################

class listen(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.listen0, movements.listenTimes['0'], 'dummy', True)

##################################
###########beatChest#########
###################################

class beatChest(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.beatChest0, movements.beatChestTimes['0'], 'dummy', True)
		self.robot.goto_position(movements.beatChest1, movements.beatChestTimes['1'], 'dummy', True)
		self.robot.goto_position(movements.beatChest2, movements.beatChestTimes['2'], 'dummy', True)
		self.robot.goto_position(movements.beatChest3, movements.beatChestTimes['3'], 'dummy', True)
		self.robot.goto_position(movements.beatChest4, movements.beatChestTimes['4'], 'dummy', True)

##################################
###########scratchHead#########
###################################

class scratchHead(pypot.primitive.Primitive):
	def __init__(self, robot):
		self.robot = robot
		pypot.primitive.Primitive.__init__(self, robot)

	def run(self):
		self.robot.goto_position(movements.scratchHead0, movements.scratchHeadTimes['0'], 'dummy', True)
		self.robot.goto_position(movements.scratchHead1, movements.scratchHeadTimes['1'], 'dummy', True)
		self.robot.goto_position(movements.scratchHead2, movements.scratchHeadTimes['2'], 'dummy', True)
		self.robot.goto_position(movements.scratchHead3, movements.scratchHeadTimes['3'], 'dummy', True)
		self.robot.goto_position(movements.scratchHead4, movements.scratchHeadTimes['4'], 'dummy', True)
class bow(pypot.primitive.Primitive):
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

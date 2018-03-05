import time
import pypot.primitive

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
        self.robot.goto_position({'left_hand': 90, 'right_hand': -90}, 1, 'dummy', True)
        print("3")
        #time.sleep(3)
        print("4")

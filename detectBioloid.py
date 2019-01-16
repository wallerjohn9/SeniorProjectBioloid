from pypot.dynamixel import autodetect_robot

my_robot = autodetect_robot()

for m in my_robot.motors:
    m.goal_position = 0.0
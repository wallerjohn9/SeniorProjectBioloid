'''
Created on Jan 21, 2018

@author: codyblack
            Brian McGinnis

            This code is mostly deprecated and its only use at this point is to
            store the dictionary of the Bioloid robot. Most of the orginal
            functions of this class have been moved to bioloid.py and this
            class should probably be deleted and the dictionary moved to a new
            file
'''
import pypot.robot
from time import sleep
import itertools
import numpy
from pypot.primitive.move import MoveRecorder, Move, MovePlayer

class Bot:






    def __init__(self):

        self.robot = pypot.robot.from_config(bot_config, True, False)

    def moveBot(self,frameList):
        #lastFrame = 0
        #timeToWait = 0
        self.robot.compliant= False
        print(self.robot)
        for frame in frameList:
            #timeToWait = .0078125 * (frame)
            motorSpeed = frame[0]
            frames = frame[1]
            timeToWait = .0078125 * frames
            print('Wait time: {}'.format(timeToWait))
            print('Motor speed: {}'.format(motorSpeed) )
            print(frame)
            #print('Wait time: {}'.format(timeToWait))
            #for motor in self.robot.motors:
                #pypot.dynamixel.io.set_moving_speed(motor, motorSpeed)

            self.robot.right_chest.goal_position = frame[2]
            #sleep(.01)
            self.robot.left_chest.goal_position = frame[3]
            #sleep(.01)
            self.robot.right_shoulder.goal_position = frame[4]
            #sleep(.01)
            self.robot.left_shoulder.goal_position = frame[5]
            #sleep(.01)
            self.robot.right_hand.goal_position = frame[6]
            #sleep(.01)
            self.robot.left_hand.goal_position = frame[7]
            #sleep(.01)
            self.robot.right_ab.goal_position = frame[8]
            #sleep(.01)
            self.robot.left_ab.goal_position = frame[9]
            #sleep(.01)
            self.robot.right_ass.goal_position = frame[10]
            #sleep(.01)
            self.robot.left_rear.goal_position = frame[11]
            #sleep(.01)
            self.robot.right_hip.goal_position = frame[12]
            #sleep(.01)
            self.robot.left_hip.goal_position = frame[13]
            #sleep(.01)
            self.robot.right_knee.goal_position = frame[14]
            #sleep(.01)
            self.robot.left_knee.goal_position = frame[15]
            #sleep(.01)
            self.robot.right_ankle.goal_position = frame[16]
            #sleep(.01)
            self.robot.left_ankle.goal_position = frame[17]
            #sleep(.01)
            self.robot.right_foot.goal_position = frame[18]
            #sleep(.01)
            self.robot.left_foot.goal_position = frame[19]
            sleep(2)


            #self.robot.__ge__(MOTOR_IDS[1]).goal_position = frame[1]
            #self.robot.self.MOTOR_IDS[1].goal_position = frame[1]
            self.robot.close()






bot_config = {
        'controllers':{
            'my_dxl_controller': {
                'port': '/dev/ttyACM0',
                'sync_read': True,
                'protocol' : 1,
                'attached_motors': ['chest', 'legs', 'arms'],
            }
        },
        'motorgroups': {
            'arms': ['left_arm','right_arm'],
            'chest': ['left_chest','right_chest','left_ab','right_ab'],
            'legs': ['left_leg','right_leg'],
            'left_arm': ['left_hand','left_shoulder'],
            'right_arm': ['right_hand','right_shoulder'],
            'left_leg': ['left_hip','left_rear','left_knee','left_foot','left_ankle'],
            'right_leg': ['right_hip','right_rear','right_knee','right_foot','right_ankle']
        },

        'motors': {

            'left_hand': {
                'id': 6,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-180.0,180.0]
                },
            'right_hand': {
                'id': 5,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-180.0,180.0]
            },
            'left_shoulder': {
                'id': 4,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
            },
            'right_shoulder': {
                'id': 3,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
            },
               'left_chest': {
                'id': 2,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
            },
            'right_chest': {
                'id': 1,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
            },
            'left_ab': {
                'id': 8,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0],
                },
            'right_ab': {
                'id': 7,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
                },
            'left_hip': {
                'id': 12,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-180.0,180.0]
                },
            'right_hip': {
                'id': 11,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-180.0,180.0]
                },
            'left_rear': {
                'id': 10,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
                },
            'right_rear': {
                'id': 9,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
                },
            'left_knee': {
                'id': 14,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-180.0,180.0]
                },
            'right_knee': {
                'id': 13,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-180.0,180.0]
                },
            'left_ankle': {
                'id': 16,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-180.0,180.0]
                },
            'right_ankle': {
                'id': 15,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-180.0,180.0]
                },
            'left_foot': {
                'id': 18,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
                },
            'right_foot': {
                'id': 17,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
            }
        }
}

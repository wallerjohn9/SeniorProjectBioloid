'''
Created on Jan 21, 2018

@author: codyblack
'''
import pypot.robot
from time import sleep
from pypot.primitive.move import MoveRecorder, Move, MovePlayer

class Bot:
    

    
   


    def __init__(self):
        
    
        self.robot = pypot.robot.from_config(bot_config)
        
        """move_recorder = MoveRecorder(self.robot, 50, self.robot.arms)
        self.robot.compliant = True;
        print("start")
        move_recorder.start()
        sleep(5)
        move_recorder.stop()
        
        with open('fuck.move','w') as f:
            move_recorder.move.save(f)
            print('saved')
        
        sleep(2)
        
        with open('fuck.move') as f:
            mov = Move.load(f)
        
        self.robot.compliant = False;
        
        move_player = MovePlayer(self.robot, mov)
        move_player.start()
        
        sleep(5)
    """
        '''
        for m in self.robot.motors:
            #print(m.present_position)
            m.compliant = False
            m.goal_position = 0.0
            
            print(m.id)
            print(m.goal_position)
            print(m.present_position)
            #time.sleep(1)
            
            #print('shitklfsd')
            
        for m in self.robot.legs:
            m.compliant = False
            m.goal_position = 0.0
            print(m.id)
        for m in self.robot.arms:
            m.compliant = False
            m.goal_position = 0.0
            #print(m.present_position)
        time.sleep(1)
        for i in range(0,10):
            self.robot.left_ab.compliant = False
            self.robot.right_ab.compliant = False
            self.robot.left_ab.goal_position = -10.0
            self.robot.right_ab.goal_position = -10.0
            for m in self.robot.arms:
                m.compliant
                pos = (i*10)
                m.goal_position = pos
            for m in self.robot.legs:
                m.compliant = False
                m.goal_position = 0.0
                #print(m.id)
                #print(m.present_position)
                #time.sleep(1)
            time.sleep(.25)
            self.robot.left_ab.compliant = False
            self.robot.right_ab.compliant = False
            self.robot.left_ab.goal_position = 10.0
            self.robot.right_ab.goal_position = 10.0
            time.sleep(.25)
            
        for i in range(10,0):
            self.robot.left_ab.compliant = False
            self.robot.right_ab.compliant = False
            self.robot.left_ab.goal_position = -10.0
            self.robot.right_ab.goal_position = -10.0
            for m in self.robot.arms:
                m.compliant
                pos = (i*10)
                m.goal_position = pos
            for m in self.robot.legs:
                m.compliant = False
                m.goal_position = 0.0
                #print(m.id)
                #print(m.present_position)
                #time.sleep(1)
            time.sleep(.25)
            self.robot.left_ab.compliant = False
            self.robot.right_ab.compliant = False
            self.robot.left_ab.goal_position = 10.0
            self.robot.right_ab.goal_position = 10.0
            time.sleep(.25)
        self.robot.close()
        
    def move(self,motors,positions):
        pass
        motors is an array of motors for desired movement.
           positions is an array of desired angles to be matched with each motor.
        
        posIndex = 0
        
        if len(motors) != len(positions):
            raise Exception('Need a position angle for each motor')  
        for m in motors:
            #print("moving motor " + m + " to " +positions[posIndex]+ " degrees.")
            if m == 'left_hand':
                print(self.robot.left_hand.present_position)
                self.robot.compliant = False
                self.robot.left_hand.goal_position = positions[posIndex]
                print(self.robot.left_hand.goal_position)
                print(self.robot.left_hand.present_position)
                sleep(.1)
            elif m == 'right_hand':
                print(self.robot.right_hand.present_position)
                self.robot.compliant = False
                self.robot.right_hand.goal_position = positions[posIndex]
                print(self.robot.right_hand.goal_position)
                print(self.robot.right_hand.present_position)
                sleep(.1)
                
            posIndex+=1
        sleep(.25)
        self.robot.close()   
        '''
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
            for motor in self.robot.motors:
                motor.goal_speed = motorSpeed
            self.robot.right_titty.goal_position = frame[2]
            #sleep(.01)
            self.robot.left_titty.goal_position = frame[3]
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
            self.robot.left_ass.goal_position = frame[11]
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
            sleep(timeToWait)
            
            
            #self.robot.__ge__(MOTOR_IDS[1]).goal_position = frame[1]
            #self.robot.self.MOTOR_IDS[1].goal_position = frame[1]
            
            
                
                
                
  
        
bot_config = {
        'controllers':{
            'my_dxl_controller': {
                'port': '/dev/tty.usbmodem1421',
                'sync_read': True,
                'protocol' : 1,
                'attached_motors': ['chest', 'legs', 'arms'],
            }
        },
        'motorgroups': {
            'arms': ['left_arm','right_arm'],
            'chest': ['left_titty','right_titty','left_ab','right_ab'],
            'legs': ['left_leg','right_leg'],
            'left_arm': ['left_hand','left_shoulder'],
            'right_arm': ['right_hand','right_shoulder'],
            'left_leg': ['left_hip','left_ass','left_knee','left_foot','left_ankle'],
            'right_leg': ['right_hip','right_ass','right_knee','right_foot','right_ankle']
        },
    
        'motors': {
        
            'left_hand': {
                'id': 6,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
                },
            'right_hand': {
                'id': 5,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
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
               'left_titty': {
                'id': 2,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
            },
            'right_titty': {
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
                'angle_limit': [-90.0,90.0]
                },
            'right_hip': {
                'id': 11,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
                },
            'left_ass': {
                'id': 10,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
                },
            'right_ass': {
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
                'angle_limit': [-90.0,90.0]
                },
            'right_knee': {
                'id': 13,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
                },
            'left_ankle': {
                'id': 16,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
                },
            'right_ankle': {
                'id': 15,
                'type': 'AX-12',
                'orientation': 'direct',
                'offset': 0.0,
                'angle_limit': [-90.0,90.0]
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
         

<<<<<<< HEAD

import pypot and other pypot stuff or what ever
from time import sleep

class playMovement:

    #half braindead at the moment so this is fun since I jottign this don as I go
    #will take in a series of positons for the robot to play and so so accordingly
    #These should be placed in a 2D Matrix or some  idk python is
    #weird with this  where the col are a series of positions
    #For each motor 1-18 and the rows are each pose it needs to make in order
    #to complete the movement.
    #going by stuff found in the movement software each second runs 128 frames.er
    #So I am playing wiht it.
    #Each frame lasts .0078125 Seconds
    #First thing in each position is the frame.
    # Not real code currently. 
    def playMovement(self, moves):
        i = 0
        j = 0
        lastFrame = 0
        timeToWait = 0
        for move in moves:
            timeToWait = .0078125 * (move[0]-lastFrame)
            lastFrame = move[0]
            motor1.GoalPosition(move[1])
            .....
            motor18.GoalPosition(move[18])

            sleep(timeToWait)



"""
Example pulled from the Robotosis think of each line as an row in the 2D Matrix
The frame is the end frame for the thing.
        <step frame="37" pose="-51.86 51.56 -68.26 67.97 -14.65 14.36 -46.58 46.29 -1.17 0.88 -48.34 48.05 -67.38 67.09 30.76 -31.05 -1.17 0.88" />
        <step frame="99" pose="-65.62 65.33 -67.97 67.68 -89.65 89.36 -46.58 46.29 -1.17 0.88 -48.34 48.05 -67.38 67.09 30.76 -31.05 -1.17 0.88" />
        <step frame="224" pose="-8.5 8.2 -67.97 67.68 -89.65 89.36 -46.58 46.29 -1.17 0.88 -121.58 121.29 -67.38 67.09 10.25 -10.55 -1.17 0.88" />
        <step frame="286" pose="-8.5 8.2 -67.97 67.68 -89.65 89.36 -46.58 46.29 -1.17 0.88 -121.58 121.29 -67.38 67.09 10.25 -10.55 -1.17 0.88" />
        <step frame="411" pose="-65.62 65.33 -67.97 67.68 -89.65 89.36 -46.58 46.29 -1.17 0.88 -48.34 48.05 -67.38 67.09 30.76 -31.05 -1.17 0.88" />
        <step frame="448" pose="-51.86 51.56 -68.26 67.97 -14.65 14.36 -46.58 46.29 -1.17 0.88 -48.34 48.05 -67.38 67.09 30.76 -31.05 -1.17 0.88" />
        <step frame="498" pose="-81.15 80.86 -68.26 67.97 -14.65 14.36 -45.12 45.12 -1.46 1.17 -50.1 49.8 -79.69 79.39 39.55 -39.84 -1.46 1.17" />


"""
=======

import pypot and other pypot stuff or what ever
from time import sleep

class playMovement:

    #half braindead at the moment so this is fun since I jottign this don as I go
    #will take in a series of positons for the robot to play and so so accordingly
    #These should be placed in a 2D Matrix or some  idk python is
    #weird with this  where the col are a series of positions
    #For each motor 1-18 and the rows are each pose it needs to make in order
    #to complete the movement.
    #going by stuff found in the movement software each second runs 128 frames.er
    #So I am playing wiht it.
    #Each frame lasts .0078125 Seconds
    #First thing in each position is the frame.
    # Not real code currently. 
    def playMovement(self, moves):
        i = 0
        j = 0
        lastFrame = 0
        timeToWait = 0
        for move in moves:
            timeToWait = .0078125 * (move[0]-lastFrame)
            lastFrame = move[0]
            motor1.GoalPosition(move[1])
            .....
            motor18.GoalPosition(move[18])

            sleep(timeToWait)



"""
Example pulled from the Robotosis think of each line as an row in the 2D Matrix
The frame is the end frame for the thing.
        <step frame="37" pose="-51.86 51.56 -68.26 67.97 -14.65 14.36 -46.58 46.29 -1.17 0.88 -48.34 48.05 -67.38 67.09 30.76 -31.05 -1.17 0.88" />
        <step frame="99" pose="-65.62 65.33 -67.97 67.68 -89.65 89.36 -46.58 46.29 -1.17 0.88 -48.34 48.05 -67.38 67.09 30.76 -31.05 -1.17 0.88" />
        <step frame="224" pose="-8.5 8.2 -67.97 67.68 -89.65 89.36 -46.58 46.29 -1.17 0.88 -121.58 121.29 -67.38 67.09 10.25 -10.55 -1.17 0.88" />
        <step frame="286" pose="-8.5 8.2 -67.97 67.68 -89.65 89.36 -46.58 46.29 -1.17 0.88 -121.58 121.29 -67.38 67.09 10.25 -10.55 -1.17 0.88" />
        <step frame="411" pose="-65.62 65.33 -67.97 67.68 -89.65 89.36 -46.58 46.29 -1.17 0.88 -48.34 48.05 -67.38 67.09 30.76 -31.05 -1.17 0.88" />
        <step frame="448" pose="-51.86 51.56 -68.26 67.97 -14.65 14.36 -46.58 46.29 -1.17 0.88 -48.34 48.05 -67.38 67.09 30.76 -31.05 -1.17 0.88" />
        <step frame="498" pose="-81.15 80.86 -68.26 67.97 -14.65 14.36 -45.12 45.12 -1.46 1.17 -50.1 49.8 -79.69 79.39 39.55 -39.84 -1.46 1.17" />


"""
>>>>>>> 1b6c8bfbf99f68645b5ea43885ee593dadd473eb

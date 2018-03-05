'''
Created on Jan 21, 2018

@author: codyblack
'''
import time
import movements
import pypot.robot
import primitives
import botSetup

def main():
    print('Configuring bioloid...')
    #bioloid = Bot()
    bioloid = pypot.robot.from_config(botSetup.bot_config)
    bioloid.start_sync()
    print('Configuration complete...\n')
    print('Bioloid:\n')
    print(bioloid)
    dance = primitives.DancePrimitive(bioloid)
    print('dance start')
    dance.start()
    print('dance end')

    dance.wait_to_stop()
    print("Stopped")
    #time.sleep(10)


    #frameList1= []
    #angleList1 = [0,-81.15, 80.86, -68.26, 67.97, -14.65, 14.36, -45.12, 45.12, -1.46, 1.17, -50.1, 49.8, -79.69, 79.39, 39.55, -39.84, -1.46, 1.17]
    #frameList1.append(angleList1)
    #bioloid.moveBot(movements.startPos())
    #print('start position complete, preparing to bow')
    #time.sleep(2)
    #bioloid.moveBot(movements.bow())
    print('Terminating sequence')


if __name__ == '__main__':
    main()

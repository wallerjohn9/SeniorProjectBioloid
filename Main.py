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

    # Primitives code block
    idlePosition = primitives.StartPosPrimitive(bioloid)
    redeem = primitives.Redeemer(bioloid)
    dance = primitives.DancePrimitive1(bioloid)
    bow = primitives.Bow(bioloid)


    #idlePosition.start()
    #idlePosition.wait_to_stop()

    bioloid.compliant = False
    idlePosition.start()
    idlePosition.wait_to_stop()
    time.sleep(3)
    bow.start()
    bow.wait_to_stop()
    """
    print('dance start')
    dance.start()
    print('dance end')

    dance.wait_to_stop()
    print("Stopped")
        #time.sleep(10)
   i = 0
   while(i < 3):
        i += 1
        idlePosition.start()
        idlePosition.wait_to_stop()
        time.sleep(2)
        redeem.start()
        redeem.wait_to_stop()
        time.sleep(2)

    idlePosition.stop()
    dance.stop()
    """
    bioloid.compliant = True
    bow.stop()
    idlePosition.stop()
    bioloid.stop_sync()
    bioloid.close()
    print('Terminating sequence')


if __name__ == '__main__':
    main()

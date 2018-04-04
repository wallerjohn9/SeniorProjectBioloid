from __future__ import print_function
import JSONfrom os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3

import picamera
#sudo apt-get update
#sudo apt-get install python-picamera

class VisualRecognition:

    def __init__():
        self.camera = picamera.PiCamera()
        self.camera.hflip = True
        self.camera.vflip = True

    '''
        Will check and see if there is motion.
        Stays in this while loop until there is motion and then returns true
    '''
    def motionDetection():

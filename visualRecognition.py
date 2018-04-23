from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3
import configparser

from picamera import PiCamera
#sudo apt-get update
#sudo apt-get install python-picamera
#will ned CV2
#will need imutils
class VisualRecognition:



    def __init__(self):
        # configuration block for visual recognition API key.
        config = configparser.ConfigParser()
        config.read('/home/pi/SeniorProjectBioloid/config.cfg')
        key = config.get('Bioloid Credentials','visualApi')

        self.cam = PiCamera()
        self.resources = '/home/pi/SeniorProjectBioloid/resources/'
        self.visualRec = VisualRecognitionV3('2016-05-20', api_key = key)


    def viewObjects(self):
        filePath = self.resources + 'tmp.jpg'
        seenObjects = []
        whatToSay = "I am pretty sure I see a"
        i = 0;
        res = {}
        self.cam.capture(filePath)
        classifier_id = 'default'
        with open(filePath, 'rb') as images_file:
            parameters = json.dumps({'threshold': 0.1, 'classifier_ids': [classifier_id, 'default']})
            results = self.visualRec.classify(images_file=images_file)

            #print(json.dumps(results))
            json.dumps(results, res)
        #iterate over the JSON file and find out how many are Object that are recognized.

        #print(res)
        print(results)
        for obj in results['images'][0]['classifiers'][0]['classes']:
            print(obj)
            print(obj['score'])
            if obj['score'] >= .6:
                seenObjects.append(obj['class'])
                print(seenObjects[i])
                i += 1

        for sObj in seenObjects:
            if sObj == (seenObjects[i-1]):
                whatToSay += " and Lastly I see a " + sObj
            else:

                whatToSay += " a " + sObj

        print(whatToSay)

        return whatToSay


    '''

    {"custom_classes": 0, "images":
        [{"classifiers":
            [{"classes":
                [{"score": 0.658, "type_hierarchy": "/furniture/table/kitchen table", "class": "kitchen table"},
                    {"score": 0.658, "class": "table"},
                    {"score": 0.739, "class": "furniture"},
                    {"score": 0.561, "class": "space heater"},
                    {"score": 0.521, "class": "corner"},
                    {"score": 0.5, "class": "stove"},
                    {"score": 0.6, "class": "heater"},
                    {"score": 0.599, "class": "indoors"},
                    {"score": 0.724, "class": "dark red color"},
                    {"score": 0.678, "class": "reddish orange color"}],
                "classifier_id": "default", "name": "default"}],
            "image": "/home/pi/SeniorProjectBioloid/resources/tmp.jpg"}],
        "images_processed": 1}

    '''

    def viewFaces(self):
        filePath = self.resources + 'tmp.jpg'
        whatToSay = "Pretty sure I see a "
        gender = ''
        ageMax = 99
        ageMin = 0
        self.cam.capture(filePath)
        classifier_id = 'default'
        with open(filePath, 'rb') as images_file:
            parameters = json.dumps({'threshold': 0.1, 'classifier_ids': [classifier_id, 'default']})
            face = self.visualRec.detect_faces(images_file=images_file)
            print(json.dumps(face))

        for f in face['images'][0]['faces']:
            gender = f['gender']['gender']
            ageMax = f['age']['max']
            ageMin = f['age']['min']
            whatToSay += gender + " between the ages of " + str(ageMin) + " and " + str(ageMax)

        return whatToSay
    '''
    {"images_processed": 1, "images": [{"faces": [{"face_location": {"height": 150, "left": 231, "top": 90, "width": 148} , "gender": {"gender": "MALE", "score": 0.9866701}, "age": {"min": 18, "max": 21, "score": 0.895782}}], "image": "/ho
    '''
    '''
        Will check and see if there is motion.
        Stays in this while loop until there is motion and then returns true
        Credit to adrian@pyimagesearch.com for this code
    ''
    def motionDetection(self):
        camera = cv2.VideoCapture(0)
        time.sleep(0.25)

        # loop over the frames of the video
        while True:
    	# grab the current frame and initialize the occupied/unoccupied
    	# text
    	(grabbed, frame) = camera.read()
    	text = "Unoccupied"

    	# if the frame could not be grabbed, then we have reached the end
    	# of the video
    	if not grabbed:
    		break

    	# resize the frame, convert it to grayscale, and blur it
    	frame = imutils.resize(frame, width=500)
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	gray = cv2.GaussianBlur(gray, (21, 21), 0)

    	# if the first frame is None, initialize it
    	if firstFrame is None:
    		firstFrame = gray
    		continue

    	# compute the absolute difference between the current frame and
    	# first frame
    	frameDelta = cv2.absdiff(firstFrame, gray)
    	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    	# dilate the thresholded image to fill in holes, then find contours
    	# on thresholded image
    	thresh = cv2.dilate(thresh, None, iterations=2)
    	(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    		cv2.CHAIN_APPROX_SIMPLE)

    	# loop over the contours
    	for c in cnts:
    		# if the contour is too small, ignore it
    		if cv2.contourArea(c) < args["min_area"]:
    			continue

    		# compute the bounding box for the contour, draw it on the frame,
    		# and update the text
    		(x, y, w, h) = cv2.boundingRect(c)
    		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    		text = "Occupied"

    	# draw the text and timestamp on the frame
    	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
    		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
    		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    	# show the frame and record if the user presses a key
    	cv2.imshow("Security Feed", frame)
    	cv2.imshow("Thresh", thresh)
    	cv2.imshow("Frame Delta", frameDelta)
    	key = cv2.waitKey(1) & 0xFF

    	# if the `q` key is pressed, break from the lop
    	if key == ord("q"):
    		break
        '''

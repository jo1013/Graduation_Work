import cv2
import numpy as np
import os
import requests
import time

def recognition():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascades/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX

    #iniciate id counter
    id = 0

    # names related to ids: example ==> loze: id=1,  etc
    names = ['None', 'HanSung', 'JungHoo', 'SangMo', 'SeungHun','SangJun','SangIn']

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture("http://192.168.0.102:8080/?action=stream")
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    chkCount = 0

    while True:
        
        ret, img =cam.read()
        #img = cv2.flip(img, -1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
            )

        for(x,y,w,h) in faces:
            chkCount
            chkCount+=1

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                id = names[id]
                #confidence = "  {0}%".format(round(100 - confidence))
                confidence = round(100 - confidence)
            else:
                id = "unknown"
                #confidence = "  {0}%".format(round(100 - confidence))
                confidence = round(100 - confidence)
                
            #if(confidence<=70):
            #    url = "http://192.168.43.30:3000/api/com/intruders"
            #    params = {'param': confidence }
            #    res = requests.get(url, params=params)
                
            #cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            #cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
            print("\n " + id +" confidence : "+ str(confidence))
            
            #print(chkCount)
            if (chkCount == 30):
                #request
                print(chkCount)
                if(int(confidence)<=50):
                    print("h")
                    url = "http://192.168.0.103:3000/api/com/intruduers"
                    params = {'param': confidence }
                    res = requests.get(url, params=params)
                chkCount = 0
            
        #cv2.imshow('camera',img) 
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
    return

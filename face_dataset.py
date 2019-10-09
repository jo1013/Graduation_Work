import cv2
import os

def makeDataset(name):
    cam = cv2.VideoCapture("http://113.198.84.22:8080/?action=stream")
    cam.set(3, 480) # set video width
    cam.set(4, 320) # set video height
    face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

    # For each person, enter one numeric face id
    #face_id = input('\n enter user id end press <return> ==>  ')
    #print("\n [INFO] Initializing face capture. Look the camera and wait ...")


    face_id = name



    # Initialize individual sampling face count
    count = 0
    path, dirs, files = next(os.walk("dataset"))

    for file in files:
        if "User."+face_id in file:
            count += 1
        
    chkCnt = count


    while(True):
       
        ret, img = cam.read()
     
        #img = cv2.flip(img, -1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            #cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >=  chkCnt+10: # Take 30 face sample and stop video
             break
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
    return

#makeDataset("1")


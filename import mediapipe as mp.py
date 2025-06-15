import threading 

import cv2 as cv
from deepface import DeepFace

cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_WIDTH,680)
cap.set(cv.CAP_PROP_FRAME_WIDTH,459)

counter=0

face_match = False

refrence_img=cv.imread("pic")

def check_face(Frame):
    global face_match
    try:
        if DeepFace.verify([frame,refrence_img.copy()])['verfied']:
            face_match = True 
        else:
            face_match = False
    except ValueError:
        pass

while True:
    ret,frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face,args=(frame.copy(),)).start()
            except ValueError:
                pass
            counter += 1

        if face_match:
            cv.putText(frame,"MATCH!",(20,450),cv.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)   
        else:
            cv.putText(frame," NO MATCH!",(20,450),cv.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        
        cv.imshow('video',frame)

    key = cv.waitkey(1)
    if key == ord('q'):
        break

cv.destroyAllWindows()




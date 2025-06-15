import cv2 as cv
import mediapipe as mp

mp_hands= mp.solutions.hands
hands = mp_hands.Hands()
cap= cv.VideoCapture(0)

if not cap.isOpened():
    print("cannot open camera")
    exit()

while True:
    ret,frame = cap.read()
    if not ret:
        print("failed")
        break

    frame_rgb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    hand_process = hands.process(frame_rgb)

    if hand_process.multi_hand_landmarks:
        for hand_landmarks in hand_landmarks.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame,hand_landmarks,mp_hands.HANDS_CONNECTION)
            
            cv.imshow('hand tracking', frame)

            if cv.waitKey(1) == ord('q'):
                break

cap.release()
cv.destroyAllWindows()

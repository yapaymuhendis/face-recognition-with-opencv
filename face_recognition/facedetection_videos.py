import face_recognition
import cv2

# Since some of the codes are the same, all the details are written in the facedetection.py file.

path = "videos/testvideo.mp4"
cap = cv2.VideoCapture(path)
color = (0,255,0)

while True:

    ret,frame = cap.read()
    faceLocations = face_recognition.face_locations(frame)
    

    for index, faceloc in enumerate(faceLocations):

        topleftY,bottomrightX,bottomrightY,topleftX = faceloc
        pt1 = (topleftX,topleftY)
        pt2 = (bottomrightX,bottomrightY)

        cv2.rectangle(frame, pt1, pt2, color)

    cv2.imshow("test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()    

import face_recognition
import cv2

cap = cv2.VideoCapture(0)
color = (0,255,0)

while True:

    ret,frame = cap.read()
    frame = cv2.flip(frame,1) 
    
    faceLocations = face_recognition.face_locations(frame)


    for index, faceloc in enumerate(faceLocations):

        topleftY,bottomrightX,bottomrightY,topleftX = faceloc
        pt1 = (topleftX,topleftY)
        pt2 = (bottomrightX,bottomrightY)

        cv2.putText(frame, text='cagan', org=(topleftX,topleftY),
            fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255,185,15),
            thickness=1, lineType=cv2.LINE_AA)

        cv2.rectangle(frame, pt1, pt2, color)

    cv2.imshow("test", frame)

    # q'ya bastığımda pencereyi kapat diyorum.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
import face_recognition
import cv2

path = ("images/testimage.jpeg")
image = cv2.imread(path)

faceLocations = face_recognition.face_locations(image)
# I am using the face_recognition library to detect faces in the image.

color = (0,255,0)
# I'm setting the color of the rectangle

for index, faceloc in enumerate(faceLocations):
    # The enumerate() method adds a counter to an iterable and returns it.

    topleftY,bottomrightX,bottomrightY,topleftX = faceloc
    pt1 = (topleftX,topleftY)
    pt2 = (bottomrightX,bottomrightY)
    #I want it to determine its coordinates to throw a rectangle on the detected face, so I use it like this after I define the 4 places.
    
    cv2.rectangle(image, pt1, pt2, color)
    # Draw a rectangle wherever you want.

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    # It stops working when I press the q key.    

cv2.imshow("test", image)
cv2.waitKey(0)

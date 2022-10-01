import face_recognition
import cv2

path = ("/Users/42cagan/Desktop/face_recognition/images/testimage.jpeg")
image = cv2.imread(path)

faceLocations = face_recognition.face_locations(image)
color = (0,255,0)

# for döngüsüne alıp enumerate fonksiyonu kullanmamdaki amaç
# yüzleri otomatik olarak kendisi bulsun diye. pt1 ve pt2'ye koordinatları söyleyip
# cv2.rectangle'a giriyorum. kendisi buluyor döngü ile.
for index, faceloc in enumerate(faceLocations):

    topleftY,bottomrightX,bottomrightY,topleftX = faceloc
    pt1 = (topleftX,topleftY)
    pt2 = (bottomrightX,bottomrightY)

    cv2.rectangle(image, pt1, pt2, color)
    # Dikdörtgen çizer istediğin yere.

    # q'ya bastığımda pencereyi kapat diyorum.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.imshow("test", image)
cv2.waitKey(0)

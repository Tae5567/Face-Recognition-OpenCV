# Using Open CV
# Detecting faces in images
import sys
import cv2


def face_detect(imgpath, nogui = False, cascadepath = "haarcascade_frontalface_default.xml"):

    image = cv2.imread(imgpath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cascadepath)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.4, # adjust scale factor if face not detected properly, adjust based on distance to camera
        minNeighbors = 5,
        minSize = (30,30)

        )

    print("The number of faces found = ", len(faces))

    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+h, y+h), (0, 255, 0), 2)

    if nogui:
        cv2.imwrite('concert.jpg', image)
        return len(faces)
    else:
        cv2.imshow("Faces found", image)
        cv2.waitKey(0)

if __name__ == "__main__":
    face_detect(sys.argv[1]) #test with different images

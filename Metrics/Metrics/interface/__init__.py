import cv2
import numpy

def DisplayImage(image, name):
    cv2.imshow(name, image)
    inputKey = cv2.waitKey(0)
    if inputKey == 27: # ESC key
        cv2.destroyWindow(name)

def DisplayEditableImage(image, name):
    editableImage = image
    cv2.namedWindow(name)
    editableImage = image
    cv2.setMouseCallback(name, DrawDot, [image, name])
    DisplayImage(image, name)

def DrawDot(event, x, y, flags, parameters):
    image = parameters[0]
    name = parameters[1]
    if event == cv2.EVENT_LBUTTONDOWN:
        newImage = cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
        DisplayEditableImage(newImage, name)
import cv2
import numpy

def LoadImage(path):
    loadedImage = cv2.imread(path, 0)
    return loadedImage
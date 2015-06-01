import cv2
import numpy
from PIL import Image

def LoadImage(path):
    pilImage = Image.open(path)
    npImage = numpy.array(pilImage)
    loadedImage = cv2.cvtColor(npImage, cv2.COLOR_RGB2BGR)
    return loadedImage
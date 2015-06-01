import loading
import interface

if __name__ == "__main__":
    imagePath = 'data//jumpingjacks.0001.png'
    loadedImage = loading.LoadImage(imagePath)
    interface.DisplayEditableImage(loadedImage, imagePath)
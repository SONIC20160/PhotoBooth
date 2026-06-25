from PIL import Image
import time
import cv2

def take_photo(index):
    x = 189 #~5cm
    y = 189 #~5cm
    size = [x,y]
    path = "PhotoBoothBack/Photos/"

    camera = cv2.VideoCapture(0)
    
    time.sleep(5)
    ret, frame = camera.read()
    if ret: 
        cv2.imwrite(f"{path}{index+1}.jpg", frame)
        image = Image.open(f"{path}{index+1}.jpg")
        image = image.resize(size)
        return image
    else:
        print("Failed to capture image")
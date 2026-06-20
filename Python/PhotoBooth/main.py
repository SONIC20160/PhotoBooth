from PIL import Image, ImageFilter, ImageEnhance
import cv2
import numpy as np
import time

def apply_filter(img , filter):
    if filter:
        return img.convert("L")
    else:
        img = img.convert("RGB")
        img = ImageEnhance.Color(img).enhance(0.4)      # desaturate
        img = ImageEnhance.Contrast(img).enhance(1.2)   # bump contrast
        r, g, b = img.split()
        r = r.point(lambda i: min(255, i + 30))        # warm red channel
        b = b.point(lambda i: max(0, i - 20))          # cool blue channel
        return Image.merge("RGB", (r, g, b))

def take_photo(i):
    time.sleep(5)
    ret, frame = cam.read()
    if ret: 
        cv2.imwrite(f"C:/Users/uriel/Pictures/Screenshots/{i+1}.jpg", frame)
        img = Image.open(f"C:/Users/uriel/Pictures/Screenshots/{i+1}.jpg")
        img = img.resize(size)
        return img
    else:
        print("Failed to capture image")

x = 189 #~5cm
y = 189 #~5cm
size = [x,y]

cam = cv2.VideoCapture(0)

cant = 1
filter_1 = False
if cant == 2:
    filter_2 = False
    tier_2 = list()
tier_1 = list()
payment = True

if payment:
        
    for i in range(5):    
        
        img = take_photo(i)
            
        if cant == 2:
            img_2 = img
            img_2 = apply_filter(img_2, filter_2)
            tier_2.append(img_2)
                
        img = apply_filter(img, filter_1)
        tier_1.append(img)
    
        take_again = True
    
        if take_again:
            take_photo(i)
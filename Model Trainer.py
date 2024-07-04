import cv2
import numpy as np
from PIL import Image
import os
print(cv2.__version__)
path = r'C:\Users\sushr\OneDrive\Pictures\Screenshots\"Screenshot 2023-09-29 234118".png'
recognizer = cv2.face.LBPHFaceRecognizer_create()  # For OpenCV versions 4.0 and above 
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def Images_And_Labels(path): 

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:
        gray_img = Image.open(imagePath).convert('L') 
        img_arr = np.array(gray_img,'uint8') 

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_arr)

        for (x,y,w,h) in faces:
            faceSamples.append(img_arr[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

faces,ids = Images_And_Labels(path)
print(faces)
recognizer.train(faces, np.array(ids))

recognizer.write('trainer/trainer.yml')

print("Done")

import cv2
import os
import numpy as np

# Path to the directory containing training images
training_path = 'training_data'

# Initialize LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the pre-trained Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to load images and corresponding labels from the training dataset
def load_training_data(training_path):
    images = []
    labels = []
    label_id = 0
    label_dict = {}

    for root, dirs, files in os.walk(training_path):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                path = os.path.join(root, file)
                label = os.path.basename(root).lower()
                if label not in label_dict:
                    label_dict[label] = label_id
                    label_id += 1
                label_id = label_dict[label]
                pil_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                numpy_image = np.array(pil_image, 'uint8')
                faces = face_cascade.detectMultiScale(numpy_image)
                for (x, y, w, h) in faces:
                    roi = numpy_image[y:y+h, x:x+w]
                    images.append(roi)
                    labels.append(label_id)
    return images, labels

# Load training data
images, labels = load_training_data(training_path)

# Train the recognizer
recognizer.train(images, np.array(labels))

# Save the trained model
recognizer.save('trained_model.yml')

print("Training complete. Model saved as trained_model.yml")

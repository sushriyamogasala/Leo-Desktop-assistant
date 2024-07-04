import cv2
import pyttsx3

engine = pyttsx3.init()
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)


def speak(audio):
    print(f"{audio}")
    engine.say(audio)
    engine.runAndWait()    


def facerec():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')  # load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach
    font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type
    id = 4  # number of persons you want to Recognize
    names = ['', 'Riya']  # names, leave first empty bcz counter starts from 0

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    i = 0
    while True:

        ret, img = cam.read()

        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(converted_image, 1.2, 5)

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])
            i = i + 1
            if accuracy < 50:
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                cam.release()
                cv2.destroyAllWindows()
                speak("Face verification successful")
                return True


            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
                speak("User authentication failed")
                if i==9:
                    return False

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break


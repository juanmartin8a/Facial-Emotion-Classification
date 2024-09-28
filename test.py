import cv2
import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image

#load model
model = model_from_json(open("modelFR.json", "r").read())
#load weights
model.load_weights('modelFR.h5')


face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


cap=cv2.VideoCapture(0)

while True:
    ret,test_img=cap.read()# captures frame and returns boolean value and captured image
    if not ret:
        continue
    gray_img= cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)


    for (count, (x, y, w, h)) in enumerate(faces_detected):
        color_cycle = ((0, 165, 16), (255, 0, 0), (0, 0, 255), (230, 230, 250))
        color = color_cycle[int(count%len(color_cycle))]
        cv2.rectangle(test_img,(x,y),(x+w,y+h),color,thickness=4)
        roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from  image
        roi_gray=cv2.resize(roi_gray,(48,48))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis = 0)
        img_pixels /= 255

        predictions = model.predict(img_pixels)
        confidence = round(max(predictions[0])*100, 2)

        #find max indexed array
        max_index = np.argmax(predictions[0])

        emotions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
        predicted_emotion = emotions[max_index]

        cv2.putText(test_img, predicted_emotion + ': ' + str(confidence) + ('%'), (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), lineType=cv2.LINE_AA)

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('Facial emotion analysis ',test_img)



    if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows
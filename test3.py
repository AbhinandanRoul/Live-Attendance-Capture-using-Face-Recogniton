import cv2,time,os, face_recognition, streamlit

known_image = face_recognition.load_image_file("C:\\Users\\myp\\Pictures\\Camera Roll\\me.jpg")
original_encoding = face_recognition.face_encodings(known_image)[0]


min=int(input("Enter the duration of the meeting in minutes"))
capture_frequency=10 #Intervals of frame capture
cap = cv2.VideoCapture(0)
i=0
while (cap.isOpened() and i<=min*60/capture_frequency):
    ret, frame = cap.read()
    if ret == False:
        break
    img_path = 'C:\\Users\\myp\\PycharmProjects\\Attendance\\Face_Images_Captured\\unknown' + str(i) + '.jpg'
    cv2.imwrite(img_path, frame)

    image = face_recognition.load_image_file(img_path)
    face_locations = face_recognition.face_locations(image)
    if not face_locations:  # in case no face locations are returned i.e., []
        print("No face detected")
    else:
        unknown_image = face_recognition.load_image_file(img_path)
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces([original_encoding], unknown_encoding)
        print(results)
    i+=1
    time.sleep(capture_frequency) #delays the execution by 10 seconds/makes the thread sleep

cap.release()
cv2.destroyAllWindows()














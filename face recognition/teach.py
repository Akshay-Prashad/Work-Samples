import cv2
import face_recognition

cap = cv2.VideoCapture(0)
while True:
    res, img = cap.read()
    rgbimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgbimg)
    for top, right, bottom, left in face_locations:
        cv2.rectangle(img, (left, top), (right, bottom), (255,0,0), 2)
    cv2.imshow("Face Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.imwrite("Attendance_images/akshay.jpg",img)

cap.release()
cv2.destroyAllWindows()
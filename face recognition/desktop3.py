import cv2
import csv
import pickle
import face_recognition
import pandas as pd
import json
def lastname():
    names = []
    with open("Files/data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            names.append(row)
    return names[-1][0]

def add_face_encoding(name,encoding):
    try:
        with open('face_encodings.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[name] = encoding.tolist()

    with open('face_encodings.json', 'w') as file:
        json.dump(data, file)

def main():
    last_name = lastname()
    path = "Attendance_images"
    enc_list = []

    cam = cv2.VideoCapture(0)

    while True:
        res, img = cam.read()

        if not res:
            break

        cv2.imshow("Webcam", img)
        cv2.imwrite(f"{path}/{last_name}.jpg", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            imgS = cv2.resize(img, (0, 0), None, 0.5, 0.5)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            face_Current_Frame = face_recognition.face_locations(imgS)
            encode_Current_Frame = face_recognition.face_encodings(imgS, face_Current_Frame)[0]
            add_face_encoding(last_name,encode_Current_Frame)
            break

    cam.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()

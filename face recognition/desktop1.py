import cv2
import face_recognition
import os
import numpy as np
import pickle
import json
global name
name="Unknown"


"""def prepare_lists():
    path="Attendance_images"
    images_list=[]
    classnames_list=[]
    mylist=os.listdir(path)


    for cls in mylist:
        curr_img=cv2.imread(f'{path}/{cls}')
        images_list.append(curr_img)
        classnames_list.append(os.path.splitext(cls)[0])
    print(classnames_list)
    return images_list,classnames_list

img_list,cls_list=prepare_lists()

def ENCODINGS(IMAGE):
    img_encodings = []
    for i in IMAGE:
        enc = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
        face_loc = face_recognition.face_locations(enc)
        encode = face_recognition.face_encodings(enc,face_loc)[0]
        img_encodings.append(encode)
    return img_encodings

Lists_known = ENCODINGS(img_list)"""

def open_():
    cls_list = []
    list_ = []
    try:
        with open('face_encodings.json', 'r') as file:
            data = json.load(file)
            for name, encoding in data.items():
                cls_list.append(name)
                list_.append(np.array(encoding))
        return cls_list,list_



    except FileNotFoundError:
        return {}

cls_list , Lists_known = open_()


cap = cv2.VideoCapture(0)

while True:
    res, img = cap.read()

    imgS = cv2.resize(img, (0, 0), None, 0.5, 0.5)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    face_Current_Frame = face_recognition.face_locations(imgS)
    encode_Current_Frame = face_recognition.face_encodings(imgS, face_Current_Frame)
    for encodeFace, faceLoc in zip(encode_Current_Frame, face_Current_Frame):
        matches = face_recognition.compare_faces(Lists_known, encodeFace)
        if True in matches:
            matchIndex = [i for i,x in enumerate(matches) if x ]
            name = cls_list[matchIndex[0]]
        break
    break
print(name)
cap.release()
cv2.destroyAllWindows()







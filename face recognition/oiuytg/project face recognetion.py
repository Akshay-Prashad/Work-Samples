import cv2
import face_recognition
import os
import csv
from datetime import datetime
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import numpy as np

class FaceRecognitionApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Welcome page")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        self.canvas = Canvas(self.root, width=self.width, height=self.height, highlightthickness=0)
        self.canvas.pack()

        self.bg_image = Image.open("img_1.jpg")
        self.bg_resized = self.bg_image.resize((self.width, self.height))
        self.bg_photo = ImageTk.PhotoImage(self.bg_resized)

        self.trans_img2 = Image.open("img.png")
        self.face_resized = self.trans_img2.resize((50, 50))
        self.trans_photo = ImageTk.PhotoImage(self.face_resized)

        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_photo)
        self.canvas.create_text(self.width * 0.5, self.height * 0.5, text="WELCOME TO PROJECT CENTER", font=("Helvetica", 25), fill="white")
        self.canvas.create_image(self.width * 0.5, self.height * 0.1, image=self.trans_photo)

        self.root.after(1000, self.check_face)
        self.root.mainloop()
    def prepare_lists(self):
        path = "Attendance_images"
        images_list = []
        classnames_list = []
        mylist = os.listdir(path)

        for cls in mylist:
            curr_img = cv2.imread(f'{path}/{cls}')
            images_list.append(curr_img)
            classnames_list.append(os.path.splitext(cls)[0])

        return images_list, classnames_list

    def ENCODINGS(self, IMAGE):
        img_encodings = []
        for enc in IMAGE:
            enc = cv2.cvtColor(enc, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(enc)[0]
            img_encodings.append(encode)
        return img_encodings

    def check_function(self, image_list):
        global img_list, cls_list
        cap = cv2.VideoCapture(0)
        name = "Unknown"

        while True:
            ret, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            face_Current_Frame = face_recognition.face_locations(imgS)
            encode_Current_Frame = face_recognition.face_encodings(imgS, face_Current_Frame)

            for encodeFace, _ in zip(encode_Current_Frame, face_Current_Frame):
                matches = face_recognition.compare_faces(image_list, encodeFace)
                faceDis = face_recognition.face_distance(image_list, encodeFace)

                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = cls_list[matchIndex].upper()
            break

        cap.release()
        cv2.destroyAllWindows()
        return name

    def check_face(self):
        global cls_list
        img_list, cls_list = self.prepare_lists()
        Lists_known = self.ENCODINGS(img_list)

        a = self.check_function(Lists_known) 

        if a == "Unknown":
            response = messagebox.askquestion("Face not found", "If not a user, sign up or try again")
            if response == "yes":
                self.root.destroy()
                self.signup()
            else:
                self.root.destroy()
        else:
            self.root.destroy()
            self.window_4()


    def window_4(self):
        window4 = Tk()
        window4.configure(bg="white")
        width = window4.winfo_screenwidth()
        height = window4.winfo_screenheight()
        window4.geometry(str(width) + "x" + str(height))

        fram = Frame(window4, bg="#3f4c6b", height=250)
        fram.pack(fill="both")
        global frame1
        frame1 = Frame(window4, bg="white", height=600)
        frame1.pack(fill="both")

        home_img = Image.open("home.png")
        home_resized = home_img.resize((40, 30))
        img = Image.open("images1.png")
        r_img = img.resize((100, 100))
        img3 = Image.open("images2.png")
        r_img2 = img3.resize((800, 500))

        image = ImageTk.PhotoImage(r_img)
        image2 = ImageTk.PhotoImage(r_img2)
        image3 = ImageTk.PhotoImage(home_resized)

        def home():
            Frame(window4, bg="red", height=600)
            frame1.pack(fill="both")
            global image2
            img3 = Image.open("images2.png")
            r_img2 = img3.resize((800, 500))
            image2 = ImageTk.PhotoImage(r_img2)
            img2_label = Label(image=image2)
            img2_label.place(in_=frame1, relx=0.3, rely=0.1)
            label1.configure(bg="#3f4c6b", fg="#FFFFF0")
            label2.configure(bg="#3f4c6b", fg="#FFFFF0")
            label3.configure(bg="#3f4c6b", fg="#FFFFF0")

        def team():
            frame2 = Frame(window4, bg="white", height=600, width=1550)
            frame2.place(in_=window4, x=0, y=250)
            label1.configure(bg="white", fg="black")
            label2.configure(bg="#3f4c6b", fg="#FFFFF0")
            label3.configure(bg="#3f4c6b", fg="#FFFFF0")

        def about():
            frame2 = Frame(window4, bg="white", height=600, width=1550)
            frame2.place(in_=window4, x=0, y=250)
            label2.configure(bg="white", fg="black")
            label1.configure(bg="#3f4c6b", fg="#FFFFF0")
            label3.configure(bg="#3f4c6b", fg="#FFFFF0")

        def hel():
            frame2 = Frame(window4, bg="white", height=600, width=1550)
            frame2.place(in_=window4, x=0, y=250)
            label3.configure(bg="white", fg="black")
            label1.configure(bg="#3f4c6b", fg="#FFFFF0")
            label2.configure(bg="#3f4c6b", fg="#FFFFF0")

        def prof():
            frame2 = Frame(window4, bg="white", height=600, width=1550)
            frame2.place(in_=window4, x=0, y=250)
            label3.configure(bg="#3f4c6b", fg="#FFFFF0")
            label1.configure(bg="#3f4c6b", fg="#FFFFF0")
            label2.configure(bg="#3f4c6b", fg="#FFFFF0")

        img1 = Button(image=image, text="Profile", font=("times", 15), fg="white", compound=TOP, bg="#3f4c6b", bd=0,
                      activebackground="#3f4c6b",
                      pady=10, cursor="hand2", command=prof)
        img1.place(in_=fram, relx=0.87, rely=0.2)

        label1 = Button(fram, text="Team", font=("times", 20), bg="#3f4c6b", fg="#FFFFF0", bd=0,
                        activebackground="#3f4c6b",
                        padx=10, pady=6, relief=FLAT, cursor="hand2", command=team)
        label2 = Button(fram, text="About", font=("times", 20), bg="#3f4c6b", fg="#FFFFF0", bd=0,
                        activebackground="#3f4c6b",
                        padx=10, pady=6, relief=FLAT, command=about, cursor="hand2")
        label3 = Button(fram, text="Help", font=("times", 20), bg="#3f4c6b", fg="#FFFFF0", bd=0,
                        activebackground="#3f4c6b", padx=14, pady=6, relief=FLAT, cursor="hand2", command=hel)
        home = Button(image=image3, text="Home", compound=TOP, bg="#3f4c6b", fg="white", bd=0,
                      activebackground="#3f4c6b",
                      activeforeground="#FFFFF0"
                      , padx=10, relief=FLAT, cursor="hand2", command=home)

        welcome = Label(text="WELCOME TO PROJECT CENTER", font=("times", 30), bg="#3f4c6b", fg="#FFFFF0")
        img2_label = Label(image=image2)

        home.place(in_=fram, relx=0.01, rely=0.78)
        label1.place(in_=fram, relx=0.05, rely=0.76)
        label2.place(in_=fram, relx=0.12, rely=0.76)
        label3.place(in_=fram, relx=0.19, rely=0.76)
        welcome.place(in_=fram, relx=0.3, rely=0.3)
        img2_label.place(in_=frame1, relx=0.3, rely=0.1)

        window4.mainloop()


    def signup(self):
        def submit_data():
            name = name_entry.get()
            email = email_entry.get()
            phone_number = phone_number_entry.get()

            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS signup_data (name TEXT, email TEXT, phone_number int)")

            with open("data.csv", "a") as csvfile:
                writer = csv.writer(csvfile)
                if not csvfile.tell():
                    writer.writerow(["name", "email", "phone_number"])
                writer.writerow([name, email, phone_number])

            connection.commit()
            connection.close()

            name_entry.delete(0, END)
            email_entry.delete(0, END)
            phone_number_entry.delete(0, END)

            window.destroy()

            capture_image()

        def capture_image():
            window3 = Tk()
            window3.title("Camera Feed")

            width = window3.winfo_screenwidth()
            height = window3.winfo_screenheight()
            window3.geometry(str(width) + "x" + str(height))

            label = Label()
            label.pack()

            cap = cv2.VideoCapture(0)

            def file_name_reader():
                names = []
                with open("data.csv", "r+") as file:
                    reader = csv.reader(file)
                    reader = list(reader)
                    name = []
                    for i in range(0, len(reader), 2):
                        name.append(reader[i])

                    return name[-1][0]

            if not cap.isOpened():
                exit()

            def update_frame():
                a = file_name_reader()
                ret, frame = cap.read()

                if ret:
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    photo = ImageTk.PhotoImage(image=Image.fromarray(rgb_frame))

                    label.photo = photo
                    label.config(image=photo)
                    cv2.imwrite(f"Attendance_images/{a}.jpg", frame)


                label.after(10,update_frame)

            update_frame()

            def quit_app():
                cap.release()
                window3.destroy()
                self.window_4()

            quit_button = Button(window3, text="Confirm", command=quit_app)
            quit_button.pack()

            window3.mainloop()

        window = Tk()
        window.title("Sign Up Form")
        window.configure(background="white")

        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.geometry(str(width) + "x" + str(height))

        tittle_label = Label(text="FILL YOUR DETAILS", fg="white", bg="#3f4c6b", font=('times', 40, ' bold '))
        name_label = Label(text="Name", fg="black", bg="white", font=('times', 15, ' bold '))
        email_label = Label(text="Email ID", fg="black", bg="white", font=('times', 15, ' bold '))
        phone_number_label = Label(text="Contact Number", fg="black", bg="white", font=('times', 15, ' bold '))

        name_entry = Entry(width=25, borderwidth=2)
        email_entry = Entry(width=25, borderwidth=2)
        phone_number_entry = Entry(width=25, borderwidth=2)

        submit_button = Button(text="Submit", width=20, padx=10, pady=10, command=submit_data)

        tittle_label.place(x=500, y=100)
        name_label.place(x=600, y=250)
        name_entry.place(x=770, y=255)
        email_label.place(x=600, y=300)
        email_entry.place(x=770, y=305)
        phone_number_label.place(x=600, y=350)
        phone_number_entry.place(x=770, y=355)
        submit_button.place(x=680, y=400)

        window.mainloop()


    def run(self):
        self.root.after(1000, self.check_face)
        self.root.mainloop()

# Instantiate the FaceRecognitionApp class and run the application
app = FaceRecognitionApp()
app.run()

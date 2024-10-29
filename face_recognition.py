from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np



# page student interface
class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1510x770+0+0")
        self.root.title("face Recognition  attendance System")

        # title ------------
        title_lbl = Label(
            self.root,
            text="Face Recognition",
            font=("times new roman", 30, "bold"),
            bg="white",
            fg="green",
        )
        title_lbl.place(x=-60, y=0, width=1530, height=50)
        # left image
        img_top = Image.open(
            r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\face_recognition\as-graphic-cyber.jpg"
        )
        img_top = img_top.resize((850, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=-20, y=50, width=850, height=700)
        # right image
        img_bottom = Image.open(
            r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\face_recognition\facial_recognition_system.webp"
        )
        img_bottom = img_bottom.resize((850, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=700, y=50, width=850, height=700)
        # button face recognistion
        b1_1 = Button(
            f_lbl,
            text="Face Recognition",
            cursor="hand2",
            command=self.face_recog,
            font=("times new roman", 18, "bold"),
            bg="blue",
            fg="white",
        )
        b1_1.place(x=320, y=610, width=200, height=40)
        #================== attendance============
    def mark_attendance(self,i,r,n,d):
        with open("wiam.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")
                




    
    # ----------------face recognition-----------------
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for x, y, w, h in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                resized_image = cv2.resize(gray_image[y:y + h, x:x + w], (450, 450))
                id, predict = clf.predict(resized_image)
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="root",
                    database="face_recognition_system",
                )
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE Student_id=" + str(id))
                n = my_cursor.fetchall()
                n = str(n[0][0]) if n else ""

                my_cursor.execute("SELECT Roll FROM student WHERE Student_id=" + str(id))
                r = my_cursor.fetchall()
                r = str(r[0][0]) if r else ""

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id=" + str(id))
                d = my_cursor.fetchall()
                d = str(d[0][0]) if d else ""

                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=" + str(id))
                i = my_cursor.fetchall()
                i = str(i[0][0]) if i else ""

                if confidence > 77:
                    cv2.putText(
                        img,
                        f"ID:{i}",
                        (x, y - 75),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Roll:{r}",
                        (x, y - 55),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Name:{n}",
                        (x, y - 30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                    cv2.putText(
                        img,
                        f"Departement:{d}",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                        )
                        
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.putText(
                        img,
                        "Unknown face",
                        (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        (255, 255, 255),
                        3,
                    )
                coord = [x, y, w, y]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), clf)
            return img

        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.namedWindow("Welcome to Face Recognition", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Welcome to Face Recognition", 450, 450)

            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()


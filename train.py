from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

# page student interface
class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1510x770+0+0")
        self.root.title("face Recognition  attendance System")

        # title ------------
        title_lbl = Label(
            self.root,
            text="Train DATA SET",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        title_lbl.place(x=-60, y=0, width=1530, height=45)
        # top images
        img_top = Image.open(
            r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\train\facialrecognition-1536x864.jpeg"
        )
        img_top = img_top.resize((1530, 350), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1530, height=350)

        # button Train data
        b1_1 = Button(
            self.root,
            text="TRAIN DATA",
            cursor="hand2",
            command=self.train_classifier,
            font=("times new roman", 20, "bold"),
            bg="red",
            fg="white",
        )
        b1_1.place(x=-50, y=380, width=1530, height=60)
        # bottom image
        img_bottom = Image.open(
            r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\train\facialrecognition-1536x864.jpeg"
        )
        img_bottom = img_bottom.resize((1530, 350), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=420, width=1530, height=350)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        img_size=(450,450)

        for image in path:
            img = Image.open(image).convert("L")  # Gray scale image
            imageNp = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split(".")[1])
            imageNp=cv2.resize(imageNp,img_size)
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)
        # ----------- train the classifier anad save -------------
        eigenfaces = cv2.face.LBPHFaceRecognizer_create()
        eigenfaces.train(faces, ids)
        eigenfaces.write("classifier.xml")
        cv2.destroyAllWindows()
        print("Result", "Training datasets completed!!!!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
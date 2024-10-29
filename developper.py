from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


# page student interface
class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1510x770+0+0")
        self.root.title("face Recognition  attendance System")
         # title ------------
        title_lbl = Label(
            self.root,
            text="DEVELOPER",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="blue",
        )
        title_lbl.place(x=-60, y=0, width=1530, height=45)
        # top images
        img_top = Image.open(
            r"developer_images\developer.jpg"
        )
        img_top = img_top.resize((1530, 680), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=680)
        #frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=900, y=0, width=600, height=600)

        img_top1 = Image.open(
            r"developer_images\us.jpeg"
        )
        img_top1 = img_top1.resize((400, 400), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        f_lbl = Label(self.root, image=self.photoimg_top1)
        f_lbl.place(x=950, y=50, width=400, height=400)
         #Developper info
        dev_label = Label(
            main_frame,
            text="Our name is Douae Tchorbo and  Wiam Terrab ",
            font=("times new roman", 16, "bold"),
            bg="yellow",
            fg="black"
        )
        dev_label.place(x=0,y=405)
        dev_label = Label(
            main_frame,
            text="we are first-year engineering students  ",
            font=("times new roman", 18, "bold"),
            bg="yellow",
            fg="black"
        )
        dev_label.place(x=0,y=440)
        dev_label = Label(
            main_frame,
            text=" in data science and cloud computing  ",
            font=("times new roman", 18, "bold"),
            bg="yellow",
            fg="black"
        )
        dev_label.place(x=0,y=470)
        dev_label = Label(
            main_frame,
            text=" at the national school of applied science",
            font=("times new roman", 18, "bold"),
            bg="yellow",
            fg="black"
        )
        dev_label.place(x=0,y=500)



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
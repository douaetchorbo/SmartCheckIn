from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developper import Developer
#from help import Help
from chatbot import ChatBot
from time import strftime
from datetime import datetime
#creer une interface graphique----------------------------------------------------------
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition  attendance System")
#image1------------------------
        img=Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\icones\ensao.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


#image2-----------------------
        img1 = Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\icones\face_reco.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
# image 3----------------------
        img2 = Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\icones\ensa.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)


# background image ---------------
        img3 = Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\icones\back.jpg")
        img3 = img3.resize((1400, 600), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1400, height=600)

        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE" , font=("times new roman",35, "bold"),bg="white",fg="red")
        title_lbl.place(x=0 , y=0,width=1400 ,height=45)
        #.............time...........
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=('tomes new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=3,y=0,width=115,height=50)
        time()
            
        #student button
        img4 = Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\icones\student.jpg")
        img4 = img4.resize((200, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4 , cursor="hand2",command=self.student_details)
        b1.place(x=100 , y=80 , width=200,height=200)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details,cursor="hand2",font=("times new roman",15, "bold"),bg="darkblue",fg="white")
        b1_1.place(x=100, y=250, width=200, height=40)

        # detect face button
        img5 = Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\icones\detector.jpg")
        img5 = img5.resize((200, 200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=400, y=80, width=200, height=200)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=400, y=250, width=200, height=40)

        # Attendance face button
        img6 = Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\icones\attendance.webp")
        img6 = img6.resize((200, 200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b1.place(x=700, y=80, width=200, height=200)
        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b1_1.place(x=700, y=250, width=200, height=40)

        # Help button
        img7 = Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\chatbot_images\chatbot.jpeg")
        img7 = img7.resize((200, 200), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.chatbot_data)
        b1.place(x=1000, y=80, width=200, height=200)

        b1_1 = Button(bg_img, text="ChatBot", cursor="hand2",command=self.chatbot_data, font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b1_1.place(x=1000, y=250, width=200, height=40)

        # Train button
        img8 = Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\icones\train.jpg")
        img8 = img8.resize((200, 200), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=100, y=320, width=200, height=200)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data,font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b1_1.place(x=100, y=480, width=200, height=40)

        # Photos face button
        img9 = Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\icones\photos.jpg")
        img9 = img9.resize((200, 200), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=400, y=320, width=200, height=200)

        b1_1 = Button(bg_img, text="Photos",command=self.open_img, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue",
                      fg="white")
        b1_1.place(x=400, y=480, width=200, height=40)

        # Developer face button
        img10 = Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\icones\developer.jpg")
        img10 = img10.resize((200, 200), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10,command=self.developer_data, cursor="hand2")
        b1.place(x=700, y=320, width=200, height=200)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data, font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b1_1.place(x=700, y=480, width=200, height=40)

        # Exit face button
        img11 = Image.open(r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\icones\exit.png")
        img11 = img11.resize((200, 200), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11,command=self.iExit,cursor="hand2")
        b1.place(x=1000, y=320, width=200, height=200)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b1_1.place(x=1000, y=480, width=200, height=40)
    def open_img(self):
        os.startfile("data")
    
    #Exit
    def iExit(self):
        if tkinter.messagebox.askyesno("Face recognition", "Are you sure you want to exit this project?"):
            self.root.destroy()

        else:
            return

    #---------unctions buttons------
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app= Face_recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app= Attendance(self.new_window)

    
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app= Developer(self.new_window)

    
    def chatbot_data(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)
    
    
    
    

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

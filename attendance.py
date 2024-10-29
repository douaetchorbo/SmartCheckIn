from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
mydata=[]
# page student interface
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1510x770+0+0")
        self.root.title("face Recognition  attendance System")
         #******************variables***********************
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

    # image1------------------------
        img = Image.open(
            r"attendance_systeme\student_attendance.jpg"
        )
        img = img.resize((780, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)


        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=-2, y=0, width=780, height=200)

        # image2-----------------------
        img1 = Image.open(
            r"attendance_systeme\std.jpg"
        )
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)


        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=700, y=-10, width=800, height=220)
        #background image
        img3 = Image.open(
            r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\icones\back.jpg")
        img3 = img3.resize((1400, 1000), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1400, height=600)
        title_lbl = Label(
            bg_img,
            text="Student management system",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="darkgreen",
        )
        title_lbl=Label(bg_img,text="Attendance Management systeme" , font=("times new roman",35, "bold"),bg="white",fg="blue")
        title_lbl.place(x=-5 , y=0,width=1400 ,height=45)
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=7, y=50, width=1350, height=500)
        # left label frame
        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Attendance Details",
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=2, width=700, height=680)
        Left_frame.place(x=10, y=2, width=730, height=680)
        img_left = Image.open(
            r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\attendance_systeme\sevisIconStudents.png"
        )
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=110, width=730, height=300)
        #LabelLand
        attendanceId_label = Label(
            left_inside_frame,
            text="AttendenceID:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        attendanceId_label.grid(row=0, column=0, padx=10, sticky=W)
        attendanceId_entry =ttk.Entry(
            left_inside_frame,
            textvariable=self.var_atten_id,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        attendanceId_entry.grid(row=0, column=1, padx=10, sticky=W)
         # student name
        rolllabel = Label(
            left_inside_frame,
            text="Roll:",
            font=("comicsansns 11 bold"),
            bg="white",
        )
        rolllabel.grid(row=0, column=2, padx=4, pady=10)
        attenroll = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_atten_roll ,
            width=22,
            font=("comicsansns 11 bold")
        )
        attenroll.grid(row=0, column=3 ,pady=8)
        #date
        Name_label = Label(
            left_inside_frame,
            text="Name:",
            font=("comicsansns 11 bold"),
            bg="white",
        )
        Name_label.grid(row=1, column=0)
        attend_name = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_atten_name,
            width=22,
             font=("comicsansns 11 bold"),
        )
        attend_name.grid(row=1, column=1,pady=8)
        # Departement
        dep_label = Label(
            left_inside_frame,
            text="Departement:",
            font=("comicsansns 11 bold"),
            bg="white",
        )
        dep_label.grid(row=1, column=2)
        attend_dep = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_atten_dep,
            width=22,
             font=("comicsansns 11 bold"),
        )
        attend_dep.grid(row=1, column=3,pady=8)
        #time
        time_label = Label(
            left_inside_frame,
            text="Time:",
            font=("comicsansns 11 bold"),
            bg="white",
        )
        time_label.grid(row=2, column=0)
        attend_time = ttk.Entry(
            left_inside_frame,
            textvariable=self.var_atten_time,
            width=22,
             font=("comicsansns 11 bold"),
        )
        attend_time.grid(row=2, column=1,pady=8)
        #Date
        date_label = Label(
            left_inside_frame,
            text="Date:",
            font=("comicsansns 11 bold"),
            bg="white",
        )
        date_label.grid(row=2, column=2)
        attend_date= ttk.Entry(
            left_inside_frame,
            textvariable=self.var_atten_date,
            width=22,
            font=("comicsansns 11 bold"),
        )
        attend_date.grid(row=2, column=3,pady=8)
        #attendance
        attendanceLabel = Label(
            left_inside_frame,
            text="Attendance Status:",
            font=("comicsansns 11 bold"),
            bg="white",
        )
        attendanceLabel.grid(row=3, column=0)
        self.attend_status = ttk.Combobox(
            left_inside_frame,
            width=20,
            textvariable=self.var_atten_attendance,
            font="comicsansns 11 bold",
            state="readonly"
           
            
        )
           
        self.attend_status["values"] = (
            "Status",
            "Present",
            "Abscent",
        )
        self.attend_status.current(0)
        self.attend_status.grid(row=3, column=1, pady=8)
        # button
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=205, width=715, height=70)
        save_btn = Button(
            btn_frame,
            text="Import csv",
            command=self.importCsv,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        save_btn.grid(row=0, column=0)

        update_btn = Button(
            btn_frame,
            text="Export csv",
            width=17,
            command=self.exportCsv,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(
            btn_frame,
            text="Update",
            command=self.reset_data,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        delete_btn.grid(row=0, column=2)
        reset_btn = Button(
            btn_frame,
            text="Reset",
    
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)
        # right label frame
        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Detail",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        Right_frame.place(x=755, y=2, width=590, height=580)
        #######table frame###########
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=575, height=400)
        #----------scroll barre
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame,
            column=(
                "id",
                "roll",
                "name",
                "departement",
                "time",
                "date",
                "attendance",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.xview)
        self.AttendanceReportTable.heading("id", text="AttendanceID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("departement", text="Departement")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("departement",width=100 )
        self.AttendanceReportTable.column("time", width=100 )
        self.AttendanceReportTable.column("date", width=100 )
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
    #*************************fetch data******************
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root) 
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)     
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                    messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0]) 
        self.var_atten_roll.set(rows[1]) 
        self.var_atten_name.set(rows[2]) 
        self.var_atten_dep.set(rows[3]) 
        self.var_atten_time.set(rows[4]) 
        self.var_atten_date.set(rows[5]) 
        self.var_atten_attendance.set(rows[6])       
    
    
    def reset_data(self):
        self.var_atten_id.set("") 
        self.var_atten_roll.set("") 
        self.var_atten_name.set("") 
        self.var_atten_dep.set("") 
        self.var_atten_time.set("") 
        self.var_atten_date.set("") 
        self.var_atten_attendance.set("")     


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
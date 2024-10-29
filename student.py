from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


# page student interface
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1510x770+0+0")
        self.root.title("face Recognition  attendance System")
        ##########variables##############
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        # image1------------------------
        img = Image.open(
            r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\student images\image-85.webp"
        )
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # image2-----------------------
        img1 = Image.open(
            r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\student images\face-recognition-806x440.webp"
        )
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
        # image 3----------------------
        img2 = Image.open(
            r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\student images\happy-female-student.webp"
        )
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=950, y=0, width=500, height=130)
        # background image ---------------
        img3 = Image.open(
            r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\student images\student-management.png"
        )
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
        title_lbl.place(x=0, y=0, relwidth=1530, height=45)
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=0, width=1500, height=600)
        # left label frame
        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Detail",
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=2, width=730, height=680)
        img_left = Image.open(
            r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\student images\studentdetail.png"
        )
        img_left = img2.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)
        # current course information
        current_course_frame = LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            text="Current course information",
            relief=RIDGE,
            font=("times new roman", 12, "bold"),
        )
        current_course_frame.place(x=5, y=70, width=720, height=150)
        # Departement
        dep_label = Label(
            current_course_frame,
            text="Departement",
            font=("times new roman", 12, "bold"),
            bg="white",
        )
        dep_label.grid(row=0, column=0, padx=10,sticky=W)
        dep_combo = ttk.Combobox(
            current_course_frame,
            font=("times new roman", 12, "bold"),
            textvariable=self.var_dep,
            width=17,
            state="read only",
        )
        dep_combo["values"] = (
            "Select Departement",
            "IDSCC",
            "Civil",
            "Industriel",
            "Electrique",
            "software",
            "Itirc",
        )
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        # course
        course_label = Label(
            current_course_frame,
            text="Course",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(
            current_course_frame,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_course,
            width=17,
            state="read only",
        )
        course_combo["values"] = (
            "Select Course",
            "Java",
            "Mecanique",
            "Python",
            "STR",
            "Database",
        )
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        # year
        year_label = Label(
            current_course_frame,
            text="Year",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(
            current_course_frame,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_year,
            width=17,
            state="read only",
        )
        year_combo["values"] = (
            "Select Course",
            "2022-23",
            "2023-24",
            "2024-25",
            "2025-26",
        )
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        # Semestre
        Semester_label = Label(
            current_course_frame,
            text="Semester",
            textvariable=self.var_semester,
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        Semester_label.grid(row=1, column=2, padx=10, sticky=W)

        Semester_combo = ttk.Combobox(
            current_course_frame,
            textvariable=self.var_semester,
            font=("times new roman", 13, "bold"),
            width=17,
            state="read only",
        )
        Semester_combo["values"] = ("Select Semestre", "Semestre-1", "Semestre-2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        # Class Student information
        class_Student_frame = LabelFrame(
            Left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Class Student information",
            font=("times new roman", 13, "bold"),
        )
        class_Student_frame.place(x=5, y=220, width=750, height=350)
        # student Id
        StudentId_label = Label(
            class_Student_frame,
            text="StudentID:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        StudentId_label.grid(row=0, column=0, padx=10, sticky=W)
        StudentId_entry = Entry(
            class_Student_frame,
            width=20,
            textvariable=self.var_std_id,
            font=("times new roman", 13, "bold"),
        )
        StudentId_entry.grid(row=0, column=1, padx=10, sticky=W)
        # student name
        studenName_label = Label(
            class_Student_frame,
            text="Student Name:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        studenName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        studenName_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_std_name,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        studenName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        # class division
        class_div_label = Label(
            class_Student_frame,
            text="Class Division:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        div_combo = ttk.Combobox(
            class_Student_frame,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_div,
            width=17,
            state="read only",
        )
        div_combo["values"] = ("DR1", "DR2", "DR3")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        # Roll NO
        roll_no_label = Label(
            class_Student_frame,
            text="Roll NO:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        roll_no_entry =ttk.Entry(
            class_Student_frame,
            textvariable=self.var_roll,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        # Gender
        gender_label = Label(
            class_Student_frame,
            text="Gender:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(
            class_Student_frame,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_gender,
            width=10,
            state="read only",
        )
        gender_combo["values"] = ("Select Gender", "Male", "Femele", "other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)
        # Roll NO
        dob_label = Label(
            class_Student_frame,
            text="DOB:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry =ttk.Entry(
            class_Student_frame,
            textvariable=self.var_dob,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        # Email
        email_label = Label(
            class_Student_frame,
            text="Email:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_email,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        # phone no
        phone_label = Label(
            class_Student_frame,
            text="Phone No:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_phone,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        # Adresse
        adresse_label = Label(
            class_Student_frame,
            text="Address:",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        adresse_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        adresse_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_address,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        adresse_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        # Teacher name
        teacher_label = Label(
            class_Student_frame,
            text="Teacher Name:",
            font=("times new roman", 9, "bold"),
            bg="white",
        )
        teacher_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        teacher_entry = ttk.Entry(
            class_Student_frame,
            textvariable=self.var_teacher,
            width=20,
            font=("times new roman", 13, "bold"),
        )
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)
        # radio buttons
        self.var_radio1 = StringVar()
        self.var_radio1.set("take Photo Sample")
        radiobnt1 = ttk.Radiobutton(
            class_Student_frame, textvariable=self.var_radio1, value="Yes"
        )
        radiobnt1.grid(row=6, column=0)
        self.var_radio2 = StringVar()
        self.var_radio2.set("No Photo Sample")
        radiobnt2 = ttk.Radiobutton(
            class_Student_frame,
            textvariable=self.var_radio2,
            compound="left",
            value="No",
        )
        radiobnt2.grid(row=6, column=1)
        # bbuttons frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=205, width=715, height=70)
        save_btn = Button(
            btn_frame,
            text="Save",
            command=self.add_data,
            width=15,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        save_btn.grid(row=0, column=0)

        update_btn = Button(
            btn_frame,
            text="Update",
            width=17,
            command=self.update_data,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        update_btn.grid(row=0, column=1)

        delete_btn = Button(
            btn_frame,
            text="Delete",
            command=self.delete_data,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        delete_btn.grid(row=0, column=2)
        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            width=17,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_btn = Button(
            btn_frame1,
            command=self.generate_dataset,
            text="Take Photo Sample",
            width=35,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        take_photo_btn.grid(row=0, column=0)
        update_photo_btn = Button(
            btn_frame1,
            text="Update Photo Sample",
            width=35,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        update_photo_btn.grid(row=0, column=1)
        # right label frame
        Right_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Detail",
            font=("times new roman", 13, "bold"),
            bg="white",
        )
        Right_frame.place(x=750, y=10, width=700, height=580)
        img_right = Image.open(
            r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\student images\studentdetail.png"
        )
        img_right = img_right.resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=10, width=720, height=130)
        ############Search System##############
        Search_frame = LabelFrame(
            Right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search System",
            font=("times new roman", 13, "bold"),
        )
        Search_frame.place(x=5, y=100, width=700, height=70)
        search_label = Label(
            Search_frame,
            text="Search By:",
            font=("times new roman", 13, "bold"),
            bg="red",
            fg="white",
        )
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(
            Search_frame,
            font=("times new roman", 13, "bold"),
            width=15,
            state="read only",
        )
        search_combo["values"] = ("Select", "Roll_NO", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        search_entry = ttk.Entry(
            Search_frame, width=10, font=("times new roman", 12, "bold")
        )
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        search_btn = Button(
            Search_frame,
            text="Search",
            width=10,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        search_btn.grid(row=0, column=3, padx=4)
        showAll_btn = Button(
            Search_frame,
            text="Show All",
            width=10,
            font=("times new roman", 12, "bold"),
            bg="blue",
            fg="white",
        )
        showAll_btn.grid(row=0, column=4, padx=4)
        #######table frame###########
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=180, width=550, height=250)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(
            table_frame,
            columns=(
                "dep",
                "course",
                "year",
                "sem",
                "id",
                "name",
                "div",
                "roll",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "teacher",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep", text="Departement")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # function declaration ---------------------
    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="root",
                    database="face_recognition_system",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Sucess",
                    "student detail has been added successfly",
                    parent=self.root,
                )
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Error due to {str(e)}", parent=self.root
                )

    # ---------fetch data -------------------------
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="face_recognition_system",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ---------------- get cursor--------------
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2])
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update function
    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Upadate = messagebox.askyesno(
                    "Update",
                    "Do you want to update this student details ",
                    parent=self.root,
                )
                if Upadate > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="root",
                        database="face_recognition_system",
                    )
                    my_cursor = conn.cursor()
                    print("Executing SQL query...")
                    my_cursor.execute(
                        "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get(),
                        ),
                    )
                    print("SQL query executed successfully.")
                    messagebox.showinfo(
                        "Success",
                        "Student details successfully updated",
                        parent=self.root,
                    )
                else:
                    if not Upadate:
                        return
                conn.commit()
                self.fetch_data()
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Error due to {str(e)}", parent=self.root
                )
            finally:
                conn.close()

    # delete function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root
            )
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page",
                    "Do you want to delete this student",
                    parent=self.root,
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="root",
                        database="face_recognition_system",
                    )
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfuly deleted student details", parent=self.root
                )
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Error due to {str(e)}", parent=self.root
                )

    # reset fucntion
    def reset_data(self):
        self.var_dep.set("Select Departement"),
        self.var_course.set("Select course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semestre"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    # ------------ Generate Data or take photo samples-----
    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root",
                    database="face_recognition_system",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id + 1,
                    ),
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ---------- load predifiend data on face frontals from opencv ------------
                face_classifier = cv2.CascadeClassifier(
                    r"C:\Users\SuperElectro\Downloads\face_recognition-systeme\face_recognition-systeme\haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(
                        gray, scaleFactor=1.3, minNeighbors=5
                    )
                    for x, y, w, h in faces:
                        face_cropped = img[y : y + h, x : x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = (
                            "data/user." + str(id) + "." + str(img_id) + ".jpeg"
                        )
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(
                            face,
                            str(img_id),
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            2,
                            (0, 255, 0),
                            2,
                        )
                        cv2.namedWindow("window_name", cv2.WINDOW_NORMAL)
                        cv2.resizeWindow("window_name", 200, 200)

                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!!!")

            except Exception as e:
                messagebox.showerror(
                    "Error", f"Error due to {str(e)}", parent=self.root
                )


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

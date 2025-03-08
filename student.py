from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #=============variable=================#
        self.var_dep = StringVar()
        self.var_course =StringVar()
        self.var_year =StringVar()
        self.var_semester =StringVar()
        self.var_std_id =StringVar()
        self.var_std_name =StringVar()
        self.var_div =StringVar()
        self.var_roll =StringVar()
        self.var_gender =StringVar()
        self.var_dob =StringVar()
        self.var_email =StringVar()
        self.var_phone =StringVar()
        self.var_address =StringVar()
        self.var_teacher =StringVar()


        img = Image.open(r"C:\face_recognition_system\collage_image\student1.jpg")   #first
        img = img.resize((500, 130),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        img1 = Image.open(r"C:\face_recognition_system\collage_image\th (1).jpg")  #second
        img1 = img1.resize((500, 130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        img2 = Image.open(r"C:\face_recognition_system\collage_image\th (2).jpg")   #third
        img2 = img2.resize((500, 130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img3 = Image.open(r"C:\face_recognition_system\collage_image\th (3).jpg")
        img3 = img3.resize((1580, 790),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Place images
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=500, y=0, width=500, height=130)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1000, y=0, width=500, height=130)
        
        #background
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1580, height=790)

        title_lbl = Label(bg_img, text="STUDENT MANGEMENT SYSTEM", font=("time new roman", 35, "bold"), bg="white", fg='darkgreen')
        title_lbl.place(x=0, y=0, width=1580, height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50,width=1450,height=600)

        #left label frame
        LEFT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("time new roman",12,"bold"))
        LEFT_frame.place(x=10,y=10,width=720,height=580)

        img_left= Image.open(r"C:\face_recognition_system\collage_image\student2.jpg") 
        img_left= img_left.resize((715,120),Image.Resampling.LANCZOS)
        self.photoimg_left= ImageTk.PhotoImage(img_left)

        f_lbl = Label(LEFT_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=710, height=100)

        #current course
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("time new roman",12,"bold"))
        current_course_frame.place(x=15,y=130,width=710,height=120)
        
        #department
        dep_label=Label(current_course_frame,text="Department",font=("time new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("time new roman",12,"bold"),width=17,state='readonly')
        dep_combo["values"]=("select department","computer","AI-ML","IT","civil","Mechical")
        dep_combo.current(0) 
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="COURSE",font=("time new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_label_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("time new roman",13,"bold"),width=17,state='readonly')
        course_label_combo["values"]=("select course","FE","SE","TE","BE")
        course_label_combo.current(0) 
        course_label_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="YEAR",font=("time new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_label_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("time new roman",13,"bold"),width=17,state='readonly')
        year_label_combo["values"]=("select year","2024-25","2025-26","2026-27","2027-28")
        year_label_combo.current(0) 
        year_label_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #semester
        course_label=Label(current_course_frame,text="SEMESTER",font=("time new roman",12,"bold"),bg="white")
        course_label.grid(row=1,column=2,padx=10,sticky=W)

        course_label_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("time new roman",13,"bold"),width=17,state='readonly')
        course_label_combo["values"]=("select semester","semester-1","semester-2")
        course_label_combo.current(0) 
        course_label_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="class student information",font=("time new roman",12,"bold"))
        class_student_frame.place(x=15,y=255,width=710,height=330)

        #student id
        studentId_label=Label(class_student_frame,text="STUDENT ID:",font=("time new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=("time new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student  name
        studentname_label=Label(class_student_frame,text="STUDENT NAME:",font=("time new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_name,font=("time new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        classdivision_label=Label(class_student_frame,text="DIVISION:",font=("time new roman",12,"bold"),bg="white")
        classdivision_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # classdivision_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_div,font=("time new roman",12,"bold"))
        # classdivision_entry.grid(row=1,column=1,padx=10,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("time new roman",13,"bold"),width=18,state='readonly')
        div_combo["values"]=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #rollno
        rollno_label=Label(class_student_frame,text="ROLLNO:",font=("time new roman",12,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("time new roman",12,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,sticky=W)

        #gender
        gender_label=Label(class_student_frame,text="GENDER:",font=("time new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        # gender_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_gender,font=("time new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("time new roman",13,"bold"),width=18,state='readonly')
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #dob
        dob_label=Label(class_student_frame,text="DOB:",font=("time new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("time new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,sticky=W)

        #email
        email_label=Label(class_student_frame,text="EMAIL:",font=("time new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("time new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,sticky=W)
        #phoneno
        phone_label=Label(class_student_frame,text="PHONE NO:",font=("time new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("time new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,sticky=W)
        #address
        address_label=Label(class_student_frame,text="ADDRESS:",font=("time new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("time new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,sticky=W)
        #teachername
        teacher_label=Label(class_student_frame,text="TEACHER name:",font=("time new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("time new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="YES")
        radiobtn1.grid(row=8,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="no photo sample",value="No")
        radiobtn2.grid(row=8,column=1)

        #bbutton frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=1,y=220,width=705,height=100)
        
        save_btn=Button(btn_frame,text="Save",width=16,command=self.add_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=2,column=0,padx=5,pady=5)

        update_btn=Button(btn_frame,text="update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=2,column=1,padx=5,pady=5)

        delete_btn=Button(btn_frame,text="delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=2,column=2,padx=5,pady=5)

        reset_btn=Button(btn_frame,text="reset", command=self.reset_date,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=2,column=3,padx=5,pady=5)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=1,y=260,width=705,height=40)

        take_photo_btn=Button(btn_frame1,text="Take a photo",command=self.generate_dataset,width=34,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=8,pady=5)

        update_btn=Button(btn_frame1,text="update photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("time new roman",12,"bold"))
        right_frame.place(x=740,y=10,width=700,height=580)

        img_right= Image.open(r"C:\face_recognition_system\collage_image\detail1.jpg") 
        img_right= img_right.resize((715,120),Image.Resampling.LANCZOS)
        self.photoimg_right= ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=700, height=150)

        #=====search system========#

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="searchb system",font=("time new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=690,height=100)

        search_label=Label(search_frame,text="SEARCH BY:",font=("time new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("time new roman",13,"bold"),state='readonly')
        search_combo["values"]=("select","roll_no","phone_no")
        search_combo.current(0) 
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        
        search_entry=ttk.Entry(search_frame,width=15,font=("time new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)

        search_btn=Button(search_frame,text="search",width=6,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)

        showall_btn=Button(search_frame,text="show All",width=8,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=2,pady=5)

        #======table frame=======
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=235,width=690,height=320)

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,
                                        column =
                                        ("dep","course","year","sem","id","name","div",
                                        "roll","gender","dob","email","gender","phone","address","teacher","photo")
                                        ,xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        


        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="YEAR")
        self.student_table.heading("sem",text="SEMESTER")
        self.student_table.heading("id",text="STUDENTID")
        self.student_table.heading("name",text="NAME")
        self.student_table.heading("div",text="DIVISION")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="EMAIL")
        self.student_table.heading("phone",text="PHONE")
        self.student_table.heading("address",text="ADDRESS")
        self.student_table.heading("teacher",text="TEACHER")
        self.student_table.heading("photo",text="PHOTOSampleStatus")
        self.student_table["show"] = "headings"


        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    # #===============function declation==============#
    def add_data(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Sanjukta8788",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
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
                                                                        self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student detail has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)


    #==========fetch data===============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Sanjukta8788",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()

    #======================get curser====================#
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]


        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
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

    #====================update function=============#

    def update_data(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                upadate=messagebox.askyesno("update","DO You Want to update this Student Detail ",parent=self.root)
                if upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="@Sanjukta8788",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Email=%s,dob=%s,Phone=%s,address=%s,teacher=%s,Photo=%s where student_id=%s",(
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
                                                                        self.var_std_id.get()
                                                                        ))
                else:
                    if not upadate:
                        return
                messagebox.showinfo("success","student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)

    #================delete function==============
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","DO YOU WANT TO DELETE THIS STUDENT",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="@Sanjukta8788",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","successfully delete studentvdetails",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)

    #=======================reset function======================#
    def reset_date(self):
        self.var_dep.set("select department")
        self.var_course.set("select course"),
        self.var_year.set("select year"),
        self.var_semester.set("selsect semester"),
        self.var_std_id.set("")
        self.var_std_name.set(""),
        self.var_div.set("select division"),
        self.var_roll.set(""),
        self.var_gender.set("male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

#===========generate data set take a photo sample=================#
    def generate_dataset(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Sanjukta8788",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Email=%s,dob=%s,Phone=%s,address=%s,teacher=%s,Photo=%s where student_id=%s",(
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
                                                                        self.var_std_id.get()==id+1
                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_date()
                conn.close()
                #================load predifine data on face frontals from opencv=============#

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #min neighbours=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()



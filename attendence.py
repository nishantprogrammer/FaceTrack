from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog,messagebox

mydata=[]
class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #===========variable===============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dept=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()



        img = Image.open(r"C:\face_recognition_system\collage_image\student1.jpg")   #first
        img = img.resize((800, 200),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)


        img1 = Image.open(r"C:\face_recognition_system\collage_image\th (1).jpg")  #second
        img1 = img1.resize((800,200),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=800, y=0, width=800, height=200)

        #background

        img3 = Image.open(r"C:\face_recognition_system\collage_image\fancy.jpg")
        img3 = img3.resize((1580, 790),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1580, height=790)

        title_lbl = Label(bg_img, text="ATTENDENCE MANGEMENT SYSTEM", font=("time new roman", 35, "bold"), bg="white", fg='darkgreen')
        title_lbl.place(x=0, y=0, width=1580, height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=55,width=1490,height=600)

        #left label frame
        LEFT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENCE ATTENDENCE details",font=("time new roman",12,"bold"))
        LEFT_frame.place(x=10,y=10,width=730,height=580)

        img_left= Image.open(r"C:\face_recognition_system\collage_image\student2.jpg") 
        img_left= img_left.resize((715,120),Image.Resampling.LANCZOS)
        self.photoimg_left= ImageTk.PhotoImage(img_left)

        f_lbl = Label(LEFT_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=10, width=720, height=100)

        left_inside_frame=Frame(LEFT_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=130,width=720,height=370)

        #label and entry
        #attendence id
        attendenceId_label=Label(left_inside_frame,text="Attendence ID:",font=("time new roman",12,"bold"),bg="white")
        attendenceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendenceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("time new roman",12,"bold"))
        attendenceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll
        roll_label=Label(left_inside_frame,text="Roll:",font=("time new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("time new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=8,pady=5,sticky=W)

        #date
        name_label=Label(left_inside_frame,text="NAME:",font=("time new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("time new roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #department
        dep_label=Label(left_inside_frame,text="DEPARTMENT:",font=("time new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dept,font=("time new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #time
        time_label=Label(left_inside_frame,text="Time:",font=("time new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("time new roman",12,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date
        date_label=Label(left_inside_frame,text="Date:",font=("time new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("time new roman",12,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attendence
        attendeceLabel=Label(left_inside_frame,text="Attendence status",bg="white",font="comicsansns 11 bold")
        attendeceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status['values']=("status","present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=1,y=300,width=715,height=40)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=2,column=0,padx=5,pady=5)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=2,column=1,padx=5,pady=5)

        delete_btn=Button(btn_frame,text="Update",width=16,command=self.update_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=2,column=2,padx=5,pady=5)

        reset_btn=Button(btn_frame,text="Reset",width=16,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=2,column=3,padx=5,pady=5)

        

        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDENCE details",font=("time new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=445)

        #==============scroll bar table===============#
        # scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        # scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        # self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","Roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        # scroll_x.pack(side=BOTTOM,fill=X)
        # scroll_y.pack(side=RIGHT,fill=Y)

        # scroll_x.config(command=self.AttendanceReportTable.xview)
        # scroll_y.config(command=self.AttendanceReportTable.yview)

        # self.AttendanceReportTable.heading("id",text="Attendence Id")
        # self.AttendanceReportTable.heading("Roll",text="Roll NO")
        # self.AttendanceReportTable.heading("name",text="name")
        # self.AttendanceReportTable.heading("department",text="Department")
        # self.AttendanceReportTable.heading("time",text="Time")
        # self.AttendanceReportTable.heading("attendence",text="Attendence")

        # self.AttendanceReportTable["show"]="headings"
        # self.AttendanceReportTable.column("id",width=100)
        # self.AttendanceReportTable.column("Roll",width=100)
        # self.AttendanceReportTable.column("name",width=100)
        # self.AttendanceReportTable.column("department",width=100)
        # self.AttendanceReportTable.column("time",width=100)
        # self.AttendanceReportTable.column("attendence",width=100)



        # self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        #modify code 

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        columns = ("id", "Roll", "name", "department", "time", "date", "attendence")

        self.AttendanceReportTable = ttk.Treeview(
                table_frame, columns=columns, show="headings",
                xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # Define column headings dynamically
        column_names = {
    "id": "Attendance ID", "Roll": "Roll No", "name": "Name",
    "department": "Department", "time": "Time", "date": "Date",
    "attendence": "Attendance"}

        for col, heading in column_names.items():
            self.AttendanceReportTable.heading(col, text=heading)
            self.AttendanceReportTable.column(col, width=120, anchor=CENTER)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)




        # ============fetch data=================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    # def importCsv(self):
    #     global mydata
    #     fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV Files,"*.csv"),("ALL File","*.*")),parent=self,root)
    #     with open(fln) as myfile:
    #         csvread=csv.reader(myfile,delimiter=",")
    #         for i in csvread:
    #             mydata.append(i)
    #         self.fetchData(mydata)

 #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        #mydata = []  # Clear previous data to avoid duplicates

    # Open file dialog for CSV selection
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV File",
            filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
            parent=self.root
        )

        if not fln:  # If no file is selected, exit function
            return

        try:
            with open(fln, newline='', encoding="utf-8") as myfile:
                csvreader = csv.reader(myfile)
                mydata.extend(csvreader)  # More efficient than appending row by row

            if not mydata:  # Check if the file was empty
                messagebox.showwarning("Warning", "The selected CSV file is empty!")
                return

            self.fetchData(mydata)  # Call function to update UI

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {str(e)}")  # Show user-friendly error message

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","NO Data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            title="Open CSV File",
            filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
            parent=self.root
        )
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","YOur data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)

#get curser
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dept.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dept.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


    #update button
    def update_data(self):
        cursor_row = self.AttendanceReportTable.focus()
    
        if not cursor_row:  # Check if a row is selected
            messagebox.showwarning("Warning", "Please select a record to update.")
            return

        updated_values = (
            self.var_atten_id.get(),
            self.var_atten_roll.get(),
            self.var_atten_name.get(),
            self.var_atten_dept.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
    )

        self.AttendanceReportTable.item(cursor_row, values=updated_values)  # Update the Treeview row
        messagebox.showinfo("Success", "Record updated successfully!")








if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()


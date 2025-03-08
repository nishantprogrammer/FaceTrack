from tkinter import *
# from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import face_recognition
from attendence import Attendence
from developer import developer
from help import help


class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # Load images
        img = Image.open(r"C:\face_recognition_system\collage_image\th.jpg")   #first
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

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1580, height=790)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg='red')
        title_lbl.place(x=0, y=0, width=1580, height=45)

        # Student button
        img4 = Image.open(r"C:\face_recognition_system\collage_image\student.jpg")
        img4 = img4.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_lbl = Button(bg_img, text="Student Details",command=self.student_details, font=("times new roman", 15, "bold"), bg="white", fg='red')
        b1_lbl.place(x=200, y=300, width=220, height=40)

        #face detect button
        img5= Image.open(r"C:\face_recognition_system\collage_image\face.jpg")
        img5= img5.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg5= ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_lbl = Button(bg_img, text="face detetection", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="white", fg='red')
        b1_lbl.place(x=500, y=300, width=220, height=40)

        #attendance 
        img6= Image.open(r"C:\face_recognition_system\collage_image\attendence.jpg")
        img6= img6.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg6= ImageTk.PhotoImage(img6)

        b1 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b1.place(x=800, y=100, width=220, height=220)

        b1_lbl = Button(bg_img, text="attendence", cursor="hand2",command=self.attendence_data,font=("times new roman", 15, "bold"), bg="white", fg='red')
        b1_lbl.place(x=800, y=300, width=220, height=40)

        #help
        img7= Image.open(r"C:\face_recognition_system\collage_image\help.jpg")
        img7= img7.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg7= ImageTk.PhotoImage(img7)

        b1 = Button(bg_img,image=self.photoimg7, cursor="hand2",command=self.help_data)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_lbl = Button(bg_img, text="HELP", cursor="hand2",command=self.help_data,font=("times new roman", 15, "bold"), bg="white", fg='red')
        b1_lbl.place(x=1100, y=300, width=220, height=40)

        #train data
        img8= Image.open(r"C:\face_recognition_system\collage_image\train.jpg")
        img8= img8.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg8= ImageTk.PhotoImage(img8)

        b1 = Button(bg_img,image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=400, width=220, height=220)

        b1_lbl = Button(bg_img, text="TRAIN DATA", cursor="hand2",command=self.train_data,font=("times new roman", 15, "bold"), bg="white", fg='red')
        b1_lbl.place(x=200, y=600, width=220, height=40)

        #photo face button
        img9= Image.open(r"C:\face_recognition_system\collage_image\photo.jpg")
        img9= img9.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg9= ImageTk.PhotoImage(img9)

        b1 = Button(bg_img,image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=400, width=220, height=220)

        b1_lbl = Button(bg_img, text="photo", cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"), bg="white", fg='red')
        b1_lbl.place(x=500, y=600, width=220, height=40)
        #developer
        img10= Image.open(r"C:\face_recognition_system\collage_image\developer.jpeg")
        img10= img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10= ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b1.place(x=800, y=400, width=220, height=220)

        b1_lbl = Button(bg_img, text="devloper",cursor="hand2",command=self.developer_data, font=("times new roman", 15, "bold"), bg="white", fg='red')
        b1_lbl.place(x=800, y=600, width=220, height=40)

        #exit
        img11= Image.open(r"C:\face_recognition_system\collage_image\exit.jpg")
        img11= img11.resize((220, 220),Image.Resampling.LANCZOS)
        self.photoimg11= ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100, y=400, width=220, height=220)

        b1_lbl = Button(bg_img, text="exit",cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg='red')
        b1_lbl.place(x=1100, y=600, width=220, height=40)


    def open_img(self):
        os.startfile("data")

        #================function===================


    def student_details(self):
        self.new_window=Toplevel(self.root)       #access the student page
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)       #access the student page
        self.app=Train(self.new_window)

    
    def face_data(self):
        self.new_window=Toplevel(self.root)       #access the student page
        self.app=face_recognition (self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)       #access the  attendence page
        self.app=Attendence(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)       #access the  developer page
        self.app=developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)       #access the  help page
        self.app=help(self.new_window)















if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()


# def student_details(self):
#     self.new_window=Toplevel(self.root)         #access the student page
#     self.app=student(self.new_window)


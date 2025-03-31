from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        
        title_lbl = Label(self.root, text="DEVELOPER", font=("time new roman", 35, "bold"), bg="white", fg='blue')
        title_lbl.place(x=0, y=0, width=1580, height=45)

        img_top= Image.open(r"C:\face_recognition_system\collage_image\developer.png") 
        img_top= img_top.resize((1530,720),Image.Resampling.LANCZOS)                      #top image 
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530, height=720)
        
        #frame
        main_frame=Frame(f_lbl,bd=2,background="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1= Image.open(r"C:\face_recognition_system\collage_image\developer.png") 
        img_top1= img_top.resize((1530,720),Image.Resampling.LANCZOS)                      #top image 
        self.photoimg_top1= ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=170,y=0,width=200, height=200)

        #developer info
        dev_label=Label(main_frame,text="hello my name nishant",font=("time new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)





if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()
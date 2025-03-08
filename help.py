from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP", font=("time new roman", 35, "bold"), bg="white", fg='blue')
        title_lbl.place(x=0, y=0, width=1580, height=45)

        img_top= Image.open(r"C:\face_recognition_system\collage_image\developer.png") 
        img_top= img_top.resize((1530,720),Image.Resampling.LANCZOS)                      #top image 
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530, height=720)

        dev_label=Label(f_lbl,text="Email.abhishek@gmail.com",font=("time new roman",20,"bold"),bg="white")
        dev_label.place(x=530,y=400)
        



if __name__ == "__main__":
    root = Tk()
    obj = help(root)
    root.mainloop()
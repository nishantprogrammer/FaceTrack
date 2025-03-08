from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class  Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("time new roman", 35, "bold"), bg="white", fg='RED')
        title_lbl.place(x=0, y=0, width=1580, height=45)

        img_top= Image.open(r"C:\face_recognition_system\collage_image\train1.jpeg") 
        img_top= img_top.resize((1530,330),Image.Resampling.LANCZOS)                      #top image 
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530, height=330)

        #button
        b1_lbl = Button(self.root,text="TRAIN DATA",command=self.train_classifer,font=("times new roman", 30, "bold"),bg="red", fg='white')
        b1_lbl.place(x=0, y=390, width=1530, height=60)

        img_bottom= Image.open(r"C:\face_recognition_system\collage_image\train2.jpg")             #bottom image 
        img_bottom= img_bottom.resize((1530,330),Image.Resampling.LANCZOS)
        self.photoimg_bottom= ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530, height=375)

    # def train_classifer(self):
    #     data_dir = "data"
    #     if not os.path.exists(data_dir):
    #         messagebox.showerror("Error", "Data directory not found!")
    #         return
    #     path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.png', '.jpeg'))]

    #     if not path:
    #        messagebox.showerror("Error", "No valid image files found in the data directory!")
    #        return
    #     faces =[]
    #     ids = []

    #     try:
    #         for image in path:
    #             img = Image.open(image).convert('L')  # Convert to grayscale
    #             imageNp = np.array(img, 'uint8')
    #             id = int(os.path.split(image)[1].split('.')[1])  # Extract ID from the filename

    #             faces.append(imageNp)
    #             ids.append(id)

    #         # Show image in OpenCV window briefly
    #             cv2.imshow("Training", imageNp)
    #             cv2.waitKey(50)  # Wait 100ms before closing
    #         id =np.array(ids)
    #         clf = cv2.face.LBPHFaceRecognizer_create()
    #         clf.train(faces, ids)
    #         clf.write("classifier.xml")
    #         cv2.destroyAllWindows()
    #         messagebox.showinfo("Result", "Training datasets complete!")
        
    #     except Exception as e:
    #         cv2.destroyAllWindows()
    #         messagebox.showerror("Error", f"An error occurred during training: {e}")




# function
    def train_classifer(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # grayscale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #================train the classifer and save===========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifer.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets complete!!!")











if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()


from tkinter import *
from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class  face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("time new roman", 35, "bold"), bg="white", fg='GREEN')
        title_lbl.place(x=0, y=0, width=1580, height=45)


        #left & right photo
        img_left= Image.open(r"C:\face_recognition_system\collage_image\face_det2.jpeg") 
        img_left= img_left.resize((650,750),Image.Resampling.LANCZOS)                      #left image 
        self.photoimg_left= ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=0,y=55,width=650,height=750)

        img_right= Image.open(r"C:\face_recognition_system\collage_image\face_det1.jpg") 
        img_right= img_right.resize((950,730),Image.Resampling.LANCZOS)                      #right image 
        self.photoimg_right= ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=650,y=55,width=950, height=730)

        #button
        b1_1 = Button(f_lbl,text="Face Recognition",cursor="hand2",font=("times new roman",18, "bold"),bg="red", fg='white',command=self.face_recog)
        b1_1.place(x=370, y=650, width=200, height=40)

        #===============================Attendence==========================#

    def mark_attendence(self,i,r,n,d):
        with open("abhishek.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")
            




        #===================face recognition=====================#

    def face_recog(self):
        def draw_boundary(img,classifer,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifer.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                conn=mysql.connector.connect(host="localhost",username="root",password="@Sanjukta8788",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)



                if  confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.putText(img,"unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        try:
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")         #same fuction using try and catch method
        except Exception as e:
                print(f"Error loading face cascade: {e}")

        
        # faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifer.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
    root = Tk()
    obj = face_recognition(root)
    root.mainloop()


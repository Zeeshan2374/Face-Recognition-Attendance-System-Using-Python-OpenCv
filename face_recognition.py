from tkinter import*
from tkinter import ttk
from typing import ItemsView
from PIL import Image,ImageTk
from tkinter import messagebox
from click import command
import datetime
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self,root):
    
        self.root = root
        self.root.geometry("1352x727+0+0")
        self.root.title("Face Recognition System")
      #label
        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("times new Roman",35,"bold"),bg="white",fg="DARK GREEN")
        title_lbl.place(x=0,y=0,width=1400,height=45)
        
      #first image
        img = Image.open(r"img\fff.jpg")
        img = img.resize((700,600),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image= self.photoimg)
        f_lbl.place(x=0,y=45,width=600,height=600)
     
      #second image
        img1 = Image.open(r"img\f2.png")
        img1 = img1.resize((1000,600),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image= self.photoimg1)
        f_lbl.place(x=580,y=45,width=800,height=600)

       #button
        b1_1 = Button(f_lbl,text = "Face Recognition",command=self.face_recog,cursor="hand2",font=("times new Roman",15,"bold"),bg="green",fg="White")
        b1_1.place(x=300,y=530,width=200,height=38)
######Attendence System#######
    def mar_attendence(self, i, j, k, n):
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dtstring = now.strftime("%H:%M:%S")

    # Open the CSV file to read and write
        with open("zeeshan.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []

        # Check for existing entries for the same user and date
            for line in myDatalist:
                entry = line.split(",")
                if entry[0] == str(i) and entry[5] == d1:  # Check if USN and date match
                    return  # Entry already exists, so we exit the method

        # If we reach here, it means the entry is new
            f.writelines(f"\n{i},{j},{k},{n},{dtstring},{d1},Present")
            print("Attendance recorded for:", i)
#==============Face recognition=========#
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            grey_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(grey_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(grey_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="2374",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select STUDENT_USN from student where STUDENT_USN="+str(id))
                result = my_cursor.fetchone()
                if result:
                    i = result[0]
                
                
                my_cursor.execute("select STUDENT_NAME from student where STUDENT_USN="+str(id))
                result = my_cursor.fetchone()
                if result:
                    j = result[0]    
                    
                    
                my_cursor.execute("select DEPARTMENT from student where STUDENT_USN="+str(id))
                result = my_cursor.fetchone()
                if result:
                    n = result[0]
                    
                my_cursor.execute("select ADDRESS from student where STUDENT_USN="+str(id))
                result = my_cursor.fetchone()
                if result:
                    k = result[0]
                    
                    
                if confidence>77:
                    cv2.putText(img,f"STUDENT USN:{i}",(x,y-105),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                    cv2.putText(img,f"STUDENT NAME:{j}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                    cv2.putText(img,f"DEPARTMENT:{n}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                    cv2.putText(img,f"ADDRESST:{k}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                    
                    self.mar_attendence(i,j,n,k)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
                coord=[x,y,w,h]
            return coord
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)== 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
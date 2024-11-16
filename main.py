from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import tkinter
from time import strftime
from datetime import datetime
import os
from student import Student
from train import train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import developer
from help import help

class FACE_RECOGNITION_SYSTEM_SOFTWARE_SUING_PYTHON:
    def __init__(self,root):
        self.root=root
        self.root.geometry("2000x1080+0+0")
        self.root.title("FACE RECOGNITION SYSTEM SOFTWARE")
        
        
        
        #First Image
        img = Image.open(r"img\1.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=430,height=130)
        
        #Second Image
        img1 = Image.open(r"img\2.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=430,y=0,width=430,height=130)
        
        
        #Third Image
        img2 = Image.open(r"img\3.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=860,y=0,width=430,height=130)
        
      #Background Image
        img3 = Image.open(r"img\bg.png")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red",)
        title_lbl.place(x=-130,y=0,width=1530,height=45)
        
        def time():
          string = strftime('%H:%M:%S: %p')
          lbl.config(text = string)
          lbl.after(1000, time)
          
        lbl = Label(title_lbl,font=('times new roman',14,'bold'),bg="white",fg="red")
        lbl.place(x=100,y=0,width=200,height=45)
        time()
      
        
        
         #Student button
        img4 = Image.open(r"img\dev.jpg")
        img4=img4.resize((250,200),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=130,y=100,width=220,height=150)
        
        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=130,y=210,width=220,height=40)
        
        #Detect face button
        img5 = Image.open(r"img\detect.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.detect_face)
        b2.place(x=430,y=100,width=220,height=150)
        
        b2_2=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.detect_face,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=430,y=210,width=220,height=40)
        
        #Attendence button
        img6 = Image.open(r"img\attendence.jpeg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b3.place(x=730,y=100,width=220,height=150)
        
        b3_3=Button(bg_img,text="ATTENDENCE",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_3.place(x=730,y=210,width=220,height=40)
        
         #Help button
        img7 = Image.open(r"img\helpp.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b4.place(x=1030,y=100,width=220,height=150)
        
        b4_4=Button(bg_img,text="HELPDESK",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_4.place(x=1030,y=210,width=220,height=40)
        
        #Train Data button
        img8 = Image.open(r"img\train.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b5=Button(bg_img,command=self.train_data,image=self.photoimg8,cursor="hand2")
        b5.place(x=130,y=300,width=220,height=150)
        
        b5_5=Button(bg_img,text="TRAIN DATA",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_5.place(x=130,y=410,width=220,height=40)
        
        #Photos button
        img9 = Image.open(r"img\photo.png")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b6=Button(bg_img,command=self.open_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=430,y=300,width=220,height=150)
        
        b6_6=Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_6.place(x=430,y=410,width=220,height=40)
        
        #Developer button
        img10 = Image.open(r"img\developer.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.dev_data,)
        b7.place(x=730,y=300,width=220,height=150)
        
        b7_7=Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.dev_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_7.place(x=730,y=410,width=220,height=40)
        
        #exit button
        img11 = Image.open(r"img\exit.jpg")
        img11=img11.resize((100,100),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b8.place(x=1030,y=300,width=220,height=150)
        
        b8_8=Button(bg_img,text="EXIT",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_8.place(x=1030,y=410,width=220,height=40) 
#######image function##
    def open_img(self):
        os.startfile("data")
      #==========Function Button ====================
      
    def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)
      
    def train_data(self):
      self.new_window=Toplevel(self.root)
      self.app=train(self.new_window)
      
    def detect_face(self):
      self.new_window=Toplevel(self.root)
      self.app=Face_Recognition(self.new_window)
      
    def attendence_data(self):
      self.new_window=Toplevel(self.root)
      self.app=Attendence(self.new_window)
      
    def dev_data(self):
      self.new_window=Toplevel(self.root)
      self.app=developer(self.new_window)
    
    def help_data(self):
      self.new_window=Toplevel(self.root)
      self.app=help(self.new_window)
        
    def iExit(self):
      self.iExit=tkinter.messagebox.askyesno("Fac Recognition","Are you sure to exit project",parent=self.root)
      if self.iExit >0:
        self.root.destroy()
      else:
        return
    
        
        
if __name__ == "__main__":
    root=Tk()
    obj=FACE_RECOGNITION_SYSTEM_SOFTWARE_SUING_PYTHON(root)
    root.mainloop()
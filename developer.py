from tkinter import*
from tkinter import ttk
from typing import ItemsView
from PIL import Image,ImageTk
from tkinter import messagebox
from click import command
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("FACE RECOGNITION SYSTEM SOFTWARE")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",25,"bold"),bg="blue",fg="chartreuse",)
        title_lbl.place(x=-120,y=0,width=1550,height=45)
        
        img_top= Image.open(r"img\dev.jpg")
        img_top=img_top.resize((1920,1282),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=-140,y=46,width=1550,height=710)
        
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=415,height=340)
        
        img_top1= Image.open(r"img\devv.jpg")
        img_top1=img_top1.resize((420,420),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=-150,y=-100,width=700,height=470)
        
#DEveloper info
        title_lbl=Label(main_frame,text="Programming is learned by writing programs",font=("times new roman",14,"bold"),bg="blue",fg="chartreuse",)
        title_lbl.place(x=-100,y=300,width=600,height=45)
        
  
if __name__ == "__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()
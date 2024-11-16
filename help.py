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
class help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("FACE RECOGNITION SYSTEM SOFTWARE")
        
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",25,"bold"),bg="blue",fg="red",)
        title_lbl.place(x=-120,y=0,width=1550,height=45)
        
        img_top= Image.open(r"img\help.jpg")
        img_top=img_top.resize((1920,1282),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=-140,y=46,width=1550,height=710)
        
        title_lbl1=Label(self.root,text="Email:zalam5577@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="red",)
        title_lbl1.place(x=450,y=400,width=370,height=45)
        
        
        

if __name__ == "__main__":
    root=Tk()
    obj=help(root)
    root.mainloop()
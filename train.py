from tkinter import*
from tkinter import ttk
from typing import ItemsView
from PIL import Image,ImageTk
from tkinter import messagebox
from click import command
import mysql.connector
import cv2
import os
import numpy as np


class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("FACE RECOGNITION SYSTEM SOFTWARE")
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",25,"bold"),bg="white",fg="red",)
        title_lbl.place(x=-120,y=0,width=1550,height=45)
        
        img_top= Image.open(r"img\train1.jpg")
        img_top=img_top.resize((1275,325),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=-140,y=53,width=1550,height=250)
        
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=-130,y=300,width=1415,height=50)
        
        img_bottom= Image.open(r"img\jj.png")
        img_bottom=img_bottom.resize((1275,325),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=-60,y=350,width=1390,height=300)  
        
    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Grey Scale
            imageNP = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training", imageNP)
            cv2.waitKey(100)  # Wait for a short time to view the image

        ids = np.array(ids)

    # Train the classifier and save
        s = cv2.face.LBPHFaceRecognizer_create()
        s.train(faces, ids)
        s.write("classifier.xml")
        cv2.destroyAllWindows()  # Ensure all OpenCV windows are closed
        messagebox.showinfo("Result", "Training dataset completed successfully!")
        
if __name__ == "__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()        
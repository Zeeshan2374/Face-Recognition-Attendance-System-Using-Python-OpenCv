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
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("FACE RECOGNITION SYSTEM SOFTWARE")
        
        ###VARiables
        self.var_atten_id=StringVar()
        self.var_atten_usn=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_status=StringVar()
        
        
        #First Image
        img = Image.open(r"img\a3.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=430,height=130)
        
        #Second Image
        img1 = Image.open(r"img\a1.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=430,y=0,width=430,height=130)
        
        #Third Image
        img2 = Image.open(r"img\a2.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=860,y=0,width=430,height=130)
        
         #Background Image
        img3 = Image.open(r"img\bg2.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="dark green",)
        title_lbl.place(x=-120,y=0,width=1530,height=45)
        
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=0,width=1400,height=515)
        
        #Left Label Frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="ATTENDENCE DETAILS",font=("times new roman",12,"bold"))
        Left_frame.place(x=2,y=10,width=660,height=500)
        
        #Left Image
        img_left= Image.open(r"img\a4.jpg")
        img_left=img_left.resize((800,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=2,y=0,width=654,height=130)
        
        left_inside_frame = Frame(bg_img,bd=2,relief=RAISED,bg="white")
        left_inside_frame.place(x=6,y=165,width=657,height=345)
        
        #labels and entry
        #Attendnece id
        attendanceId_label=Label(left_inside_frame,text=" STUDENT USN",font=("times new roman",9,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=20,sticky=W)
        
        student_usn_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=30,font=("times new roman",9,"bold"))
        student_usn_entry.grid(row=0,column=1,padx=10,pady=20,sticky=W)
        
        
        #Student Name
        student_name_label=Label(left_inside_frame,text="STUDENT NAME",font=("times new roman",9,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=20,sticky=W)
        
        student_name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_usn,width=30,font=("times new roman",9,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=20,sticky=W)
        
        #Student Name
        student_name_label=Label(left_inside_frame,text="DEPARTMENT",font=("times new roman",9,"bold"),bg="white")
        student_name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        student_name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=30,font=("times new roman",9,"bold"))
        student_name_entry.grid(row=1,column=1,padx=10,pady=20,sticky=W)
        
        #Student Name
        student_name_label=Label(left_inside_frame,text="ADDRESS",font=("times new roman",9,"bold"),bg="white")
        student_name_label.grid(row=1,column=2,padx=10,pady=20,sticky=W)
        
        student_name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=30,font=("times new roman",9,"bold"))
        student_name_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Student Name
        student_name_label=Label(left_inside_frame,text="TIME:",font=("times new roman",9,"bold"),bg="white")
        student_name_label.grid(row=2,column=0,padx=10,pady=20,sticky=W)
        
        student_name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=30,font=("times new roman",9,"bold"))
        student_name_entry.grid(row=2,column=1,padx=10,pady=20,sticky=W)
        
        #Student Name
        student_name_label=Label(left_inside_frame,text="DATE:",font=("times new roman",9,"bold"),bg="white")
        student_name_label.grid(row=2,column=2,padx=10,pady=20,sticky=W)
        
        student_name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=30,font=("times new roman",9,"bold"))
        student_name_entry.grid(row=2,column=3,padx=10,pady=20,sticky=W)
        
        
        
        student_gender_label=Label(left_inside_frame,text="ATENDENCE STATUS",font=("times new roman",9,"bold"),bg="white")
        student_gender_label.grid(row=3,column=0,padx=10,pady=20,sticky=W)
        
        gender_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_status,font=("times new roman",9,"bold"),state="read only",width=22)
        gender_combo['values']=("STATUS","ABSENT","PRESENT")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=1,padx=2,pady=20,sticky=W)
        
        #Button Frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=680,height=30)
        
        #Save Botton
        save_btn=Button(btn_frame,text="IMPORT CSV",command=self.importCsv,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        #Update Botton
        update_btn=Button(btn_frame,text="EXPORT CSV",command=self.exportCsv,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        #Delete Botton
        delete_btn=Button(btn_frame,text="UPDATE",width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        #Reset Botton
        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        #Right Label Frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="ATTENDENCE DETAILS",font=("times new roman",12,"bold"))
        right_frame.place(x=665,y=10,width=610,height=500)
        
        #Button Frame 2
        table_frame1=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame1.place(x=0,y=0,width=605,height=475)
        
##Scrool bar & table
        scroll_x=ttk.Scrollbar(table_frame1,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame1,orient=VERTICAL)
        
        self.AttendencereportTable=ttk.Treeview(table_frame1,columns=("0","1","2","3","4","5","6"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendencereportTable.xview) 
        scroll_y.config(command=self.AttendencereportTable.yview)   
        
        self.AttendencereportTable.heading("0",text="ATTENDENCE ID")
        self.AttendencereportTable.heading("1",text="STUDENT USN")
        self.AttendencereportTable.heading("2",text="STUDENT NAME")
        self.AttendencereportTable.heading("3",text="DEPARTMENT")
        self.AttendencereportTable.heading("4",text="TIME")
        self.AttendencereportTable.heading("5",text="DATE")
        self.AttendencereportTable.heading("6",text="ATTENDENCE STATUS")
        
        self.AttendencereportTable["show"]="headings"

        self.AttendencereportTable.column("0",width=100)
        self.AttendencereportTable.column("1",width=100)
        self.AttendencereportTable.column("2",width=100)
        self.AttendencereportTable.column("3",width=100)
        self.AttendencereportTable.column("4",width=100)
        self.AttendencereportTable.column("5",width=100)
        self.AttendencereportTable.column("6",width=100)
        
        self.AttendencereportTable.pack(fill=BOTH,expand=1)
        
        
        self.AttendencereportTable.bind("<ButtonRelease>",self.get_cursor)
#fetch data
    def fetchData(self,rows):
        self.AttendencereportTable.delete(*self.AttendencereportTable.get_children())
        for i in rows:
            self.AttendencereportTable.insert("",END,values=i)
#import csv            
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="OPEN CSV",filetypes=(("CSV FILE","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
#Export Export
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("WARNING","NO DATA FOUND TO EXPORT",parent=self.root)
                return False
            fln=fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="OPEN CSV",filetypes=(("CSV FILE","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("DATA EXPORT","YOUR DATA EXPORTED SUCCESSFULY TO"+os.path.basename(fln)+"SUCCESSFULLY")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row=self.AttendencereportTable.focus()
        content=self.AttendencereportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_usn.set(rows[1])
        self.var_atten_name.set(rows[2]) 
        self.var_atten_dep.set(rows[3]) 
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_status.set(rows[6])   
        
        #reset
    def reset_data(self):
            
        self.var_atten_id.set("")
        self.var_atten_usn.set("")
        self.var_atten_name.set("") 
        self.var_atten_dep.set("") 
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("")   
        
if __name__ == "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()
        
from tkinter import*
from tkinter import ttk
from typing import ItemsView
from PIL import Image,ImageTk
from tkinter import messagebox
from click import command
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("FACE RECOGNITION SYSTEM SOFTWARE")
        
        #==============Variables==========
        
        self.var_DEPARTMENT=StringVar()
        self.var_COURSE=StringVar()
        self.var_YEAR=StringVar()
        self.var_SEMESTER=StringVar()
        self.var_STUDENT_USN=StringVar()
        self.var_STUDENT_NAME=StringVar()
        self.var_DATE_OF_BIRTH=StringVar()
        self.var_AGE=StringVar()
        self.var_GENDER=StringVar()
        self.var_BLOOD_GROUP=StringVar()
        self.var_ADDRESS=StringVar()
        self.var_EMAIL=StringVar()
        self.var_STUDENT_PHONE_NO=StringVar()
        self.var_PARENT_PHONE_NO=StringVar()  
            
        
        #First Image
        img = Image.open(r"C:\Users\t14\Desktop\FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE USING PYTHON\img\4.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=430,height=130)
        
        #Second Image
        img1 = Image.open(r"C:\Users\t14\Desktop\FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE USING PYTHON\img\5.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=430,y=0,width=430,height=130)
        
        
        #Third Image
        img2 = Image.open(r"C:\Users\t14\Desktop\FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE USING PYTHON\img\6.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=860,y=0,width=430,height=130)
        
         #Background Image
        img3 = Image.open(r"C:\Users\t14\Desktop\FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE USING PYTHON\img\bg2.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="dark green",)
        title_lbl.place(x=-0,y=0,width=1530,height=45)
      
        #Main Frame  
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=0,width=1400,height=515)
        
        #Left Label Frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Left_frame.place(x=2,y=10,width=660,height=500)
        
        #Left Image
        img_left= Image.open(r"C:\Users\t14\Desktop\FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE USING PYTHON\img\8.jpg")
        img_left=img_left.resize((800,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=2,y=0,width=654,height=130)
        
        #Current Course Information
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="CURRENT COURSE INFORMATION",font=("times new roman",12,"bold"))
        current_course_frame.place(x=2,y=130,width=654,height=100)
        
        #Department
        dep_label=Label(current_course_frame,text="DEPARTMENT",font=("times new roman",9,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_DEPARTMENT,font=("times new roman",9,"bold"),state="read only",width=22)
        dep_combo['values']=("SELECT DEPARTMENT","CSE","CIVIL","ELECTRICAL","MECHANICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Course
        course_label=Label(current_course_frame,text="DEPARTMENT",font=("times new roman",9,"bold"),bg="white")
        course_label.grid(row=0,column=0,padx=10)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_COURSE,font=("times new roman",9,"bold"),state="read only",width=22)
        course_combo['values']=("SELECT COURSE","DIPLOMA","BE","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year
        year_label=Label(current_course_frame,text="DEPARTMENT",font=("times new roman",9,"bold"),bg="white")
        year_label.grid(row=0,column=0,padx=10)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_YEAR,font=("times new roman",9,"bold"),state="read only",width=22)
        year_combo['values']=("SELECT YEAR","FIRST YEAR","SECOND YEAR","THIRD YEAR","FINAL YEAR")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        sem_label=Label(current_course_frame,text="DEPARTMENT",font=("times new roman",9,"bold"),bg="white")
        sem_label.grid(row=0,column=0,padx=10)
        
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_SEMESTER,font=("times new roman",9,"bold"),state="read only",width=22)
        sem_combo['values']=("SELECT SEMESTER","1","2","3","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="CLASS STUDENT INFORMATION",font=("times new roman",12,"bold"))
        class_student_frame.place(x=2,y=230,width=654,height=246)
        
        #Student USN
        student_usn_label=Label(class_student_frame,text="STUDENT USN",font=("times new roman",9,"bold"),bg="white")
        student_usn_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        student_usn_entry=ttk.Entry(class_student_frame,textvariable=self.var_STUDENT_USN,width=30,font=("times new roman",9,"bold"))
        student_usn_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        #Student Name
        student_name_label=Label(class_student_frame,text="STUDENT NAME",font=("times new roman",9,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_STUDENT_NAME,width=30,font=("times new roman",9,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #Student DOB
        student_dob_label=Label(class_student_frame,text="DATE OF BIRTH",font=("times new roman",9,"bold"),bg="white")
        student_dob_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        student_dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_DATE_OF_BIRTH,width=30,font=("times new roman",9,"bold"))
        student_dob_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Student Age
        student_age_label=Label(class_student_frame,text="AGE",font=("times new roman",9,"bold"),bg="white")
        student_age_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        student_age_entry=ttk.Entry(class_student_frame,textvariable=self.var_AGE,width=30,font=("times new roman",9,"bold"))
        student_age_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Student Gender
        student_gender_label=Label(class_student_frame,text="GENDER",font=("times new roman",9,"bold"),bg="white")
        student_gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_GENDER,font=("times new roman",9,"bold"),state="read only",width=22)
        gender_combo['values']=("MALE","FEMALE","OTHER")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=2,sticky=W)
        
        #Student Blood Group
        student_blood_label=Label(class_student_frame,text="BLOOD GROUP",font=("times new roman",9,"bold"),bg="white")
        student_blood_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        student_gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_BLOOD_GROUP,width=30,font=("times new roman",9,"bold"))
        student_gender_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Student Address
        student_address_label=Label(class_student_frame,text="ADDRESS",font=("times new roman",9,"bold"),bg="white")
        student_address_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        student_address_entry=ttk.Entry(class_student_frame,textvariable=self.var_ADDRESS,width=30,font=("times new roman",9,"bold"))
        student_address_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #Student Email
        student_email_label=Label(class_student_frame,text="EMAIL",font=("times new roman",9,"bold"),bg="white")
        student_email_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        student_email_entry=ttk.Entry(class_student_frame,textvariable=self.var_EMAIL,width=30,font=("times new roman",9,"bold"))
        student_email_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Student Contact Number
        student_contact_label=Label(class_student_frame,text="STUDENT PHONE NO.",font=("times new roman",9,"bold"),bg="white")
        student_contact_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        student_contact_entry=ttk.Entry(class_student_frame,textvariable=self.var_STUDENT_PHONE_NO,width=30,font=("times new roman",9,"bold"))
        student_contact_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Parents Contact Number
        parents_contact_label=Label(class_student_frame,text="PARENT'S PHONE NO.",font=("times new roman",9,"bold"),bg="white")
        parents_contact_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        parents_contact_entry=ttk.Entry(class_student_frame,textvariable=self.var_PARENT_PHONE_NO,width=30,font=("times new roman",9,"bold"))
        parents_contact_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #Radio Button 1
        self.var_RADIO1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_RADIO1,text="TAKE PHOTO SAMPLE",value="YES")
        radiobtn1.grid(row=7,column=0)
        
         #Radio Button 2
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_RADIO1,text="NO SAMPLE DETECTED",value="NO")
        radiobtn2.grid(row=7,column=1)
        
        #Button Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=175,width=680,height=30)
        
        #Save Botton
        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        #Update Botton
        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        #Delete Botton
        delete_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        #Reset Botton
        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=22,font=("times new roman",9,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        #Button Frame 2
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=200,width=680,height=40)
        
        #Take Photo Sample Botton
        take_photo_sample_btn=Button(btn_frame1,command=self.generate_dataset,text="TAKE A PHOTO SAMPLE",width=45,font=("times new roman",9,"bold"),bg="blue",fg="white")
        take_photo_sample_btn.grid(row=1,column=0)
        
        #Update Photo Sample Botton
        update_photo_sample_btn=Button(btn_frame1,text="UPDATE A PHOTO SAMPLE",width=45,font=("times new roman",9,"bold"),bg="blue",fg="white")
        update_photo_sample_btn.grid(row=1,column=1)
        
        #Right Label Frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        right_frame.place(x=665,y=10,width=610,height=500)
        
        img_right= Image.open(r"C:\Users\t14\Desktop\FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE USING PYTHON\img\7.jpg")
        img_right=img_right.resize((800,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=654,height=130)
        
        #Search System
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="SEARCH SYSTEM",font=("times new roman",12,"bold"))
        search_frame.place(x=2,y=130,width=654,height=60)
    
        #Search Bar
        search_label=Label(search_frame,text="SEARCH BY",font=("times new roman",9,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        #Search Combo Box
        search_combo=ttk.Combobox(search_frame,font=("times new roman",9,"bold"),state="read only",width=15)
        search_combo['values']=("SELECT","STUDENT USN","NAME","STUDENT PHONE NO.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        search_entry=ttk.Entry(search_frame,width=30,font=("times new roman",9,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        #Search Botton
        search_btn=Button(search_frame,text="SEARCH",width=10,font=("times new roman",9,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4) 
        
        #Show All Botton
        show_btn=Button(search_frame,text="SHOW ALL",width=10,font=("times new roman",9,"bold"),bg="blue",fg="white")
        show_btn.grid(row=0,column=4,padx=4)
        
        #Table Frame
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
        table_frame.place(x=2,y=190,width=600,height=285) 
        
        #Scroll Bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
                               
        self.student_table=ttk.Treeview(table_frame,column=('DEPARTMENT','COURSE','YEAR','SEMESTER','STUDENT USN','STUDENT NAME',"DATE OF BIRTH","AGE","GENDER","BLOOD GROUP","ADDRESS","EMAIL","STUDENT PHONE NO.","PARENT'S PHONE NO.","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("DEPARTMENT",text="DEPARTMENT")
        self.student_table.heading("COURSE",text="COURSE")
        self.student_table.heading("YEAR",text="YEAR")
        self.student_table.heading("SEMESTER",text="SEMESTER")
        self.student_table.heading("STUDENT USN",text="STUDENT USN")
        self.student_table.heading("STUDENT NAME",text="STUDENT NAME")
        self.student_table.heading("DATE OF BIRTH",text="DATE OF BIRTH")
        self.student_table.heading("AGE",text="AGE")
        self.student_table.heading("GENDER",text="GENDER")
        self.student_table.heading("BLOOD GROUP",text="BLOOD GROUP")
        self.student_table.heading("ADDRESS",text="ADDRESS")
        self.student_table.heading("EMAIL",text="EMAIL")
        self.student_table.heading("STUDENT PHONE NO.",text="STUDENT PHONE NO.")
        self.student_table.heading("PARENT'S PHONE NO.",text="PARENT'S PHONE NO.")
        self.student_table.heading("photo",text="PHOTO SAMPLE STATUS")
        self.student_table["show"]="headings"
        
        self.student_table.column("DEPARTMENT",width=100)
        self.student_table.column("COURSE",width=100)
        self.student_table.column("YEAR",width=100)
        self.student_table.column("SEMESTER",width=100)
        self.student_table.column("STUDENT USN",width=120)
        self.student_table.column("STUDENT NAME",width=150)
        self.student_table.column("DATE OF BIRTH",width=100)
        self.student_table.column("AGE",width=100)
        self.student_table.column("GENDER",width=100)
        self.student_table.column("BLOOD GROUP",width=100)
        self.student_table.column("ADDRESS",width=150)
        self.student_table.column("EMAIL",width=150)
        self.student_table.column("STUDENT PHONE NO.",width=150)
        self.student_table.column("PARENT'S PHONE NO.",width=150)
        self.student_table.column("photo",width=150)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    
    #===========function Decleration============
    
    def add_data(self):
        if self.var_DEPARTMENT.get()=="SELECT DEPARTMENT" or self.var_STUDENT_NAME.get()=="" or self.var_STUDENT_USN.get()=="" or self.var_STUDENT_PHONE_NO.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="2374",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_DEPARTMENT.get(),
                                                                                                                self.var_COURSE.get(),
                                                                                                                self.var_YEAR.get(),
                                                                                                                self.var_SEMESTER.get(),
                                                                                                                self.var_STUDENT_USN.get(),
                                                                                                                self.var_STUDENT_NAME.get(),
                                                                                                                self.var_DATE_OF_BIRTH.get(),
                                                                                                                self.var_AGE.get(),
                                                                                                                self.var_GENDER.get(),
                                                                                                                self.var_BLOOD_GROUP.get(),
                                                                                                                self.var_ADDRESS.get(),
                                                                                                                self.var_EMAIL.get(),
                                                                                                                self.var_STUDENT_PHONE_NO.get(),
                                                                                                                self.var_PARENT_PHONE_NO.get(),
                                                                                                                self.var_RADIO1.get(),
                                                                                    
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Succes","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    ###Fetch Data########
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="2374",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()
        
#Get cursor###########
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
    
        self.var_DEPARTMENT.set(data[0]),
        self.var_COURSE.set(data[1]),
        self.var_YEAR.set(data[2]),
        self.var_SEMESTER.set(data[3]),
        self.var_STUDENT_USN.set(data[4]),
        self.var_STUDENT_NAME.set(data[5]),
        self.var_DATE_OF_BIRTH.set(data[6]),
        self.var_AGE.set(data[7]),
        self.var_GENDER.set(data[8]),
        self.var_BLOOD_GROUP.set(data[9]),
        self.var_ADDRESS.set(data[10]),
        self.var_EMAIL.set(data[11]),
        self.var_STUDENT_PHONE_NO.set(data[12]),
        self.var_PARENT_PHONE_NO.set(data[13]),
        self.var_RADIO1.set(data[14])
        
        ####################Update Function=====================
    def update_data(self):
        if self.var_DEPARTMENT.get()=="SELECT DEPARTMENT" or self.var_STUDENT_NAME.get()=="" or self.var_STUDENT_USN.get()=="" or self.var_STUDENT_PHONE_NO.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if  Update>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="2374",database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update student set DEPARTMENT=%s,COURSE=%s,YEAR=%s,SEMESTER=%s,STUDENT_NAME=%s,DATE_OF_BIRTH=%s,AGE=%s,GENDER=%s,BLOOD_GROUP=%s,ADDRESS=%s,EMAIL=%s,STUDENT_PHONE_NO=%s,PARENT_PHONE_NO=%s,PHOTO_SAMPLE_STATUS=%s where STUDENT_USN=%s",(
                            
                                                                                                                                                                                                                                                                    self.var_DEPARTMENT.get(),
                                                                                                                                                                                                                                                                    self.var_COURSE.get(),
                                                                                                                                                                                                                                                                    self.var_YEAR.get(),
                                                                                                                                                                                                                                                                    self.var_SEMESTER.get(),
                                                                                                                                                                                                                                                                    self.var_STUDENT_NAME.get(),
                                                                                                                                                                                                                                                                    self.var_DATE_OF_BIRTH.get(),
                                                                                                                                                                                                                                                                    self.var_AGE.get(),
                                                                                                                                                                                                                                                                    self.var_GENDER.get(),
                                                                                                                                                                                                                                                                    self.var_BLOOD_GROUP.get(),
                                                                                                                                                                                                                                                                    self.var_ADDRESS.get(),
                                                                                                                                                                                                                                                                    self.var_EMAIL.get(),
                                                                                                                                                                                                                                                                    self.var_STUDENT_PHONE_NO.get(),
                                                                                                                                                                                                                                                                    self.var_PARENT_PHONE_NO.get(),
                                                                                                                                                                                                                                                                    self.var_RADIO1.get(),
                                                                                                                                                                                                                                                                    self.var_STUDENT_USN.get()
                                                                                                                                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Successfully Upadated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)               
######Delete function#######                       
            
    def delete_data(self):
        if self.var_STUDENT_USN.get()=="":
            messagebox.showerror("Error","STUDENT USN must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete the student detail",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="2374",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where STUDENT_USN=%s"
                    val=(self.var_STUDENT_USN.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student detail",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
####Reset Function ######
    def reset_data(self):
        self.var_DEPARTMENT.set("Select Department")
        self.var_COURSE.set("Select Course")
        self.var_YEAR.set("Select Year")
        self.var_SEMESTER.set("Select Semester")
        self.var_STUDENT_USN.set("")
        self.var_STUDENT_NAME.set("")
        self.var_DATE_OF_BIRTH.set("")
        self.var_AGE.set("")
        self.var_GENDER.set("Select Gender")
        self.var_BLOOD_GROUP.set("")
        self.var_ADDRESS.set("")
        self.var_EMAIL.set("")
        self.var_STUDENT_PHONE_NO.set("")
        self.var_PARENT_PHONE_NO.set("")
#####Generate data set and take photo sample##################
    def generate_dataset(self):
        if self.var_DEPARTMENT.get()=="SELECT DEPARTMENT" or self.var_STUDENT_NAME.get()=="" or self.var_STUDENT_USN.get()=="" or self.var_STUDENT_PHONE_NO.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="2374",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set DEPARTMENT=%s,COURSE=%s,YEAR=%s,SEMESTER=%s,STUDENT_NAME=%s,DATE_OF_BIRTH=%s,AGE=%s,GENDER=%s,BLOOD_GROUP=%s,ADDRESS=%s,EMAIL=%s,STUDENT_PHONE_NO=%s,PARENT_PHONE_NO=%s,PHOTO_SAMPLE_STATUS=%s where STUDENT_USN=%s",(
                            
                                                                                                                                                                                                                                                                    self.var_DEPARTMENT.get(),
                                                                                                                                                                                                                                                                    self.var_COURSE.get(),
                                                                                                                                                                                                                                                                    self.var_YEAR.get(),
                                                                                                                                                                                                                                                                    self.var_SEMESTER.get(),
                                                                                                                                                                                                                                                                    self.var_STUDENT_NAME.get(),
                                                                                                                                                                                                                                                                    self.var_DATE_OF_BIRTH.get(),
                                                                                                                                                                                                                                                                    self.var_AGE.get(),
                                                                                                                                                                                                                                                                    self.var_GENDER.get(),
                                                                                                                                                                                                                                                                    self.var_BLOOD_GROUP.get(),
                                                                                                                                                                                                                                                                    self.var_ADDRESS.get(),
                                                                                                                                                                                                                                                                    self.var_EMAIL.get(),
                                                                                                                                                                                                                                                                    self.var_STUDENT_PHONE_NO.get(),
                                                                                                                                                                                                                                                                    self.var_PARENT_PHONE_NO.get(),
                                                                                                                                                                                                                                                                    self.var_RADIO1.get(),
                                                                                                                                                                                                                                                                    self.var_STUDENT_USN.get()==id+1
                                                                                                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
##########Load predefined data on face frontal from opencv###################
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) #scaling factor =1.3 / #minimum neighbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generated data set successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                

                
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
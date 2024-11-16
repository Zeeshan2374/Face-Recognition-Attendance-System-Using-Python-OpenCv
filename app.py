import tkinter as tk
from tkinter import Toplevel, messagebox
from PIL import Image, ImageTk
import random
import smtplib
from email.mime.text import MIMEText
import subprocess  # Import subprocess to run main.py

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("FACE RECOGNITION SYSTEM SOFTWARE")

        # Load and set the background image for the main window
        self.bg_image = Image.open(r"img\a3.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a label to hold the main background image
        self.background_label = tk.Label(root, image=self.bg_photo)
        self.background_label.place(relwidth=1, relheight=1)

        # Background Image
        img3 = Image.open(r"img\3.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = tk.Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=710)

        # Create a frame for the login form
        self.frame = tk.Frame(root, bg='white', bd=5)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Load and set the background image for the frame
        frame_bg_image = Image.open(r"img\3.jpg")
        frame_bg_image = frame_bg_image.resize((550, 450), Image.LANCZOS)
        self.frame_bg_photo = ImageTk.PhotoImage(frame_bg_image)

        # Create a label to hold the frame background image
        frame_background_label = tk.Label(self.frame, image=self.frame_bg_photo)
        frame_background_label.place(relwidth=1, relheight=1)

        # Create and place the username label and entry
        label_username = tk.Label(self.frame, text="Username:", bg='red', font=('Arial', 12))
        label_username.pack(pady=(10, 5))

        self.entry_username = tk.Entry(self.frame, font=('Arial', 12))
        self.entry_username.pack(pady=5)

        # Create and place the password label and entry
        label_password = tk.Label(self.frame, text="Password:", bg='red', font=('Arial', 12))
        label_password.pack(pady=(10, 5))

        self.entry_password = tk.Entry(self.frame, show="*", font=('Arial', 12))
        self.entry_password.pack(pady=5)

        # Create and place the login button
        self.button_login = tk.Button(self.frame, text="Login", command=self.validate_login, bg='red', fg='white', font=('Arial', 12))
        self.button_login.pack(pady=(20, 10))
        
        # Load users from the users.txt file
        self.users = self.load_users()

        # Set focus to the username entry field
        self.entry_username.focus()

        # Login attempts counter
        self .login_attempts = 0
        self.max_attempts = 3

        # To store the generated OTP
        self.generated_otp = None
        self.user_email = None  # You can store user's email here if you modify the registration

    def load_users(self):
        users = {}
        try:
            with open("users.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(",")
                        if len(parts) == 3:
                            username, password, email = parts
                            users[username] = (password, email)
                        else:
                            print(f"Skipping line: {line}. Expected 3 values but got {len(parts)}.")
        except FileNotFoundError:
            messagebox.showerror("Error", "User  data file not found.")
        return users

    def validate_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username in self.users and self.users[username][0] == password:
            self.user_email = self.users[username][1]
            self.send_otp_email(self.user_email)  # Send OTP to the user's email
            self.show_otp_window()  # Show the OTP window
        else:
            self.login_attempts += 1
            if self.login_attempts >= self.max_attempts:
                messagebox.showerror("Error", "Maximum login attempts exceeded.")
                self.root.quit()  # Close the application
            else:
                messagebox.showerror("Error", "Invalid username or password. Please try again.")

    def send_otp_email(self, email):
        self.generated_otp = random.randint(100000, 999999)  # Generate a random 6-digit OTP
        subject = "Your OTP Code"
        body = f"Your OTP code is: {self.generated_otp}"

        # Set up the email server and send the email
        try:
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = "ssse2374@gmail.com"  # Replace with your email
            msg['To'] = email

            with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Replace with your SMTP server
                server.starttls()
                server.login("ssse2374@gmail.com", "vpmt fapb sbkd copj")  # Replace with your email and password
                server.send_message(msg)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send OTP email: {str(e)}")

    def show_otp_window(self):
        self.otp_window = Toplevel(self.root)
        self.otp_window.title("Enter OTP")
        self.otp_window.geometry("300x200")

        label_otp = tk.Label(self.otp_window, text="Enter OTP:", font=('Arial', 12))
        label_otp.pack(pady=10)

        self.entry_otp = tk.Entry(self.otp_window, font=('Arial', 12))
        self.entry_otp.pack(pady=5)

        button_verify = tk.Button(self.otp_window, text="Verify OTP", command=self.verify_otp, bg='blue', fg='white', font=('Arial', 12))
        button_verify.pack(pady=20)

    def verify_otp(self):
        entered_otp = self.entry_otp.get()
        if entered_otp == str(self.generated_otp):
            self.otp_window.destroy()  # Close the OTP window
            self.run_main_script()  # Call the method to run main.py
        else:
            messagebox.showerror("Error", "Invalid OTP. Please try again.")

    def run_main_script(self):
        subprocess.Popen(["python", r"C:\Users\t14\Desktop\FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE USING PYTHON\main.py"])  # Use raw string
        self.root.quit()  # Close the login application window if needed

    def open_registration_window(self):
        messagebox.showinfo("Info", "Registration window is not implemented yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import ttk, PhotoImage
import os
import csv

# Initialize the main window
window = tk.Tk()
window.geometry("1280x720")
window.resizable(True, False)
window.title("Attendance System")
window.configure(background='#262523')

# Function definitions (placeholders)
def show_frame1():
    frame1.pack(fill='both', expand=True)
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()

def show_frame2():
    frame2.pack(fill='both', expand=True)
    frame1.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()

def show_frame3():
    frame3.pack(fill='both', expand=True)
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()

def show_frame4():
    frame4.pack(fill='both', expand=True)
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()

def TrackImages():
    pass

def change_pass():
    pass

def contact():
    pass

def clear():
    pass

def clear2():
    pass

def TakeImages():
    pass

def psw():
    pass

def tick():
    pass

# Title label
message3 = tk.Label(window, text="Face Recognition Based Attendance System", fg="white", bg="#262523", width=55, height=1, font=('times', 29, 'bold'))
message3.pack(pady=10)

# Date and Time Frames
frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text="Date Placeholder", fg="orange", bg="#262523", width=55, height=1, font=('times', 22, 'bold'))
datef.pack(fill='both', expand=1)

clock = tk.Label(frame3, fg="orange", bg="#262523", width=55, height=1, font=('times', 22, 'bold'))
clock.pack(fill='both', expand=1)
tick()

# Frame 1 - Attendance
frame1 = tk.Frame(window, bg="#00aeff")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

head1 = tk.Label(frame1, text="Attendance", fg="black", bg="#3ece48", font=('times', 17, 'bold'))
head1.place(x=0, y=0)

lbl3 = tk.Label(frame1, text="Attendance", width=20, fg="black", bg="#00aeff", height=1, font=('times', 17, 'bold'))
lbl3.place(x=100, y=115)

tv = ttk.Treeview(frame1, height=13, columns=('name', 'date', 'time'))
tv.column('#0', width=82)
tv.column('name', width=130)
tv.column('date', width=133)
tv.column('time', width=133)
tv.grid(row=2, column=0, padx=(0, 0), pady=(150, 0), columnspan=4)
tv.heading('#0', text='ID')
tv.heading('name', text='NAME')
tv.heading('date', text='DATE')
tv.heading('time', text='TIME')

scroll = ttk.Scrollbar(frame1, orient='vertical', command=tv.yview)
scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
tv.configure(yscrollcommand=scroll.set)

quitWindow = tk.Button(frame1, text="Quit", command=window.destroy, fg="black", bg="red", width=35, height=1, activebackground="white", font=('times', 15, 'bold'))
quitWindow.place(x=30, y=450)

# Frame 2 - Registration
frame2 = tk.Frame(window, bg="#00aeff")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

head2 = tk.Label(frame2, text="For New Registrations", fg="black", bg="#3ece48", font=('times', 17, 'bold'))
head2.grid(row=0, column=0)

lbl = tk.Label(frame2, text="Enter ID", width=20, height=1, fg="black", bg="#00aeff", font=('times', 17, 'bold'))
lbl.place(x=80, y=55)

txt = tk.Entry(frame2, width=32, fg="black", font=('times', 15, 'bold'))
txt.place(x=30, y=88)

lbl2 = tk.Label(frame2, text="Enter Name", width=20, fg="black", bg="#00aeff", font=('times', 17, 'bold'))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2, width=32, fg="black", font=('times', 15, 'bold'))
txt2.place(x=30, y=173)

message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile", bg="#00aeff", fg="black", width=39, height=1, activebackground="yellow", font=('times', 15, 'bold'))
message1.place(x=7, y=230)

message = tk.Label(frame2, text="", bg="#00aeff", fg="black", width=39, height=1, activebackground="yellow", font=('times', 16, 'bold'))
message.place(x=7, y=450)

clearButton = tk.Button(frame2, text="Clear", command=clear, fg="black", bg="#ea2a2a", width=11, activebackground="white", font=('times', 11, 'bold'))
clearButton.place(x=335, y=86)

clearButton2 = tk.Button(frame2, text="Clear", command=clear2, fg="black", bg="#ea2a2a", width=11, activebackground="white", font=('times', 11, 'bold'))
clearButton2.place(x=335, y=172)

takeImg = tk.Button(frame2, text="Take Images", command=TakeImages, fg="white", bg="blue", width=34, height=1, activebackground="white", font=('times', 15, 'bold'))
takeImg.place(x=30, y=300)

trainImg = tk.Button(frame2, text="Save Profile", command=psw, fg="white", bg="blue", width=34, height=1, activebackground="white", font=('times', 15, 'bold'))
trainImg.place(x=30, y=380)

# Frame 3 - Image Background
frame3 = tk.Frame(window)
frame3.pack_forget()  # Initially hidden

# Load image and set as background
bg_image = PhotoImage(file="png.png")  # Update path to your image
bg_label = tk.Label(frame3, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Frame 4 - About Information
frame4 = tk.Frame(window, bg="#f0f0f0")
frame4.pack_forget()  # Initially hidden

# About Paragraph
about_text = """\
This Attendance System is designed to provide a convenient and efficient way to monitor attendance using facial recognition technology. 

Features:
- Registration of new users
- Capture and save facial images
- Track and view attendance records
- User-friendly interface

Developed by: [Your Name]
Version: 1.0
"""
about_label = tk.Label(frame4, text=about_text, bg="#f0f0f0", font=('times', 16), padx=20, pady=20, wraplength=800)
about_label.pack(expand=True)

# Menubar setup
menubar = tk.Menu(window, relief='ridge', bg='#262523', fg='white', activebackground='#3ece48', activeforeground='black')

# Attendance menu
attendance_menu = tk.Menu(menubar, tearoff=0, bg='#262523', fg='white', activebackground='#3ece48', activeforeground='black')
attendance_menu.add_command(label='Home', command=show_frame3, font=('times', 14, 'bold'))
attendance_menu.add_command(label='Take Attendance', command=TrackImages, font=('times', 14, 'bold'))
attendance_menu.add_command(label='New Registration', command=show_frame2, font=('times', 14, 'bold'))
attendance_menu.add_command(label='View Attendance', command=show_frame1, font=('times', 14, 'bold'))

# File menu
filemenu = tk.Menu(menubar, tearoff=0, bg='#262523', fg='white', activebackground='#3ece48', activeforeground='black')
filemenu.add_command(label='Change Password', command=change_pass, font=('times', 14, 'bold'))
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.destroy, font=('times', 14, 'bold'))

# Help menu
help_menu = tk.Menu(menubar, tearoff=0, bg='#262523', fg='white', activebackground='#3ece48', activeforeground='black')
help_menu.add_command(label='Help', command=contact, font=('times', 14, 'bold'))
help_menu.add_command(label='About', command=show_frame4, font=('times', 14, 'bold'))

# Adding menus to menubar
menubar.add_cascade(label='Attendance', menu=attendance_menu)
menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Help', menu=help_menu)

# Adding the menu to the window
window.configure(menu=menubar)

# Initialize frame display
show_frame3()

# Start the Tkinter main loop
window.mainloop()

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import subprocess
from PIL import Image, ImageTk
from student_details import open_student_details_window
from attendance_details import open_attendance_details_window  # Importing the function from attendance_details.py
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['Project']
collection = db['time table']

def update_clock():
    now = datetime.now()
    time_label.config(text=now.strftime("%I:%M:%S %p"), fg="#800000")
    date_label.config(text=now.strftime("%B %d, %Y"), fg="#800000")
    time_label.after(1000, update_clock)

def show_time_table():
    try:
        time_table_data = list(collection.find())

        if len(time_table_data) > 0:
            # Create a new window for displaying time table
            time_table_window = tk.Toplevel(root)
            time_table_window.title("Time Table")
            time_table_window.configure(bg="#f0f0f0")

            # Create Treeview
            columns = ["Day", "8:30-9:45", "9:45-10:45", "11:10-12:10", "12:10-1:10", "1:50-2:40", "2:40-3:30"]
            tree = ttk.Treeview(time_table_window, columns=columns, show="headings")
            for col in columns:
                tree.heading(col, text=col)
            tree.pack(fill=tk.BOTH, expand=True)

            # Insert data into Treeview
            for record in time_table_data:
                values = [record.get(col, '') for col in columns]
                tree.insert('', 'end', values=values)
        else:
            messagebox.showinfo("Time Table", "No time table data found.")
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching time table data: {e}")

def run_fill_script(subject, period):
    # Run the fill.py script with selected subject and period
    try:
        subprocess.Popen(["python", "fill.py", subject, period])  # Pass selected subject and period
    except Exception as e:
        messagebox.showerror("Error", f"Error running fill.py: {e}")

def open_admin_portal():
    # Function to open the admin portal window
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Portal")

    # Student Details button with hover effect
    button_student_details = tk.Button(admin_window, text="Student Enrol", width=30, height=2, bg="#007bff", fg="#FFFFFF", font=("Arial", 14), command=lambda: open_student_details_window(root), highlightbackground="#007bff", highlightcolor="#007bff", bd=0)
    button_student_details.pack(pady=20)
    button_student_details.bind("<Enter>", on_enter)
    button_student_details.bind("<Leave>", on_leave)

    # Attendance Details button with hover effect
    button_attendance_details = tk.Button(admin_window, text="Attendance Details", width=30, height=2, bg="#007bff", fg="#FFFFFF", font=("Arial", 14), command=open_attendance_details_window, highlightbackground="#007bff", highlightcolor="#007bff", bd=0)
    button_attendance_details.pack(pady=20)
    button_attendance_details.bind("<Enter>", on_enter)
    button_attendance_details.bind("<Leave>", on_leave)

def on_enter(event):
    event.widget.config(bg="#0056b3")

def on_leave(event):
    event.widget.config(bg="#007bff")

def open_fill_attendance_window():
    fill_attendance_window = tk.Toplevel(root)
    fill_attendance_window.title("Fill Attendance")

    fill_attendance_window.configure(bg="#f0f0f0")

    subject_label = tk.Label(fill_attendance_window, text="Select Subject:", font=("Arial", 20), bg="#f0f0f0")
    subject_label.grid(row=0, column=0, padx=20, pady=20)

    subjects = ["Cloud Computing", "Machine Learning", "Soft Core", "Management Perspective", "Research Methodology", "Cryptography", "Project"]
    subject_var = tk.StringVar(fill_attendance_window)
    subject_var.set(subjects[0])
    subject_dropdown = tk.OptionMenu(fill_attendance_window, subject_var, *subjects)
    subject_dropdown.config(font=("Arial", 18))
    subject_dropdown.grid(row=0, column=1, padx=20, pady=20)

    period_label = tk.Label(fill_attendance_window, text="Select Period:", font=("Arial", 20), bg="#f0f0f0")
    period_label.grid(row=1, column=0, padx=20, pady=20)

    periods = ["8:30-9:45", "9:45-10:45", "11:10-12:10", "12:10-1:10", "1:50-2:40", "2:40-3:30"]
    period_var = tk.StringVar(fill_attendance_window)
    period_var.set(periods[0])
    period_dropdown = tk.OptionMenu(fill_attendance_window, period_var, *periods)
    period_dropdown.config(font=("Arial", 18))
    period_dropdown.grid(row=1, column=1, padx=20, pady=20)

    fill_button = tk.Button(fill_attendance_window, text="Fill", width=10, height=2, bg="#007bff", fg="#FFFFFF", font=("Arial", 14), command=lambda: run_fill_script(subject_var.get(), period_var.get()), highlightbackground="#007bff", highlightcolor="#007bff", bd=0)  # Pass selected subject and period
    fill_button.grid(row=2, columnspan=2, padx=20, pady=20)

def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

root = tk.Tk()
root.title("Real-time Face Attendance System")
root.configure(bg="#f0f0f0")

# Set window to full screen
root.attributes('-fullscreen', True)

# Load background image and resize it to fit the window
background_image = Image.open("home.png")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
background_image = background_image.resize((width, height))
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_heading = tk.Label(root, text="Real Time Face Attendance System", font=("Arial", 32), background=None, fg="#800000")
label_heading.place(relx=0.5, rely=0.1, anchor="center")

button_fill_attendance = tk.Button(root, text="Fill Attendance", width=30, height=2, bg="#007bff", fg="#FFFFFF", font=("Arial", 14), command=open_fill_attendance_window, highlightbackground="#007bff", highlightcolor="#007bff", bd=0)
button_fill_attendance.place(relx=0.5, rely=0.3, anchor="center")
button_fill_attendance.bind("<Enter>", on_enter)
button_fill_attendance.bind("<Leave>", on_leave)

button_admin_portal = tk.Button(root, text="Admin Portal", width=30, height=2, bg="#007bff", fg="#FFFFFF", font=("Arial", 14), command=open_admin_portal, highlightbackground="#007bff", highlightcolor="#007bff", bd=0)
button_admin_portal.place(relx=0.25, rely=0.5, anchor="center")
button_admin_portal.bind("<Enter>", on_enter)
button_admin_portal.bind("<Leave>", on_leave)

button_time_table = tk.Button(root, text="Time Table", command=show_time_table, width=30, height=2, bg="#007bff", fg="#FFFFFF", font=("Arial", 14), highlightbackground="#007bff", highlightcolor="#007bff", bd=0)
button_time_table.place(relx=0.75, rely=0.5, anchor="center")
button_time_table.bind("<Enter>", on_enter)
button_time_table.bind("<Leave>", on_leave)

date_label = tk.Label(root, text="", font=("Arial", 18), bg=None, fg="#008000")
date_label.place(relx=0.1, rely=0.9, anchor="center")

time_label = tk.Label(root, text="", font=("Arial", 18), bg=None, fg="#008000")
time_label.place(relx=0.9, rely=0.9, anchor="center")

update_clock()

# Bind Escape key to toggle fullscreen mode
root.bind("<Escape>", toggle_fullscreen)

root.mainloop()

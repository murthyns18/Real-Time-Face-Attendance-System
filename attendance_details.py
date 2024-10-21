import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import Calendar
from pymongo import MongoClient

def open_attendance_details_window():
    attendance_details_login_window = tk.Toplevel()
    attendance_details_login_window.title("Attendance Details Login")

    correct_username = "murthy"
    correct_password = "ns123"

    def validate_login():
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        if entered_username == correct_username and entered_password == correct_password:
            attendance_details_login_window.destroy()  
            open_attendance_data_window()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

    username_label = tk.Label(attendance_details_login_window, text="Username:", font=("Arial", 16))
    username_label.grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(attendance_details_login_window, font=("Arial", 16))
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    password_label = tk.Label(attendance_details_login_window, text="Password:", font=("Arial", 16))
    password_label.grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(attendance_details_login_window, show="*", font=("Arial", 16))
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    login_button = tk.Button(attendance_details_login_window, text="Login", width=10, height=1, bg="#007bff", fg="#FFFFFF", font=("Arial", 16), command=validate_login)
    login_button.grid(row=2, columnspan=2, padx=10, pady=10)

def display_attendance_details(attendance_data):
    attendance_dialog = tk.Toplevel()
    attendance_dialog.title("Attendance Details")

    columns = ["Name", "Register Number", "Department", "Date", "Period", "Subject"]
    for i, column in enumerate(columns):
        tk.Label(attendance_dialog, text=column, font=("Helvetica", 12)).grid(row=0, column=i, padx=10, pady=5)

    for j, data in enumerate(attendance_data):
        tk.Label(attendance_dialog, text=data.get("student_name", ""), font=("Helvetica", 12)).grid(row=j+1, column=0, padx=10, pady=5)
        tk.Label(attendance_dialog, text=data.get("register_number", ""), font=("Helvetica", 12)).grid(row=j+1, column=1, padx=10, pady=5)
        tk.Label(attendance_dialog, text=data.get("department", ""), font=("Helvetica", 12)).grid(row=j+1, column=2, padx=10, pady=5)
        tk.Label(attendance_dialog, text=data.get("date", ""), font=("Helvetica", 12)).grid(row=j+1, column=3, padx=10, pady=5)
        tk.Label(attendance_dialog, text=data.get("period", ""), font=("Helvetica", 12)).grid(row=j+1, column=4, padx=10, pady=5)
        tk.Label(attendance_dialog, text=data.get("subject", ""), font=("Helvetica", 12)).grid(row=j+1, column=5, padx=10, pady=5)

def open_attendance_data_window():
    attendance_data_window = tk.Toplevel()
    attendance_data_window.title("Attendance Data")

    subjects = ["Cloud Computing", "Machine Learning", "Soft Core", "Management Perspective", "Research Methodology", "Cryptography", "Project"]
    subject_var = tk.StringVar(attendance_data_window)
    subject_dropdown = tk.OptionMenu(attendance_data_window, subject_var, *subjects)
    subject_dropdown.config(font=("Arial", 12))
    subject_dropdown.grid(row=0, column=1, padx=10, pady=10)
    tk.Label(attendance_data_window, text="Select Subject:", font=("Arial", 16)).grid(row=0, column=0, padx=10, pady=10)

    cal = Calendar(attendance_data_window, font="Arial 14", selectmode='day', cursor="hand1", year=datetime.now().year, month=datetime.now().month, day=0)
    cal.grid(row=1, column=1, padx=10, pady=10)
    tk.Label(attendance_data_window, text="Select Date:", font=("Arial", 16)).grid(row=1, column=0, padx=10, pady=10)

    def fetch_attendance_data():
        selected_subject = subject_var.get()
        selected_date_str = cal.get_date()
        
        if selected_subject:
            if selected_date_str:
                selected_date = datetime.strptime(selected_date_str, "%m/%d/%y")
                formatted_date = selected_date.strftime("%d-%m-%Y")
            else:
                selected_date = None
                formatted_date = ""

            client = MongoClient('localhost', 27017)
            db = client['Project']
            attendance_details = db['attendance_details']

            if selected_date:
                attendance_data = list(attendance_details.find({"subject": selected_subject, "date": {"$regex": formatted_date}}, {"_id": 0}))
            else:
                attendance_data = list(attendance_details.find({"subject": selected_subject}, {"_id": 0}))

            if attendance_data:
                display_attendance_details(attendance_data)
            else:
                messagebox.showerror("Error", "No attendance data found for the selected subject and date.")
        else:
            messagebox.showerror("Error", "Please select a subject.")

    fetch_button = tk.Button(attendance_data_window, text="Fetch", width=10, height=1, bg="#007bff", fg="#FFFFFF", font=("Arial", 16), command=fetch_attendance_data)
    fetch_button.grid(row=3, column=0, padx=10, pady=10)

    def search_individual():
        def check_individual(student_name, register_number, selected_subject, formatted_date):
            client = MongoClient('localhost', 27017)
            db = client['Project']
            attendance_details = db['attendance_details']
            
            attendance_record = attendance_details.find_one({"student_name": student_name, "register_number": register_number, "subject": selected_subject, "date": formatted_date})

            if attendance_record:
                messagebox.showinfo("Attendance Found", f"{student_name} is present on {formatted_date} for {selected_subject}.")
            else:
                messagebox.showinfo("Attendance Not Found", f"{student_name} is not present on {formatted_date} for {selected_subject}.")

        individual_window = tk.Toplevel()
        individual_window.title("Search by Individual")
        
        tk.Label(individual_window, text="Student Name:", font=("Arial", 16)).grid(row=0, column=0, padx=10, pady=10)
        student_name_entry = tk.Entry(individual_window, font=("Arial", 16))
        student_name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(individual_window, text="Register Number:", font=("Arial", 16)).grid(row=1, column=0, padx=10, pady=10)
        register_number_entry = tk.Entry(individual_window, font=("Arial", 16))
        register_number_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(individual_window, text="Select Subject:", font=("Arial", 16)).grid(row=2, column=0, padx=10, pady=10)
        subject_var_individual = tk.StringVar(individual_window)
        subject_dropdown_individual = tk.OptionMenu(individual_window, subject_var_individual, *subjects)
        subject_dropdown_individual.config(font=("Arial", 12))
        subject_dropdown_individual.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(individual_window, text="Select Date:", font=("Arial", 16)).grid(row=3, column=0, padx=10, pady=10)
        cal_individual = Calendar(individual_window, font="Arial 14", selectmode='day', cursor="hand1", year=datetime.now().year, month=datetime.now().month, day=0)
        cal_individual.grid(row=3, column=1, padx=10, pady=10)

        check_button = tk.Button(individual_window, text="Check", width=10, height=1, bg="#007bff", fg="#FFFFFF", font=("Arial", 16), command=lambda: check_individual(student_name_entry.get(), register_number_entry.get(), subject_var_individual.get(), datetime.strptime(cal_individual.get_date(), "%m/%d/%y").strftime("%d-%m-%Y")))
        check_button.grid(row=4, columnspan=2, padx=10, pady=10)

    search_button = tk.Button(attendance_data_window, text="Search by Individual", width=15, height=1, bg="#007bff", fg="#FFFFFF", font=("Arial", 16), command=search_individual)
    search_button.grid(row=3, column=1, padx=10, pady=10)

# Uncomment the following lines if you're running this script directly
# root = tk.Tk()
# root.mainloop()

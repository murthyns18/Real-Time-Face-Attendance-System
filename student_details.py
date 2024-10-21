import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient

def open_student_details_window(root):
    # Function to open the student details window
    student_window = tk.Toplevel(root)
    student_window.title("Student Details")

    # Create labels and entry fields for capturing student details
    student_name_label = tk.Label(student_window, text="Student Name:", font=("Arial", 14), fg="#000000")
    student_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    student_name_entry = tk.Entry(student_window, font=("Arial", 14))
    student_name_entry.grid(row=0, column=1, padx=10, pady=5)

    register_number_label = tk.Label(student_window, text="Register Number:", font=("Arial", 14), fg="#000000")
    register_number_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    register_number_entry = tk.Entry(student_window, font=("Arial", 14))
    register_number_entry.grid(row=1, column=1, padx=10, pady=5)

    division_label = tk.Label(student_window, text="Division:", font=("Arial", 14), fg="#000000")
    division_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    division_var = tk.StringVar(student_window)
    division_options = ["A", "B"]
    division_dropdown = ttk.Combobox(student_window, textvariable=division_var, values=division_options, font=("Arial", 14), width=8)
    division_dropdown.grid(row=2, column=1, padx=10, pady=5)

    department_label = tk.Label(student_window, text="Department:", font=("Arial", 14), fg="#000000")
    department_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    department_var = tk.StringVar(student_window)
    department_options = ["MCA", "MBA", "BCA", "BCOM", "BBA"]
    department_dropdown = ttk.Combobox(student_window, textvariable=department_var, values=department_options, font=("Arial", 14), width=8)
    department_dropdown.grid(row=3, column=1, padx=10, pady=5)

    semester_label = tk.Label(student_window, text="Semester:", font=("Arial", 14), fg="#000000")
    semester_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    semester_var = tk.StringVar(student_window)
    semester_options = ["1", "2", "3", "4"]
    semester_dropdown = ttk.Combobox(student_window, textvariable=semester_var, values=semester_options, font=("Arial", 14), width=8)
    semester_dropdown.grid(row=4, column=1, padx=10, pady=5)

    year_label = tk.Label(student_window, text="Year:", font=("Arial", 14), fg="#000000")
    year_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    year_var = tk.StringVar(student_window)
    year_options = ["1", "2"]
    year_dropdown = ttk.Combobox(student_window, textvariable=year_var, values=year_options, font=("Arial", 14), width=8)
    year_dropdown.grid(row=5, column=1, padx=10, pady=5)

    def save_student_details():
        # Get values from entry fields and dropdowns
        student_name = student_name_entry.get()
        register_number = register_number_entry.get()
        division = division_var.get()
        department = department_var.get()
        semester = semester_var.get()
        year = year_var.get()

        # Check if all fields are filled
        if student_name and register_number and division and department and semester and year:
            # Connect to MongoDB
            client = MongoClient('localhost', 27017)
            db = client['Project']
            collection = db['student_details']

            # Check if same name and register number already exist in the database
            existing_student = collection.find_one({"$or": [{"student_name": student_name}, {"register_number": register_number}]})
            if existing_student:
                # Display error message if same name or register number already exist
                tk.messagebox.showerror("Error", "Student already registered!")
            else:
                # Insert student details into the database
                student_data = {
                    "student_name": student_name,
                    "register_number": register_number,
                    "division": division,
                    "department": department,
                    "semester": semester,
                    "year": year
                }
                collection.insert_one(student_data)

                # Display success message
                tk.messagebox.showinfo("Success", "Student details saved successfully!")
        else:
            # Display error message if any field is empty
            tk.messagebox.showerror("Error", "Please fill all the fields.")

    # Save button
    save_button = tk.Button(student_window, text="Save", width=8, height=1, bg="#007bff", fg="#FFFFFF", font=("Arial", 12), command=save_student_details)
    save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="n")

    student_window.mainloop()

# Testing the window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test")
    open_student_details_window(root)

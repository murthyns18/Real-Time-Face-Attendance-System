# Real-Time-Face-Attendance-System Using Python

**About**

The system uses machine learning to automate attendance by recognizing students' faces. It reduces manual effort and ensures accurate attendance marking. Students register by entering their details and uploading their images, which are used for face recognition during class sessions.

**Key Features**

**Student Registration**

Students enter their details, and their photos are taken and saved in the database.

**Automated Attendance**

During each class, the system compares the detected faces with the stored images. If a match is found, the attendance is marked. If no match is found, a notification prompts the student to register.

**Attendance Details**

Attendance details can be fetched subject-wise, date-wise, and for individual students.

**Class Timetable** Students can view their class timetable in the system.

**Hardware Requirements**

Processor: Core i3 / i5
Hard Disk: 1TB
RAM: 8 GB

**Software Requirements**

Operating System: Windows 8 or higher
Programming Language: Python
Frontend: Python Tkinter
Framework: Anaconda/Miniconda
Database: MongoDB
IDE: VS Code
Libraries: OpenCV, NumPy, Tkinter, Dlib, Pymongo, PIL

**Tools and Technologies Used**

Python
OpenCV (Computer Vision)
NumPy (Numerical Computing)
Tkinter (GUI)
Dlib (Face Detection)
Pymongo (MongoDB Connection)
PIL (Image Processing)
Algorithms Used:
HOG (Histogram of Oriented Gradients)
CNN (Convolutional Neural Networks)

**Update fill.py File**

self.client = pymongo.MongoClient("mongodb://localhost:27017/")
self.db = self.client["FaceAttendanceSystem"]
self.student_collection = self.db["student_details"]
self.attendance_collection = self.db["attendance_details"]

**Steps to Run the Real-Time Face Attendance System**

**Install Miniconda**

Download and install Miniconda from the official website.

**Set Up the Project Directory**

Locate to your project directory

**Install Required Libraries**

Open a terminal or command prompt and run the following commands to install dependencies:
pip install opencv-python numpy tkinter dlib pymongo pillow

**Set Up the Database**

Install MongoDB Compass from the MongoDB website.
Open MongoDB Compass, create a new database named FaceAttendanceSystemi inside this database. 

**create the following collections**

attendance_details
student_details
time_table

**Run the Project**

Open Miniconda or your terminal.
Navigate to your project directory and run
python gui.py

**Screenshots**

**1 : Home Page**
![image alt]()

**2 : Filling Attendance Page**
![image alt]()

**3 : Home Page**
![image alt]()

**4 : Admin Page**
![image alt]()

**5 : Admin Login Page**
![image alt]()

**6 : Student Registration Page**
![image alt]()

**7 : Attendance Details Page**
![image alt]()

**8 : Individual Details Page**
![image alt]()


**9 : Class Time Table Page**
![image alt]()



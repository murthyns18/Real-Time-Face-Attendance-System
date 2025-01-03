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


**Class Timetable** 

Students can view their class timetable in the system.


**Hardware Requirements**

1 : Processor: Core i3 / i5
2 : Hard Disk: 1TB
3 : RAM: 8 GB


**Software Requirements**

1 : Operating System: Windows 8 or higher

2 : Programming Language: Python

3 : Frontend: Python Tkinter

4 : Framework: Anaconda/Miniconda

5 : Database: MongoDB

6 : IDE: VS Code

7 : Libraries: OpenCV, NumPy, Tkinter, Dlib, Pymongo, PIL


**Tools and Technologies Used**

1 : Python

2 : OpenCV (Computer Vision)

3 : NumPy (Numerical Computing)

4 : Tkinter (GUI)

5 : Dlib (Face Detection)

6 : Pymongo (MongoDB Connection)

7 : PIL (Image Processing)


**Algorithms Used**

1 : HOG (Histogram of Oriented Gradients)

2 : CNN (Convolutional Neural Networks)



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

![image alt](https://github.com/murthyns18/Real-Time-Face-Attendance-System/blob/df445b3ea032939af591e75641cad5f46a86648b/Home.png)




**2 : Filling Attendance Page**

![image alt](https://github.com/murthyns18/Real-Time-Face-Attendance-System/blob/d34a6ee74308327f412621debf6e34e44c961bce/Filling%20Attendance.png)




**3 : Attendace Filled Page**

![image alt](https://github.com/murthyns18/Real-Time-Face-Attendance-System/blob/c0098c12b2cb938fc6fa31bc192455b71df8c1ee/Attendance%20Filled.png)




**4 : Admin Page**

![image alt](https://github.com/murthyns18/Real-Time-Face-Attendance-System/blob/07f15047cf7425cd2757fd0b4324a5c387993bd9/Admin%20Prtal.png)




**5 : Admin Login Page**

![image alt](https://github.com/murthyns18/Real-Time-Face-Attendance-System/blob/07f15047cf7425cd2757fd0b4324a5c387993bd9/Admin%20Login.png)




**6 : Student Registration Page**

![image alt](https://github.com/murthyns18/Real-Time-Face-Attendance-System/blob/c0098c12b2cb938fc6fa31bc192455b71df8c1ee/Student%20Registration.png)



**7 : Attendance Details Page**

![image alt](https://github.com/murthyns18/Real-Time-Face-Attendance-System/blob/d13726a5ccc5b48e4750b88837f1354b04ade532/Attendance%20Details.png)




**8 : Individual Details Page**

![image alt](https://github.com/murthyns18/Real-Time-Face-Attendance-System/blob/1f65fa7d96d93bdbfef2afb1de24b3726a50dcef/Search%20By%20Individual.png)




**9 : Class Time Table Page**

![image alt](https://github.com/murthyns18/Real-Time-Face-Attendance-System/blob/1f65fa7d96d93bdbfef2afb1de24b3726a50dcef/Class%20Time%20Table.png)



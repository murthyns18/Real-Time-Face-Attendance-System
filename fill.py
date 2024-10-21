import face_recognition
import os
import cv2
import numpy as np
import math
import pymongo
import sys
import dlib
from datetime import datetime, date
from tkinter import messagebox

def face_confidence(face_distance, face_match_threshold=0.6):
    range_val = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range_val * 2.0)
    
    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val +((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2) )) * 100
        return str(round(value, 2)) + '%'

class FaceRecognition:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.load_known_faces()
        self.process_current_frame = True

        # Connect to MongoDB
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["Project"]
        self.student_collection = self.db["student_details"]
        self.attendance_collection = self.db["attendance_details"]

    def load_known_faces(self):
        for image_file in os.listdir('faces'):
            if image_file.endswith('.jpg') or image_file.endswith('.png'):
                face_image = face_recognition.load_image_file(os.path.join('faces', image_file))
                face_encoding = face_recognition.face_encodings(face_image)[0]
                self.known_face_encodings.append(face_encoding)
                self.known_face_names.append(os.path.splitext(image_file)[0])

        print("Known faces:", self.known_face_names)

    def is_sunday(self):
        # Get the current day
        current_day = date.today().weekday()
        # Sunday is represented by 6 in Python's date module
        return current_day == 6

    def run_recognition(self, selected_subject, selected_period):  # Accept selected subject and period
        if self.is_sunday():
            messagebox.showinfo("Holiday", "Today is Sunday. Attendance cannot be filled.")
            return

        video_capture = cv2.VideoCapture(0)

        if not video_capture.isOpened():
            sys.exit('Video source not found...')

        attendance_filled = False

        while True:
            ret, frame = video_capture.read()

            if self.process_current_frame:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = 'Unknown'
                    confidence = 'Unknown'

                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)

                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                        confidence = face_confidence(face_distances[best_match_index])

                        # Check if the recognized face matches with any student in the database
                        student = self.student_collection.find_one({"student_name": name})
                        if student and not attendance_filled:
                            # Store attendance details along with subject, period, and current date
                            self.attendance_collection.insert_one({
                                "student_name": student["student_name"],
                                "register_number": student["register_number"],
                                "department": student["department"],
                                "division": student["division"],
                                "semester": student["semester"],
                                "subject": selected_subject,  # Use selected subject
                                "period": selected_period,  # Use selected period
                                "date": datetime.now().strftime("%d-%m-%Y")  # Current date (day-month-year)
                            })
                            attendance_filled = True

                    face_names.append(name)

            self.process_current_frame = not self.process_current_frame

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), -1)
                
                cv2.putText(frame, f"{name} ({confidence})", (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

            cv2.imshow('Face Recognition', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                if 'Unknown' in face_names:
                    messagebox.showinfo("Attendance Not Filled", "Attendance cannot be filled for unknown students")
                else:
                    messagebox.showinfo("Attendance Filled", "Attendance filled successfully")  # Show alert message
                break

        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    # Get the selected subject and period from command-line arguments
    selected_subject = sys.argv[1] if len(sys.argv) > 1 else "Default Subject"
    selected_period = sys.argv[2] if len(sys.argv) > 2 else "Default Period"
    
    fr = FaceRecognition()
    fr.run_recognition(selected_subject, selected_period)

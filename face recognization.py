

import face_recognition
import cv2
import numpy as np
import os
from datetime import datetime



known_face_encodings = []
known_face_names = []

for filename in os.listdir('known_faces'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image = face_recognition.load_image_file(f'known_faces/{filename}')
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(os.path.splitext(filename)[0])


video_capture = cv2.VideoCapture(0)

def mark_attendance(name):
    with open('attendance.csv', 'r+') as file:
        lines = file.readlines()
        names = [line.split(',')[0] for line in lines]
        
        if name not in names:
            now = datetime.now()
            dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
            file.write(f'{name},{dt_string}\n')


while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        
        mark_attendance(name)
        
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
    
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()


from tkinter import *
from PIL import ImageTk
import pyttsx3
import speech_recognition as sr
import google.generativeai as genai
from tkinter import messagebox
import cv2
import numpy as np
def fun1():
    l1.config(text="Listening...")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            engine = pyttsx3.init()

            x="AIzaSyCDGF67u4Szetf_pUpAdAlNkXMWAi61uhg"
            genai.configure(api_key=x)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(text)
            l1.config(text="Answering...")
            engine.say(response.text)
            
            engine.runAndWait()
    
        except sr.UnknownValueError:
            messagebox.showinfo("info","Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            
            messagebox.showinfo("info","Could not request results")

    l1.config(text="🎤say something...")
def fun2():
    l1.config(text="Listening...")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            engine = pyttsx3.init()
            voices = engine.getProperty('voices') # Get the available voices

            # Set the voice to index 1 for female voice
            engine.setProperty('voice', voices[1].id)

            x="AIzaSyCDGF67u4Szetf_pUpAdAlNkXMWAi61uhg"
            genai.configure(api_key=x)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(text)
       
            engine.say(response.text)
            l1.config(text="Answering...")
            engine.runAndWait()
    
        except sr.UnknownValueError:
            messagebox.showinfo("info","Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            messagebox.showinfo("info","Could not request results")
        l1.config(text="🎤say something...")

def fun3():
  

    video = cv2.VideoCapture(0)
    facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    faces_data = []
    i = 0

    while True:
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            crop_img = frame[y:y+h, x:x+w, :]
            resized_img = cv2.resize(crop_img, (50, 50))
            if len(faces_data) <= 100 and i % 10 == 0:
                faces_data.append(resized_img)
            i = i + 1
            cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
        cv2.imshow("Frame", frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


root=Tk()
root.geometry("1600x900")
root.title("Talker")


photo = ImageTk.PhotoImage(file = "logo.png")
root.iconphoto(False,photo)

root.configure(bg='lightblue')


bg3=ImageTk.PhotoImage(file="logo.png")
bglb3=Label(root,image=bg3)
bglb3.place(x=80,y=100,width=100,height=100)

l2=Label(root,text="Connct in")


bg2=ImageTk.PhotoImage(file="girl.png")
bglb2=Label(root,image=bg2)
bglb2.place(x=900,y=0,width=640,height=900)


bg1=ImageTk.PhotoImage(file="man.png")
bglb1=Label(root,image=bg1)
bglb1.place(x=260,y=0,width=640,height=900)

b1=Button(root,text="Start talking",fg="white",bg="green",command=fun1)
b1.place(x=620,y=600)

b2=Button(root,text="Start talking",fg="white",bg="green",command=fun2)
b2.place(x=1250,y=600)

b3=Button(root,text="open camera",fg="white",bg="green",command=fun3)
b3.place(x=20,y=600)

l1=Label(root,text="🎤say something...",bg="white",fg="black")
l1.place(x=20,y=500)


root.mainloop()


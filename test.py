import pyttsx3
import speech_recognition as sr
import google.generativeai as genai
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
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
        engine.runAndWait()
    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")



       
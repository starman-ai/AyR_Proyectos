# pip3 install pyaudio
# pip3 install SpeechRecognition
# usar el Python Interpreter para instalar ambas cosas


import speech_recognition as sr

#  from Intro_SpeechRecognition import speech_recognition as sr
r = sr.Recognizer()

print("Habla:")
with sr.Microphone() as source:
    # r.adjust_for_ambient_noise(source) # listen for 1 second
    # to calibrate the energy threshold for ambient noise levels
    audio = r.listen(source)

print("Registro Generado!")
try:
    # print(You said: ) + r.recognize_google(audio)) # normal
    print("You said: " + r.recognize_google(audio, language="es-MX"))  # personalized

except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(e)
    print("Could not request results; ".format(e))

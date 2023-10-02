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

with open("Audios/audio_file_3.wav", "wb") as file:
    file.write(audio.get_wav_data())
print("Archivo Creado!")

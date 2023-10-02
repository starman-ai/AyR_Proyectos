
import speech_recognition as sr

#  from Intro_SpeechRecognition import speech_recognition as sr
r = sr.Recognizer()

audio_file = sr.AudioFile("Audios/audio_file_2.wav")

try:
    with audio_file as source:
        #  r.adjust_for_ambient_noise(source) # listen for 1 second
    #  to calibrate the energy threshold for ambient noise levels
    audio = r.record(source)

    var = r.recognize_google(audio, language="es-MX", show_all=false)
    print("Mensaje: ")
    print(var)
palabras = str(var).split()
print(palabras)

except sr.UnknownValueError:
    print("No se pudo reconocer el audio")
except sr.RequestError as e:
    print(f"Error en la solicitud: {e}")
import speech_recognition as sr
import serial

arduino = serial.Serial('COM7', 9600)  # Es el puerto que nos ha servido, en dado caso hay que cambiarlo

recognizer = sr.Recognizer()

# Mapeo de los comandos a un valor numérico
command_mapping = {
    "avanzar": 0,
    "retroceder": 1,
    "derecha": 2,
    "izquierda": 3,
    "detener": 4
}

while True:
    with sr.Microphone() as source:
        print("Escuchando...")  # Para indicar estado de escucha
        audio = recognizer.listen(source)
        try:
            # Mandamos el reconocimiento en minúsculas para facilitar su identificación
            command = recognizer.recognize_google(audio, language="es-MX").lower()

            # Revisa si el comando se encuentra en el mapeo, de lo contrario, manda "detener"
            numeric_command = command_mapping.get(command, 4)

            if numeric_command < 5:
                print("Dijiste: " + command)  # Para corroborar que sí recibe correctamente el comando

                # Enviar el comando numérico a Arduino
                arduino.write(str(numeric_command).encode())
                print("Comando enviado al Arduino: " + str(numeric_command))  # Para debugging
            else:
                # Comando desconocido, envía "detener"
                arduino.write(str(4).encode())
                print("No entendí el audio.")
        except sr.UnknownValueError:
            print("No se detectó ninguna voz. Intenta de nuevo.")
        except sr.RequestError as e:
            print("No se pudieron solicitar resultados; {0}".format(e))

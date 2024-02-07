import serial 
import speech_recognition as sr

#Establish serial communication with Arduino arduino serial.Serial('COM4, 9600, timeout=1)

def rotate_servo(angle):
    arduino.write(angle.encode()) # Send the angle command to Arduino

# Initialize the speech recognizer
r = sr.Recognizer()

#Infinite loop to listen for voice commands
while True:
    with sr.Microphone() as source: 
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("Voice Command:", command)

        if command in ['close', '0']:
            rotate_servo('0')
        elif command in ['open', '1']:
            rotate_servo('1')
        else:
            print("Invalid command. Please try again.")

    except sr.UnknownValueError:
        print("Unable to recognize speech.")
    except sr.RequestError as e:
        print("Error occurred; (0)".format(e))
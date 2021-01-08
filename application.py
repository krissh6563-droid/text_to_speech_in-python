#import pyttsx3 library
import pyttsx3

#object creation
root = pyttsx3.init()
while(1):

    print("Write something for me to speak or write stop to exit")
    input_text = input()
    if input_text == "stop":
        break
    else:
        root.say(input_text)
        root.runAndWait()

from gtts import gTTS
import datetime
import os
question = "What is your name?"
file = "myfile2.mp3"
tts1 = gTTS(question)
os.system('mpg123' + file)
s = input("Enter name: ")
by = int(input("Year born: "))
cy = datetime.datetime.now().year
age=cy-by
message = "hello, "+s+"! You are " + str(age) + " years old."
file = "myfile.mp3"
tts = gTTS(message, 'en')
tts.save(file)
os.system('mpg123' + file)
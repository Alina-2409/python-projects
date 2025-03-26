from gtts import gTTS
import os

t=input("enter text :")
language='en'
obj=gTTS(text=t,lang=language,show=False)
obj.save("file.mp3")
os.system("C:\Users\alfiy\OneDrive\Desktop\file.mp3")
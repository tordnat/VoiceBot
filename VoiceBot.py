import os
from gtts import gTTS
import time
import playsound
import speech_recognition as sr

#startup sound

playsound.playsound("startup.mp3")
filestring = "VoiceBot"
def customSound(hei, spraak):
        	tts = gTTS(text=hei, lang = spraak)
        	filename = filestring+".mp3"
        	tts.save(filename)
        	playsound.playsound(filename)
        	
#testing if voice assistant is workink
customSound("Welcome to Tord's Voice-Bot, powered by Google's text to speach API. If you can hear this, the bot is working.", "en")
os.remove("VoiceBot.mp3")

while True:
		x = str(input("Text ('quit' to quit):"))
		y = str(input("Language (gTTS alias):"))
		if x == "quit":
			break
		else:
                    
                    if input("Do you want to save the file [y/n]:") == "y":    
                        filestring = str(input("Insert filename (no format):"))
                        customSound(x,y)
                    else:
                        
                        customSound(x,y)
                        os.remove("VoiceBot.mp3")
	

import speech_recognition_testing 
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def gideon_say(phrase):
	print("Gideon: " + phrase)
	engine.say(phrase)
	engine.runAndWait()

def read_aloud(phrase):
	print(phrase)
	engine.say(phrase)
	engine.runAndWait()
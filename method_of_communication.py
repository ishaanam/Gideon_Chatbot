from gideon_saying import gideon_say 
from speech_recognition_testing import gideon_speech_recognition as gsr

#different functions used to relay information to Gideon

def get_communication_method():
	f = open("my_communication_method.txt", "r+")
	f.truncate()
	gideon_say("Would you like to type(t) or speak(s)?")
	communication_method = input("Method of communication: ")
	if communication_method == "t":
		f = open("my_communication_method.txt", "a")
		f.write("t")
	elif communication_method == "s":
		f = open("my_communication_method.txt", "a")
		f.write("s")

def communicate(communication_method):
	if communication_method == "t":
		sentence = input("You: ")
	elif communication_method == "s":
		sentence = gsr()
		print("You: " + sentence)
	else:
		quit()
	return sentence

def communicate_better():
	f = open("my_communication_method.txt", "r+")
	communication_method = f.read()
	if communication_method == "t":
		sentence = input("You: ")
	elif communication_method == "s":
		sentence = gsr()
		if sentence == "":
			pass
		else:
			print("You: " + sentence)
	return sentence
	

def raw_communicate_better():
	f = open("my_communication_method.txt", "r+")
	communication_method = f.read()
	if communication_method == "t":
		sentence = input()
	elif communication_method == "s":
		sentence = gsr()
		print(sentence)
	return sentence
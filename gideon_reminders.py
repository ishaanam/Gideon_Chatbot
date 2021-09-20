from speech_recognition_testing import gideon_speech_recognition as gsr
from gideon_saying import gideon_say, read_aloud

#writes reminders to a file which Gideon reads when you say good morning 

chosen_file = 'reminders.txt'

def list_combiner(sent):
    num = len(sent)
    sentence = ""
    for i in range(num):
        current = i + 1
        last = num
        if current == num:
            sentence += sent[i]
        else:
            sentence += sent[i]
            sentence += " "
    return sentence


def write_reminders(sentence):
	phrase = list_combiner(sentence)
	phrase = phrase[13:]
	f = open("reminders.txt", "a")
	f.write("\n" + phrase)
	gideon_say("Ok, I will remind you to " + phrase + " tomorrow morning")

def wipe_file():
	f = open("reminders.txt", "r+")
	f.truncate()

def read_reminders():
	f = open("reminders.txt", "r+")
	gideon_say("Here are your reminders for today: ")
	if f.read() != "":
		read_aloud(f.read())
	else:
		gideon_say("You don't have any reminders today, here are your links!")
	


import random
import webbrowser
import datetime
import time
from random import randint
import smtplib
from email.message import EmailMessage
import speech_recognition_testing 
import pyttsx3
from gideon_saying import gideon_say
from method_of_communication import raw_communicate_better as rcb 

#writes to a file you can refer to later

def files():
    chosen_file = "my_notes.txt"
    print('\n')
    writing = input()
    with open(chosen_file, 'a') as text_file:
        text_file.write("\n" + writing)
    gideon_say("Saved!")
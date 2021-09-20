# chat.py
# gideon_1.0
import random
import json
import pyttsx3
import speech_recognition as sr
from speech_recognition_testing import gideon_speech_recognition as gsr
from gideon_saying import gideon_say
from method_of_communication import get_communication_method, communicate_better, communicate  


import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from better_passwords import password


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


with open("intents.json", "r") as json_data:
    intents = json.loads(json_data.read())

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Gideon"

active = True

password()

get_communication_method()

while active:

    sentence = communicate_better()
    if sentence == "quit":
        active = False

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                text_output = random.choice(intent['responses'])
                gideon_say(text_output)
            if tag == "bye":
                active = False
        if tag == "rps":
            import play_rps
            play_rps.play_rps()
        elif tag == "battleship":
            import battle_ship
            battle_ship.battle_ship()
        elif tag == "links":
            import find_links
            find_links.find_links(sentence)
        elif tag == "tell": 
            import send_messages
            send_messages.send_message(sentence)
        elif tag == "morning":
            import good_morning
            good_morning.good_morning()
        elif tag == "files" : 
            import files
            files.files()
        elif tag == "wiki" :
            import my_wiki
            my_wiki.my_wiki(sentence)
        elif tag == "reminder":
            import gideon_reminders
            gideon_reminders.write_reminders(sentence)
        elif tag == "funny":
            from pyjokes import get_joke
            gideon_say(get_joke('en'))
        








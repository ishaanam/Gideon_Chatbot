import wikipedia
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from speech_recognition_testing import gideon_speech_recognition as gsr
from gideon_saying import gideon_say as gs 
from method_of_communication import raw_communicate_better as rcb

#reads the introductions of wikipedia pages

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



def my_wiki(example_sentence):
	#try:

	example_sentence = list_combiner(example_sentence)

	stop_words = set(stopwords.words("english"))

	words = word_tokenize(example_sentence)
	filtered_sentence = []
	for w in words:
		if w not in stop_words:
		    filtered_sentence.append(w)


	final = list_combiner(filtered_sentence)
	gs("Would you like me to read this aloud?(yes/no)")
	read_aloud = rcb()

	try:
		if read_aloud.lower() == 'yes':
			gs(wikipedia.summary(final))
		else:
			print(wikipedia.summary(final))
	except Exception:
		gs("I'm sorry, there isn't a Wikipedia page under this title")

	#except Exception:
		#gs("I do not understand...")

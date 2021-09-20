import speech_recognition as sr

#allows Gideon to turn speech into text
def gideon_speech_recognition():
	try:
		r = sr.Recognizer()
		mic = sr.Microphone(device_index=2)

		with mic as source:
			audio = r.listen(source)

		my_output = r.recognize_google(audio)

		return my_output

	except Exception:
		return ""

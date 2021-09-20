import smtplib
from email.message import EmailMessage
from gideon_saying import gideon_say as gs
from method_of_communication import communicate_better

#sends text messages from an email

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

my_recipients = {
	"person" : "phone number"
}

def send_message(sentence):
	person = sentence[1]
	if person in my_recipients:
		to = my_recipients[person]
		subject = "Message from  : "
		body = list_combiner(sentence[2:])
		
		msg = EmailMessage()
		msg.set_content(body)
		msg["subject"] = subject
		msg["to"] = to

		gs("Would you like me to send the following(yes/no)\n:" + "subject: " + subject + "\n" + "body: " + body + "\n")

		confirm = communicate_better()

		if confirm.lower() == "yes":
			user = ""
			msg["from"] = user
			password = ""

			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.starttls()
			server.login(user, password)
			server.send_message(msg)

			gs("You're message was relayed  !")

			server.quit()
		else:
			gs("Ok, I've cancelled")
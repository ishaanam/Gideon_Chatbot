import webbrowser
import time
from gideon_reminders import wipe_file, read_reminders


links = []

#opens links to start the day + reads out the reminders you previously wrote
def good_morning():
	num = len(links)
	read_reminders()

	for i in range(num):
		link = links[i]
		if i == 0:
			webbrowser.open(link, new=0)
		else:
			webbrowser.open(link, new=2)

	#wipes the reminders file
	wipe_file()

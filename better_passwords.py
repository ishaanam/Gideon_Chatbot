from hashlib import sha256
import hashlib
from gideon_saying import read_aloud as ra
from gideon_saying import gideon_say as gs
import getpass

def abort_gideon():
	#Incorrect passwords initiate a fake self destruct sequence
	ra("IMPOSTER detected")
	ra("Self-destruct in ")
	ra("3...")
	ra("2...")
	ra("1...")
	quit()

def my_test(personal_prompt, correct_hash):
	#password function
	personal_pass = getpass.getpass(prompt=personal_prompt)
	pass_hash = hashlib.sha256(personal_pass.encode())
	pass_hash = pass_hash.hexdigest()
	pass_true = pass_hash == correct_hash
	if pass_true:
		ra("Test passed!")
	else:
		abort_gideon()

def password():
	all_tests = []
	#any number of passwords, just for fun
	#replace "hash #x" with the hash of the correct password
	my_test("password #1: ", "hash #1")
	all_tests.append(True)
	my_test("password #2: ", "hash #2")
	all_tests.append(True)
	my_test("password #3: ", "hash #3")
	all_tests.append(True)

	if all(all_tests):
		gs("All tests passed, welcome back  !")

	



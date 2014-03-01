record = []
while True:
	info = []
	userInput = raw_input("Enter something:")
	if userInput == "exit":
		break
	else:
		info = userInput.split(",")
		record += [info]
print record
	
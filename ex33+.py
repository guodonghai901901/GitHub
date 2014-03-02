def loop_your_number(argv1, argv2):
	i = 0
	numbers = []

	while i < argv1:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + argv2
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	
	print "The numbers: "

	for num in numbers:
		print num
		
number_string = raw_input("Please enter your number that you want it to be looped: ")
number = int(number_string)
number2_string = raw_input("Please enter the count you want your number adds: ")
number2 = int(number2_string)
loop_your_number(number, number2)
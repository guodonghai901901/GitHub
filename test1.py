import random

i = 1
for i in range(1, 6):
	j = int[raw_input("j:")]
	if j < 1:
		print "nothing!"
	else:
		if j == 1:
			break
		else:
			print "not break!"
	j += 1
	print "i = ", i
	print "J = ", j
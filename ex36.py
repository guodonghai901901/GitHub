# psychology test python script version
# -*- coding: UTF-8 -*-
from sys import exit

def first_choice():
	print """
	\n\tImage that you come to a new school, 
	and face a wholly new place. After the class, 
	which selection would you prefer with below three? 
	There're three choices for you: \n
	A To make friends with classmates \n
	B Wait the classmates to talk to you first\n
	C Go out alone. \n\n"""
	choice1 = raw_input("Please enter A, B or C: ")
	if choice1 == "A":
		print "-> 2 item"
		second_choice()
	elif choice1 == "B":
		print "-> 3 item"
		third_choice()
	elif choice1 == "C":
		print "-> 5 item"
		fifth_choice()
	else:
		print "I have no idea what did you enter..."
		exit(1)
	

def second_choice():
	print """
	\n\tSince you make friends with classmates, but
	she/him doesn't want to play with you, what would
	you do? \n
	A Turn around and leave \n
	B Shout at him angrily then leave \n
	C Continue to play with her/him
	\n\n"""
	choice2 = raw_input("Please end A, B or C:")
	if choice2 == "A":
		print "-> 5 item"
		fifth_choice()
	elif choice2 == "B":
		result("B")
	elif choice2 == "C":
		print "-> 3 item"
		third_choice()
	else:
		print "I have no idea what did you enter..."
		exit(1)
	
			
def third_choice():
	print """
	\n\tWow wow wow, here's another classmate 
	come to make friends with you, you will...\n
	A Ignore her/him \n
	B Play with her/him \n
	C Say no to her/him and leave. \n\n"""
	choice3 = raw_input("Please enter A, B or C :")
	if choice3 == "A":
		print "-> 4 item"
		forth_choice()
	elif choice3 == "B":
		print "-> 5 item"
		fifth_choice()
	elif choice3 == "C":
		result("D")
	else:
		print "I have no idea what did you enter..."
		exit(1)


def forth_choice():
	print """
	\n\tRing ring! it's quiz day! There's a subject 
	you don't know the answer, you will... \n
	A let it go \n
	B throw a paper ball to your classmate for help \n
	C finish it with wrong answer \n\n"""
	choice4 = raw_input("Please enter A, B or C :")
	if choice4 == "A":
		result("A")
	elif choice4 == "B":
		print "-> 5 item"
		fifth_choice()
	elif choice4 == "C":
		result("C")
	else:
		print "I have no idea what did you enter..."
		exit(1)
	
def fifth_choice():
	print """
	\n\tThe paper is done!
	Your classmate asks you for help with one subjject
	and you finish that subject on your paper, you will...\n
	A Tell her/him a wrong answer \n
	B Ignore her/him \n
	C Tell her/him right answer \n
	D Tell her that finish by herself \n\n"""
	choice5 = raw_input("Please enter A, B, C or D :")
	if choice5 == "A":
		result("A")
	elif choice5 == "B":
		result("B")
	elif choice5 == "C":
		result("C")
	elif choice5 == "D":
		result("D")
	else:
		print "I have no idea what did you enter..."
		exit(1)

def result(argv):
	if argv == "A":
		print """You're a very mean person, you are unlike-able. \n
		Sad for you. \n\n"""
		exit(0)
	elif argv == "B":
		print """You're a mean person too, but you're cool outside. \n\n"""
	elif argv == "C":
		print """You're a warm-hearted person, and good luck for you! \n\n"""
	else:	
		print """You're a sunshine for everyone, good for you ! \n\n"""


first_choice()
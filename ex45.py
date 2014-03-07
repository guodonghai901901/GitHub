# -*- coding: UTF-8 -*-
import random
from sys import exit
import p_c



power = 0
penny = 1000
blood = 0



class Practice_house(object):
	
	def __init__ (self):
		self.name = 'Practice_house'
	
	def ride_bike(self):
		
		p_c.add(power, 50)
		p_c.sub(penny, 100)
		print "\t You know ridding bike can make you add power,smart! Power + 50: %d" % power
		print """\t But you have to know that ridding in Practice 
		house will cost you 5 pennies each time. Penny + 100: %d """ % penny
			
	def running_band(self):
		p_c.add(power, 50)
		p_c.sub(penny, 50)
		print "\t You know ridding bike can make you add power,smart! Power + 50: %d" % power
		print """\t But you have to know that ridding in Practice 
		house will cost you 5 pennies each time. Penny + 50: %d""" % penny
		
		
		

class Lucky_room(object):

	def __init__ (self):
		self.name = 'Lucky room'

	def Bag(self):
		print """ \t Lucky guy, since you choose the bag, open it!
		See what you've got!
		"""
		number1 = random.randint(1, 100)
		print "\t Oh, you got %d pennies for lucky prize, not bad!!" % number1
		p_c.add(penny, number1)
		print "\t Ding!Ding!Ding! Your penny raise! See how many penny you got now! %d ." % penny
		
	def Apple(self):
		print "\t Apple can get you more power, how many people do you want?"
		number_a = raw_input("Input a number between 1 to 3:")
		if number_a == "1":
			print "\t En, one apple is very suitable for you! You power raises 100 points."
			p_c.add(power, 100)
			p_c.sub(penny, 100)
		elif number_a == "2":
			print "\t En, two apple is a little much for normal person! OK, the normal person I'm meaning me!  Whatever!"
			p_c.add(power, 50)
			p_c.sub(penny, 200)
		elif number_a == "3":
			print "\t Ah h, I have to say that three apples are really too many, because these apples aren't be washed clean!"
			p_c.sub(power, 50)
			p_c.sub(penny, 300)
		else:
			print "\t I have no idea what you typed...."
			exit(1)
			
	def Bomb(self):
		print """\t Oh god, you pick bomb stuff! 
				\t Maybe it brings you a lot of pennies or maybe bring you death!
				Here it comes!"""
		print """\t -------------------------------------------------------"""
		print """\t -------------------------------------------------------"""
		b = random.randint(0, 1001)
		if b <= 100:
			blood = 0
			print "\t Oh god, sad news! You blood is bombed out and you gonna die.... "
		elif b >= 900:
			penny = 10000
			print """\t You penny raises to 10000, that means you can take helicopter to Tower!
			\t How can you be so lucky! I got buy bones in your name! 
			You win the game! Lucky man!"""
			print """\t ****************************************************
						\t****************************************************"""
			exit(0)
		else:
			print "\t Nothing you got from bomb. :( Also you're lucky! :)"
	
	def Cake(self):
		print """\t Wow, you choose a cake, cake is delicious~ Yummy, yummy~~~"""
		p_c.add(blood, 100)
		print """\t Your blood raises 100 points! Power comes to: %d """ % blood
	
class Dead_bridge(object):

	def __init__ (self):
		self.name = 'Dead_bridge'

	def Bridge(self):
		step = random.randint(1, penny / 10)
		p_c.sub(power, step)
		p_c.sub(blood, step)
		
		
class Tower(object):
	
	def __init__ (self):
		self.name = 'Tower'
	
	def Tower(self):
		sum_p = power + blood
		if (sum_p >= 150 and penny >= 500) :
			print "\t Your features are: %d %d %d " % (power, blood, penny)
			print "\t You got to the tower! You win! "
		else: 
			print "\t Sorry, your point doesn't achieve much enough! Restart the game, please input restart or exit by 0! "
			
		
practice_house = Practice_house()
lucky_room = Lucky_room()
dead_bridge = Dead_bridge()
tower = Tower()
		

def f_practice_house():

	print "\t Now you enter the room, there is a bike and a running band. "
	print "\t Please choose which tool you want to use?"
	loop = True
	goon = 'Y'
	while (loop or goon):
		tool = raw_input("Enter bike or run : ")
		if tool == "bike":
			practice_house.ride_bike()
			loop = False
		elif tool == "run":
			practice_house.running_band()
			loop = False
		else:
			print "\t Enter wrong name! "
			yesorno = raw_input("Y or N to continue: ")
			if yesorno == "Y":
				tool = raw_input("Enter bike or run: ")
			else:
				print "\t You lose the last chance! You quit the game!"
				exit(0)
		print "\t Want to leave this room? Press Y to leave, N to keep in."
		goon = raw_input("Enter Y/N : ")


def f_lucky_room():
	print "\t Welcome to lucky room!"
	print "\t There are four things you could use, but you can choose only one time. "
	print "\t A bag, an red apple, a bomb or a cake? "
	lucky = raw_input("Enter bag, apple, bomb or cake: ")
	while lucky:
		if lucky == "bag":
			lucky_room.Bag()
			lucky = False
				
		elif lucky == "apple":
			lucky_room.Apple()
			lucky = False
				
		elif lucky == "bomb":
			lucky_room.Bomb()
			lucky = False

		elif lucky == "cake":
			lucky_room.Cake()
			lucky = False

		else:
			print "\t You enter wrong name.? Try again. "
			lucky = raw_input("Enter bag, apple, bomb or cake: ")
				
def f_dead_bridge():
	print "\t Welcome to dead bridge! But are you scared? "
	dead_bridge.Bridge()
	
def f_tower():
	tower.Tower()

def start():	
	

	print """ \t Welcome! This is the game: Tower \n
			\t First of all, you got to enter practice house to strength your energy.\n\n
			"""
			
	f_practice_house()

	print """\t As followed choose where you want to go, Lucky Room or Dead Bridge? """
	choice = raw_input("Enter Lucky room or Dead bridge: ")
	while choice:
		if choice == 'Lucky room' or choice == 'lucky room':
			f_lucky_room()
			choice = False
		elif choice == 'Dead bridge' or choice == 'dead bridge':
			f_dead_bridge()
			choice = False
		else:
			print "\t You enter wrong name, try again? "
			choice = raw_input("Enter Lucky room or Dead bridge or exit: ")
			if choice == 'exit':
				print "\t You don't have patience! "
				exit(1)
	
	if (power >= 500 and blood >= 500):
		f_tower()
	else:	
		print "\t Restart your game: "
		
start()

		
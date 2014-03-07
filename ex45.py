# -*- coding: UTF-8 -*-
import random
#from sys import exit
import function



power = 0
penny = 1000
blood = 0



class Practice_house(object):
	

	def __init__ (self):
		self.name = 'Practice_house'
	
	def ride_bike(self):
		
		global power
		global penny
		global blood
		power += 50
		penny -= 100
		print "\t You know ridding bike can make you add power,smart! Power + 50: %d" % power
		print """\t But you have to know that ridding in Practice 
		house will cost you 100 pennies each time. Penny + 100: %d """ % penny
			
	def running_band(self):
		global power
		global penny
		global blood
		power += 50
		penny -= 50
		print "\t You know ridding bike can make you add power,smart! Power + 50: %d" % power
		print """\t But you have to know that ridding in Practice 
		house will cost you 50 pennies each time. Penny + 50: %d""" % penny
		
		
		

class Lucky_room(object):

	def __init__ (self):
		self.name = 'Lucky room'

	def Bag(self):
		global penny
		print """ \t Lucky guy, since you choose the bag, open it!
		See what you've got!
		"""
		number1 = random.randint(1, 100)
		print "\t Oh, you got %d pennies for lucky prize, not bad!!" % number1
		
		penny += number1
		print "\t Ding!Ding!Ding! Your penny raise! See how many penny you got now! %d ." % penny
		
	def Apple(self):
		global power
		global penny
		global blood
		
		print "\t Apple can get you more power, how many people do you want?"
		number_a = raw_input("\t Input a number between 1 to 3:")
		if number_a == "1":
			print "\t En, one apple is very suitable for you! You power raises 100 points."
			power -= 100
			blood += 100
			penny -= 100
		elif number_a == "2":
			print "\t En, two apple is a little much for normal person! OK, the normal person I'm meaning me!  Whatever!"
			power += 50
			blood += 200
			penny -= 200
		elif number_a == "3":
			print "\t Ah h, I have to say that three apples are really too many, because these apples aren't be washed clean!"
			power -= 50
			blood += 300
			penny -= 300
		else:
			print "\t I have no idea what you typed...."
			function.exit_1()
			
	def Bomb(self):
		global power
		global penny
		global blood
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
			function.exit_1()
		else:
			print "\t Nothing you got from bomb. :( Also you're lucky! :)"
	
	def Cake(self):
		global blood
		print """\t Wow, you choose a cake, cake is delicious~ Yummy, yummy~~~"""
		blood += 100
		print """\t Your blood raises 100 points! Power comes to: %d """ % blood
	
class Dead_bridge(object):

	def __init__ (self):
		self.name = 'Dead_bridge'

	def Bridge(self):
		global power
		global penny
		global blood
		step = random.randint(1, 150)
		print "\t Cross the bridge will spend 150 points of you power and blood and 500 pennies!"
		power -= step
		blood -= step
		
		
class Tower(object):
	
	def __init__ (self):
		self.name = 'Tower'
	
	def Tower(self):
		global power
		global penny
		global blood
		sum_p = power + blood
		if (sum_p >= 1000 and penny >= 500) :
			print "\t Your features are: %d %d %d " % (power, blood, penny)
			print "\t You got to the tower! You win! "
		else: 
			print "\t Sorry, your point doesn't achieve much enough!  "
			
		
practice_house = Practice_house()
lucky_room = Lucky_room()
dead_bridge = Dead_bridge()
tower = Tower()
		

def f_practice_house():
	global power
	global penny
	global blood

	print "\t Now you enter the room, there is a bike and a running band. "
	print "\t Please choose which tool you want to use?"
	loop = True
	goon = True
	while (loop or goon):
		tool = raw_input("\t Enter bike or run: ")
		if tool == "bike":
			practice_house.ride_bike()
			loop = False
		elif tool == "run":
			practice_house.running_band()
			loop = False
		else:
			print "\t Enter wrong name! "
			yesorno = raw_input("\t Y or N to continue: ")
			if yesorno == "Y":
				tool = raw_input("\t Enter bike or run: ")
			else:
				print "\t You lose the last chance! You quit the game!"
				function.exit_1()
		print "\t Want to keep in this room? Press Y to keep in, N to leave."
		yes2 = raw_input("\t Enter Y/N : ")
		if yes2 == 'Y':
			goon = True
		else:
			goon = False


def f_lucky_room():
	i = 0
	print "\t Welcome to lucky room!"
	print "\t There are four things you could use, but you can choose only one time. "
	print "\t A bag, an red apple, a bomb or a cake? "
	lucky = raw_input("\t Enter bag, apple, bomb or cake: ")
	while (lucky and i <4):
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
			lucky = raw_input("\t Enter bag, apple, bomb or cake: ")
			i += 1
			
				
def f_dead_bridge():
	print "\t Welcome to dead bridge! But are you scared? "
	dead_bridge.Bridge()
	
def f_tower():
	tower.Tower()

def start():	
	global power
	global penny
	global blood
	
	print """ \t Welcome! This is the game: Tower \n
\t First of all, you got to enter practice house to strength your energy.\n\n
"""	
	f_practice_house()
	
	if (penny > 0):
		print """\t As followed you will go to Lucky Room! """
		f_lucky_room()
	else:
		print "\t Your resources run out...... You lose the game!"
		function.exit_1()
		
	if (penny > 0):
		f_dead_bridge()
	else:
		print "\t Your resources run out...... You lose the game!"
		function.exit_1()
		
	if (power > 0 and blood > 0 and penny > 0):
		f_tower()		
	else:
		print "\t Your resources run out...... "
		if power <= 0:
			print "\t Your power % d is not enough!" % power
		elif blood <= 0:
			print "\t Your blood % d is not enough!" % blood
		else:
			print "\t Your penny % d is not enough!" % penny
		function.exit_1()
		print "\t You lose the game!"
start()

		
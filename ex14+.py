from sys import argv
script, user_name, your_husband_name = argv
prompt = '->'
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print "So %s is your husband?" % your_husband_name
facts = raw_input(prompt)
print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print "Which city is your husband now?"
husband_city = raw_input(prompt)
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. 
Also you say %r that liuchong is your hasband.
""" % (likes, lives, computer, facts),
print """By the way, your husband is now in %r too, 
you guys are so happy.""" % husband_city

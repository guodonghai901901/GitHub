# 此三行是定义people cars buses的取值分别为 30 40 15
people = 30
cars = 40
buses = 15

# 判断cars和people哪个值比较大，输出相应的语句
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

#判断buses和cars哪个值比较大，输出相应的语句
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

#判断people和buses哪个值比较大，输出相应的语句
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
	
#1. elif 的功能是如果存在三种或者三种以上情况，用来提供这些分支的判断；
# else的功能是最后或者是第二种情况
# 2. 结果会不一样，走另外的分支
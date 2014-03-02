# -*- coding: UTF-8 -*-
# range(0, 6)
# 不行，因为这样的话elements只有1个位于0到6之间的值了
# insert, expend, findtext, getchildren 等等

elements = []
for i in range(0,6):
	number_text = raw_input("Please enter your number: ")
	number = int(number_text)
	elements.append(number)

for i in range (0, 6):	
	print elements[i]
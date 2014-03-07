# -*- coding: utf-8 -*-
# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r " % (arg1, arg2)
	# ok, that * args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r" % arg1
# this one takes no arguments
def print_one(arg1):
	print "arg1: %r" % arg1
# this one takes no arguments
def print_none():
	print "I got nothing."
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()


# 1. 是的
# 2. 不一定
# 3. 对。
# 4. 对。
# 5. 是的
# 6. 是的。
# 7. 不太懂什么意思。
# 8. 还是不太懂。

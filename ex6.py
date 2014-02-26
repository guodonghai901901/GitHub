# -*- coding: utf-8 -*-
#x被赋值为一个字符串，此处有个格式化字符d
x = "There are %d types of people." % 10
# binary被赋值为字符串 binary
binary = "binary"
# do_not被赋值为字符串 don't
do_not = "don't'"
# y被赋值为 there who know binary and those who don't,此处有两个格式化字符s
y = "There who know %s and those who %s." % (binary, do_not)
# 输出x变量的值
print x
# 输出y变量的值
print y
# 输出字符串，此处有格式化字符r
print "I said: %r." % x
# 输出字符串，此处有格式化字符r
print "I also said: '%s'." % y
# 设置hilarious变量为 False
hilarious = False
# 设置joke_evaluation 为字符串，其中字符串里包含格式化字符r
joke_evaluation = "Isn't that joke so funny?! %r"
# 输出字符串，其实包含格式化字符r的引用
print joke_evaluation % hilarious
# 设置变量w为此字符串
w = "This is the left side of..."
# 设置变量e为此字符串
e = "a string with a right side."
# 设置输出w和e合并的字符串
print w + e
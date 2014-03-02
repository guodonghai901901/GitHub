# -*- coding: UTF-8 -*-
#使用参数模组
from sys import argv
#定义script和filename是参数变量
script, filename = argv
#定义txt为打开的这个文件
txt = open(filename)
#输出here's your file和文件名
print "Here's your file %r:" % filename
#输出文件内容
print txt.read()
txt.close()
#输出Type the filename again:
print "Type the filename again:"
#定义file_again为输入的文件名
file_again = raw_input(">")
#定义txt_agian为打开的文件
txt_again = open(file_again)
#输出文件内容
print txt_again.read()
txt_again.close()

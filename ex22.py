# -*- coding: utf-8 -*-
# print # 打印
# 符号为注释符号，单行注释
# -*- coding: UTF-8 -*- 其他字符解编码字符串
# + - * / %  > < >= <= 分别为 加 减 乘 除 求余 运算符以及 大于 小于 大于等于 小于等于 逻辑运算符
# = 等于赋值符号
# 格式化字符： %d %r %s %f %x %e %c %% 分别是十进制有符号整数；debug使用的字符串； 一般使用的字符串符号
# 浮点数字；无符号十六进制整数 科学计数法浮点数字；字符；百分号标记；
# False 逻辑值假
# print "", print "" 中间的逗号代表不换行打印，默认不带逗号的情况下，print会换行
# print """xxx""" 三引号之间不能输入空格 其作用是可以在三引号之间输入任意多行的文字
# \t \\ \n \r \b \' \" \v 其余的不太常用 依次是：tab， \ 换行 回车 删除 ' '' 
# 垂直换行符 
# raw_input() raw_input("your words before input:") 原始输入函数,保存为字符串
# while True:循环函数 if 条件：else; break 功能 record += [info] info = []
# 分别是while 条件的时候循环下去，
# from sys import argv  script, filename = argv 使用参数模组的方法，除此以外在运行此脚本的时候，
# 需要加参数，如 python ex7.py ex7_txt.txt
# open(filename) 打开一个文件返回的是文件对象；file.read()读取此文件的所有内容，返回所有内
# open(filename,'w')以写权限打开此文件；file.write(text1)把text1的内容写入file中
# from os.path import exists 使用exists函数模组 exists(filename) 返回值为True或者是False
# file.close()当使用了open(file)后，需要使用close关闭
# def 函数名(参数1，参数2)：调用的时候： 函数名（参数1，参数2）
# seek(0)使得文件回复到初始位置进行读取 readline() 读取当前这一行的文本且输入换行符，且读取位置自动转入下一行
# def 函数名（参数1，参数2） return result
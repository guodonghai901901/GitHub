# -*- coding: utf-8 -*-
#定义一个父类
class Parent(object):
	
	# 父类包含的override函数为打印以下字符串
	def override(self):
		print "PARENT override()"
	
	# 父类包含的implicit函数为打印以下字符串
	def implicit(self):
		print "PARENT implicit()"
	
	# 父类包含的altered函数为打印以下字符串
	def altered(self):
		print "PARENT altered()"

# 定义一个子类Child		
class Child(Parent):
	
	#子类中包含一个自定义的override函数
	def override(self):
		print "CHILD override()"
		
	#子类中包含一个自定义的altered函数 此函数中输出一部分字符，调用了父类的altered()函数 再输出一部分字符
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

#建立父类实例 建立子类实例		
dad = Parent()
son = Child()

#调用父类对象的implicit()函数；调用子类对象的implicit()函数
dad.implicit()
son.implicit()

# 调用父类对象的override()函数;调用父类对象的override()函数
dad.override()
son.override()

# 调用父类对象的altered()函数;调用父类对象的altered()函数
dad.altered()
son.altered()
		
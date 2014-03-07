# -*- coding: UTF-8 -*-
#给变量cars赋值100整数
cars = 100
#给变量space_in_a_car赋值4.0浮点数
space_in_a_car = 4.0
#给变量drivers赋值30整数
drivers = 30
#给变量passengers赋值90整数
passengers = 90
#变量cars_not_driven被赋值为cars变量减去drivers变量的值
cars_not_driven = cars - drivers
#变量cars_driven被赋值为drivers
cars_driven = drivers
#carpool_capacity被赋值为变量cars_driven与space_in_a_car的乘数值
carpool_capacity = cars_driven * space_in_a_car
#average_passengers_per_car被赋值为变量passgeners与变量cars_driven相除后的值
average_passengers_per_car = passengers / cars_driven
print "There are", cars, "cars available." 
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

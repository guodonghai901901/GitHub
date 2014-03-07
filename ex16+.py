from sys import argv
script, filename = argv
my_file_content = open(filename, 'w+')
print my_file_content.read()
line1 = raw_input("Line 1:")
my_file_content.write(line1)
print "Here is the line1: %s ." % line1
line2 = raw_input("Line 2:")
my_file_content.write(line2)
print "Here is the line2: %s ." % line2
line3 = raw_input("Line3: ")
my_file_content.write(line3)
print "Here is the line3: %s ." % line3


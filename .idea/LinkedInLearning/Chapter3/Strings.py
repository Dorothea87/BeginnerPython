import math
from idlelib.colorizer import prog_group_name_to_tag

#Slicing (uses the same features on lists and strings)
name = 'My name is Dorothea'
print(name[0])
print(name[1])
print(name[0:7])
print(name[:7])
print(name[11:])

my_list = [1, 2, 3, 4, 5,]
print(my_list[2:4])
print(len(name))
print(len(my_list))

#Formatting
my_number ='My number is: '+str(6)
print(my_number)

x = 7
your_number_sentence = f'Your number is {x}'
print(your_number_sentence)

rounded_pi = f'Pi is: {math.pi:.2f}'
print(rounded_pi)

nonrounded_pi ='Pi is: {}'.format(math.pi)
print(nonrounded_pi)

#Multi-line String (three single quotes)
newString = '''
Here is a long block of text
I can even add new lines!
the text does not stop until it sees \'\'\'
'''
print(newString)
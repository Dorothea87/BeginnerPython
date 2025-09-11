#Lists
my_list = [1,2,3,4]
print(my_list)
strings_list = ['I', 'am', 'tired']
print(strings_list)
mixed_list = [False, True, 'name', [1,2,3]]
print(len(mixed_list))
[1,2] == [2, 1] #false, order of elements matter

#Sets all elements have to be unique
my_set = {1, 2, 3, 4}
print(my_set)
print(type(my_set))
print(len(my_set))
new_set = {1, 1, 2, 2}
print(len(new_set))
print(new_set)
{1,2} == {2, 1} #true, order doesn't matter

#Tuples, order does matter, we cannot append to or remove from them
my_tuples = (1, 2, 3)
len(my_tuples)
(1, 2) == (2, 1) #false, order matters
#once a tuple is declared you cannot add to it or change any of the values in it -> memory efficient, Python uses only excatly the amount of storage it needs
#good for storing little things, like x, y coordinates

#Dictionaries, keys have to be unique
#Dictionaries & Sets: both have curly bracket, sets have unique values, dictionaries have unique keys, order doesn't matter
my_dictionary = {
    'apple': 'A fruit that grows on a tree',
    'bear': 'A scary animal'
}
print(my_dictionary['apple'])
#if/else statement
a = True
b = True
c = True
if a:
    print('It is true!')
    print('Also print this')
    if b:
        print('Both are true')
        if c:
            print('All three are true')
else:
    print('It is false!')
print('Always print this')

#for loops - iterate over iterables e.g. list
list = [1, 2, 3, 4, 5]
for item in list:
    print(item)

#while loops - keeps looping until boolean we pass is false
number = 0
while number <5:
    print(number)
    number = number + 1
#Functions
def multiplyByThree(val):
    return 3 * val

multiplyByThree(4)
print(multiplyByThree(4))

def multiply(val1, val2):
    return val1 * val2
print(multiply(3, 4))

a = [1, 2, 3]

def appendFour(myList):
    myList.append(4)

appendFour(a)
print(a)

#print returns None (special keyword) represents absence of value, none type
print(print("hello"))
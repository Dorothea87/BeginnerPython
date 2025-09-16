#Casting
print(bool(0))
print(bool(1))
print(bool(7)) #everything that is not 0 is cast as True, see:

print(bool('True'))
print(bool('False'))
print(bool(''))
print(bool([]))
print(bool({}))
print(bool([1,2]))
print(bool(None))

myList = [1,2]
if myList:
    print('mylist has some values in it') #this is casting, I could also write: if bool(myList):

#Boolean Logic
weatherIsNice = False
haveUmbrella = True

if not haveUmbrella or weatherIsNice:
    print("stay inside")
else:
    print("go for a walk")

weatherIsNice = True
haveUmbrella = False

if (not haveUmbrella) and (not weatherIsNice):
    print("stay inside")
else:
    print("go for a walk")

weatherIsNice = True
haveUmbrella = False

if haveUmbrella or weatherIsNice:
    print("go for a walk")
else:
    print("stay inside")
from decimal import Decimal, getcontext

#Integers and what you can do with it
print(int('100')) #casting as an int

int('100', 2) #converts it from one base to another, but has to be string first, takes the second number as the base to convert it from
print(int('100', 2)) #converts it from one base to another, but has to be string first, takes the second number as the base to convert it from

#Decimal
print(getcontext())
result = Decimal(1) / Decimal(3)
print(result)
getcontext().prec=4
print(getcontext())

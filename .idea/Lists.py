#List of strings
students = ["Anna", "Peter", "Karl"]
#List of numbers
numbers = [1, 2, 3, 4]
#empty List
certificates = []

print(students)
print(students[2])

#length of a list
print(len(students))

#Update an element in the list
students[1] = "Julie"
print(students)

#Add an element to the list
students.append("Sofia")
print(students)
students.insert(3, "Marc")
print(students)

#remove an element from the list
students.remove("Sofia")
print(students)
students.pop()
#can also do students.pop(2) and indicate an index you want to delete
print(students)

#Order a list
students = ["Maria", "Julian", "Frank", "Anna"]
students.sort()
print(students)
print(sorted(students))
students.reverse()
print(students)
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


#homework
countries = ["Japan", "Iceland", "New Zealand"]
print(countries)
countries.pop()
print(countries)
countries.insert(0, "South Africa")
print(countries)
print(len(countries))
countries.sort()
print(countries)

students = ["Maria", "Julian", "Marc", "Steve"]
#for loop
for student in students:
    print(f"The student's name is {student.title()}.")


countries = ["Japan", "France", "Norway"]
index = 0
for country in countries:
    print(f"My number {index + 1} country is {country.title()}")
    index = index + 1
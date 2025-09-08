#Creating a dictionary with key value pairs
temperatures = {"Lisbon": 12, "Paris": 15}
values = {1: 3, 2: 5, 3: 7}
ranking = {
    1: "Sara",
    2: "Julie",
    3: "Daniela"
}

#Creating a dictionary that is empty
winners = {}

#Accessing a value
print(temperatures["Paris"])
print(ranking)
print(temperatures.get("New York"))

#Add a key value pair
temperatures["Munich"] = 2
print(temperatures)

#Modify an existing value
temperatures["Lisbon"] = 25
print(temperatures)

#Remove key value pairs
del temperatures["Lisbon"]
print(temperatures)
temperatures.pop("Munich")

students = {
    1: {
    "first_name": "Maria",
    "last_name": "Miller",
    "country": "UK",
    "graduated": True
},
    2: {
        "first_name": "Peter",
        "last_name": "Miller",
        "country": "UK",
        "graduated": False
    }
}

countries = {"Japan": "Kyoto", "South Africa": "Cape Town", "Brazil": "Rio"}

print(countries)
del countries["Brazil"]
print(countries)
countries["New Zealand"] = "Auckland"
print(countries)
print(countries["Japan"])
print(countries["South Africa"])
print(countries["New Zealand"])

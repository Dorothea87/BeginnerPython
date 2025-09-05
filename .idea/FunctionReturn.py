def full_name(first_name, last_name, middle_name=None):
    """generate full name from first and last name"""
    if middle_name:
        return first_name + " " + middle_name + " " + last_name
    else:
        return first_name + " " + last_name

name = full_name("Peter", "Parker")
print("The full name is " + name)
name = full_name("Peter", "Parker", "Booboo")
print("The full name is " + name)

temperature = 15
city = "London"
print(f"It is currently {temperature}ºC in {city}.")

def farenheit_calculator(temperature):
    farenheit_temp = (temperature * 9/5) + 32
    return farenheit_temp

farenheit = farenheit_calculator(temperature)
print(f"it is currently {farenheit} ºF in {city}.")
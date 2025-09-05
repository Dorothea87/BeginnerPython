#function with two params
#call function twice
def city_temp(city, temp):
    """This method returns a string with a city and a temperature"""
    print(f"The temperature in {city} is currently {temp} degrees.")

city_temp("London", 17)
city_temp("Paris", 25)

def display_full_name(first_name, last_name, middle_name=""):
    """Display a full name"""
    if middle_name:
        full_name = first_name + " " + middle_name+ " "+ last_name
    else:
        full_name = first_name + " " + last_name
    print(full_name)

display_full_name("Sam", "Smith")
display_full_name("John", "Smith", "Peter")

#Create a function that has 3 parameters (a city temperature and humidity level) and display the following message:
#The temperature in London is 7 degrees with a humidity of 40%

def weather_display(city, temp, humidity=None):
    message = f"The temperature in {city} is {temp} degrees"
    if humidity:
        print(f"{message} with a humidity of {humidity}%.")
    print(f"{message}.")

weather_display("London", 11)
weather_display("Munich", 25, 35)
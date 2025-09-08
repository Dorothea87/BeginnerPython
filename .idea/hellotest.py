print("Hello World")
print("Hola Amiga, Sandra bonita!"); print("me gusta mucho el Python!")

def hello_world():
    name = input("What is your name? ")
    print(f"Hello {name.capitalize()}! ")

hello_world()

happy = input("Are you happy? (yes/no)")

if happy == 'yes':
    hello_world()


#Create a function asking for the city where you are and the current temperature and display this message:
#You are in Lisbon and it is currently 17ºC.
#Call this function twice.
#Bonus point: Display an error message if the user doesn’t enter a city or a temperature
def city_and_temp():
    city = input("Which city are you in?")
    temp = input("Whats the temperature in celcius?")
    if not city or not temp:
        print("Sorry, please enter a city and a temperature.")
    else:
        print(f"You are in {city.capitalize()} and it is currently {temp} °C.")
city_and_temp()
city_and_temp()

def greet_user(name, last_name):
    print(f"Hello {name} {last_name}")

greet_user("Dorothea", "Toeller")
import car_game.car  # local user class importing
from colorama import Fore, Style
import platform  # internal Python library

# pip is Python package manager/installer

print(platform.python_version())
print(Fore.GREEN + 'some red text' + Style.RESET_ALL)

print('one line')
print(car_game.car.Car)


def get_greeting():
    greeting = "Hello, SDA!"
    return greeting


print(get_greeting())

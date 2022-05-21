import pyfiglet
from termcolor2 import colored


massage = input('what would you like to print? : ')
colo = input('what color? : ')
ascii_art = pyfiglet.figlet_format(massage)
ascii_art = colored(ascii_art, (colo))

print(ascii_art)

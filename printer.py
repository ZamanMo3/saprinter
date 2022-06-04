import os
import pyfiglet
from termcolor2 import colored

os.system('pip install pyfiglet')
os.system('pip install termcolor2')

os.system('cls')


chanel = '@termux_scripte'
nexus = 'printer tools'
# c = pyfiglet.figlet_format(chanel)
z = pyfiglet.figlet_format(nexus)
p = colored(chanel, ('cyan'))
pr = colored(z, ('yellow'))

print(p)
print(pr)


massage = input('what would you like to print? : ') 
# massage = colored(massage, ('blue'))
colo = input('what color? : ')
# colo = colored(colo, ('red'))
ascii_art = pyfiglet.figlet_format(massage)
as_art = colored(ascii_art, (colo))


print(as_art)

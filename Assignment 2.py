

import pyfiglet

from rich import print

pyfiglet_colored_1 = pyfiglet.figlet_format("Welcome!",font="small", justify="center",width=130)
colors = ['bold yellow']
for color in colors:
    print(f'[{color}]{pyfiglet_colored_1}[/{color}]')
    
print(pyfiglet.figlet_format("Allow me to ask some questions", font="term", justify="center",width=130))

def if_else_no() :
    input_name = input("What is your name?: ")

    input_age = input("Now "+input_name+", how old are you?: ")

    input_address = input("Where do you live?: ")
    

    pyfiglet_colored_2 = pyfiglet.figlet_format("\n""So your name is: "+input_name+"", font="term", justify="center",width=130)
    pyfiglet_colored_3 = pyfiglet.figlet_format("\n""You are: "+input_age+"", font="term", justify="center",width=130)
    pyfiglet_colored_4 = pyfiglet.figlet_format("\n""And you live in: "+input_address+"", font="term", justify="center",width=130)
    for color in colors:
        print(f'[{color}]{pyfiglet_colored_2}[/{color}]')
        print(f'[{color}]{pyfiglet_colored_3}[/{color}]')
        print(f'[{color}]{pyfiglet_colored_4}[/{color}]')
    
    pyfiglet_colored_5 = pyfiglet.figlet_format("Thank you for answering", font="small", justify="center",width=135)
    input_result = input("If this is correct, type y, if not, type n: ")

    if input_result == 'y':
        print(f'[{color}]{pyfiglet_colored_5}[/{color}]')
    elif input_result == 'Y' :
        print(f'[{color}]{pyfiglet_colored_5}[/{color}]')
    elif input_result == 'yes' :
        print(f'[{color}]{pyfiglet_colored_5}[/{color}]')
    elif input_result == 'Yes' :
        print(f'[{color}]{pyfiglet_colored_5}[/{color}]')
    else:
        (if_else_no())
   
if_else_no()

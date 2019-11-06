import sys
import pandas
import random
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import colored,  cprint 
from pyfiglet import figlet_format                           
import inquirer

print(colored("""\

░█▀▀█ █░░ ░▀░ █▀▀█ █▀▀ 
▒█▄▄█ █░░ ▀█▀ █▄▄█ ▀▀█ 
▒█░▒█ ▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀ 

------------------------
Generate a fake biography.....by Jenius.io
------------------------

 ""","magenta"))

colnames = ['Fname', 'Lname', 'Status', 'Location', 'Occupation']
data = pandas.read_csv('alias3.csv', names=colnames)

Fname = data.Fname.tolist()
Lname = data.Lname.tolist()
Status = data.Status.tolist()
Location = data.Location.tolist()
Occupation = data.Occupation.tolist()

#cleaned lists
Fname2 = [x for x in Fname if str(x) != 'nan']
Lname2 = [x for x in Lname if str(x) != 'nan']
Status2 = [x for x in Status if str(x) != 'nan']
Location2 = [x for x in Location if str(x) != 'nan']
Occupation2 = [x for x in Occupation if str(x) != 'nan']

questions = [
  inquirer.List ('pronoun',
                message= colored("Choose pronouns","white"),
                choices=['She/Her', 'He/Him', 'They/Them'],
            ),
]
answers = inquirer.prompt(questions)

print(answers)

if answers == {'pronoun': 'She/Her'}:
# printing the list using loop 
    print("Your name is",random.choice(Fname2), random.choice(Lname2))
    print("You are",random.choice(Status2))
    print("You live in",random.choice(Location2))
    print("You work as a",random.choice(Occupation2))

elif answers == {'gender': 'He/Him'}:
    print("Still working on this..")

elif answers == {'gender': 'They/Them'}:
    print("Still working on this..")

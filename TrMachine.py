from colorama import init, Fore, Style;
from webbrowser import open;
import time;
import os;

def cls():
  os.system("cls");

def cooldown(seconds):
  time.sleep(seconds);

class Screen1:
  def choice1():
    inicial_logo = r"""
      ___________         _____                .__    .__                             /\
      \__    ___/______  /     \ _____    ____ |  |__ |__| ____   ____            /\  ||  /\
        |    |  \_  __ \/  \ /  \\__  \ _/ ___\|  |  \|  |/    \_/ __ \           ||--++--||
        |    |   |  | \/    Y    \/ __ \\  \___|   Y  \  |   |  \  ___/           ||--++--||
        |____|   |__|  \____|__  (____  /\___  >___|  /__|___|  /\___  >          \/  ||  \/
                              \/     \/     \/     \/        \/     \/                \/
      """
    print();
    print(Fore.GREEN + Style.BRIGHT + inicial_logo + Style.RESET_ALL);

    print()
    print(Fore.YELLOW + Style.BRIGHT + "[1]: open the holy terminal ... ");
    print("[2]: enter our whatsapp group ... ");
    print("[exit]: exit ... " + Style.RESET_ALL);

    global choice; choice = input(Fore.GREEN + Style.BRIGHT + "[ ... " + Style.RESET_ALL);

class Screen2:

  def the_holy_terminal(): # THE MOST IMPORTANT PART OF THE CODE . . .
    global command_of_user; command_of_user = True; # ((incomplete)) . . .

Screen1.choice1(); #RUNNING THE MAIN CODE

if choice == "exit":
  number_of_loading = 5;
  number_of_dots = 0;
  dot = "((error: dots not defined, fix it u monkey))";

  for loading in range(5):
    if number_of_dots != 3: number_of_dots += 1;
    elif number_of_dots == 3: number_of_dots = 1;
    else: number_of_dots = 0; 

    if number_of_dots == 1: dot = " . ";
    elif number_of_dots == 2: dot = " . . ";
    elif number_of_dots == 3: dot = " . . . ";
    else: dot = " ((error: your code is a chaos, lad)) ";

    cls();
    print(Fore.YELLOW + Style.BRIGHT + "[ info: closing the system in ", number_of_loading ," secconds", dot ,"]" + Style.RESET_ALL);
    cooldown(1);

    number_of_loading -= 1;

  exit();

elif choice == "1":
  number_of_loading = 3;
  number_of_dots = 0;
  dot = "((error: dots not defined, fix it u monkey))";

  for loading in range(3):
    if number_of_dots != 3: number_of_dots += 1;
    elif number_of_dots == 3: number_of_dots = 1;
    else: number_of_dots = 0; 

    if number_of_dots == 1: dot = " . ";
    elif number_of_dots == 2: dot = " . . ";
    elif number_of_dots == 3: dot = " . . . ";
    else: dot = " ((error: your code is a chaos, lad)) ";

    cls();
    print(Fore.YELLOW + Style.BRIGHT + "[ info: opening the holy terminal in ", number_of_loading ," secconds", dot ,"]" + Style.RESET_ALL);
    cooldown(1);

    number_of_loading -= 1;

  Screen2.the_holy_terminal();

elif choice == "2":
  number_of_loading = 3;
  number_of_dots = 0;
  dot = "((error: dots not defined, fix it u monkey))";

  for loading in range(3):
    if number_of_dots != 3: number_of_dots += 1;
    elif number_of_dots == 3: number_of_dots = 1;
    else: number_of_dots = 0; 

    if number_of_dots == 1: dot = " . ";
    elif number_of_dots == 2: dot = " . . ";
    elif number_of_dots == 3: dot = " . . . ";
    else: dot = " ((error: your code is a chaos, lad)) ";

    cls();
    print(Fore.YELLOW + Style.BRIGHT + "[ info: redirecting in ", number_of_loading ," secconds", dot ,"]" + Style.RESET_ALL);
    cooldown(1);

    number_of_loading -= 1;

  open("https://chat.whatsapp.com/LoMbxPwhj6vGacSQIvGU2I?mode=wwt");

else:
    print("put a valid answer.")
    cooldown(2.5);
    cls();
    Screen1.choice1();

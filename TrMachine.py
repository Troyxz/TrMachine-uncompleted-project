from colorama import init, Fore, Style
import time;
import os;

def cls():
  os.system("cls")

def cooldown(seconds):
  time.sleep(seconds)

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
    print(Fore.GREEN + Style.BRIGHT + inicial_logo + Style.RESET_ALL)

    print()
    print(Fore.YELLOW + Style.BRIGHT + "[sb]: search in bible ... ")
    print("[sc]: search in cathecism ... ")
    print("[exit]: exit ... " + Style.RESET_ALL)

    global choice; choice = input(Fore.GREEN + Style.BRIGHT + "[ ... " + Style.RESET_ALL)

class Screen2:

  def bible_section():
    print()

  def cathecism_section():
    print()

Screen1.choice1() #RUNNING THE MAIN CODE

if choice == "exit":
  print()
  print(Fore.YELLOW + Style.BRIGHT + "[ info: closing the system in 5 seconds ... ]" + Style.RESET_ALL)
  cooldown(5)
  exit()

elif choice == "sb":
  print()
  print(Fore.YELLOW + Style.BRIGHT + "[ info: Opening the bible section ... ]" + Style.RESET_ALL)
  cooldown(2.5)
  Screen2.bible_section()

elif choice == "sc":
  print()
  print(Fore.YELLOW + Style.BRIGHT + "[ info: Opening the cathecis, section ... ]" + Style.RESET_ALL)
  cooldown(2.5)
  Screen2.cathecism_section()

else:
    print("put a valid answer.")
    cooldown(2.5)
    cls()
    Screen1.choice1()
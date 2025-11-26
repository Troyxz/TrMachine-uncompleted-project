from stringprep import in_table_b1
from colorama import init, Fore, Style
from webbrowser import open
import time
import os

global command

def cls():
    os.system("cls")

def cooldown(seconds):
    time.sleep(seconds)

class Loading:

    @staticmethod
    def the_exit(loading_time): # 3
        number_of_dots = 0
        dot = "((error: dots not defined, fix it u monkey))"

        for loading in range(loading_time):

            if number_of_dots != 3: number_of_dots += 1
            elif number_of_dots == 3: number_of_dots = 1
            else: number_of_dots = 0

            if number_of_dots == 1: dot = " . "
            elif number_of_dots == 2: dot = " . . "
            elif number_of_dots == 3: dot = " . . . "
            else: dot = " ((error: your code is a chaos, lad)) "

            cls()
            print(Fore.YELLOW + Style.BRIGHT + "[ info: closing the system in ", loading_time ," secconds", dot ,"]" + Style.RESET_ALL)
            cooldown(1)
            loading_time = loading_time - 1

    @staticmethod
    def the_holy_terminal(loading_time):
        number_of_dots = 0
        dot = "((error: dots not defined, fix it u monkey))"

        for loading in range(loading_time):
            if number_of_dots != 3: number_of_dots += 1
            elif number_of_dots == 3: number_of_dots = 1
            else: number_of_dots = 0

            if number_of_dots == 1: dot = " . "
            elif number_of_dots == 2: dot = " . . "
            elif number_of_dots == 3: dot = " . . . "
            else: dot = " ((error: your code is a chaos, lad)) "

            cls()
            print(Fore.YELLOW + Style.BRIGHT + "[ info: open the terminal in ", loading_time ," secconds", dot ,"]" + Style.RESET_ALL)
            cooldown(1)

            loading_time -= 1
    @staticmethod
    def the_redirect(number_of_loading):
         number_of_dots = 0
         dot = "((error: dots not defined, fix it u monkey))"

         for loading in range(3):
               if number_of_dots != 3: number_of_dots += 1
               elif number_of_dots == 3: number_of_dots = 1
               else: number_of_dots = 0

               if number_of_dots == 1: dot = " . "
               elif number_of_dots == 2: dot = " . . "
               elif number_of_dots == 3: dot = " . . . "
               else: dot = " ((error: your code is a chaos, lad)) "

               cls()
               print(Fore.YELLOW + Style.BRIGHT + "[ info: redrecting in ", number_of_loading ," secconds", dot ,"]" + Style.RESET_ALL)
               cooldown(1)

               number_of_loading -= 1


class Screen1:
    choice = ""

    @staticmethod
    def choice1():
        inicial_logo = r"""
          ___________         _____                .__    .__                             /\
          \__    ___/______  /     \ _____    ____ |  |__ |__| ____   ____            /\  ||  /\
            |    |  \_  __ \/  \ /  \\__  \ _/ ___\|  |  \|  |/    \_/ __ \           ||--++--||
            |    |   |  | \/    Y    \/ __ \\  \___|   Y  \  |   |  \  ___/           ||--++--||
            |____|   |__|  \____|__  (____  /\___  >___|  /__|___|  /\___  >          \/  ||  \/
                                  \/     \/     \/     \/        \/     \/                \/
          """
        print()
        print(Fore.GREEN + Style.BRIGHT + inicial_logo + Style.RESET_ALL)

        print()
        print(Fore.YELLOW + Style.BRIGHT + "[1]: open the holy terminal ... ")
        print("[2]: enter our whatsapp group ... ")
        print("[exit]: exit ... " + Style.RESET_ALL)

        choice = input(Fore.GREEN + Style.BRIGHT + "[ ... " + Style.RESET_ALL)

        if choice == "exit":
            Loading.the_exit(3)
            exit()
        elif choice == "1":
            Loading.the_holy_terminal(3)
            Screen2.the_holy_terminal_wellcome()
        elif choice == "2":
            Loading.the_redirect(3)
            open("https://chat.whatsapp.com/LoMbxPwhj6vGacSQIvGU2I?mode=wwt")
        else:
            print("put a valid answer.")
            cooldown(2.5)
            cls()
            Screen1.choice1()

class Check:
    @staticmethod
    def execute_commands(command):
        Screen2.command_input()
        commands_list = {"commands", "time", "exit"}
        match command:
            case "commands":
                print(f"commands: {commands_list}")
            case _:
                print("╒══[info]═════════════════════════╕")
                print("│invalid command ...              │")
                print("│press enter to continue ...      │")
                print("╘═════════════════════════════════╛")
                input("... ")
                cls()
                Screen2.command_input()
        return True

class Screen2:
    command_loop = True
    @staticmethod
    def the_holy_terminal_wellcome(): # THE MOST IMPORTANT PART OF THE CODE . . .
        cls()
        print("""
    1.  Wellcome to the terminal !
    2.  This work is marked by no copyrights, public domain. (CC) (0)
    3.  You can use, modify, whatever. Christianity is free !
    4.  To view a copy of this mark, visit https://creativecommons.org/publicdomain/zero/1.0/
        """)
        print("")
        print("╒══[info]═════════════════════════╕")
        print("│press enter to continue ...      │")
        print("╘═════════════════════════════════╛")
        input("... ")
        cls()

        Screen2.command_input()

    @staticmethod
    def command_input():
        command_loop = True
        command = ""
        while command_loop:
            command = input("▷ ")
            Check.execute_commands(command)
            command_loop = False


Screen1.choice1() # RUNNING THE MAIN CODE

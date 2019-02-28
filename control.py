from custom_control import *
from error_checks import *
import sys


def enter_mode(mode, rerun_count=0):
    if mode == "sectors":
        Sectors(rerun_count)
    else:
        Custom(rerun_count)


def get_choices():
    print("\nYou can exit the program, run another test in the current mode, or switch modes.")
    ans = str_verify("I want to (exit/switch/rerun): ", "exit,switch,rerun", lower = 'yeet')

    return ans


def get_modes():
    print("\nPlease select from one of the following modes:\nCustom\nSectors\n")
    mode = str_verify("I choose (custom/sectors): ", "custom,sectors", lower = "yeet")

    return mode


def parse_choice(firsttime, mode):
    if firsttime == True:
        enter_mode(mode)

    else:   
        choice = get_choices()

        if choice == 'exit':
            print("\nSee you later!")
            sys.exit()
        
        elif choice == 'rerun':
            enter_mode(mode, rerun_count = 1)

        else:
            mode = get_modes()
            enter_mode(mode)


def main():
        first_time = True

        print("BIG MAN, THIS IS THE ALGORITHMIC TRADING SVM\n")
        
        mode = get_modes()
        parse_choice(first_time, mode)
        first_time = False

        while True:
            choice = parse_choice(first_time, mode)   


if __name__ == '__main__':
    main()
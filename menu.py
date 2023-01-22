## Menu to types of IA
import os
from colorama import Fore
from .types import bg
from .types import ml
from .types import dl

clear = lambda: os.system('cls')


def main_menu():
        clear()
        try:
            print_menu()
            option = int(input('Escolhe uma opção, neste caso um número: '))
            choose_menu(option)
        except KeyboardInterrupt:
            print("Obrigado!")
        except:
            print("Peço desculpa. Algo correu mal! :(")


def print_menu():
    menu_options = {
    1: 'Machine Learning',
    2: 'Deep Learning',
    3: 'Big Data',
    4: 'Exit',
}
    for key in menu_options.keys():
        print(Fore.LIGHTCYAN_EX + key, Fore.GREEN + '->', Fore.LIGHTWHITE_EX + menu_options[key], end=Fore.RESET) 

def choose_menu(option):
    clear()
    if option == 1:
        m = bg.BG()
        m.menu()
    elif option == 2:
        d = ml.ML()
        d.menu()
    elif option == 3:
        b = bg.BG()
        b.menu()
    elif option == 4:
        print('Obrigado por teres estado aqui! Até uma próxima.')
        exit()
    else:
        print('Opção inválida. Por favor, escolhe um número entre 1 e 4.')
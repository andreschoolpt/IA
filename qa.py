## Questions && Asks
from alan import Alan_Turing
from colorama import Fore
alan = Alan_Turing()

def start(user):
    ask = input("[S]/[N] Sim ou Não -> ").upper()
    if ask == "S":
        print("É impossível saberem quem começou... Desculpa, não foi o Sr. João! 🙁", end="\n")
        print("Será mesmo que sabes, %s?" % user)
        if (input(f"{Fore.CYAN}[{Fore.GREEN}S{Fore.CYAN}]{Fore.YELLOW}/{Fore.CYAN}[N] ").upper()) == "S":
            print(f"{Fore.MAGENTA + user}{Fore.RESET}, fico feliz de saberes!! Vamos lá ver mais acerca de IA...")
            from menu import main_menu
            main_menu()
    elif ask == "N":
        alan.explicacao()
    else:
        print(f"{Fore.LIGHTRED_EX}Ahh.. Acho que essa resposta não é válida mas... okay... {Fore.RESET}")
        start(user)
import qa
from colorama import Fore, init


def intro(user):
    print(f"{Fore.RESET}Olá {Fore.MAGENTA + user}{Fore.RESET}, desde já, agradeço por estares a ler isto num computador, mas já pensanste que poderia ser num telemóvel... Sabes quem é que começou com a ideia da Inteligência Artifical? ")
    print(f"{Fore.LIGHTRED_EX}André Castanho - 9ºC {Fore.RESET}")
    qa.start(user)

if __name__ == "__main__":
    init()
    print(f"{Fore.LIGHTYELLOW_EX}AVISO{Fore.YELLOW} -{Fore.CYAN} Nas questões de {Fore.GREEN}SIM {Fore.CYAN}ou {Fore.RED}NÃO{Fore.CYAN}, Por favor responder com a letra indicada {Fore.LIGHTBLUE_EX}(S/N){Fore.RESET}")
    user = str(input(f"Qual é o seu nome? {Fore.MAGENTA}"))
    try:
        if user is None or user == "":
            print("Por favor, tente escolher um nome... :(")
    except:
            print("Curioso... O seu nome não deve ser %s" % user)
    intro(user)
    

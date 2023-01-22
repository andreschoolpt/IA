## Machine Learning
import os
from menu import main_menu
clear = lambda: os.system('cls')
class ML():
    def __init__(self) -> None:
        pass
        
    def menu(self): #Menu para escolher a opção dentro do ramo pretendido
        print("Machine Learning")
        self.lista = {}
        self.lista[1] = "Definição"
        self.lista[2] = "Como pode ajudar as pessoas?"
        self.lista[3] = "Recuar"
        for op in self.lista:
            print(op, "->", self.lista[op])
        try:
            usr = int(input("-> Quero saber mais da opção Nº"))
            if usr == 1:
                self.what_is()
                self.back()
            elif usr == 2:
                self.help_people()
                self.back()
            else:
                main_menu()
        except KeyboardInterrupt:
          print("Obrigado!! Até uma próxima! :D")
        except:
            clear()
            print("Ops! Algo deu erro. Desculpa.")

        def back():
            if input("\nVoltar atrás? Y/N") == "Y":
                clear()
                self.menu()
            else:
                print("Muito obrigado por teres estado aqui! :)")
                exit()


    def what_is(self): # What is it?
        clear()
        print("Machine learning é um método de análise de dados que automatiza a construção de modelos analíticos")
        self.back()

    def help_people(self): # Que maneiras este ramo ajudou
        clear()
        self.arr = ['Automatizar tarefas', 'Gerenciar dados não estruturados', 'Resolver problemas que humanos não conseguem']
        for i, l in enumerate(self.arr):
            print(f"{i}. {l}")
        self.back()


    def back(self):
            if input("\nVoltar atrás? Y/N") == "Y":
                clear()
                self.menu()
            else:
                print("Muito obrigado por teres estado aqui! :)")
                exit()
## Classe do Alan Turing para termos uma noção da importância dele do avanço da tecnologia

class Alan_Turing():
    def __init__(self) -> None:
        self.nome = "Alan Mathison Turing"
        self.birthday = "23 Junho 1912"
        self.death = "07 Junho 1954"
        self.resumo = ("Turing foi uma das pessoas a trabalharem nos primeiros computadores", "Ele estabeleceu as bases teóricas para o desenvolvimento dos computadores modernos, foi um dos pioneiros na pesquisa sobre inteligência artificial")

    def explicacao(self):
        print("Então... Alan Turning basicamente criou uma nova era da tecnologia, sem ele, nada era como a conhecemos hoje.")
        if (input("\rQueres mais um pequeno resumo? [S/N]").upper() == "S"):
            self.resumo()
        else:
            print("Não queres mesmo saber quem é... ? :(")
            print("Sendo assim... Não-te quero mais aqui. Desculpa.")

    def resumo(self):
        return self.resumo[1]
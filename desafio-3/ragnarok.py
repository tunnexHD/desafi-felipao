class HeroiRagnarok:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "Lanças de Gelo"
        elif self.tipo == "espadachim":
            ataque = "Golpe Fulminante"
        elif self.tipo == "gatuno":
            ataque = "Envenenar"
        elif self.tipo == "noviço":
            ataque = "Luz Divina"
        elif self.tipo == "mercador":
            ataque = "Mammonita"
        elif self.tipo == "arqueiro":
            ataque = "Rajada de Flechas"
        else:
            ataque = "não possui um ataque definido"

        mensagem = f"O {self.tipo} atacou usando {ataque}"
        print(mensagem)


heroi1 = HeroiRagnarok("Heimdall", 75, "espadachim")
heroi1.atacar()

heroi2 = HeroiRagnarok("Hogun", 40, "arqueiro")
heroi2.atacar()

heroi3 = HeroiRagnarok("Loki", 60, "mago")
heroi3.atacar()

heroi4 = HeroiRagnarok("Odin", 99, "gatuno")
heroi4.atacar()

heroi5 = HeroiRagnarok("Frigga", 88, "noviço")
heroi5.atacar()

heroi6 = HeroiRagnarok("Thor", 75, "mercador")
heroi6.atacar()

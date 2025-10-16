import random

def jugar():
    print("\n-- Adivina el número --")
    numero_secret = random.randint(1, 10)
    intents = 3
    while intents > 0:
        try:
            num = int(input(f"Introdueix un número del 1 al 10 ({intents} intents): "))
            if not 1 <= num <= 10:
                print("Número fora de rang.")
                continue
        except ValueError:
            print("Has d'introduir un número.")
            continue

        if num == numero_secret:
            print("🎉 Has encertat el número!")
            return
        elif num < numero_secret:
            print("El número és més gran.")
        else:
            print("El número és més petit.")
        intents -= 1
    print(f"Has perdut! El número era {numero_secret}.")

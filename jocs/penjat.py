from faker import Faker
import random

def generar_paraules(num=30):
    fake = Faker("es_ES")  # Locale español válido
    paraules = set()
    while len(paraules) < num:
        paraula = fake.word()
        if 3 <= len(paraula) <= 7 and paraula.isalpha():
            paraules.add(paraula.lower())
    return list(paraules)

def jugar():
    print("\n-- El Penjat --")
    paraules = generar_paraules()
    paraula = random.choice(paraules)
    lletres_adivinades = set()
    intents = len(paraula) * 2

    def mostrar_tauler():
        return ' '.join([lletra if lletra in lletres_adivinades else '_' for lletra in paraula])

    while intents > 0:
        print("\nParaula:", mostrar_tauler())
        lletra = input(f"Introdueix una lletra ({intents} intents): ").lower()
        if len(lletra) != 1 or not lletra.isalpha():
            print("Has d'introduir una sola lletra.")
            continue
        if lletra in lletres_adivinades:
            print("Ja has introduït aquesta lletra.")
            continue

        lletres_adivinades.add(lletra)
        if lletra in paraula:
            print("✅ Correcte!")
        else:
            print("❌ Incorrecte.")
            intents -= 1

        if all(l in lletres_adivinades for l in paraula):
            print("\n🎉 Has guanyat! La paraula era:", paraula)
            return

    print("\nHas perdut! La paraula era:", paraula)

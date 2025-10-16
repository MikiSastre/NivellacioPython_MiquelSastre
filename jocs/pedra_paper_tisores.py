import random

def jugar():
    print("\n-- Pedra - Paper - Tisores --")
    opcions = ["pedra", "paper", "tisores"]
    puntuacio_usuari = 0
    puntuacio_maquina = 0

    def determinar_guanyador(usuari, maquina):
        if usuari == maquina:
            return "empat"
        if (usuari == "pedra" and maquina == "tisores") or \
           (usuari == "paper" and maquina == "pedra") or \
           (usuari == "tisores" and maquina == "paper"):
            return "usuari"
        return "maquina"

    while puntuacio_usuari < 3 and puntuacio_maquina < 3:
        print(f"\nMarcador → Tu: {puntuacio_usuari} - Maquina: {puntuacio_maquina}")
        usuari = input("Pedra, paper o tisores? ").lower()
        if usuari not in opcions:
            print("Opció no vàlida.")
            continue
        maquina = random.choice(opcions)
        print(f"La màquina ha triat: {maquina}")
        resultat = determinar_guanyador(usuari, maquina)
        if resultat == "usuari":
            print("Guanyes aquest punt!")
            puntuacio_usuari += 1
        elif resultat == "maquina":
            print("La màquina guanya aquest punt!")
            puntuacio_maquina += 1
        else:
            print("Empat!")

    guanyador = "Tu" if puntuacio_usuari == 3 else "La màquina"
    print(f"\n🎉 {guanyador} has guanyat el joc!")

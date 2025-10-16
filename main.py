from jocs import adivina, pedra_paper_tisores, penjat, tres_en_ratlla

def mostrar_menu():
    print("\n===== MENÚ DE JOCS =====")
    print("1. Adivina el número")
    print("2. Pedra - Paper - Tisores")
    print("3. El Penjat")
    print("4. Tres en ratlla")
    print("0. Sortir")

def input_valid(opcions):
    while True:
        opcio = input("Selecciona una opció: ")
        if opcio in opcions:
            return opcio
        else:
            print("Opció no vàlida. Torna-ho a intentar.")

def main():
    while True:
        mostrar_menu()
        opcio = input_valid(["0", "1", "2", "3", "4"])
        if opcio == "1":
            adivina.jugar()
        elif opcio == "2":
            pedra_paper_tisores.jugar()
        elif opcio == "3":
            penjat.jugar()
        elif opcio == "4":
            tres_en_ratlla.jugar()
        elif opcio == "0":
            print("Adéu! 👋")
            break

if __name__ == "__main__":
    main()

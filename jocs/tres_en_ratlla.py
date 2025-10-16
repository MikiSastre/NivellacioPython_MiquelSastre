def jugar():
    print("\n-- Tres en ratlla --")
    tauler = [" "]*9

    def mostrar_tauler():
        print("\n")
        for i in range(0, 9, 3):
            print(f"{tauler[i] or i+1} | {tauler[i+1] or i+2} | {tauler[i+2] or i+3}")
            if i < 6:
                print("--+---+--")

    def comprovar_guanyador(jugador):
        combinacions = [(0,1,2),(3,4,5),(6,7,8),
                        (0,3,6),(1,4,7),(2,5,8),
                        (0,4,8),(2,4,6)]
        return any(tauler[a] == tauler[b] == tauler[c] == jugador for a,b,c in combinacions)

    jugador = "X"
    for torn in range(9):
        mostrar_tauler()
        while True:
            try:
                casella = int(input(f"Torn de {jugador}. Tria una casella (1-9): ")) - 1
                if tauler[casella] == " ":
                    break
                else:
                    print("Casella ocupada.")
            except:
                print("Entrada no vàlida.")
        tauler[casella] = jugador
        if comprovar_guanyador(jugador):
            mostrar_tauler()
            print(f"🎉 El jugador {jugador} ha guanyat!")
            return
        jugador = "O" if jugador == "X" else "X"
    mostrar_tauler()
    print("Empat!")

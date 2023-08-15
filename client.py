from sudoku import sudoku

if __name__ == "__main__":
    game = sudoku()
    mode = False
    while(not mode):
        print("Selecciona com vols la creacio del mapa:")
        print("")
        print("1- Mapa predefinit")
        print("")
        print("2- Generar mapa aleatori")
        print("")
        option = int(input("Opcio : "))
        mode = game.selectMode(option)
    if mode == 2:
        dificulty = False
        while(not dificulty):
            print("Selecciona el nivell de dificultat del mapa:")
            print("")
            print("1- Facil")
            print("")
            print("2- Mitja")
            print("")
            print("3- Dificil")
            print("")
            option = int(input("Opcio : "))
            dificulty = game.selectDificulty(option)
    while(game.tries > 0 and not game.win):
        game.printMap()
        print("Inroduce el numero i la casilla donde lo quieres introducir ")
        num = int(input("Numero : "))
        posx = int(input("Posicion de la columna: "))
        posy = int(input("Posicion de la fila: "))
        tried = game.addNumber(num,posx,posy)
        if tried:
            game.win = game.checkWin()
    if game.win:
        print("You have won")
    else:
        print("You have lost")
import os
import random

move_list = ["Pedra", "Papel", "Tesoura"]

player_win = 0
computer_win = 0
print("=====================================")
print("\nBem vindo ao jogo Pedra, Papel ou Tesoura")

def main_print():
    print("=====================================")
    print("\nPlacar")
    print(f"Você ganhou {player_win} vezes")
    print(f"O computador ganhou {computer_win} vezes")
    print(" ")
    print("Escolha qual jogar?")
    print("| 0 - Pedra | 1 - Papel | 2 - Tesoura |")

def select_move():
    return random.choice(move_list)

def get_player_move():
    while True:
        try:
            player_move = int(input())
            if player_move not in [0, 1, 2]:
                raise
            return move_list[player_move]
        except Exception as error:
            print(error)

def select_winner(p_move, c_move):
    global player_win, computer_win
    if p_move == "Papel":
        if c_move == "Pedra":
            player_win += 1
            return "p"
        elif c_move == "Tesoura":
            computer_win += 1
            return "c"
    else:
        return "d"

    if p_move == "Pedra":
        if c_move == "Tesoura":
            player_win += 1
            return "p"
        elif c_move == "Papel":
            computer_win += 1
            return "c"
    else:
        return "d"

    if p_move == "Tesoura":
        if c_move == "Papel":
            player_win += 1
            return "p"
        elif c_move == "Pedra":
            computer_win += 1
            return "c"
    else:
        return "d"

again = 1
while again == 1:
    main_print()
    player_move = get_player_move()
    computer_move = select_move()
    winner = select_winner(player_move, computer_move)

    print("") 
    print("=================================")
    print(f"Sua jogada foi: {player_move}")
    print(f"\nA jogada do computador foi: {computer_move}")

    if winner == "p":
        print("Você venceu!")
    elif winner == "c":
        print("Você perdeu!")
    else:
        print("Empatou!!!")
    print("==========================")

    while True:
        print("Deseja jogar novamente? 0 - SIM || 1 - NÃO")
        next = int(input())
        if next == 0:
            break
        elif next == 1:
            again = 0
            break
    os.system("clear")
import random

board_size = 5
num_ships = 3

def create_board():
    board = []
    for _ in range(board_size):
        row = ["O"] * board_size
        board.append(row)
    return board

def place_ships(board):
    ships_placed = 0
    while ships_placed < num_ships:
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        if board[row][col] == "O":
            board[row][col] = "S"
            ships_placed += 1

def print_board(board):
    for row in board:
        print(" ".join(row))

def play_game():
    board = create_board()
    place_ships(board)

    print("=== Permainan Battleship ===")
    print("Anda harus menembak {} kapal.".format(num_ships))
    print("Koordinat berada dalam rentang 0-{}.".format(board_size - 1))

    num_guesses = 0
    while True:
        print("\nTebak koordinat:")
        guess_row = int(input("Baris: "))
        guess_col = int(input("Kolom: "))

        if guess_row < 0 or guess_row >= board_size or guess_col < 0 or guess_col >= board_size:
            print("Koordinat di luar rentang. Silakan coba lagi.")
            continue

        if board[guess_row][guess_col] == "X":
            print("Anda telah menebak koordinat ini sebelumnya. Silakan coba lagi.")
            continue

        if board[guess_row][guess_col] == "S":
            print("Selamat! Anda menghancurkan sebuah kapal.")
            board[guess_row][guess_col] = "X"
            num_guesses += 1
        else:
            print("Tembakan Anda meleset.")
            num_guesses += 1

        print("Papan Permainan:")
        print_board(board)

        if num_guesses == num_ships:
            print("\nAnda berhasil menghancurkan semua kapal!")
            break

def main():
    while True:
        play_game()
        play_again = input("\nIngin bermain lagi? (y/n): ")
        if play_again.lower() != 'y':
            break

    print("Terima kasih telah bermain!")

if __name__ == '__main__':
    main()

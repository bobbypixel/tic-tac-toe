def get_choice(prompt, options) -> str:
    while (choice := input(prompt).lower()) not in options:
        print(f"Error! Your options are: {', '.join(options)}")

    return choice


def check_game_win(board: str) -> bool:
    winning_positions = [
        [2, 6, 10],
        [25, 29, 33],
        [48, 52, 56],
        [2, 25, 48],
        [6, 29, 52],
        [10, 33, 56],
        [2, 29, 56],
        [10, 29, 48],
    ]
    return any(
        all(board[j] != " " and board[j] == board[i[0]] for j in i)
        for i in winning_positions
    )


def start_game():
    print("New game started!")

    game_over = False
    board = "\n   |   |  \n-----------\n   |   |  \n-----------\n   |   |   \n"
    board_guide = "\n   |   |         0 | 1 | 2 \n-----------     -----------\n   |   |         3 | 4 | 5 \n-----------     -----------\n   |   |         6 | 7 | 8 \n"
    current_player = 0
    turn = 0

    board_positions = [2, 6, 10, 25, 29, 33, 48, 52, 56]
    player_options = list(map(str, range(9)))

    while not game_over:
        turn += 1
        player_prompt = (
            f"select a position [{', '.join(i for i in player_options)}]:\n>>> "
        )
        position = get_choice(
            f"{board_guide if turn == 1 else board}\nTurn {turn}.\nPlayer {[1,2][current_player]}, {player_prompt}",
            player_options,
        )
        player_options.remove(position)
        player_piece = ["O", "X"][current_player]
        player_move = board_positions[int(position)]
        board = board[:player_move] + player_piece + board[player_move + 1 :]
        current_player = (current_player + 1) % 2
        game_over = check_game_win(board) or not len(player_options)

    print(board)
    if check_game_win(board):
        print(f"Game over! Player {[1, 2][current_player-1]} wins!")
    else:
        print("Tie game!")


def show_instructions():
    board_options = (
        "\n 0 | 1 | 2 \n-----------\n 3 | 4 | 5 \n-----------\n 6 | 7 | 8 \n"
    )
    print(board_options)
    print(
        "Rules of Tic-Tac-Toe: Each player will take turns placing their pieces on a 3x3 grid. The integer on the grid are the positions that the players can place their pieces. The first player to get three in a row wins!"
    )


def start():
    print("❌ A SIMPLE TIC-TAC-TOE GAME ⭕")

    menu_prompt = "\nMain menu: [S]tart a new game, [I]nstructions, [Q]uit game\n>>> "
    menu_options = {
        "s": start_game,
        "i": show_instructions,
        "q": None,
    }

    choice = get_choice(menu_prompt, menu_options)
    while choice != "q":
        menu_options[choice]()
        choice = get_choice(menu_prompt, menu_options)

    print("Thanks for playing!")


if __name__ == "__main__":
    start()

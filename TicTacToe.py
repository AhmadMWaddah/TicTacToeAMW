#   --------------------  Creating Global Variables.    --------------------
game_still_going = True
winner = None
player_totem = 'X'
tic_tac_toe_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
cells = ['0', '1', '2', '3', '4', '5', '6', '7', '8']


#   --------------------  Drawing Tic Tac Toe Board.    --------------------
def draw_board():
    print(f'||~~~~~||~~~~~||~~~~~||')
    print(f'||  {tic_tac_toe_board[0]}  ||  {tic_tac_toe_board[1]}  ||  {tic_tac_toe_board[2]}  ||')
    print(f'||~~~~~||~~~~~||~~~~~||')
    print(f'||  {tic_tac_toe_board[3]}  ||  {tic_tac_toe_board[4]}  ||  {tic_tac_toe_board[5]}  ||')
    print(f'||~~~~~||~~~~~||~~~~~||')
    print(f'||  {tic_tac_toe_board[6]}  ||  {tic_tac_toe_board[7]}  ||  {tic_tac_toe_board[8]}  ||')
    print(f'||~~~~~||~~~~~||~~~~~||')


draw_board()


#   --------------------  Tic Tac Toe Game Play Function Code.    --------------------
def play_tic_tac_toe():
    # Starting Player.
    global player_totem

    # Display Board
    draw_board()

    # While Game Still Going.
    global game_still_going
    while game_still_going:
        # Handle Turn For Each Player.
        handle_players_turn(player_totem)

        # Check If Game Over,
        check_game_over()

        # Flipping Player.
        flipping_player()

    # If There Is Winner.
    if winner == 'X' or winner == 'O':
        print(f'Player "{winner}" Has Won.')
    elif winner is None:
        print('This Is Tie.')


#   --------------------  Handle Single Player Turn Function Code.    --------------------
def handle_players_turn(player_icon):
    # Display Player Turns
    print(f"{player_icon}'s Player Turn.")

    # Taking Board Cell From Player.
    board_cell = input(' Please Enter Number From 0 To 8 : ')
    global cells
    # Check Player Input Validation Ask Again If Not Valid.
    while board_cell not in cells:
        board_cell = input(' Please Enter Number From 0 To 8 : ')

    board_cell = int(board_cell)
    # Insert Player Totem Inside The Chosen Board Cell
    if tic_tac_toe_board[board_cell] == ' ':
        tic_tac_toe_board[board_cell] = player_icon
        # Draw The Tic Tac Toe Again
        draw_board()
    else:
        handle_players_turn(player_icon)


#   --------------------  Check If Game Is Over Function Code.    --------------------
def check_game_over():
    # Check If There Is A Winner.
    check_if_win(player_totem)

    # Check If There Is No Winner, And It Is Tie.
    check_if_tie()


#   --------------------  Check If There Is A Winner Function Code.    --------------------
def check_if_win(player_symbol):
    # Manipulate Global Variables.
    global winner
    global game_still_going
    # Check If There Is Any Contiguous Three Cells Have Same Symbol For Any Player.
    if (tic_tac_toe_board[0] == player_symbol and tic_tac_toe_board[1] == player_symbol and tic_tac_toe_board[
        2] == player_symbol) or (
            tic_tac_toe_board[3] == player_symbol and tic_tac_toe_board[4] == player_symbol and tic_tac_toe_board[
        5] == player_symbol) or (
            tic_tac_toe_board[6] == player_symbol and tic_tac_toe_board[7] == player_symbol and tic_tac_toe_board[
        8] == player_symbol) or (
            tic_tac_toe_board[0] == player_symbol and tic_tac_toe_board[3] == player_symbol and tic_tac_toe_board[
        6] == player_symbol) or (
            tic_tac_toe_board[1] == player_symbol and tic_tac_toe_board[4] == player_symbol and tic_tac_toe_board[
        7] == player_symbol) or (
            tic_tac_toe_board[2] == player_symbol and tic_tac_toe_board[5] == player_symbol and tic_tac_toe_board[
        8] == player_symbol) or (
            tic_tac_toe_board[0] == player_symbol and tic_tac_toe_board[4] == player_symbol and tic_tac_toe_board[
        8] == player_symbol) or (
            tic_tac_toe_board[2] == player_symbol and tic_tac_toe_board[4] == player_symbol and tic_tac_toe_board[
        6] == player_symbol):
        # Set Game To Stop To Get Out Of The Playing Game Loop.
        game_still_going = False
        #
        winner = player_symbol
    return


#   --------------------  Check If There Is No Winner, And It Is Tie Function Code.    --------------------
def check_if_tie():
    # Access Global Variables
    global game_still_going
    # Check If There Is Any Cell In Board Still Empty.
    if ' ' not in tic_tac_toe_board:
        game_still_going = False
        print('Game Over, No Player Wins, It Is A Tie.')
    return


#   --------------------  Flipping Player Function Code.    --------------------
def flipping_player():
    # Access Global Variables.
    global player_totem
    # Check For Current Player To Flip To The Other Player.
    if player_totem == 'X':
        player_totem = 'O'
    elif player_totem == 'O':
        player_totem = 'X'
    return


#   --------------------  Start The Whole Game.    --------------------
play_tic_tac_toe()

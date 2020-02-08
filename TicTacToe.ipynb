{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Global Variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "game_still_going = True\n",
    "winner = None\n",
    "player_totem = 'X'\n",
    "tic_tac_toe_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']\n",
    "cells = ['0', '1', '2', '3', '4', '5', '6', '7', '8']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Drawing Tic_Tac_Toe Board."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def draw_board():\n",
    "    print(f'||~~~~~||~~~~~||~~~~~||')\n",
    "    print(f'||  {tic_tac_toe_board[0]}  ||  {tic_tac_toe_board[1]}  ||  {tic_tac_toe_board[2]}  ||')\n",
    "    print(f'||~~~~~||~~~~~||~~~~~||')\n",
    "    print(f'||  {tic_tac_toe_board[3]}  ||  {tic_tac_toe_board[4]}  ||  {tic_tac_toe_board[5]}  ||')\n",
    "    print(f'||~~~~~||~~~~~||~~~~~||')\n",
    "    print(f'||  {tic_tac_toe_board[6]}  ||  {tic_tac_toe_board[7]}  ||  {tic_tac_toe_board[8]}  ||')\n",
    "    print(f'||~~~~~||~~~~~||~~~~~||')\n",
    "\n",
    "draw_board()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Tic Tac Toe Game Play Function Code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Tic Tac Toe Game Play Function Code.\n",
    "def play_tic_tac_toe():\n",
    "    # Starting Player.\n",
    "    global player_totem\n",
    "\n",
    "    # Display Board\n",
    "    draw_board()\n",
    "\n",
    "    # While Game Still Going.\n",
    "    global game_still_going\n",
    "    while game_still_going:\n",
    "        # Handle Turn For Each Player.\n",
    "        handle_players_turn(player_totem)\n",
    "\n",
    "        # Check If Game Over,\n",
    "        check_game_over()\n",
    "\n",
    "        # Flipping Player.\n",
    "        flipping_player()\n",
    "\n",
    "    # If There Is Winner.\n",
    "    if winner == 'X' or winner == 'O':\n",
    "        print(f'Player \"{winner}\" Has Won.')\n",
    "    elif winner is None:\n",
    "        print('This Is Tie.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Handle Single Player Turn Function Code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Handle Single Player Turn Function Code.\n",
    "def handle_players_turn(player_icon):\n",
    "    # Display Player Turns\n",
    "    print(f\"{player_icon}'s Player Turn.\")\n",
    "\n",
    "    # Taking Board Cell From Player.\n",
    "    board_cell = input(' Please Enter Number From 0 To 8 : ')\n",
    "    global cells\n",
    "    # Check Player Input Validation Ask Again If Not Valid.\n",
    "    while board_cell not in cells:\n",
    "        board_cell = input(' Please Enter Number From 0 To 8 : ')\n",
    "\n",
    "    board_cell = int(board_cell)\n",
    "    # Insert Player Totem Inside The Chosen Board Cell\n",
    "    if tic_tac_toe_board[board_cell] == ' ':\n",
    "        tic_tac_toe_board[board_cell] = player_icon\n",
    "        # Draw The Tic Tac Toe Again\n",
    "        draw_board()\n",
    "    else:\n",
    "        handle_players_turn(player_icon)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Check If Game Is Over Function Code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check If Game Is Over Function Code.\n",
    "def check_game_over():\n",
    "    # Check If There Is A Winner.\n",
    "    check_if_win(player_totem)\n",
    "\n",
    "    # Check If There Is No Winner, And It Is Tie.\n",
    "    check_if_tie()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Check If There Is A Winner Function Code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check If There Is A Winner Function Code.\n",
    "def check_if_win(player_symbol):\n",
    "    # Manipulate Global Variables.\n",
    "    global winner\n",
    "    global game_still_going\n",
    "    # Check If There Is Any Contiguous Three Cells Have Same Symbol For Any Player.\n",
    "    if (tic_tac_toe_board[0] == player_symbol and tic_tac_toe_board[1] == player_symbol and tic_tac_toe_board[\n",
    "        2] == player_symbol) or (\n",
    "            tic_tac_toe_board[3] == player_symbol and tic_tac_toe_board[4] == player_symbol and tic_tac_toe_board[\n",
    "        5] == player_symbol) or (\n",
    "            tic_tac_toe_board[6] == player_symbol and tic_tac_toe_board[7] == player_symbol and tic_tac_toe_board[\n",
    "        8] == player_symbol) or (\n",
    "            tic_tac_toe_board[0] == player_symbol and tic_tac_toe_board[3] == player_symbol and tic_tac_toe_board[\n",
    "        6] == player_symbol) or (\n",
    "            tic_tac_toe_board[1] == player_symbol and tic_tac_toe_board[4] == player_symbol and tic_tac_toe_board[\n",
    "        7] == player_symbol) or (\n",
    "            tic_tac_toe_board[2] == player_symbol and tic_tac_toe_board[5] == player_symbol and tic_tac_toe_board[\n",
    "        8] == player_symbol) or (\n",
    "            tic_tac_toe_board[0] == player_symbol and tic_tac_toe_board[4] == player_symbol and tic_tac_toe_board[\n",
    "        8] == player_symbol) or (\n",
    "            tic_tac_toe_board[2] == player_symbol and tic_tac_toe_board[4] == player_symbol and tic_tac_toe_board[\n",
    "        6] == player_symbol):\n",
    "        # Set Game To Stop To Get Out Of The Playing Game Loop.\n",
    "        game_still_going = False\n",
    "        #\n",
    "        winner = player_symbol\n",
    "    return"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Check If There Is No Winner, And It Is Tie Function Code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check If There Is No Winner, And It Is Tie Function Code.\n",
    "def check_if_tie():\n",
    "    # Access Global Variables\n",
    "    global game_still_going\n",
    "    # Check If There Is Any Cell In Board Still Empty.\n",
    "    if ' ' not in tic_tac_toe_board:\n",
    "        game_still_going = False\n",
    "        print('Game Over, No Player Wins, It Is A Tie.')\n",
    "    return"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Flipping Player Function Code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Flipping Player Function Code.\n",
    "def flipping_player():\n",
    "    # Access Global Variables.\n",
    "    global player_totem\n",
    "    # Check For Current Player To Flip To The Other Player.\n",
    "    if player_totem == 'X':\n",
    "        player_totem = 'O'\n",
    "    elif player_totem == 'O':\n",
    "        player_totem = 'X'\n",
    "    return"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "play_tic_tac_toe()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

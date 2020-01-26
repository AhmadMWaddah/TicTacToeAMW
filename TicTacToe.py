#!/usr/bin/env python
# coding: utf-8

# # Tic Tac Toe Game 
# ##### Scratch Building
# ##### No GUI Required 

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[1]:


from IPython.display import clear_output

def board_size(cells):
    print(f'||~~~~~||~~~~~||~~~~~||')
    print(f'||  {cells[0]}  ||  {cells[1]}  ||  {cells[2]}  ||')
    print(f'||~~~~~||~~~~~||~~~~~||')
    print(f'||  {cells[3]}  ||  {cells[4]}  ||  {cells[5]}  ||')
    print(f'||~~~~~||~~~~~||~~~~~||')
    print(f'||  {cells[6]}  ||  {cells[7]}  ||  {cells[8]}  ||')
    print(f'||~~~~~||~~~~~||~~~~~||')
    


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[2]:


test_board = ['X','O','X','O','X','O','X','O','X']
board_size(test_board)


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[2]:


def player_input():
    position = ''
    while (position.upper() != 'X') or (position.upper() != 'O'):
        position = input(' Please Enter "X" Or "O".: ')
        if position.upper() == 'X':
            print(f' Player {position.upper()}.')
            break
        elif position.upper() == 'O':
            print(f' Player {position.upper()}.')
            break


# **TEST Step 2:** run the function to make sure it returns the desired output

# In[4]:


player_input()


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[3]:


thrd_brd = ['X','O','X','O','X','O','X','O','X']

def place_marker(board, marker, position):
    board[position] = marker 

        
def display_board(cells):
    print(f'| {cells[0]} | {cells[1]} | {cells[2]} |')
    print(f'| {cells[3]} | {cells[4]} | {cells[5]} |')
    print(f'| {cells[6]} | {cells[7]} | {cells[8]} |')


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# In[6]:


place_marker(thrd_brd,'#',1)
display_board(thrd_brd)


# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[7]:


def win_check(brd, mark):
    if (brd[0] == mark and brd[1] == mark and brd[2] == mark) or (brd[3] == mark and brd[4] == mark and brd[5] == mark) or (brd[6] == mark and brd[7] == mark and brd[8] == mark) or (brd[0] == mark and brd[3] == mark and brd[6] == mark) or (brd[1] == mark and brd[4] == mark and brd[7] == mark) or (brd[2] == mark and brd[5] == mark and brd[8] == mark) or (brd[0] == mark and brd[5] == mark and brd[8] == mark) or (brd[2] == mark and brd[4] == mark and brd[6] == mark):
        return True
    else:
        return False
        


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# In[8]:


win_check(thrd_brd,'X')


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[10]:


# Random Choice For String
from random import choice

def pick_turn():
    play_turn = choice(['X', 'O'])
    print(f'Player {play_turn} Will Be Starting The Game at First.')


pick_turn()


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[11]:


spc_brd = ['X','O','X','O','X','O',0,'O','X']
def space_check(board, position):
    if board[position] == 0:
        return True
    else:
        return False
    
    
space_check(spc_brd, 6)


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[12]:


ful_brd = ['X','O','X','O','X','O',' ','O','X']

def chk_brd(brd):
    if brd[0] == ' ' or brd[1] == ' ' or brd[2] == ' ' or brd[3] == ' ' or brd[4] == ' ' or brd[5] == ' ' or brd[6] == ' ' or brd[7] == ' ' or brd[8] == ' ':
        print('No, Board Is Not Full.')
    else:
        print('Yes, Board Is Full.')


chk_brd(ful_brd)


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[14]:


spc_brd = ['X', '', 'X', 'O', 'X', 'O', 'X', 'O', 'X']


def player_choice():
    nxt_pos = int(input(' Please Enter Number Between 0 and 8: '))

    def space_check(board, position):
        if board[position] == '':
            print(' Empty Cell. ')
        else:
            print(' Full Cell. ')

    space_check(spc_brd, nxt_pos)


player_choice()
    
    


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[15]:


def replay():
    rply = input('Want To Play Again, (Yes Or No): ')
    if rply.lower() == 'no':
        return False
    elif rply.lower() == 'yes':
        return True
    else:
        print('wronh')


replay()


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[ ]:


tic_brd = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Check Board Cells.
def chk_brd(brd):
    while brd[0] == ' ' or brd[1] == ' ' or brd[2] == ' ' or brd[3] == ' ' or brd[4] == ' ' or brd[5] == ' ' or brd[6] == ' ' or brd[7] == ' ' or brd[8] == ' ':
        print('Board Is Not Full.')

        def board_size(cells):
            print(f'||~~~~~||~~~~~||~~~~~||')
            print(f'||  {cells[0]}  ||  {cells[1]}  ||  {cells[2]}  ||')
            print(f'||~~~~~||~~~~~||~~~~~||')
            print(f'||  {cells[3]}  ||  {cells[4]}  ||  {cells[5]}  ||')
            print(f'||~~~~~||~~~~~||~~~~~||')
            print(f'||  {cells[6]}  ||  {cells[7]}  ||  {cells[8]}  ||')
            print(f'||~~~~~||~~~~~||~~~~~||')

        board_size(tic_brd)

        def player_input():
            position_one = ''
            while (position_one.upper() != 'X') or (position_one.upper() != 'O'):
                position_one = input(' Please Enter "X" Or "O".: ').upper()
                if position_one.upper() == 'X':
                    print(f' Player One {position_one}.')
                    break
                elif position_one.upper() == 'O':
                    print(f' Player One {position_one}.')
                    break

            def place_marker(board):
                if position_one:
                    cel = int(input(' Enter Cell: '))
                    while cel < 0 or cel > 9:
                        cel = int(input(f' Cell {cel} Is Out Of Range ( 0 - 8 ): '))
                    else:
                        while board[cel] != ' ':
                            cel = int(input(f' Cell {cel} Is Full Enter Another Cell: '))
                            continue
                        else:
                            board[cel] = position_one

            board_size(tic_brd)

            # Check Win
            def win_check(brdd, pos_on):
                while (brdd[0] == pos_on and brdd[1] == pos_on and brdd[2] == pos_on) or (
                        brdd[3] == pos_on and brdd[4] == pos_on and brdd[5] == pos_on) or (
                        brdd[6] == pos_on and brdd[7] == pos_on and brdd[8] == pos_on) or (
                        brdd[0] == pos_on and brdd[3] == pos_on and brdd[6] == pos_on) or (
                        brdd[1] == pos_on and brdd[4] == pos_on and brdd[7] == pos_on) or (
                        brdd[2] == pos_on and brdd[5] == pos_on and brdd[8] == pos_on) or (
                        brdd[0] == pos_on and brdd[5] == pos_on and brdd[8] == pos_on) or (
                        brdd[2] == pos_on and brdd[4] == pos_on and brdd[6] == pos_on):
                    print(f'Game Over. {pos_on} Win.')
                else:
                    place_marker(tic_brd)
                    board_size(tic_brd)

            win_check(tic_brd, position_one)

        player_input()
    else:
        print(f'Yes, Board Is Full. Game Over. ')


chk_brd(tic_brd)


# ## Good Job!

# libraries and modules

import random
import sys
import string
import hashlib
import time
import csv

# constants

health_value_one = 5
health_value_two = 5
alphabet_lst_upper = list(string.ascii_uppercase)
alphabet_lst = list(string.ascii_lowercase) + list(string.ascii_uppercase)
correct_guess_one = 0
correct_guess_two = 0
incorrect_guess_one = 0
incorrect_guess_two = 0
one_to_eight = ['1', '2', '3', '4', '5', '6', '7', '8']

# 2.1 Generate the Game World


grid = [['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['C', 'L', 'A', 'S', 'S', '#', '#', 'S', '#'],
        ['#', 'O', '#', '#', '#', '#', '#', 'L', '#'],
        ['#', 'O', '#', '#', '#', '#', '#', 'I', '#'],
        ['#', 'P', 'I', 'P', '#', '#', '#', 'C', '#'],
        ['#', '#', '#', '#', '#', '#', '#', 'E', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#']]
"""Figure 1"
#Words: (pip, class, loop, slice)"""

# 2.2 Initial state of the codeword puzzle
initial_state = [['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                 ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                 ['3', '4', '1', '5', '5', '#', '#', '5', '#'],
                 ['#', '2', '#', '#', '#', '#', '#', '4', '#'],
                 ['#', '2', '#', '#', '#', '#', '#', '7', '#'],
                 ['#', '6', '7', '6', '#', '#', '#', '3', '#'],
                 ['#', '#', '#', '#', '#', '#', '#', '8', '#'],
                 ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
                 ['#', '#', '#', '#', '#', '#', '#', '#', '#']]


# "Figure 2"


# 2.3 Create the key for each letter
def key_grid():
    final_key = {
        1: 'A',
        2: 'O',
        3: 'C',
        4: 'L',
        5: 'S',
        6: 'P',
        7: 'I',
        8: 'E',
    }
    """ “0” will replace with ‘P’, “3” will be replaced by “H”, etc. This provides the player with the
    indexes of each letter in the code_grid. The player must guess what letter is in each available
    index using the player_key."""
    "Figure 3"
    return final_key


# 2.3 Create the player key
def player_key_display():
    player_key = {
        1: '_',
        2: '_',
        3: '_',
        4: '_',
        5: '_',
        6: '_',
        7: '_',
        8: '_',
    }
    """When the player inputs their guess of what letter is in a cell on the crossword puzzle grid,
    the letter they guess will be inserted into the player_key. If the letter they guess in the
    specified index is the same as the specified index in the key_grid, then the player gains 2
    points in their health value. If not, the letter is unassigned from both the code_grid and
    the player_grid, and 2 points are subtracted from the health value"""
    "Figure 4"
    return player_key


# 2.4 Create Users


def name_one(first_name_one, last_name_one):
    return "Name: ", first_name_one + last_name_one


def username_player_one(first_name_one, last_name_one):
    first = first_name_one[0]

    second_index = random.randint(1, len(first_name_one) - 1)
    third_index = random.randint(1, len(last_name_one) - 1)

    second = first_name_one[second_index]
    third = last_name_one[third_index]

    fourth = last_name_one[0]

    user_name = first + second + third + fourth
    user_name1 = user_name.lower()

    encrypted_username_one = hashlib.sha256(user_name1.encode('utf-8')).hexdigest()
    return "encrypted username: " + encrypted_username_one

    # We use the hashlib library to encrypt the passwords and usernames


def password_player_one():
    """for the alphabet we decided to obtain a list of ascii characters
    for the 1st, 2nd, 3rd, 5th, 6th, 7th letters, we pick a random letter in the alphabet list
    for the 4th character, a random number between 0 and 9 is selected
    for the 8th character, a special character is selected from the ones in the special character list
    the password is encrypted using the hashlib library"""

    alphabet_lst = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    special_char = ['"', '!', '#', '%']

    first_three_one_index = random.randint(0, len(alphabet_lst) - 1)
    first = alphabet_lst[first_three_one_index]

    first_three_two_index = random.randint(0, len(alphabet_lst) - 1)
    second = alphabet_lst[first_three_two_index]

    first_three_three_index = random.randint(0, len(alphabet_lst) - 1)
    third = alphabet_lst[first_three_three_index]

    fourth = random.randint(0, 9)

    first_three_five_index = random.randint(0, len(alphabet_lst) - 1)
    fifth = alphabet_lst[first_three_five_index]

    first_three_six_index = random.randint(0, len(alphabet_lst) - 1)
    sixth = alphabet_lst[first_three_six_index]

    first_three_seven_index = random.randint(0, len(alphabet_lst) - 1)
    seventh = alphabet_lst[first_three_seven_index]

    eight_index = random.randint(0, len(special_char) - 1)
    eighth = special_char[eight_index]

    password = first, second, third, fourth, fifth, sixth, seventh, eighth
    password1 = (' '.join([str(i) for i in password])).replace(" ", "")

    encrypted_password_one = hashlib.sha256(password1.encode('utf-8')).hexdigest()
    return "encrypted password: " + encrypted_password_one
    # We use the hashlib library to encrypt the passwords and usernames


def name_two(first_name_two, last_name_two):
    return "Name: ", first_name_two + last_name_two


def username_player_two(first_name_two, last_name_two):
    first = first_name_two[0]

    second_index = random.randint(1, len(first_name_two) - 1)
    third_index = random.randint(1, len(last_name_two) - 1)

    second = first_name_two[second_index]
    third = last_name_two[third_index]

    fourth = last_name_two[0]

    user_name = first + second + third + fourth
    user_name2 = user_name.lower()
    encrypted_username_two = hashlib.sha256(user_name2.encode('utf-8')).hexdigest()
    return "encrypted username: " + encrypted_username_two

    # We use the hashlib library to encrypt the passwords and usernames


def password_player_two():
    """
    for the alphabet we decided to obtain a list of ascii characters
    for the 1st, 2nd, 3rd, 5th, 6th, 7th letters, we pick a random letter in the alphabet list
    for the 4th character, a random number between 0 and 9 is selected
    for the 8th character, a special character is selected from the ones in the special character list
    the password is encrypted using the hashlib library
    """

    alphabet_lst = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    special_char = ['"', '!', '#', '%']

    first_three_one_index = random.randint(0, len(alphabet_lst) - 1)
    first = alphabet_lst[first_three_one_index]

    first_three_two_index = random.randint(0, len(alphabet_lst) - 1)
    second = alphabet_lst[first_three_two_index]

    first_three_three_index = random.randint(0, len(alphabet_lst) - 1)
    third = alphabet_lst[first_three_three_index]

    fourth = random.randint(0, 9)

    first_three_five_index = random.randint(0, len(alphabet_lst) - 1)
    fifth = alphabet_lst[first_three_five_index]

    first_three_six_index = random.randint(0, len(alphabet_lst) - 1)
    sixth = alphabet_lst[first_three_six_index]

    first_three_seven_index = random.randint(0, len(alphabet_lst) - 1)
    seventh = alphabet_lst[first_three_seven_index]

    eight_index = random.randint(0, len(special_char) - 1)
    eighth = special_char[eight_index]

    password = first, second, third, fourth, fifth, sixth, seventh, eighth
    password2 = (' '.join([str(i) for i in password])).replace(" ", "")

    encrypted_password_two = hashlib.sha256(password2.encode('utf-8')).hexdigest()
    return "encrypted password: " + encrypted_password_two


encrypted_confirmation_message = "these usernames and passwords have been encrypted\n"


def store_player_details(name_one, name_two, user_name1, user_name2, password1, password2):
    all_details = [[name_one, user_name1, password1], [name_two, user_name2, password2]]
    with open('login_details', 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, delimiter=' ')
        my_writer.writerow(all_details)
    return all_details


def store_administrator_details(name_one, user_name1, password1):
    all_details = [name_one, user_name1, password1]
    with open('login_details_administrator', 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, delimiter=' ')
        my_writer.writerow(all_details)
    return all_details

# We use the hashlib library to encrypt the passwords and usernames


player_key = player_key_display()
final_key = key_grid()


def play(name_one, name_two, health_value_one, health_value_two, player_key, final_key,
         correct_guess_one, correct_guess_two, incorrect_guess_one, incorrect_guess_two, one_to_eight, alphabet_lst):
    """Initializes health value to 5 by assigning a variable called health_value (for player 1
    and then another for player 2) and assigning the number 5 to them both. They will change as the
    game goes on"""

    """Store name, encrypted usernames and password and store them in a list.
    e.g [[name1, username1, password1], [name2, username2, password2, health1], [name3,
    username3, password3, health2]]"""
    while '_' in player_key.values() and (health_value_one >= 2) and (health_value_two >= 2):
        for b in range(0, 2):
            if b == 0:
                print(player_key)
                index_choice = input("""Pick a square to fill in (from 1 to 8):\n""")

                while index_choice not in one_to_eight:
                    print("Invalid input")
                    index_choice = input("""Pick a square to fill in (from 1 to 8):\n""")

                index_choice = int(index_choice)

                letter = input("Guess which letter is in this square:\n")
                print("Which letter could it be {}?".format(name_one))

                while letter not in alphabet_lst:
                    print("Invalid input")
                    letter = input("Guess which letter is in this square:\n")
                    print("Which letter could it be {}?".format(name_one))

                letter = str(letter)

                if final_key[index_choice] == letter.upper():
                    correct_guess_one = correct_guess_one + 1
                    player_key[index_choice] = letter.upper()
                    health_value_one += 2
                    print(health_value_one)
                else:
                    incorrect_guess_one = incorrect_guess_one + 1
                    health_value_one -= 2
                    print(health_value_one)
                for i in range(0, len(initial_state)):
                    for j in range(0, len(initial_state[i])):
                        if initial_state[i - 1][j] == str(index_choice):
                            initial_state[i - 1][j] = letter.upper()
                for x in initial_state:
                    print(*[e[0] for e in x])
                print('\n')
            elif b == 1:
                print(player_key)
                index_choice = input("""Pick a square to fill in (from 1 to 8):\n""")

                while index_choice not in one_to_eight:
                    print("Invalid input")
                    index_choice = input("""Pick a square to fill in (from 1 to 8):\n""")

                index_choice = int(index_choice)

                letter = input("Guess which letter is in this square:\n")
                print("Which letter could it be {}?".format(name_two))

                while letter not in alphabet_lst:
                    print("Invalid input")
                    letter = input("Guess which letter is in this square:\n")
                    print("Which letter could it be {}?".format(name_two))

                letter = str(letter)
                if final_key[index_choice] == letter.upper():
                    correct_guess_two = correct_guess_two + 1
                    player_key[index_choice] = letter.upper()
                    health_value_two += 2
                    print(health_value_two)
                else:
                    incorrect_guess_two = incorrect_guess_two + 1
                    health_value_two -= 2
                    print(health_value_one)

                for i in range(0, len(initial_state)):
                    for j in range(0, len(initial_state[i])):
                        if initial_state[i - 1][j] == str(index_choice):
                            initial_state[i - 1][j] = letter.upper()
                for x in initial_state:
                    print(*[e[0] for e in x])
                print('\n')

    # 3.2 Players' Logic - After Game is Over

    """Checks who won, player 1 or 2
    After the game is over, print the player statistics: players names,
    number of correct gu00esses, number of incorrect guesses and current
    health value."""

    if health_value_one > health_value_two:
        with open('scores', 'a', newline='') as scores:
            finish_game_statement = "Player's Health = {}, correct_guesses = {}, incorrect_guesses = {}, " \
               "Well done {} ".format(health_value_one, correct_guess_one, incorrect_guess_one, name_one)
            my_writer = csv.writer(scores, delimiter=' ')
            my_writer.writerow(finish_game_statement)
        return finish_game_statement
    elif health_value_one < health_value_two:
        with open('scores', 'a', newline='') as scores:
            finish_game_statement = "Player's Health = {}, correct_guesses = {}, incorrect_guesses = {}, " \
               "Well done {} ".format(health_value_two, correct_guess_two, incorrect_guess_two, name_two)
            my_writer = csv.writer(scores, delimiter=' ')
            my_writer.writerow(finish_game_statement)
        return finish_game_statement
    elif health_value_one == health_value_two:
        with open('scores', 'a', newline='') as scores:
            finish_game_statement = "{}'s Health = {}, correct_guesses = {}, incorrect_guesses = {}  \
               ... {}'s Health = {}, correct_guesses = {}, " \
                                    "incorrect_guesses = {}, TIE :D!".format(name_one,
                                                                             health_value_one,
                                                                             correct_guess_one,
                                                                             incorrect_guess_one,
                                                                             name_two,
                                                                             health_value_two,
                                                                             correct_guess_two,
                                                                             incorrect_guess_two)
            my_writer = csv.writer(scores, delimiter=' ')
            my_writer.writerow(finish_game_statement)
        return finish_game_statement


# 4 Administrator Logic


def administrator(grid):
    change_or_not = 1
    while change_or_not == 1:
        change_or_not = input("Would you like to change any words in the crossword grid? (Y = Yes, N = no)\n")
        change_or_not = change_or_not.upper()
        while (change_or_not != 'Y') and (change_or_not != 'N'):
            print("Invalid Input")
            change_or_not = input("Would you like to change any words in the crossword grid? (1 = Yes, 0 = no)\n")
        if change_or_not == 'Y':
            word = input("Type in the word you'd like to change (Look at the 1st grid, figure 1)\n")
            word = str(word.upper())
            if word.upper() == "PIP":
                word_change = input("Enter the word you'd like to replace this word with:\n")
                word_change = word_change.upper()
                if len(word_change) == 3:
                    grid[5][1] = word_change[0]
                    grid[5][2] = word_change[1]
                    grid[5][3] = word_change[2]
            elif word.upper() == "CLASS":
                word_change = input("Enter the word you'd like to replace this word with:\n")
                word_change = word_change.upper()
                if len(word_change) == 5:
                    grid[2][0] = word_change[0]
                    grid[2][1] = word_change[1]
                    grid[2][2] = word_change[2]
                    grid[2][3] = word_change[3]
                    grid[2][4] = word_change[4]
            elif word.upper() == "LOOP":
                word_change = input("Enter the word you'd like to replace this word with:\n")
                word_change = word_change.upper()
                if len(word_change) == 4:
                    grid[2][1] = word_change[0]
                    grid[3][1] = word_change[1]
                    grid[4][1] = word_change[2]
                    grid[5][1] = word_change[3]
            elif word.upper() == "SLICE":
                word_change = input("Enter the word you'd like to replace this word with:\n")
                word_change = word_change.upper()
                if len(word_change) == 5:
                    grid[2][7] = word_change[0]
                    grid[3][7] = word_change[1]
                    grid[4][7] = word_change[2]
                    grid[5][7] = word_change[3]
                    grid[6][7] = word_change[4]

            for x in grid:
                print(*[e[0] for e in x])
            print('\n')

            """for b in range(0, len(final_key)):
                print(final_key[b+1])
                if str(grid[5][1]) in final_key[b+1]:
                    print("Yes")
                    for i in range(0, len(final_key)):
                        if grid[5][1] == final_key[i+1]:
                            for j in range(0, len(initial_state)):
                                for k in range(0, len(initial_state[j])):
                                    """

        for x in initial_state:
            print(*[e[0] for e in x])
        print('\n')
    return grid


"""
Allow the user to add a different word to the puzzle.
Allow the user to delete a word from the puzzle.
Show the changed grids of figures 1,2,3,4 after each alteration.

Edit the grid you have instead of replacing with a new grid.
"""

print("""Unfortunately this part of the code was unsuccessful, I could not alter figure 2 3 nor 4. Only figure 1.
I attempted to use the pandas module for this section, but when it was downloaded using pip, some modules were missing
during installation, therefore I could not use the entire module as a whole.

I attempted to use excel files to do this, but it ultimately turned out to be too difficult to implement
the change of words into the code.
""")


# 3.1 Boot Up


print("""Choose an option """)
start_option = input("""a. Administrator (login as an administrator and change/replace the words used in 
the game)\n
b. Player (login as a player and play without altering the grids at all)\n
c. Exit the system (Quit the Game)\n""")
start_option = start_option.upper()
while (start_option != 'A') and (start_option != 'B') and (start_option != 'C'):
    print("Invalid Input")
    print("""Choose an option """)
    start_option = input("""a. Administrator (login as an administrator and change/replace the words used in
    the game)\n
b. Player (login as a player and play without altering the grids at all)\n
c. Exit the system (Quit the Game)\n""")
    start_option = start_option.upper()


if start_option == 'A':
    first_name_one = input("Enter your first name:\n")
    last_name_one = input("Enter your last name:\n")

    name_one = name_one(first_name_one, last_name_one)

    user_name1 = username_player_one(first_name_one, last_name_one)
    password1 = password_player_one()

    print(name_one)
    print(user_name1)
    # print(password1)

    # print(store_administrator_details(name_one, user_name1, password1))

    for i in grid:
        print(*[e[0] for e in i])
    print('\n')

    for i in initial_state:
        print(*[e[0] for e in i])
    print('\n')

    print(key_grid())
    print(player_key_display())

    print(administrator(grid))

    for i in initial_state:
        print(*[e[0] for e in i])
    print('\n')

    key_grid()

    play_or_not = input("Do you want to play? Y = Yes, N = No")
    play_or_not = play_or_not.upper()
    while (play_or_not != 'Y') and (play_or_not != 'N'):
        play_or_not = input("Invalid Input. Do you want to play? 1 = Yes, 0 = No")
        play_or_not = play_or_not.upper()

    if play_or_not == 'Y':
        player_healths = play(name_one, name_two, health_value_one, health_value_two, player_key, final_key,
                              correct_guess_one, correct_guess_two, incorrect_guess_one, incorrect_guess_two,
                              one_to_eight, alphabet_lst)

        print(player_healths)
    elif play_or_not == 'N':
        print("Cya around {} :)".format(name_one))
        time.sleep(1)
        sys.exit()

elif start_option == 'B':
    play_or_not = input("Do you want to play? Y = Yes, N = No")
    play_or_not = play_or_not.upper()
    while (play_or_not != 'Y') and (play_or_not != 'N'):
        play_or_not = input("Invalid Input. Do you want to play? Y = Yes, N = No")
        play_or_not = play_or_not.upper()

    if play_or_not == 'Y':
        first_name_one = input("Enter your first name Player 1:\n")
        last_name_one = input("Enter your last name Player 1:\n")

        name_one = name_one(first_name_one, last_name_one)

        user_name1 = username_player_one(first_name_one, last_name_one)
        password1 = password_player_one()

        print(name_one)
        print(user_name1)
        # print(password1)
        
        first_name_two = input("Enter your first name Player 2:\n")
        last_name_two = input("Enter your last name Player 2:\n")

        name_two = name_two(first_name_two, last_name_two)

        user_name2 = username_player_two(first_name_two, last_name_two)
        password2 = password_player_two()

        print(name_two)
        print(user_name2)
        # print(password2)

        # print(store_player_details(name_one, name_two, user_name1, user_name2, password1, password2))

        for i in initial_state:
            print(*[e[0] for e in i])
        print('\n')

        key_grid()

        player_healths = play(name_one, name_two, health_value_one, health_value_two, player_key, final_key,
                              correct_guess_one, correct_guess_two, incorrect_guess_one, incorrect_guess_two,
                              one_to_eight, alphabet_lst)

        print(player_healths)

    elif play_or_not == 'N':
        print("Cya around :)")
        time.sleep(1)
        sys.exit()

elif start_option == 'C':
    print("Thanks for Playing :)")
    print("Cya around :)")
    time.sleep(1)
    sys.exit()
"""
Gives the user 3 options before they login and start the game:
1. Administrator (login as an administrator and change/replace the words used in the game)
2. Player (login as a player and play without altering the grids at all)
3. Exit the system (Quit the Game)
"""

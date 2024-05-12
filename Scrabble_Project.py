import random
import pandas as pd
import openpyxl
import os

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

limit_letter = 100

# 1. Create a dictionary with points assigned to its corresponding letter
letter_to_points = {key: value for key, value in zip(letters, points)}


# 2. Create a prompt to ask how many people will play and to add player name
player_words = {} #create a dictionary to store users and their words
letters_used = 0 #create a variable to store the number of letters
# player_status = pd.DataFrame({}) #a dataframe with player points
count_turns = 0 #provide the turn number
count_players = 0 #create a variable to distribute total words left equally for each player
player_range = range(1,
                        int(input("Enter number of players:")
                                )+1
                      ) #create a variable with the number of players, from 1 to n
words_left = 100
cards_drawn = {}
file_path = os.curdir+'\scores.xlsx'


def insert_players(player_number): #Add player names in the dictionary and draw card
    global count_players
    global cards_drawn
    for i in player_number:
        x = random.randrange(1, 26) #extract random card from 1 to 26
        user = input(f'Enter player {i} name: ')
        player_words[user] = [] #add user name in player_words dict
        count_players += 1 #for each player add the number of players in count_player variable
        cards_drawn[user] = x #map each player to their letter drawn


def insert(): #increment the number of turns, ask player to add words until nr of letters available per player < 2
    global count_players
    global count_turns
    global letters_used
    global player_words
    global words_left
    global letters
    sorted_user = dict(sorted(cards_drawn.items(), key=lambda keyvalue: keyvalue[1])) #sort the cards based in asc order to decide who places the first word
    loop = 0
    for player, letter in sorted_user.items():
        print(f'Player {player} draw letter: {letters[letter]}')
        loop += 1
    print(f'Player {list(sorted_user.keys())[0]} places the first word. \n')

    while words_left/count_players > 2: #while number of letters is more than maximum number allowed, execute

        count_turns += 1 #count turn
        print(f'Turn {count_turns}:')
        print(f'')
        if letters_used > 0: #if there are words inserted, calculate the new max nr of letters admitted
            max_letters = round(words_left/count_players)

            for player in sorted_user.keys():
                while True:     # while user above max letters admitted prompt the user to add the word, else, append in player_words
                    add_word = input(f'Hey {player}! Please insert a word of max {max_letters}: ')
                    if len(add_word) > max_letters:
                        print(f'Word length is higher than {max_letters}. Please try again' )
                        continue
                    else: #if word length is ok, append the word
                        print(f'Word \'{add_word}\' ok')
                        player_words[player].append(add_word)
                        for letter in add_word: #add letter in letters_used
                            letters_used += 1
                        break
            words_left = limit_letter - letters_used #recalculate nr. of letters left

        else: #if this is the first insertion, calculate the max threshold and prompt the user to add the word
            max = round(words_left/count_players)
            for player in sorted_user.keys(): #ask each player added in insert_players to insert a word < max lenght admitted
                while True:
                    add_word = input(f'Hey {player}! Please insert a word of max {max}: ')
                    if len(add_word) > max:
                        print(f'Word length is higher than {max}. Please try again')
                        continue
                    else: #if word length is ok, append word in player_words
                        print(f'Word \'{add_word}\' ok')
                        player_words[player].append(add_word)
                        for letter in add_word:
                            letters_used += 1
                        break
            words_left = limit_letter - letters_used #recalculate nr. of letters left

    else:
        print(f'Game over. Number of words letters left:{words_left}. The final score per player is: ')



#3. Calculate the final score per player, add the score for each player in a dataframe and ask user if he and to export to excel
def update_point_totals():
    global player_words
    new_dct = {} #create a temporary dicitonary to add the player and score. List cannot be used in "from_dict" method
    sorted_user = dict(cards_drawn.items(), key=lambda keyvalue: keyvalue[1]) #sort the user according to the card drawn. Will be used to decide who gets the doubleword
    players_ordered = list(sorted_user.keys()) #create a list with all the players in asc order
    for player in player_words.keys():  # for each player and each list of words, calculate the current socore
        score = []
        while player == players_ordered[0]: #while player from player_words = first player, do the following
            loop = 0
            for word in player_words[player]:
                loop += 1
                while loop == 1: #for first word inserted double its score
                    for letter in word:
                        point = letter_to_points.get(letter.upper(), 0)*2 #score as doublword
                        score.append(point)  # calculate score per word ana append in score list
                    break
                else:
                    for letter in word: #for the rest of words and players, calculate the score normally
                        point = letter_to_points.get(letter.upper(), 0)
                        score.append(point)  # calculate score per word ana append in score list
            break

        else:
            for word in player_words[player]: #for the rest of words and players, calculate the score normally
                for letter in word:
                    point = letter_to_points.get(letter.upper(), 0)
                    score.append(point) # calculate score per word ana append in score list

        new_dct[player] = [sum(score)]  # add player as key and player_points as values
    player_status = pd.DataFrame.from_dict(new_dct) #create a dataframe with new_dct dictionary
    print(player_status.to_string(index=False))  #print the score table
    while True: #while input wrong, ask user again. If input 'y', export excel and stop, else, just stop
        want_excel = input('Would you like to export the results?: ')
        if want_excel != "y" and  want_excel != "n":
            print("Didn't get that. Please answer with y or n")
            print(type(want_excel))
            continue
        else:
            if want_excel == "y":
                player_status.to_excel(file_path, engine= 'openpyxl', index= False)
                break
            else:
                break


#4. Create a function to start the game
def start():
    insertpl = insert_players(player_range)
    insert_words = insert()
    total_points = update_point_totals()


#5. Execute it
if __name__ == "__main__":
    start()



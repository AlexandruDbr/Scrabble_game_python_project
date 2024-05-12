import random
import pandas as pd

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

limit_letter = 100

# 1. Create a dictionary with points assigned to its corresponding letter
letter_to_points = {key: value for key, value in zip(letters, points)}

# 2. Type how many people will play and create a function which will prompt user to create the player name:
player_words = {} #create a dictionary to store users and their words
letters_used = 0 #create a variable to store the number of letters
# player_status = pd.DataFrame({}) #a dataframe with player points
count_turns = 0 #provide the turn number
count_players = 0 #create a variable to distribute total words left equally for each player
player_range = range(1,
                        int(input("Enter number of players: ")
                                )+1
                      ) #create a variable with the number of players, from 1 to n
words_left = 100

def insert_players(player_number): #Add player names in the dictionary
    global count_players
    for i in player_number:
        user = input(f'Enter player {i} name: ')
        player_words[user] = []
        count_players += 1 #add the number of players in count_player variable


def insert(): #increment the number of turns, ask player to add words until nr of letters available per player < 2
    global count_players
    global count_turns
    global letters_used
    global player_words
    global words_left

    while words_left/count_players > 2: #check if: number of letters is already beyond the maximum number allowed
                                  # players have at least 2 words per player
        count_turns += 1
        print(f'Turn {count_turns}:')
        # all_words = sum(player_words.values(), [])  # add all words in a single list to count the nr of letters
        # print(all_words)
        # for word in all_words:  # count the total number of letters
        #     for letter in word:
        #         letters_used += 1

        if letters_used > 0: #if there are words inserted, calculate the new max nr of letters admitted
            max_letters = round(words_left/count_players)
            for player in player_words.keys():
                while True:     # while user inserted word's letters > than the max nr of letters admitted, prompt the user to add the word
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
            words_left = limit_letter - letters_used
        else: #if this is the first insertion, calculate the max threshold and prompt the user to add the word
            max = round(words_left/count_players)
            for player in player_words.keys(): #ask each player added in insert_players to insert a word < max lenght admitted
                while True: #Loop
                    add_word = input(f'Hey {player}! Please insert a word of max {max}: ')
                    if len(add_word) > max:
                        print(f'Word length is higher than {max}. Please try again')
                        continue
                    else: #if word length is ok, do the next operation
                        print(f'Word \'{add_word}\' ok')
                        player_words[player].append(add_word)
                        for letter in add_word:
                            letters_used += 1
                        break
            words_left = limit_letter - letters_used

    else:
        print("Game over. Number of words letters left < 4 . The score is: """)

def update_point_totals():
    global player_words
    new_dct = {} #create a temporary dicitonary to help insert data in df with "from_dict" method
    for player in player_words.keys():  # for each player and each list of words, calculate the current socore
        score = []
        for word in player_words[player]:
            for letter in word:
                score.append(letter_to_points.get(letter.upper(), 0))  # add each letter from each word from "player_to_words" and store the score in variable "score"
        new_dct[player] = [sum(score)]  # add player as key and player_points as values
    player_status = pd.DataFrame.from_dict(new_dct) #create a dataframe with the scores of each player
    print(player_status)  #print the score table


def start():
    insertpl = insert_players(player_range)
    insert_words = insert()
    total_points = update_point_totals()


if __name__ == "__main__":
    start()



#
#
# # 6. Create a function to loop through "player_to_words" dictionary and calculate score for each player
# player_to_points = {} #this dictionary will be of format: player : point
#
#
# # You need to append each player in the new dataframe
# # You need to add the score next to the word each time the user adds a new word
# # calculate the points for each user by getting each word from each tupple, extract the point corresponding to each
# # letter from letter_to_points, summing each point in a variable,  the
# # You need a variable to store points BUT
#
#
#
#
# update_point_totals(player_to_words) #Run update_point_totals and print result
# print(player_to_points)
#
#
#
# insert_word = insert(player_status)
#
#
# print(player_status)
# print(player_letters)
# print(count_turns)
# print(count_players)
#
#
#
#     # 3. This function will take user input and return how many points is the word worth
#     def score_word(word):
#         point_total = 0
#         for letter in word:
#             point_total += letter_to_points.get(letter.upper(), 0)
#         return point_total
#
#
#     word = input("Please add your word:")
#
#
#     # 4. Test score_word
#     brownie_points = score_word(word)
#     print(brownie_points, end='\n\n')
#
#
#     # 5. Create a dictionary which tracks some players and the words they played
#     player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
#                        'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}
#
#
#
#
#
#     # Checking: Add player 1001 with a list of names
#     player1001 = {'Alexandru': ['Polymorphism', 'Abstraction', 'Incapsulation']}
#
#     player1001['Alexandru'].append('Chess')  # append other names into the values
#     player1001['Alexandru'].append('Tennis')  # append other names into the values
#     player1001['Alexandru'].append("Other3")
#
#
#     #  Checking: Add player 70012 with a list of names
#     player70012 = {'Silviu': ['Tracking', 'Coding', 'Carting']}
#
#     # Call play_word function and check the dictionary with players
#     play_word(player1001, player_to_words)
#     play_word(player70012, player_to_words)
#
#
#
#     # Check if the program creates lists in case user does not add values as lists
#     # 1. Create variables to store user input
#     player11 = {'player1': 'think'}
#     player111 = {'player1': 'train'}
#     player3 = {'player3': 'trust'}
#     player4 = {'player3': 'etiquette'}
#
#
#     # 2. Add user input in the dictionary
#     play_word(player11, player_to_words)
#     play_word(player3, player_to_words)
#     play_word(player4, player_to_words)
#
#
#     player_to_words['Alexandru'].append("Other")
#     player_to_words['Alexandru'].append("Other2")
#     player1001['Alexandru'].append("Other2")
#
#
#     # 3. Check final result
#     print(player_to_words)
#
#     # Make letter_to_points function to handle lowercase inputs as well. Added upper in the for loop.
#
#     # Call update_point_totals()
#     update_point_totals(player_to_words)
#
#     # check updated score list
#     print(player_to_points)
#
#     check_alex = score_word('Polymorphism')
#     print(check_alex)
#


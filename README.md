# Scrabble game project

## Project overview

This project partially resembles a scrabble game with 100 pieces.
The project scope is not to emphasise proficiency in game development, but rather a good comprehension of Python functions, lists, dictionaries, strings and control flow. 
Therefore, although I tried to make this game reasonably close to reality by applying most of the rules, 
some of them were not implemented. <br>

Below are mentioned the rules of this version of the game and how to play it. <br>



# Scope of the game: 

To make as many words as possible, preferably words with high score per letter, in order to 
obtain the highest nr. of points at the end of the game. 
The game ends when users used all 100 pieces or when there are less than 2 letters available per
player.


## How does this game work?<br>

1. At the beginning, user needs to add the nr. of players for the entire game.
I recommend not more than 10, in order to have 10 letters per player.

2. Each player draws a random card. 
Player who has the card closest to A places first and his/hers first word's value is x2 its normal score
(doubleword). For the rest of the words of each player, the score is based on 
the sum of scores of each letter. This data is from a dictionary mapped with letters and their correspondent points.
For the sake of simplicity, blank card was not introduced.

3. The limit of letters inserted per game is 100. The game takes place in turns, with the current turn being displayed in the prompt.
Afterwards, each player will be asked to insert their word with a certain letter limit. After each word insertion, the available 
number of letters will decrease and until each user has reached the limit of letters and cannot add words anymore.

4. Finally, a table will be displayed with each player's score and a prompt will ask if
   him/her/they want the data exported in Excel, to keep a record for the next rounds. If 'y' is inputed, the file will be exported
in the folder where you run the script, so the user/s do not need to insert nothing in the source code.

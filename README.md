# Scrabble game project

## Project overview

This project partially resembles a scrabble game with 100 pieces.
The project scope is not to emphasise proficiency in game development, but rather a good comprehension of Python functions and control flow. 
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
Player who has the card closest to A places first and his/hers first word's value is x2 its normal score.
(doubleword). For the rest of the words of each player, the score of words is based on 
a dictionary mapped with letters and their respective points.
For the sake of simplicity, blank card was not introduced.

3. The number limit of letters inserted per game is 100. The game takes place in turns, which will be displayed in the prompt.
Afterward, each player will be asked to insert their word with a certain letter limit. After each word insertion, the available 
number of letters will decrease and finally, the game will stop when each user has reached the limit of letters.

4. Finally, a table will be displayed with each player's score and a prompt will ask you if
you want the data exported in Excel, to keep a record for the next rounds. The file will be exported
in the folder where you run the script, so the user does not need to insert nothing in the source code.
